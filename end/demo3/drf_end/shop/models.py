from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 设计完模型类 将开发的应用注册到项目的settings中

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="分类名")

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=20, verbose_name="商品名字")
    desc = models.CharField(max_length=100, null=True, blank=True, verbose_name="商品描述")
    #在序列化关联模型时一定要声明related_name
    # 一照多 related_name没定义 c1.good_set.all()  related_name定义了 c1.定义的值.all() c1.goods.all()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类", related_name="goods")

    def __str__(self):
        return self.name

# 商品跟商品的图片 一对多关系
class GoodImgs(models.Model):
    img = models.ImageField(upload_to='goodimg', verbose_name="商品展示图")
    good = models.ForeignKey(Good,on_delete=models.CASCADE,verbose_name="商品",related_name="imgs")

    def __str__(self):
        return self.good.name


class User(AbstractUser):
    telephone = models.CharField(max_length=11,verbose_name="手机号")


class Order(models.Model):
    """
    简单模拟 一个订单 只有一个商品 没有数量
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    goods = models.ManyToManyField(Good, verbose_name="商品")

    def __str__(self):
        return self.user.username+"的订单"


# 注册用的验证码校验类
class Verfiy(models.Model):
    code = models.CharField(max_length=6)
    telephone = models.CharField(max_length=11,unique=True)
    createTime = models.DateTimeField(auto_now_add=True)