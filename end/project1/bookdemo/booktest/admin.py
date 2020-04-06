from django.contrib import admin
# 定义后端显示页面
from django.contrib.admin import ModelAdmin
# Register your models here.
# django自带后台管理操作需要在此处实现
# 注册自己需要管理的模型 Book  Hero
from .models import Book,Hero


class HeroInline(admin.StackedInline):
    '''
    定义内联表
    '''
    model = Hero
    # 关联几个
    extra = 1

class BookAdmin(ModelAdmin):
    # 更改后端显示列
    list_display = ('title','pub_date')
    # 更改后端每页显示多少个
    list_per_page = 2
    # 定义后端能使用的搜索字段
    search_fields = ('title','pub_date')

    list_filter = ('title','pub_date')
    # 关联对应的内嵌表
    inlines = [HeroInline]
    pass



class HeroAdmin(ModelAdmin):

    list_display = ('name','gender')








admin.site.register(Book,BookAdmin)
admin.site.register(Hero,HeroAdmin)

