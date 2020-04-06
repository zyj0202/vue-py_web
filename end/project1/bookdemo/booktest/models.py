from django.db import models

# Create your models here.
# mvt  m数据模型
# ORM  M数据模型
# 编写数据模型类
# 因为orm映射功能每一张表就是一个模型类
# 通过操作模型类实现sql语句

# 有了模型类 如何实现与数据库的交互
# 1.在项目目录的settings.py中的TNSTALLED_APPS注册应用名
# 2.生成迁移文件 用于与数据库交互 python manage.py makemigrations 会在对应的应用下方生成对应的迁移文件
# 3.执行迁移 会在对应的数据库生成对应的表 python manage.py migrate



class Book(models.Model):
    '''
    book继承Model类 因为Model据有操作数据库的功能
    '''

    title = models.CharField(max_length=20)
    # price = models.FloatField(default=0)
    pub_date = models.DateField(default="1983-06-01")
    # 必须返回字符串
    def __str__(self):
        return self.title


    pass




class Hero(models.Model):
    '''
    Hero继承了models，具有操作数据库的功能
    '''
    name = models.CharField(max_length=20)
    # choices（）传入选项 有几个就传几个元组
    gender = models.CharField(max_length=6,choices=(('male','男'),('female','女')),default='male')
    content = models.CharField(max_length=100)
    # book是一对多的外键 一本书有多个英雄，on_delete为级联删除即删除主表数据时如何做
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    def __str__(self):
        return self.name+"=="

# django orm 关联查询
# 多方Hero 一方Book
# 多找一，  多方对象.跟多方的关系字段  exp: h1.book
# 一找多， 一方对象.小写多方_set.all()  exp: b1.hero_set.all()
