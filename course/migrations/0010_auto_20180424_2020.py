# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-24 23:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_color_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
