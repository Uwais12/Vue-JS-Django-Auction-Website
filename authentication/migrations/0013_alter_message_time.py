# Generated by Django 4.1.2 on 2022-12-05 11:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0012_messageresponse_remove_message_public_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 5, 11, 31, 11, 525801)
            ),
        ),
    ]
