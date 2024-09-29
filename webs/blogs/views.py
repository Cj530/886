from django.shortcuts import render,HttpResponse
import json
from datetime import datetime



def index(request):
    blogs = request.GET['blogs']
    return HttpResponse("这一个<a href='127.0.0.1:8000'>"+ blogs +"</a>的网页！！！")


def getNews(request):
    list1=[{'title':"哪里的人为什么这么帅啊",'data':"2024-02-03 10:21"},
           {'title':"Django为什么这么帅啊",'data':"2024-02-03 14:21"}]
    strjson = json.dumps(list1)
    return HttpResponse(strjson)

#首页文件
def myHome(request):
    blog_name = "这是一个网页",
    lie=[666,888]
    list=[{'title':"这里是我的 敏感词1",'author':"张三",'date':datetime.strptime("2024-02-03 10:21:20",'%Y-%m-%d %H:%M:%S')},
           {'title':"django为什么这么帅啊",'author':"李四",'date':datetime.strptime("2024-02-03 10:21:20",'%Y-%m-%d %H:%M:%S')}]
    return render(request,"index.html",context={'blog_name':blog_name,"articlelist":list,'lie':lie})

def aboutme(request):
    list=[{'title':"这是关于我的一个文章列表",'author':"张三",'date':datetime.strptime("2024-02-03 10:21:20",'%Y-%m-%d %H:%M:%S')},
           {'title':"django为什么这么帅啊",'author':"李四",'date':datetime.strptime("2024-02-03 10:21:20",'%Y-%m-%d %H:%M:%S')}]
    return render(request,'about.html',context={"list":list})