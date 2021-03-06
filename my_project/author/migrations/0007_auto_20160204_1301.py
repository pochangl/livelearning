# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0006_book_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneToOneBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='one_to_one_book', to='author.Author')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='author.Author'),
        ),
    ]
