# Generated by Django 4.1.4 on 2022-12-16 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0058_alter_message_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 10, 40, 11, 359606)),
        ),
    ]
