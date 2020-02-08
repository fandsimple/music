# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-08-04 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taskId', models.IntegerField(primary_key=True, serialize=False, verbose_name='任务id')),
                ('taskName', models.CharField(max_length=255, verbose_name='任务名')),
                ('taskType', models.CharField(default='spider', max_length=255, verbose_name='任务类型')),
                ('taskStatus', models.CharField(default='new', max_length=255, verbose_name='任务状态')),
                ('parentTaskId', models.CharField(default='0', max_length=255, verbose_name='父任务id')),
                ('taskIP', models.CharField(max_length=255, verbose_name='任务执行时主机ip')),
                ('taskRet', models.CharField(max_length=255, verbose_name='任务执行结果')),
                ('extra', models.CharField(max_length=255, verbose_name='扩展属性')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('startTime', models.DateTimeField(auto_now=True, verbose_name='任务开始时间')),
                ('finishTime', models.DateTimeField(auto_now=True, verbose_name='任务结束时间')),
            ],
            options={
                'verbose_name_plural': '任务表',
                'db_table': 'task',
            },
        ),
    ]
