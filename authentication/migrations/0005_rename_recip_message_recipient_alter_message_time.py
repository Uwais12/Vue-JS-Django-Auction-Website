# Generated by Django 4.1.3 on 2022-12-02 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_profile_message_user_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='recip',
            new_name='recipient',
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 15, 28, 32, 415650)),
        ),
    ]
