from django.contrib import admin

from spiderTask.models import Task, Proxy, Pic, Log

admin.site.site_header = 'Stronger Spider'
admin.site.site_title = 'Stronger Spider'
class BaseAdmin(admin.ModelAdmin):
    list_per_page = 10  # 每页显示多少条
    actions_on_top = True  # 顶部操作显示
    actions_on_bottom = True  # 底部操作显示
    actions_selection_counter = True  # 选中条数显示
    empty_value_display = ' 空白 '  # 空白字段显示格式


# Task
@admin.register(Task)
class TaskAdmin(BaseAdmin):
    ordering = ('taskId',)
    list_display = (
    'taskId', 'taskName', 'taskType', 'taskStatus', 'parentTaskId', 'taskIP', 'taskRet',  'priority',
    'createTime', 'startTime', 'finishTime')  # 显示字段
    search_fields = ('taskId',)  # 搜索条件配置
    list_filter = ('taskType',)  # 过滤字段配置
    # list_editable = ['taskName']

    # list_display_links = ('id', 'caption') # 配置点击进入详情字段


# Proxy
@admin.register(Proxy)
class TaskAdmin(BaseAdmin):
    ordering = ('updateTime',)
    list_display = (
    'proxyId', 'ip', 'port', 'country', 'updateTime') # 显示字段
    search_fields = ('ip', 'country', 'port')  # 搜索条件配置
    list_filter = ('country',)  # 过滤字段配置
    # list_editable = ['taskName']
    # list_display_links = ('id', 'caption') # 配置点击进入详情字段

# pic
@admin.register(Pic)
class TaskAdmin(BaseAdmin):
    ordering = ('updateTime',)
    list_display = (
    'picId', 'picUrlMd5', 'picUrl', 'spiderName', 'taskId', 'picPath', 'picKey', 'updateTime') # 显示字段
    search_fields = ('picUrl', 'spiderName', 'taskId', 'picKey')  # 搜索条件配置
    list_filter = ('spiderName',)  # 过滤字段配置
    # list_editable = ['taskName']
    # list_display_links = ('id', 'caption') # 配置点击进入详情字段


# Log
@admin.register(Log)
class TaskAdmin(BaseAdmin):
    ordering = ('logId',)
    list_display = (
    'logId', 'logDetail', 'taskId', 'level', 'url', 'spiderName', 'extInfo', 'ip') # 显示字段
    search_fields = ('taskId', 'spiderName')  # 搜索条件配置
    list_filter = ('spiderName',)  # 过滤字段配置
    # list_editable = ['taskName']
    # list_display_links = ('id', 'caption') # 配置点击进入详情字段


