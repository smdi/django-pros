# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-09 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relation_in_django', '0002_auto_20190109_1902'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookName',
            new_name='Book',
        ),
    ]