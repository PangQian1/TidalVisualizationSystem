# Generated by Django 3.0.4 on 2020-11-29 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateGrid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('girdNum', models.BigIntegerField(default=0)),
                ('date', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='GridAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('girdNum', models.BigIntegerField(default=0)),
                ('x_coor', models.BigIntegerField(default=0)),
                ('y_coor', models.BigIntegerField(default=0)),
                ('longi', models.FloatField()),
                ('lati', models.FloatField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]