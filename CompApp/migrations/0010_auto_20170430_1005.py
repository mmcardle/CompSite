# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-30 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompApp', '0009_auto_20170426_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimming',
            name='stroke',
            field=models.CharField(choices=[('BS', 'Breast Stroke'), ('BA', 'Backstroke'), ('FR', 'Freestyle'), ('OP', 'Open')], default='FR', max_length=2),
        ),
    ]