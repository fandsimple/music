# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2020-02-07 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderTask', '0018_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='likeTag',
            field=models.CharField(default='华语', max_length=255, verbose_name='喜欢类型'),
        ),
    ]