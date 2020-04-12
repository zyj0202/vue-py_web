"""bookdemo URL Configuration

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

# 路由 网址  每一个路由都需要对应的视图函数 视图函数做返回页面内容
#  MVT  V是视图函数  三个作用：接受请求  处理数据 返回响应


# 总的路由匹配文件
urlpatterns = [
    path('admin/', admin.site.urls),
    # 使用path将booktest下的urls进行包含,命名空间的值与应用设置的应用名一致
    path('',include('booktest.urls',namespace='booktest'))

]


# 项目的所有路由地址配置文件
# admin是django自带的后台管理路由

# 一个项目的总路由匹配文件 == 项目路由文件（使用include包含应用路由文件）

# 硬编码 在html文件中很多的超链接 其中如果href写成绝对路径，就叫硬编码
# 但在开发过程中可能需要反复修改路由 所以硬编码就很不方便
# 解除硬编码方法：
# 1 在应用的路由文件中（urls.py）设置一个 app_name = "应用名"
# 2.在项目路由中给应用分流时  在include中提供命名空间 即给 namespace=
# 3 在应用中给定每个路由一个名字 即name字段
# 4.在html中使用时 href = {% '命名空间名：路由name' 实参列表%}
# django原生自带正则定位路由 靠总路由正则表达式+应用路由正则表达式
# 解除硬编码后 室友 应用命名空间+应用路由名字



