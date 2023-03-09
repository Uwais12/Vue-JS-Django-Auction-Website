# Generated by Django 4.1.2 on 2022-12-05 17:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0017_alter_message_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="message_response",
            field=models.ForeignKey(
                blank=True,
                default=2,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="response",
                to="authentication.messageresponse",
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 5, 17, 21, 1, 822575)
            ),
        ),
    ]
