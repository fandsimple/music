from django.db import models

from datetime import datetime
from time import time
from django.db import models


class BaseMode(models.Model):
    class Meta:
        abstract = True

    def to_dict(self, *ignore_fileds):
        '''将一个 model 转换成一个 dict'''
        attr_dict = {}
        for field in self._meta.fields:  # 遍历所有字段
            name = field.attname  # 取出字段名称
            if name not in ignore_fileds:  # 检查是否是需要忽略的字段
                tem_attr = getattr(self, name)
                if isinstance(tem_attr, datetime):
                    attr_dict[name] = tem_attr.strftime("%Y-%m-%d %X")  # 获取字段对应的值
                else:
                    attr_dict[name] = getattr(self, name)  # 获取字段对应的值
        return attr_dict


class Task(BaseMode):
    class Meta:
        verbose_name_plural = '抓取任务'
        db_table = 'task'

    TASK_TYPE = (
        ('spider', '全量抓取'),
        ('spider_update', '部分抓取')
    )
    taskId = models.AutoField(primary_key=True, verbose_name='任务id')
    taskName = models.CharField(max_length=255, null=False, verbose_name='任务名')
    taskType = models.CharField(choices=TASK_TYPE,default='全量抓取',max_length=255, verbose_name='任务类型')
    taskStatus = models.CharField(max_length=255, editable=False, default='new', verbose_name='任务状态')
    parentTaskId = models.CharField(max_length=255, default='0', verbose_name='父任务id')
    taskIP = models.CharField(max_length=255, editable=False,default='0.0.0.0', verbose_name='任务执行时主机ip')
    taskRet = models.CharField(max_length=255, default='空', editable=False, verbose_name='任务执行结果')
    extra = models.CharField(max_length=255, editable=False, default='空', verbose_name='扩展属性')
    startUrls = models.TextField(null=True, default='空', verbose_name='配置入口链接')
    sourceUrls = models.TextField(null=True, default='空', verbose_name='配置详情链接')
    priority = models.IntegerField(default=1, verbose_name='任务执行优先级')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    startTime = models.DateTimeField(auto_now=True, verbose_name='任务开始时间')
    finishTime = models.DateTimeField(auto_now=True, verbose_name='任务结束时间')


class Proxy(BaseMode):
    class Meta:
        verbose_name_plural = '代理ip'
        db_table = 'proxy'

    proxyId = models.AutoField(primary_key=True, verbose_name='代理ID')
    ip = models.CharField(max_length=255, null=False, verbose_name='IP')
    port = models.CharField(max_length=10, null=False, verbose_name='端口号')
    country = models.CharField(max_length=255, null=False, verbose_name='国家')
    updateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')


class Log(BaseMode):
    class Meta:
        verbose_name_plural = '抓取日志'
        db_table = 'log'

    logId = models.IntegerField(primary_key=True, verbose_name='日志ID')
    logDetail = models.CharField(max_length=512, null=False, verbose_name='日志详情')
    taskId = models.CharField(max_length=50, null=False, verbose_name='任务ID')
    level = models.CharField(max_length=20, null=False, verbose_name='错误级别')
    url = models.CharField(max_length=256, null=False, verbose_name='发生错误URL')
    spiderName = models.CharField(max_length=256, null=False, verbose_name='spider名字')
    ip = models.CharField(max_length=20, default='0.0.0.0', verbose_name='发生错误所在机器')
    extInfo = models.TextField(null=True, verbose_name='预留字段')


class Pic(BaseMode):
    class Meta:
        verbose_name_plural = '抓取图片'
        db_table = 'pic'

    picId = models.IntegerField(primary_key=True, verbose_name='图片ID')
    picUrlMd5 = models.CharField(max_length=256, null=False, verbose_name='图片链接MD5值')
    picUrl = models.CharField(max_length=256, null=False, verbose_name='图片链接')
    spiderName = models.CharField(max_length=256, null=False, verbose_name='spider名字')
    taskId = models.CharField(max_length=20, null=False, verbose_name='任务ID')
    picPath = models.CharField(max_length=256, null=False, verbose_name='图片在本机路径')
    picKey = models.CharField(max_length=256, null=False, verbose_name='上传到CDN上的key')
    updateTime = models.DateTimeField(auto_now=True, verbose_name='更新时间')






class User(BaseMode):

    class Meta:
        verbose_name_plural = '用户信息'
        db_table = 'user'

    SEX_TYPE = (
        ('0', '男'),
        ('1', '女'),
    )
    userId = models.AutoField(primary_key=True, verbose_name='用户Id')
    userName = models.CharField(max_length=255, null=False, verbose_name='用户名')
    sex = models.CharField(choices=SEX_TYPE, default='男', max_length=255, verbose_name='性别')
    phone = models.CharField(max_length=255, editable=True, default='110', verbose_name='手机号')
    age = models.IntegerField(default=22)
    password = models.CharField(max_length=255, null=False, verbose_name='密码')
    likeTag = models.CharField(max_length=255, null=False, verbose_name='喜欢类型', default='华语')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

class Playlist(BaseMode):
    # playlistId	playlistName	playlistTag	playlistDec
    class Meta:
        verbose_name_plural = '歌单'
        db_table = 'playlist'

    playlistId = models.CharField(max_length=255, primary_key=True, verbose_name='歌单Id')
    playlistName = models.CharField(max_length=255, null=False, verbose_name='歌单名称')
    playlistTag = models.CharField(max_length=255, null=False, verbose_name='歌单分类')
    playlistDec = models.CharField(max_length=255, null=False, verbose_name='歌单描述')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


class RecderAlter(BaseMode):
    # userId	songId	songTag
    class Meta:
        verbose_name_plural = '收听记录表'
        db_table = 'recderalter'

    userId = models.CharField(max_length=255, default='', verbose_name='用户Id')
    songId = models.CharField(max_length=255, null=False, verbose_name='已收听歌曲Id')
    songTag = models.CharField(max_length=255, null=False, verbose_name='歌曲分类')
    songName = models.CharField(max_length=255, null=False, verbose_name='曲名', default='')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')



class RecRetAlter(BaseMode):
    class Meta:
        verbose_name_plural = '推介结果表'
        db_table = 'recretalter'

    userId = models.CharField(max_length=255, default='', verbose_name='用户Id')
    songId = models.CharField(max_length=255, null=False, verbose_name='歌曲Id')
    songName = models.CharField(max_length=255, default='', verbose_name='曲名')
    source = models.CharField(max_length=255, default='热歌推介', verbose_name='推介来源')
    isReced = models.CharField(max_length=1, default='否', verbose_name='是否被推介过')
