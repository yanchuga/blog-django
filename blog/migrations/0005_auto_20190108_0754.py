# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-08 05:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190108_0750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='dep',
        ),
    ]
