#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG
# 引入路由绑定函数
from django.conf.urls import url
from . import views


app_name = 'booktest'

urlpatterns = [
    # r在正则代表原始字符串
    # 传入路由地址和视图函数,name给路由命名 解除硬编码
    # url(r'^index$',views.index),去掉index字符
    url(r'^$',views.index,name='index'),
    # url(r'^category/$',views.category,name='category'),
    # url(r'^mine/$', views.mine,name='mine'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^delete/(\d+)/$', views.deletebook, name='deletebook'),

    url(r'^deletehero/(\d+)$',views.deletehero,name='deletehero'),
    url('^addhero/(\d+)$',views.addhero,name='addhero'),
    url(r'^edithero/(\d+)$',views.edithero,name='edithero')
]



