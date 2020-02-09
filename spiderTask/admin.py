from django.contrib import admin

from spiderTask.models import User, Playlist, RecderAlter, RecRetAlter

admin.site.site_header = '智能音乐'
admin.site.site_title = '智能音乐'


class BaseAdmin(admin.ModelAdmin):
    list_per_page = 10  # 每页显示多少条
    actions_on_top = True  # 顶部操作显示
    actions_on_bottom = True  # 底部操作显示
    actions_selection_counter = True  # 选中条数显示
    empty_value_display = ' 空白 '  # 空白字段显示格式


# Task
# @admin.register(Task)
# class TaskAdmin(BaseAdmin):
#     ordering = ('taskId',)
#     list_display = (
#     'taskId', 'taskName', 'taskType', 'taskStatus', 'parentTaskId', 'taskIP', 'taskRet',  'priority',
#     'createTime', 'startTime', 'finishTime')  # 显示字段
#     search_fields = ('taskId',)  # 搜索条件配置
#     list_filter = ('taskType',)  # 过滤字段配置
#     # list_editable = ['taskName']
#
#     # list_display_links = ('id', 'caption') # 配置点击进入详情字段
#
#
# # Proxy
# @admin.register(Proxy)
# class TaskAdmin(BaseAdmin):
#     ordering = ('updateTime',)
#     list_display = (
#     'proxyId', 'ip', 'port', 'country', 'updateTime') # 显示字段
#     search_fields = ('ip', 'country', 'port')  # 搜索条件配置
#     list_filter = ('country',)  # 过滤字段配置
#     # list_editable = ['taskName']
#     # list_display_links = ('id', 'caption') # 配置点击进入详情字段
#
# # pic
# @admin.register(Pic)
# class TaskAdmin(BaseAdmin):
#     ordering = ('updateTime',)
#     list_display = (
#     'picId', 'picUrlMd5', 'picUrl', 'spiderName', 'taskId', 'picPath', 'picKey', 'updateTime') # 显示字段
#     search_fields = ('picUrl', 'spiderName', 'taskId', 'picKey')  # 搜索条件配置
#     list_filter = ('spiderName',)  # 过滤字段配置
#     # list_editable = ['taskName']
#     # list_display_links = ('id', 'caption') # 配置点击进入详情字段
#
#
# # Log
# @admin.register(Log)
# class TaskAdmin(BaseAdmin):
#     ordering = ('logId',)
#     list_display = (
#     'logId', 'logDetail', 'taskId', 'level', 'url', 'spiderName', 'extInfo', 'ip') # 显示字段
#     search_fields = ('taskId', 'spiderName')  # 搜索条件配置
#     list_filter = ('spiderName',)  # 过滤字段配置
#     # list_editable = ['taskName']
#     # list_display_links = ('id', 'caption') # 配置点击进入详情字段


# User
@admin.register(User)
class TaskAdmin(BaseAdmin):
    ordering = ('userId',)
    list_display = (
        'userId',
        'userName',
        'sex',
        'phone',
        'age',
        'password',
        'likeTag',
        'createTime',
    )  # 显示字段
    search_fields = ('userName', 'phone')  # 搜索条件配置
    list_filter = ('sex', 'age', 'likeTag')  # 过滤字段配置
    # list_editable = ['taskName']
    # list_display_links = ('id', 'caption') # 配置点击进入详情字段


# Playlist
@admin.register(Playlist)
class TaskAdmin(BaseAdmin):
    ordering = ('playlistId',)
    list_display = (
        'playlistId',
        'playlistName',
        'playlistTag',
        'playlistDec',
        'createTime',
    )  # 显示字段
    search_fields = ('playlistName', 'playlistTag')  # 搜索条件配置
    list_filter = ('playlistName', 'playlistTag')  # 过滤字段配置
    # list_editable = ['taskName']
    # list_display_links = ('id', 'caption') # 配置点击进入详情字段


# RecderAlter
@admin.register(RecderAlter)
class TaskAdmin(BaseAdmin):
    ordering = ('id',)
    list_display = (
        'userId',
        'songId',
        'songTag',
        'songName',
        'createTime',
    )  # 显示字段
    search_fields = ('songName',)  # 搜索条件配置
    list_filter = ('songTag',)  # 过滤字段配置
    # list_editable = ['taskName']
    # list_display_links = ('id', 'caption') # 配置点击进入详情字段


# RecRetAlter
@admin.register(RecRetAlter)
class TaskAdmin(BaseAdmin):
    ordering = ('id',)
    list_display = (
        'userId',
        'songId',
        'songName',
        'source',
        'isReced',
    )  # 显示字段
    search_fields = ('userId', 'songName', 'songId')  # 搜索条件配置
    list_filter = ('source', 'isReced')  # 过滤字段配置
    # list_editable = ['taskName']
    # list_display_links = ('id', 'caption') # 配置点击进入详情字段
