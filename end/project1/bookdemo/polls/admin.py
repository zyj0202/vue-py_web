from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.
from .models import *
# 使用django自带的用户系统


class ChoiceInline(admin.StackedInline):
    '''
    定义内联表
    '''
    model  = Choices
#     关联几个
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    # 问题是一方，问题内联到选项表
    inlines = [ChoiceInline]
    pass

class ChoiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choices,ChoiceAdmin)
admin.site.register(User)