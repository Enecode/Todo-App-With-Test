# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-12-08 05:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_item_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='text',
            new_name='texts',
        ),
    ]