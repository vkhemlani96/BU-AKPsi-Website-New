# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-19 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brothers', '0007_auto_20180419_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brother',
            name='linkedin',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
