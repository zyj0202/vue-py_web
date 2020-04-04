from django.db import models

# Create your models here.
# mvt  m数据模型
# ORM  M数据模型
# 编写数据模型类
# 因为orm映射功能每一张表就是一个模型类
# 通过操作模型类实现sql语句

class Book(models.Model):
    '''
    book继承Model类 因为Model据有操作数据库的功能
    '''

    title = models.CharField(max_length=20)
    pub_date = models.DateField(default="1983-06-01")



    pass
class Hero(models.Model):
    '''
    Hero继承了models，具有操作数据库的功能
    '''
    name = models.CharField(max_length=20)
    # choices（）传入选项 有几个就传几个元组
    gender = models.CharField(max_length=5,choices=(('male','男'),('female','女')),default='male')
    content = models.CharField(max_length=100)
    # book是一对多的外键 一本书有多个英雄，on_delete为级联删除即删除主表数据时如何做
    book = models.ForeignKey(Book,on_delete=models.CASCADE)



