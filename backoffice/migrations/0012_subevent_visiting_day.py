# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 01:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0011_auto_20170312_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='subevent',
            name='visiting_day',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sub_events', to='backoffice.VisitingDay'),
            preserve_default=False,
        ),
    ]