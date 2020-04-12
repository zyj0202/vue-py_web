from django.shortcuts import render,redirect,reverse
# Create your views here.
# 视图模块 接受请求 处理数据 返回响应
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Book,Hero

# 回档时需要关掉数据库的链接和服务器

def index(request):
    # return HttpResponse('这是首页视图函数的作用')
    # 1.首先导入模板加载器，并获取模板即html文件
   #  template = loader.get_template('index.html')
   # # 2.渲染模板数据，构建上下文
   # #  context = {"name":"zyj","age":21}
    books = Book.objects.all()
   #  context = {"books": books}
   #  result = template.render(context)
   #  # 3.将渲染结果使用HttpResponse返回
   #  return HttpResponse(result)
    return render(request,'index.html',{"books": books})

# 通过传入某本书的id 找到该书并传入到模板
def detail(request,bookid):
    # template = loader.get_template('detail.html')
    # # get（）通过id找到对应的一本书，all（）方法为所有书
    book = Book.objects.get(id=bookid)
    # context = {'book':book}
    # result =template.render(context)
    # return HttpResponse(result)
    return render(request,'detail.html',{'book':book})

def deletebook(request,bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    # 删除一本书之后回到首页
    # return  HttpResponseRedirect(redirect_to='/')
    # 在view视图中解决硬编码，reverse逆向解析完返回 /
    url = reverse("booktext:index")
    print(url)
    return redirect(to='/')

def edithero(request,heroid):
    hero = Hero.objects.get(id=heroid)
    if request.method == 'GET':
        return render(request,'edithero.html',{"hero":hero})
    elif request.method =='POST':
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.save()
        # 通过当前英雄实例找到书的id，然后逆向解析到book的详情
        url = reverse("booktest:detail",args=(hero.book.id,))
        return redirect(to=url)
# 惰性查询，能不操作数据库就不操作数据库
def deletehero(request,heroid):
    # 通过id得到对应的对象，且没有操作数据库
    hero = Hero.objects.get(id=heroid)
    # 先找到id对应的英雄实例后，再通过对象找到对应的分类(即hero对应的的书)，再删除
    bookid = hero.book.id
    hero.delete()
    # 通过上方获取到了书的id，就能确定该书的详情页面内容
    url = reverse("booktest:detail",args=(bookid,))
    return redirect(to=url)

def addhero(request,bookid):

    if request.method == 'GET':

        return render(request,'addhero.html')
    elif request.method == 'POST':
        hero = Hero()
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender =request.POST.get("sex")
        # 为当前英雄的信息添加进所属书籍
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url = reverse("booktest:detail",args=(bookid,))
        return redirect(to=url)
def category(request):
    return HttpResponse('这是分类页面')

def mine(request):
    return HttpResponse('这里是我的页面')

