# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_auto_20160128_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='sex',
            field=models.CharField(default='F', max_length=16),
            preserve_default=False,
        ),
    ]