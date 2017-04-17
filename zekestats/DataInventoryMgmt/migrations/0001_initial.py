# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='category')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='datasets')),
                ('data', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('categories', models.ManyToManyField(to='DataInventoryMgmt.Category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
