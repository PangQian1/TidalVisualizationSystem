# Generated by Django 3.0.4 on 2020-11-29 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tidal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gridattr',
            old_name='name',
            new_name='road_name',
        ),
    ]
