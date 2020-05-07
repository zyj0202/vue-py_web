from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import *
from .forms import CommentForm
# django自带了分页和分页器
from django.core.paginator import Paginator,Page
# 一个Page中有 object_list 代表当前页的所有对象
# has_next 是不是有下一页
# has_previous 是否有上一页
# next_page_number 下一页的编号
# previous_page_number 上一页的编号
# self.number 当前页的编号
# self.paginator 当前页的分页器


# 一个Paginator中的object_list代表所有未分页对象
# self.per_page 每一页有多少个对象
# get_page(self, number): 从分页器中取第几页对象
# page_range(self): 返回分页列表(第一也到n页)


# Create your views here.


def index(request):
    ads = Ads.objects.all()
    type_page = request.GET.get("type")
    year = None
    month = None
    category_id = None
    tag_id = None
    if type_page == "date":
        year = request.GET.get("year")
        month = request.GET.get("month")
        articles = Article.objects.filter(create_name__year=year, create_name__month=month).order_by("-create_name")
    elif type_page == "category":
        category_id = request.GET.get("category_id")
        try:
            category = Category.objects.get(id=category_id)
            articles = category.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse("分类不合法")
    elif type_page == "tag":
        tag_id = request.GET.get("tag_id")
        try:
            tag = Tag.objects.get(id=tag_id)
            articles = tag.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse("请求不合法")
    else:
        articles = Article.objects.all()
    # locals将作用域局部变量封装成对象并返回
    # print(locals())

    paginator = Paginator(articles, 2)
    # 获取get请求中的页码参数  默认为1
    num = request.GET.get("pagenum", 1)
    page = paginator.get_page(num)
    # 这样每个页面都传参麻烦 可以自定义标签
    # latest3articles = articles.order_by("-create_name")[:3]
    return render(request, 'index.html', locals())
    # return render(request, 'index.html', {"ads": ads, "page": page, "type": type_page, "year": year, "month": month,
    #                                       "category_id":category_id})
    # return HttpResponse('首页')


def detail(request, article_id):
    if request.method == "GET":
        try:
            article = Article.objects.get(id=article_id)
            cf = CommentForm()
            return render(request, 'single.html', locals())
        except Exception as e:
            print(e)
            return HttpResponse("文章不合法")
    elif request.method == "POST":
        #定义页面表单的post请求表单对象含数据信息
        cf = CommentForm(request.POST)
        if cf.is_valid():
            # print(cf)
            # 先不保存，默认commit为true时保存实例，用commit=false先指明对应文章
            # 由表单的返回值 生成评论的数据模型 进行保存到数据库中
            comment = cf.save(commit=False)
            comment.article = Article.objects.get(id=article_id)
            # 在保存评论数据模型之前需要指明哪一个文章的评论
            comment.save()
            url = reverse("blogapp:detail", args=(article_id,))
            return redirect(to=url)


    # return HttpResponse("详情页"+articleid)


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse('联系我们')


def favicon(request):
    # 如果获取logo则重定向到一个图片资源
    return redirect(to="/static/favicon.ico")