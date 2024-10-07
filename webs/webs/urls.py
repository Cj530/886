"""
URL configuration for webs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blogs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',blogs.views.index),
    path('getnews/',blogs.views.getNews), #新闻列表接口
    path('',blogs.views.myHome), #网页首页
    path('about/',blogs.views.aboutme),#关于我
    path('register/',blogs.views.register),#注册页面
    path('register/add/',blogs.views.regiadd),#注册功能
    path('userlist/',blogs.views.userlist),#用户管理
    path('userlist/edit/',blogs.views.useredit), #编辑用户页
    path('userlist/edit/action/',blogs.views.useredit_action), #数据库中修改用户信息功能
    path('userlist/del/<str:userID>/',blogs.views.userdel_action), #数据库中删除页面的url功能
]

