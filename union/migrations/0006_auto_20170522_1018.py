# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-22 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('union', '0005_member_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_id',
            field=models.IntegerField(max_length=50, unique=True),
        ),
    ]
