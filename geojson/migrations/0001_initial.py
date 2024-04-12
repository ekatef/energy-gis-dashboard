# Generated by Django 4.2.7 on 2024-01-24 00:59

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Buses_geojson_data', max_length=100)),
                ('geojson_file', models.FileField(blank=True, null=True, upload_to='geojson_files/')),
                ('json_file', models.FileField(blank=True, null=True, upload_to='json_files/')),
                ('uploaded_time', models.DateTimeField(default=datetime.datetime.now)),
                ('geometry', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='JSONBus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('json_file', models.FileField(blank=True, null=True, upload_to='json_files/')),
                ('uploaded_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]