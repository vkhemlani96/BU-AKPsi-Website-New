# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-18 00:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nccg', '0003_nccgadvisor_nccgclient_nccgpartner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nccgadvisor',
            options={'verbose_name': 'Advisor', 'verbose_name_plural': 'Advisors'},
        ),
    ]
