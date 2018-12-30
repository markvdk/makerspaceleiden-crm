from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from simple_history.models import HistoricalRecords

from members.models import User

class PermitType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description =  models.CharField(max_length=200)
    permit = models.ForeignKey(
	'self', 
	on_delete=models.CASCADE,
        blank=True, null=True,
	verbose_name='Permit reqiured',
        help_text='i.e. permit required by the issuer (default is none needed)"',
    )
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description =  models.CharField(max_length=200,blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Machine(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description =  models.CharField(max_length=200,blank=True)
    location = models.ForeignKey(Location,related_name="is_located",on_delete=models.CASCADE, blank=True, null=True)
    requires_instruction = models.BooleanField(default=False)
    requires_form = models.BooleanField(default=False)
    requires_permit = models.ForeignKey(PermitType,related_name='has_permit',on_delete=models.CASCADE, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Entitlement(models.Model):
    active = models.BooleanField( default=False,)
    permit = models.ForeignKey(
	PermitType,
	on_delete=models.CASCADE,
        related_name='isRequiredToOperate',
    )
    holder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='isGivenTo',
    )
    issuer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='isIssuedBy',
    )
    history = HistoricalRecords()

    def __str__(self):
        return str(self.holder) + '@' + self.permit.name +'(Active:'+str(self.active)+')'

    class EntitlementViolation(Exception):
        pass

    def save(self, *args, **kwargs):

        # rely on the contraints to bomb out if there is nothing in kwargs and self. and self.
        if not self.issuer and request in kwargs:
                  self.issuer = kwargs['request'].user
              
        issuer_permit = PermitType.objects.get(pk = self.permit.pk)

        if 'request' in kwargs:
          if issuer_permit and not PermitType.objects.filter(permit=issuer_permit,holder=request.user):
             raise EntitlementViolation("issuer of this entitelment lacks the entitlement to issue it.")
           
        return super(Entitlement, self).save(*args, **kwargs)

