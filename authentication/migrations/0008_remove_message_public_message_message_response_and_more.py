# Generated by Django 4.1.2 on 2022-12-02 17:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0007_message_product_alter_message_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="public",
        ),
        migrations.AddField(
            model_name="message",
            name="message_response",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="response",
                to="authentication.message",
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 2, 17, 56, 38, 187287)
            ),
        ),
    ]