# Generated by Django 4.2.8 on 2024-09-05 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailinglists', '0003_auto_20230328_1839'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailinglist',
            options={'ordering': ['name']},
        ),
    ]
