# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 15:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20170727_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='itemName',
            new_name='Name',
        ),
    ]