# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-22 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('union', '0003_member_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='sex',
            field=models.CharField(choices=[('M', 'man'), ('W', 'women')], max_length=10),
        ),
    ]
