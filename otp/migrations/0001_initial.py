# Generated by Django 4.1.7 on 2023-02-26 12:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OTP",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "txn_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("email_or_mobile", models.CharField(max_length=64)),
                ("otp", models.CharField(max_length=6, unique=True)),
                ("expire_at", models.DateTimeField()),
                ("is_verified", models.BooleanField(default=False)),
            ],
            options={
                "db_table": "OTP",
                "ordering": ("-created_at",),
            },
        ),
    ]
