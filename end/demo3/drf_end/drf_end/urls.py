"""drf_end URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from shop.views import *
from django.conf.urls import url
from django.views.static import serve
from .settings import MEDIA_ROOT
# 使用drf自带的路由类
from rest_framework import routers
# 引入api文档路由
from rest_framework.documentation import include_docs_urls

# 引入restframework_jwt路由
# from rest_framework_jwt.views import obtain_jwt_token
# 引入restframework_simple 路由
from rest_framework_simplejwt.views import token_obtain_pair,token_refresh

# 通过router默认注册资源
router = routers.DefaultRouter()
# 第一个参数是前缀(资源名字一般是名词加s)，第二个是视图名字
# router.register('categorys', CategoryViewSets2,basename='category') # 模型视图集合的路由配置 最终版(自己封装了分类数据和单个分类详情数据)
router.register('categorys', CategoryViewSets,basename='category')
router.register('goods', GoodViewSets)
router.register('goodimgs', GoodImgsViewSets)
router.register('users', UserViewSets)
router.register('orders', OrderViewSets)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),
    # 配置RestFulApi
    path('api/v1/', include(router.urls)),

    # 使用函数视图的路由设置
    # url(r'^categorylist/$', categoryList, name="categorylist"),
    # url(r'^categorydetail/(\d+)/$', categoryDetail, name="categorydetail"),

    # 使用类视图的路由设置
    # url(r'^categorylist/$', CategoryListView.as_view(), name="categorylist"),
    # url(r'^^categorydetail/(\d+)/$', CategoryDetailView.as_view(), name="categorydetail"),

    # 使用混合类路由设置 访问详情页是将id取个别名pk
    # url(r'^categorylist/$', CategoryListView.as_view(), name="categorylist"),
    # url(r'^^categorydetail/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name="categorydetail"),

    # 使用模型视图集的路由设置(初级版)
    # url(r'^categorys/$', CategoryViewSets2.as_view({'get':'list','post':'create'})),
    # url(r'^categorys/(?P<pk>\d+)/$', CategoryViewSets2.as_view({'get':'retrieve','put':'update','patch':'update',\
    #                                                           'delete':'destroy'})),
    # 先通过用户名面得到Token VUE将refresh和access保存，通过access请求服务器 通过refresh获取新的access
    url(r'^obtaintoken/$',token_obtain_pair,name='obtaintoken'),
    url(r'^refresh/$',token_refresh,name='refresh'),
    url(r'^getuserinfo/$', getuserinfo),

    # 处理手机验证码
    url(r'^sendmsg/',sendmsg),
    # api文档地址
    path('api/v1/docs/', include_docs_urls(title="RestFulAPI", description="RestFulAPI v1")),
    # path('', include("shop.urls", namespace='shop'))  # django自带的分离开发不好
    # 为了在drf路由调试界面能够使用用户相关功能需要引入以下路由
    path('', include('rest_framework.urls')),


]
