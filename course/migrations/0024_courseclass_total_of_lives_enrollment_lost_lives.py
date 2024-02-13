# Generated by Django 5.0.2 on 2024-02-12 22:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0023_remove_widget_html_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseclass',
            name='total_of_lives',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='lost_lives',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
