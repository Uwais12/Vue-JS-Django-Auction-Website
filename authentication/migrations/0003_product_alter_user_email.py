# Generated by Django 4.1.2 on 2022-12-02 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_alter_user_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=200)),
                ("starting_price", models.PositiveSmallIntegerField()),
                ("finish_date", models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="email address"
            ),
        ),
    ]
