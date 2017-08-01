# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-01 15:15
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transformations', '0009_auto_20170801_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='transformation',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='noslug', editable=False, populate_from=b'title'),
            preserve_default=False,
        ),
    ]
