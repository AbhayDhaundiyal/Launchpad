# Generated by Django 2.2.24 on 2022-04-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pads',
            name='For',
            field=models.IntegerField(default=0),
        ),
    ]
