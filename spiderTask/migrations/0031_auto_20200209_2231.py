# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2020-02-09 22:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spiderTask', '0030_auto_20200208_2033'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Log',
        ),
        migrations.DeleteModel(
            name='Pic',
        ),
        migrations.DeleteModel(
            name='Proxy',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]