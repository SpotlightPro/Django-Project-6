# Generated by Django 5.0.7 on 2024-07-16 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="passwd",
            field=models.CharField(default="123456", max_length=10),
        ),
        migrations.AddField(
            model_name="member",
            name="passwd2",
            field=models.CharField(default="123456", max_length=10),
        ),
        migrations.AlterField(
            model_name="member",
            name="qmo_level",
            field=models.CharField(max_length=15),
        ),
    ]
