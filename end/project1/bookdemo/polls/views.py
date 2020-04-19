from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse,FileResponse,StreamingHttpResponse
# 因为调用django 的方法重名 故
from django.contrib.auth import authenticate,login as lin,logout as lout
from .forms import LoginForm
from .forms import RegistForm
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
        print("当前用户：",request.user.username)
        # 路由守卫，未登陆和匿名用户不能投票
        if request.user and request.user.username !="":
            # 登陆过，判断是否已投票过，未投进入投票，投过进入投票结果
            print(request.user.questions.all())
            # 此处判断已投过的问题不建议用in  数据量大的时候 效率低
            try:
                question = Question.objects.get(id=qid)
                if question in request.user.questions.all():
                    print("该问题已投，进入该问题的结果页面")
                    url = reverse("polls:result",args=(qid,))
                    return redirect(to=url)
                else:
                    #未投票
                    try:
                        return render(request, 'polls/detail.html', {"question": question})
                    except Exception as e:
                        return HttpResponse('问题不合法')
                        print(e)
                    print("未投票正常进入详情进行投票")
            except Exception as e:
                print("问题不合法")
                print(e)
        else:
            # 未登陆进入登陆页面,并处理登陆后的重定向
            url = reverse("polls:login")+"?next=/polls/detail"+qid+"/"
            return redirect(to=url)

    elif request.method == 'POST':
        choiced = request.POST.get("num")
        try:
            choice = Choices.objects.get(id=choiced)
            choice.votes+=1
            choice.save()
            # 投票成功，因为问题表与用户多对多关系，然后将用户和问题关联起来
            request.user.questions.add(Question.objects.get(id=qid))
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
        # 构建表单类不好用
        # lf = LoginForm()
        # return render(request,'polls/login.html',{"lf":lf})
        # 需要在html中自己手动编写表单
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
            next = request.GET.get("next")
            if next:
                url = next
                print(next)
            else:
                url = reverse("polls:index")
            return redirect(to=url)
        else:
            # url = reverse("polls:login")
            # return redirect(to=url)
            # render可传参
            return render(request,'polls/login.html',{"errors":"用户名密码不匹配"})


def register(request):
    if request.method == "GET":
        # 模型表单类
        rf = RegistForm()
        return render(request,"polls/register.html",{"rf":rf})
        # return render(request,'polls/register.html')
    else:
        # 切记将请求的对象传入
        rf = RegistForm(request.POST)
        if rf.is_valid():
            print(rf,"==")
            username = rf.cleaned_data['username']
            password = rf.cleaned_data['password']
            password2 = rf.cleaned_data['password2']
            if User.objects.filter(username=username).count() > 0:
                return render(request, 'polls/register.html', {"errors": "用户名已存在"})
        # 第一照片那个html标签获取表单数据
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # password2 = request.POST.get('password2')
        # if User.objects.filter(username=username).count()>0:
        #     # return HttpResponse("用户名已存在")
        #     return render(request, 'polls/register.html',{"errors":"用户名已存在"})
            else:
                if password == password2:
                    #创建用户
                    User.objects.create_user(username=username, password=password)
                    # 根据模型表单类创建用户
                    # rf.save()  这个方法保存到数据库的密码是明文在登录有问题，但是放在验证表单后就能是sha加密后的密码，建议用django的创建用户
                    url = reverse("polls:index")
                    return redirect(to=url)
                else:
                    # return HttpResponse("密码不一致")
                    return render(request, 'polls/register.html', {"errors": "密码不一致"})

def logout(request):
    # 调用django的登出方法，为了删除cookie
    lout(request)
    url = reverse("polls:index")
    return redirect(to=url)


