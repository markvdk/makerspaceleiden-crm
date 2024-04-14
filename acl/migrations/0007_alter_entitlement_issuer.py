# Generated by Django 3.2.7 on 2021-12-28 13:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("acl", "0006_auto_20201030_1054"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entitlement",
            name="issuer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="isIssuedBy",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]