#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import pdb
import sys
import django
import json
import requests
import time
sys.path.append('/Users/fanding/gitProjects/spiderAdmin') # 将项目路径添加到系统搜寻路径当中
os.environ['DJANGO_SETTINGS_MODULE'] = 'spiderAdmin.settings' # 设置项目的配置文件
django.setup() # 加载项目配置
from spiderTask.models import Playlist, RecRetAlter, User


def getRecSongsByTag(userId, playlistTag):  # 通过注册tag获取推介歌曲
    playlist = Playlist.objects.get(playlistTag=playlistTag)
    playlistId = playlist.playlistId
    headers = {
        'authority': 'api.imjad.cn',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'sec-fetch-user': '?1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
    params = (
        ('type', 'playlist'),
        ('id', playlistId),
    )
    response = requests.get('https://api.imjad.cn/cloudmusic/', headers=headers, params=params)
    songData = json.loads(response.text)
    recSongs = songData.get('playlist', {}).get('tracks', [])
    for song in recSongs:
        recret = RecRetAlter()
        recret.isReced = '否'
        recret.userId = userId
        recret.songId = song.get('id')
        recret.songName = song.get('name')
        recret.source = '您可能喜欢'
        recret.save()


if __name__ == '__main__':
    while True:
        time.sleep(3)

        # 为所有用户添加喜欢tag的歌曲
        users = User.objects.all()
        for user in users:
            retUser = RecRetAlter.objects.filter(userId=user.userId)
            if retUser:
                continue
            getRecSongsByTag(user.userId, user.likeTag)








