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
from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150,label="输入用户名",help_text="最大150")
    password = forms.CharField(max_length=20,min_length=6,widget=forms.PasswordInput,help_text="密码最少6位，最长20",label="输入密码")

# 根据模型构建表单类
class RegistForm(forms.ModelForm):
    '''
    定义一个注册表单生成html表单
    '''
    password2 = forms.CharField(widget=forms.PasswordInput,label="重复密码")
    class Meta:
        # 关联到的模型
        model = User
#        关联到模型的字段有哪些
        fields = ["username","password"]
        # 键需要是关联的模型的字段
        labels = {
            "username":"输入用户名",
            "password":"输入密码"
        }

        help_texts = {
            "username": "长度<150",
            "password": "长度>=6"
        }
        # 更改密码的约束，默认为charfield
        widgets = {
            "password":forms.PasswordInput
        }





