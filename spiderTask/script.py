#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import django
sys.path.append('/Users/fanding/gitProjects/spiderAdmin') # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'spiderAdmin.settings' # 设置项目的配置文件
django.setup() # 加载项目配置
from spiderTask.models import Playlist


# 创建歌单信息
def createPlaylist():
    playlistInfo = [
        ['2507067464', '写作业必备歌单「安静中文」', '华语', '这个歌单是我目前为止最火的歌单啦'],
        ['2836875765', '「暴燃版BGM」打野专场 持续更新~', '摇滚', '最优质的歌曲加入歌单，尽量让大家既爱听又不觉得烦躁，谢谢支持'],
        ['3226995486', '就算路不坦荡，也要做自己的太阳', '流行', '我愿做一个不被改变的人。'],
        ['2500857826', '对不起我又想你了（丧说唱）', '伤感', '你回头看看我，我不相信你两眼空空'],
        ['2193563343', '细数那些值得单曲循环的英文歌', '经典', '在这个浮躁的世界,我只想一个人静静的听会儿歌']
    ]
    for info in playlistInfo:
        playlist = Playlist()
        playlist.playlistId = info[0]
        playlist.playlistName = info[1]
        playlist.playlistTag = info[2]
        playlist.playlistDec = info[3]
        playlist.save()
    print('添加歌单完成')



if __name__ == '__main__':
    # 添加歌单
    createPlaylist()



