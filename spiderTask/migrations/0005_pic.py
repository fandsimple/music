# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-08-08 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiderTask', '0004_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('picId', models.IntegerField(primary_key=True, serialize=False, verbose_name='')),
                ('picUrlMd5', models.CharField(max_length=256, verbose_name='')),
                ('picUrl', models.CharField(max_length=256, verbose_name='')),
                ('spiderName', models.CharField(max_length=256, verbose_name='')),
                ('taskId', models.CharField(max_length=20, verbose_name='')),
                ('picPath', models.CharField(max_length=256, verbose_name='')),
                ('picKey', models.CharField(max_length=256, verbose_name='')),
                ('updateTime', models.DateTimeField(auto_now=True, verbose_name='')),
            ],
            options={
                'verbose_name_plural': '抓取图片',
                'db_table': 'pic',
            },
        ),
    ]