# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-23 07:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rolls', '0002_hotel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_Main_Img',
            new_name='hotel_Img',
        ),
    ]