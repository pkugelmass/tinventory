# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-26 19:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transformations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transformation',
            old_name='transformation_title',
            new_name='title',
        ),
    ]
