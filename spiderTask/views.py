#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import pdb
import hashlib
import requests
import json

from django.urls import reverse

from spiderTask.models import User, Playlist


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        user = User()
        # 创建md5对象
        hl = hashlib.md5()
        user.userName = request.POST.get('userName', '小花生')
        user.phone = request.POST.get('phone', '15735183131')
        hl.update(request.POST.get('password').encode(encoding='utf-8'))
        user.password = hl.hexdigest()
        user.age = request.POST.get('age', '22')
        user.sex = request.POST.get('sex', '0')
        user.likeTag = request.POST.get('tag', '华语')
        user.save()
        return render(request, 'login.html')
    elif request.method == 'GET':
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        userName = request.POST.get('userName', '')
        password = request.POST.get('password', '')
        userList = User.objects.filter(userName=userName)
        if userList:
            dbPassword = userList[0].password
            hl = hashlib.md5()
            hl.update(password.encode(encoding='utf-8'))
            if dbPassword == hl.hexdigest():
                # 登录成功
                return redirect(reverse('index', kwargs={'username': userName}))
            else:
                # 登录失败
                pass
        # 登录失败
        pass
    elif request.method == 'GET':
        return render(request, 'login.html')


def getSongListById(request):  # 通过歌单Id获取歌单
    playlistTag = request.GET.get('playlistTag', '华语')
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
    return JsonResponse(songData)
