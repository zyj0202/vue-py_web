from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''
    自定义用户类继承django自带用户系统
    '''
    telephone = models.CharField(max_length=20,verbose_name="手机号")
    # 设置成多对多的关系 用户和问题
    questions = models.ManyToManyField('Question')


class Question(models.Model):
    '''
    投票问题类
    '''
    title = models.CharField(max_length=50,verbose_name="投票问题")
   # 创建时间
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "投票表"
        verbose_name_plural = verbose_name
        # 时间降序
        ordering = ["-create_date"]

class Choices(models.Model):
    '''
    投票选项类
    '''
    content = models.CharField(max_length=50,verbose_name="选项")
    # 正整数
    votes = models.PositiveIntegerField(verbose_name="得票数")
    create_date = models.DateField(auto_now_add=True,verbose_name="创建时间")
    # 设置选项跟问题为多对一关系
    questions = models.ForeignKey(Question,on_delete=models.CASCADE,related_name="choices",verbose_name="所属问题")

    def __str__(self):
        return self.content

    class Meta:
        # 时间降序
        verbose_name = "选项表"
        verbose_name_plural = verbose_name
        ordering = ["-create_date"]

# 最好呢 先将模型需要对数据库的相关信息代码写完整，再生成并执行迁移文件






