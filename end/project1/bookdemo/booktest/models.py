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
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="heros")
    def __str__(self):
        return self.name+"=="

# django orm 关联查询
# 多方Hero 一方Book
# 多找一，  多方对象.跟多方的关系字段  exp: h1.book
# 一找多， 一方对象.小写多方_set.all()  exp: b1.hero_set.all() 如果定义了related_name="heros"  则在一找多时用吧b1.heros.all()
# 自定义用户管理类
class UserManager(models.Manager):
    '''
    自定义模型管理类，
    该模型不在具有objects对象
    '''
    def deleteByTelePhone(self,tele):
        # django默认的是objects，是Manager类型
        user = self.get(tel=tele)
        user.delete()
    def creatUser(self,tele):
        # 这个等于user=User()
        user = self.model()
        user.tel = tele
        user.save()
    pass

class User(models.Model):
    tel = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号码")
    # 为了习惯默认django的objects管理类 即 *.objects.all()等方法管理模型
    # 所以就实例一个管理对象为objects，这样就能User.objects.deleteByTelePhone(实参tele)，通过实参删除一个User对象
    objects = UserManager()

    def __str__(self):
        return self.tel


    class Meta:
        # 定义在数据库中的表名
        db_table = "用户类"
        # 按tel降序排
        ordering = ["id"]
        # admin进入模型类显示的名字
        verbose_name = "用户模型类a"
        # admin页面下方显示的模型名
        verbose_name_plural = "用户模型类s"

# 一方找一方时 当没有定义related_name使用 例如 a.concact.c方属性字段
# 当定义了related_name  则 a找c为 a.con.c方字段
#一对一的 关系字段可定义在任意一个一方 但需要注意类的代码位置关系
class Account(models.Model):
    username = models.CharField(max_length=20,verbose_name="用户名")
    password = models.CharField(max_length=20,verbose_name="密码")
    regist_date = models.DateField(auto_now_add=True,verbose_name="注册日期")
    # concact = models.OneToOneField(Concact,models.CASCADE)


class Concact(models.Model):
    telephone = models.CharField(max_length=11,verbose_name="手机号")
    email = models.EmailField(default="1448197724@qq.com")
    # 注意定义related_name字段的值时不要跟另一方的小写类名重复
    account = models.OneToOneField(Account,models.CASCADE,related_name="con")

# 多对多关系 多方Article 实例a 多方Tag 实例t 关系字段可定义在任意一方
class Article(models.Model):
    title = models.CharField(max_length=20,verbose_name="标题")
    sumary = models.TextField(verbose_name="正文")

class Tag(models.Model):
    name = models.CharField(max_length=10,verbose_name="标签名")
    # 多对多没有级联删除 因为一个标签可以对应多个文章，一个文章又对应对个标签
    aticles = models.ManyToManyField(Article)
    # 在shell中 t1.articles.add(a1)  t1标签就能关联到a1文章
    # 在shell中 t1.articles.add(a2)  t1标签就能关联到a2文章
    # 在shell中 t1.articles.remove(a2)  t1标签就能删除关联到的a2文章
    # 在shell中 t1.articles.all() 找t1对应的所有文章
    # 在shell中 a1.tag_set.all() 找a1对应的所有tag
