# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-13 10:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '员工表', 'verbose_name_plural': '员工表'},
        ),
        migrations.AlterModelTable(
            name='userinfo',
            table='员工表',
        ),
    ]
