# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0008_manytomanybook'),
    ]

    operations = [
        migrations.AddField(
            model_name='manytomanybook',
            name='title',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]
