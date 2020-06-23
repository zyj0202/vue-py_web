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
"""
可以自定义权限
"""
from rest_framework import permissions


class CategorysPermission(permissions.BasePermission):
    # 视图级别的
    def has_permission(self, request, view):
        return True


class OrdersPermission(permissions.BasePermission):
    # 对象级别
    def has_object_permission(self, request, view, obj):
        # print(obj,"==",request.user)
        # print(obj.user==request.user)
        return obj.user == request.user


