# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-25 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('url', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': '权限表',
                'db_table': '权限表',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('permissions', models.ManyToManyField(to='permission_rbac.Permission')),
            ],
            options={
                'verbose_name': '角色表',
                'db_table': '角色表',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
                ('roles', models.ManyToManyField(to='permission_rbac.Role')),
            ],
            options={
                'verbose_name': '用户表',
                'db_table': '用户表',
            },
        ),
    ]
