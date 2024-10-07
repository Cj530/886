from django.shortcuts import render,HttpResponse,redirect
import json
from datetime import datetime
from django.db import connection

mycursor = connection.cursor() #获取游标对象

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

def register(request):
    return render(request,'register.html',)

def regiadd(request):
    userID = request.POST['userID']
    username = request.POST['username']
    password = request.POST['password']
    truename = request.POST['truename']
    sex = request.POST['sex']
    age = request.POST['age']
    print(userID,username,password,truename,sex,age)
    mycursor.execute('insert into user_info(userID,username,password,truename,sex,age) values(%s,%s,%s,%s,%s,%s)',(userID,username,password,truename,sex,age))
    return HttpResponse("恭喜你，注册成功")


def userlist(request):
    mycursor.execute('select * from user_info')
    myusert = mycursor.fetchall()
    mydes = [deshead[0] for deshead in mycursor.description]
    myuser = []
    for user in myusert:
       myzip = zip(mydes,user)
       myuser.append(dict(myzip))
    return render(request,'userlist.html',{"myusert":myusert,"myuser":myuser})

def useredit(request):
    userID= request.GET['userID']
    print(type(userID))
    mycursor.execute("select * from user_info where userID=%s",(userID,))
    curuser = mycursor.fetchone()
    return render(request,'useredit.html',{'curuser':curuser})

def useredit_action(request):
    userID = request.POST['userID']
    username = request.POST['username']
    password = request.POST['password']
    truename = request.POST['truename']
    sex = request.POST['sex']
    age = request.POST['age']
    print(userID,username,password,truename,sex,age)
    mycursor.execute('update user_info set username=%s,password=%s,truename=%s,sex=%s,age=%s where userID=%s', (username,password,truename,sex,age,userID))
    return redirect('/userlist/')

def userdel_action(request,userID):
    print(type(userID),userID)
    mycursor.execute('delete from user_info where userID=%s',(userID,))
    return redirect('/userlist/')
    