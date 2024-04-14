# Generated by Django 2.2.5 on 2020-10-30 09:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("acl", "0005_recentuse"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalpermittype",
            name="require_ok_trustee",
            field=models.BooleanField(
                default=False,
                help_text="i.e. the trustees need to also explictly approve it when the permit is granted.",
                verbose_name="Requires explicit trustee OK",
            ),
        ),
        migrations.AddField(
            model_name="permittype",
            name="require_ok_trustee",
            field=models.BooleanField(
                default=False,
                help_text="i.e. the trustees need to also explictly approve it when the permit is granted.",
                verbose_name="Requires explicit trustee OK",
            ),
        ),
    ]