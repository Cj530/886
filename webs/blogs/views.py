from django.shortcuts import render,HttpResponse
import json



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
    blog_name = "这是一个网页"
    list=[{'title':"哪里的人为什么这么帅啊",'author':"作者",'data':"2024-02-03 10:21"},
           {'title':"Django为什么这么帅啊",'author':"张三",'data':"2024-02-03 14:21"}]
    return render(request,"index.html",context={'blog_name':blog_name,"articlelist":list})
