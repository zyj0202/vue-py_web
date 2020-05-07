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
from django.template import Library
from ..models import Article,Category,Tag
'''
自定义过滤器标签方法
'''
# 注册过滤器
register = Library()
@register.filter
def dateFormat(data):
    return "%d-%d-%d"%(data.year, data.month, data.day)
# 自定义过滤器
@register.filter
def authorFormat(author, info):
    return info+":"+author.upper()

# 注册自定义标签（在模板中不可继承）
@register.simple_tag
def get_laestarticles(num=3):
    return Article.objects.all().order_by("-create_name")[:num]

@register.simple_tag
def get_latest_dates(num=2):
    # 查看框架的源码dates() 可看见参数说明 DESC降序排序
    dates = Article.objects.dates("create_name", "month", "DESC")[:num]
    print(dates)
    return dates

@register.simple_tag
def get_categoys():
    return Category.objects.all().order_by("-id")

@register.simple_tag
def get_tags():
    return Tag.objects.all().order_by("-id")