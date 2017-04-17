# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataInventoryMgmt', '0007_auto_20170412_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='metadata',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]