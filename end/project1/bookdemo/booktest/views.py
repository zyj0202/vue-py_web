from django.shortcuts import render
# Create your views here.
# 视图模块 接受请求 处理数据 返回响应
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Book,Hero

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

def delete(request,bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    # 删除一本书之后回到首页
    return  HttpResponseRedirect(redirect_to='/')


def category(request):
    return HttpResponse('这是分类页面')

def mine(request):
    return HttpResponse('这里是我的页面')

