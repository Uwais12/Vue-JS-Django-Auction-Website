# Generated by Django 4.1.2 on 2022-12-05 11:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0011_remove_message_message_response_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MessageResponse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=4096)),
            ],
        ),
        migrations.RemoveField(
            model_name="message",
            name="public",
        ),
        migrations.RemoveField(
            model_name="user",
            name="profile",
        ),
        migrations.AddField(
            model_name="message",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="about",
                to="authentication.product",
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 5, 11, 8, 43, 228754)
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="message_response",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="response",
                to="authentication.messageresponse",
            ),
        ),
    ]