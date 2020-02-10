#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import pdb
import hashlib
import requests
import json

from django.urls import reverse

from spiderTask.models import User, Playlist, RecderAlter, RecRetAlter


def index(request):
    userName = request.session.get('username')
    if userName:
        return render(request, 'index.html', {'userName': userName})
    return render(request, 'index.html', {'userName': 'null'})


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
                request.session['username'] = userName
                return redirect('/spidertask/index/')
            else:
                # 登录失败
                return render(request, 'login.html', {'userName': 'error'})
        # 登录失败
        return render(request, 'login.html', {'userName': 'error'})
    elif request.method == 'GET':
        return render(request, 'login.html')


def getSongListById(request):  # 通过歌单Id获取歌单
    playlistTag = request.POST.get('playlistTag', '华语')
    playlist = Playlist.objects.filter(~Q(playlistTag=playlistTag))
    playlist = random.choice(playlist)
    playlistId = playlist.playlistId
    tag = playlist.playlistTag
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
    songData['mytag'] = tag
    return JsonResponse(songData)


def myrec(request):
    songTag = request.GET.get('songTag')
    if not songTag:
        songTag = '喜欢'
    userName = request.GET.get('userName')
    data = {
        'code': 200,
        'msg': '游客不记录'
    }
    print(userName)
    if not userName:
        return JsonResponse(data)
    user = User.objects.filter(userName=userName)
    if not user:
        return JsonResponse(data)
    userId = user[0].userId
    recder = RecderAlter()
    recder.songId = request.GET.get('songId')
    recder.songName = request.GET.get('songName')
    recder.songTag = songTag
    recder.userId = userId
    recder.save()
    data = {
        'code': 200,
        'msg': 'success'
    }
    return JsonResponse(data)


def getRec(request):
    userName = request.GET.get('userName', '')
    user = User.objects.filter(userName=userName)
    userId = ''
    if user:
        userId = user[0].userId
    # 请求热歌
    hotData = []
    data = getHot()
    for hot in data:
        hotData.append([
            hot.get('id'),
            hot.get('name'),
            '热歌推介'
        ])

    # 请求recretalter中对应用户的歌曲

    userData = []
    if userId:
        recretalter = RecRetAlter.objects.filter(userId=userId)
        if recretalter:
            for per in recretalter:
                persong = [
                    per.songId,
                    per.songName,
                    '您可能喜欢'
                ]
                userData.append(persong)

    # # 根据同龄人进行推介 todo
    # if userId:
    #     user = User.objects.filter(userId=userId)
    #     if user:
    #         age = user.age

    # 同龄人听
    sameData = []
    sameDataTem = getSameAgeSong()
    for sd in sameDataTem:
        sameData.append([
            sd.get('id'),
            sd.get('name'),
            '同龄人在听'
        ])

    resData = hotData + userData + sameData
    random.shuffle(resData)
    data = {
        'msg': 200,
        'data': random.choice(resData),
        # 'data':resData,
    }
    return JsonResponse(data)


def getHot():
    playlist = Playlist.objects.filter(playlistTag='华语')
    playlist = random.choice(playlist)
    playlistId = playlist.playlistId
    tag = playlist.playlistTag
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
    songData = songData.get('playlist', {}).get('tracks', [])
    return songData


def getSameAgeSong():
    playlistId = '2356878562'
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
    songData = songData.get('playlist', {}).get('tracks', [])
    return songData
