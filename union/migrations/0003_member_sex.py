# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-22 01:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('union', '0002_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='sex',
            field=models.CharField(choices=[('MAN', 'man'), ('WOMAN', 'woman')], default=datetime.datetime(2017, 5, 22, 1, 43, 4, 122748, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
    ]
