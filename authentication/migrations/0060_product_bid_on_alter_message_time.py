# Generated by Django 4.1.4 on 2022-12-16 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0059_alter_message_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bid_on',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 10, 48, 34, 275404)),
        ),
    ]
