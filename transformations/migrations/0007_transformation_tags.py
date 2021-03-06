# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-28 23:35
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('transformations', '0006_auto_20170728_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='transformation',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
