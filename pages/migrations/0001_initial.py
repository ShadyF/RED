# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-30 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('picture', models.ImageField(upload_to='')),
                ('position', models.CharField(max_length=40)),
                ('job_description', models.TextField()),
                ('join_date', models.DateTimeField()),
            ],
        ),
    ]
