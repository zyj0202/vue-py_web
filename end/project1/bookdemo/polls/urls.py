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

from django.conf.urls import url
from . import views


app_name = 'polls'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^result/(\d+)/$',views.result,name='result'),
    url(r'^login/$',views.login,name="login"),
    url(r'^register/$',views.register,name="register"),
    url(r'^logout/$',views.logout,name="logout")

]


