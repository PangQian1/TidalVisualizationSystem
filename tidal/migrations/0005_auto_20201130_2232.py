# Generated by Django 3.0.4 on 2020-11-30 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tidal', '0004_auto_20201130_2204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dategrid',
            old_name='girdNum',
            new_name='gridNum',
        ),
        migrations.RenameField(
            model_name='gridattr',
            old_name='girdNum',
            new_name='gridNum',
        ),
    ]
