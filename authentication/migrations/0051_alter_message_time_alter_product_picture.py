# Generated by Django 4.1.4 on 2022-12-15 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0050_alter_message_time_alter_product_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 15, 19, 37, 10, 6895)),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, default='../media/images/download.png', upload_to='images'),
        ),
    ]
