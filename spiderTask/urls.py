from django.conf.urls import url

from spiderTask import views

urlpatterns = [
    # 测试跑通
    url(r'index', views.index, name='index'),
    url(r'login', views.login, name='login'),
    url(r'register', views.register, name='register'),
    url(r'getSongListById', views.getSongListById, name='getSongListById'),


]