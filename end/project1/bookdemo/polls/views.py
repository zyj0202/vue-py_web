from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse,FileResponse,StreamingHttpResponse
# 因为调用django 的方法重名 故
from django.contrib.auth import authenticate,login as lin,logout as lout
# Create your views here.

# 从客户端传来的是request的对象，wsgi我们服务器的入口
# request.GET获取客户端GET请求传来的QueryDict 类字典对象 包含去请求的参数
def index(request):
    print(request)
    # print(request.COOKIES)
    # print(request.session)
    # print(request.GET.get('name'))
    questions = Question.objects.all()
    return render(request,'polls/index.html',{'questions':questions})
    # return JsonResponse({"name":"xxx"})
    # return FileResponse(open("static/img/background.jpg","rb"),content_type="image/png",filename="aa.jpg",as_attachment=True)
    # 响应对象可以使Json对象和流的形式(流主要是指文件)

def detail(request,qid):
    if request.method == 'GET':
        try:
            question = Question.objects.get(id=qid)
            return render(request,'polls/detail.html',{"question":question})
        except Exception as e:
            return HttpResponse('问题不合法')
            print(e)
    elif request.method == 'POST':
        choiced = request.POST.get("num")
        try:
            choice = Choices.objects.get(id=choiced)
            choice.votes+=1
            choice.save()
            # 逆向解析到具体问题的结果页需要通过问题的id确认问题
            url = reverse("polls:result",args=(qid,))
            return redirect(to=url)
        except:
            return HttpResponse('选项不合法')


# get方法容易出错
def result(request,qid):
    try:
        question = Question.objects.get(id=qid)
        return render(request, 'polls/result.html', {"question": question})
    except Exception as e:
        print(e)
        return HttpResponse('问题不合法')


def login(request):
    if request.method == "GET":
        return render(request,'polls/login.html')
    elif request.method == 'POST':
        # 与登陆的表单页面标签的value值一致
        username = request.POST.get("username")
        password = request.POST.get("password")
#       使用django的自带的用户认证系统 认证成功返回用户 失败返回None
        user = authenticate(username=username,password=password)
        print(user)
        # 不可把django的方法放在判断user前面否则会有匿名用户的错误
        if user:
            # 调用django的login方法是为了生成session
            lin(request, user)
            url = reverse("polls:index")
            return redirect(to=url)
        else:
            url = reverse("polls:login")
            return redirect(to=url)


def register(request):
    if request.method == "GET":
        return render(request,'polls/register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username).count()>0:
            return HttpResponse("用户名已存在")
        else:
            if password == password2:
                User.objects.create_user(username=username, password=password)
                url = reverse("polls:index")
                return redirect(to=url)
            else:
                return HttpResponse("密码不一致")


def logout(request):
    # 调用django的登出方法，为了删除cookie
    lout(request)
    url = reverse("polls:index")
    return redirect(to=url)


