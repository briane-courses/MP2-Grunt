# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20170727_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='Name',
            new_name='name',
        ),
    ]