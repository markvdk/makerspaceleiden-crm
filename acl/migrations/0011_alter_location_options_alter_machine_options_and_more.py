# Generated by Django 4.2.8 on 2024-09-05 10:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("acl", "0010_changetracker"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="location",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="machine",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="permittype",
            options={"ordering": ["name"]},
        ),
    ]
