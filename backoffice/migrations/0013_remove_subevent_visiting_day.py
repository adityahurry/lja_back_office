# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 01:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0012_subevent_visiting_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subevent',
            name='visiting_day',
        ),
    ]
