# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-26 16:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permission_rbac', '0003_auto_20180426_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='group',
        ),
        migrations.DeleteModel(
            name='PermissionGroup',
        ),
    ]
