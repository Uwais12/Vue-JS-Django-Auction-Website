# Generated by Django 4.1.4 on 2022-12-15 19:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0054_alter_message_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 15, 19, 45, 24, 997862)),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, default='../media/images/download.png', upload_to='images'),
        ),
    ]