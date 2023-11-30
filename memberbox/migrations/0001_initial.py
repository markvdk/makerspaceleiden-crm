# Generated by Django 3.2.23 on 2023-11-29 10:51

import dynamic_filenames
import simple_history.models
import stdimage.models
import stdimage.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HistoricalMemberbox",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "image",
                    models.TextField(
                        blank=True,
                        help_text="Optional - but highly recommened.",
                        max_length=100,
                        null=True,
                        validators=[
                            stdimage.validators.MinSizeValidator(100, 100),
                            stdimage.validators.MaxSizeValidator(8000, 8000),
                        ],
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        db_index=True,
                        help_text="Use left/right - shelf (top=1) - postion. E.g. R24 is the right set of shelves, second bin on the 4th row from the bottom. Or use any other descriptive string (e.g. 'behind the bandsaw')",
                        max_length=40,
                    ),
                ),
                (
                    "extra_info",
                    models.CharField(
                        help_text="Such as 'plastic bin'. Especially important if you are keeping things in an odd place.",
                        max_length=200,
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical memberbox",
                "verbose_name_plural": "historical memberboxs",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Memberbox",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    stdimage.models.StdImageField(
                        blank=True,
                        force_min_size=False,
                        help_text="Optional - but highly recommened.",
                        null=True,
                        upload_to=dynamic_filenames.FilePattern(
                            filename_pattern="{app_label:.25}/{model_name:.30}/{uuid:base32}{ext}"
                        ),
                        validators=[
                            stdimage.validators.MinSizeValidator(100, 100),
                            stdimage.validators.MaxSizeValidator(8000, 8000),
                        ],
                        variations={
                            "large": (600, 400),
                            "medium": (300, 200),
                            "thumbnail": (100, 100, True),
                        },
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        help_text="Use left/right - shelf (top=1) - postion. E.g. R24 is the right set of shelves, second bin on the 4th row from the bottom. Or use any other descriptive string (e.g. 'behind the bandsaw')",
                        max_length=40,
                        unique=True,
                    ),
                ),
                (
                    "extra_info",
                    models.CharField(
                        help_text="Such as 'plastic bin'. Especially important if you are keeping things in an odd place.",
                        max_length=200,
                    ),
                ),
            ],
        ),
    ]
