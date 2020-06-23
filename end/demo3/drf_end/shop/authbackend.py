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
from django.contrib.auth import backends
from .models import User
from django.db.models import Q
"""
自定义认证类(对登录内容使用用户名邮箱或着电话都能登录)
重写django的认证方式
"""


class MyLoginBackend(backends.BaseBackend):
    def authenticate(self, request, **kwargs):
        print(kwargs,"认证参数")
        username = kwargs["username"]
        password = kwargs["password"]
        # 返回的是查询集所以取第一个
        # user = User.objects.filter(username=username).first()
        # if not user:
        #     user = User.objects.filter(email=username).first()
        #     if not user:
        #         user = User.objects.filter(telephone=username).first()
        # Q方法可放查询语句省去if语句
        user = User.objects.filter(Q(username=username)|Q(email=username)|Q(telephone=username)).first()
        # django自带的校验密码方法
        b = user.check_password(password)
        if b:
            return user
        else:
            None