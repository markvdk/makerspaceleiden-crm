# Generated by Django 4.2.8 on 2024-09-05 10:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("memberbox", "0004_auto_20230328_1839"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="memberbox",
            options={"ordering": ["location"]},
        ),
    ]
