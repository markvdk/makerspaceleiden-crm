# Generated by Django 3.2.4 on 2021-10-01 14:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0011_auto_20190929_1430"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicaluser",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
    ]
