# Generated by Django 4.1.2 on 2022-12-15 20:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0055_alter_message_time_alter_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 15, 20, 43, 23, 715542)),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, default='../media/images/download.jpeg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
