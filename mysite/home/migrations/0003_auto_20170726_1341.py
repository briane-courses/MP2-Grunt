# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 05:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170726_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(upload_to='home/photos/'),
        ),
    ]