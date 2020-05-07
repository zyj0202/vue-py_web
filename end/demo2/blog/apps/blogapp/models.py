from django.db import models
# 导入前需要将两个文件夹（apps和extra_apps）表示为根目录 即sources root
from DjangoUeditor.models import UEditorField
# Create your models here.
'''
轮播图
分类表
标签表
文章表
评论表

分类和文章一对多关系，将关系字段定义在多方为外键
文章和评论为一对多关系，将关系字段定义在多方为外键
文章个标签为多对多关系，关系字段课定义在任意一方 
'''
#使用图片字段需要安装pillow模块

class Ads(models.Model):
    # upload_to 指图片的保存地址，不写默认根目录
    img = models.ImageField(upload_to='ads',verbose_name='图片')
    desc = models.CharField(max_length=20,null=True,blank=True,verbose_name='图片描述')

    def __str__(self):
        return self.desc


class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name='分类名')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='标签名')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name="文章标题")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    create_name = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_name = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    author = models.CharField(max_length=20, verbose_name='作者')
    views = models.PositiveIntegerField(default=0, verbose_name='浏览量')
    # body = models.TextField(verbose_name="正文")
    #使用百度ueditor 富文本字段类型
    body = UEditorField(imagePath='imgs/', width='100%')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name="评论人")
    url = models.URLField(default="http://www.zyj.com", verbose_name="个人主页")
    email = models.EmailField(default="965511759@qq.com", verbose_name="个人邮箱")
    body = models.CharField(max_length=500, verbose_name="评论内容")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="所属文章")

    def __str__(self):
        return self.name
