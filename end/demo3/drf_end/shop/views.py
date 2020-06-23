# from django.shortcuts import render
# from django.http import HttpResponse,JsonResponse
# from .models import *
# from django.core import serializers    # django自带的序列化
# Create your views here.
# '''
# django本身 就可以完成前后端分离开发 为前端提供json数据返回，但是django本身的序列化很麻烦，基本无用
# 可以使用DRF框架可以提供方便的序列化开发
# '''

# 这是django自带的 分离序列化 很麻烦无用
# def index(request):
#     # 前后端分离开发 返回给前端json或着xml形式的数据
#     categorys = Category.objects.all()
#     result = serializers.serialize("json", categorys)
#     return JsonResponse(result, safe=False)
#
#     # 如果使用django模板就是前后端不分离
#     # return render(request, "模板名字", "传递参数")
#     # return HttpResponse("这是首页")
###################################################################

from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse
from rest_framework.decorators import api_view,action  # api_view drf的请求
from rest_framework.response import Response  # drf的响应
from rest_framework import status

from django.shortcuts import get_object_or_404  # 得到一个对象，得不到返回404

"""
在DRF中获取参数方式：
GET方法中使用 request.query_params
POST PUT PATCH DELETE 都用request.data
"""

from django.views import View
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions  # 配置权限类
from . import permissions as mypermissions # 使用自定义的权限类

from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .throttling import Myanon,MyUser  # 自定义频次类
from .pagination import MyPagination  # 自定义分页
# 引入django的过滤类
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters  # 模糊查询


from rest_framework_simplejwt.authentication import JWTAuthentication
@api_view(["GET"])
def getuserinfo(request,):
    # print(request.headers["Authorization"])
    user = JWTAuthentication().authenticate(request)
    # print("用户",user[0])
    seria = UserSerializer(instance=user[0])
    # print("用户数据",seria.data)
    return Response(seria.data,status=status.HTTP_200_OK)


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListView2(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
    混合类 可以扩展原有类的功能，但是不继承原有类，通过查看查看混合类的代码发现
    ListModelMixin里有两个方法是GenericAPIView中写的
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # 上方两个属性等价与下方的get_queryset，get_serializer_class方法的作用
    # def get_queryset(self):
    #     return Category.objects.all()
    #
    # def get_serializer_class(self):
    #     return CategorySerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)


class CategoryDetailView2(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    """
    混合类的增删改查的类 里面的调用一些方法 都是写在了GenericAPIView类里
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def patch(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.delete(request,pk)


class CategoryListView1(APIView):
    """
    1.继承django的View类需要重写对应的http方法
    2.继承DRF自带的APIView类即可完成响应请求的封装 APIView继承封装了Django的View
    """
    def get(self,request):
        # instance是在数据库中取的数据
        queryset = Category.objects.all()
        seria = CategorySerializer(instance=queryset, many=True)
        return Response(seria.data, status=status.HTTP_200_OK)

    def post(self,request):
        # data从请求中取的数据
        seria = CategorySerializer(data=request.data)
        # if seria.is_valid():
        #     seria.save()
        #     return Response(seria.data, status=status.HTTP_200_OK)
        # else:
        #     return Response(seria.errors)

        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data, status=status.HTTP_201_CREATED)


class CategoryDetailView1(APIView):

    def get(self,request,cid):
        seria = CategorySerializer(instance=get_object_or_404(Category, pk=cid))
        return Response(seria.data, status=status.HTTP_200_OK)

    def put(self,request,cid):
        seria = CategorySerializer(instance=get_object_or_404(Category, pk=cid), data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_200_OK)

    def patch(self,request,cid):
        seria = CategorySerializer(instance=get_object_or_404(Category, pk=cid), data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_200_OK)

    def delete(self,request,cid):
        get_object_or_404(Category, pk=cid).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 通过api_view装饰器可以将基于函数的视图转换成APIView基于类的视图
@api_view(['GET','POST'])
def categoryList(request):
    if request.method == "GET":
        # print("GET请求参数",request.GET)
        queryset = Category.objects.all()
        # instance为需要序列化的对象来源于数数据库 多个分类对象用many=True
        seria = CategorySerializer(instance=queryset, many=True)
        # print(seria.data)
        return Response(seria.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        print("POST请求参数", request.POST)
        # data 为序列化对象 来源于请求中提取的数据
        seria = CategorySerializer(data=request.data)
        #从请求中提取的数据序列化之前需要进行校验
        if seria.is_valid():
            # 校验成功 保存到数据库
            seria.save()
            return Response(seria.data, status=status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def categoryDetail(request, cid):
    # 通过id找到具体的一个对象
    model = get_object_or_404(Category, pk=cid)
    if request.method == "GET":
        # print('获取参数，',request.query_params)
        seria = CategorySerializer(model)
        return Response(seria.data, status=status.HTTP_200_OK)
    elif request.method == "PUT" or request.method == "PATCH":
        # print("PUT请求参数", request.data)
        # print("PATCH请求参数", request.data)
        # 更新就是从请求中提取参数,替换掉数据库中取出的数据.instance取出来的就是数据库的原模型
        seria = CategorySerializer(instance=model, data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_200_OK)
        else:
            return Response(seria.errors, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return HttpResponse("当前路由不允许"+request.method+"操作")


class CategoryViewSets2(viewsets.ModelViewSet):
    """
    如果返回的内容就是模型列表直接用queryset
    如果需要处理  在注册路由时使用basename 并结合get_queryset方法进行数据处理
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def get_queryset(self):
    #     return Category.objects.all()[:3]

    @action(methods=['GET'],detail=False)
    def getlatestcategory(self,request):
        num = int(request.query_params.get('num'))
        seria = CategorySerializer(instance=Category.objects.all()[:num],many=True)
        return Response(data=seria.data,status=status.HTTP_200_OK)


class CategoryViewSets(viewsets.ModelViewSet):
    '''
    分类视图
    继承ModelViewSet 之后拥有 GET POST PATCH DELETE 等HTTP动词操作
    queryset 指明需要操作的模型列表
    serializer_class  指明序列化类
    '''
    queryset = Category.objects.all()
    # 1.通过属性指明序列化类
    # serializer_class = CategorySerializer
    # 2.通过方法返回序列化类 属性或着方法任选一个

    def get_serializer_class(self):
        return CategorySerializer
    # 需求是 用户没有登录不显示 分类列表 优先级别高于全局配置
    # permission_classes = [permissions.IsAdminUser]

    # 授权的前提是认证 登录过（认证过）之后进行权限判断

    # 对于超级管理员能添加分类，普通用户可以查看分类
    def get_permissions(self):
        if self.action == "create" or self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            return [permissions.IsAdminUser()] # 写在方法里需要带()指明实例
            # return [mypermissions.CategorysPermission()] # 使用自定义的权限类进行分配权限
        else:
            return []

    # 局部配置频次类 可以反爬虫
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    # 局部配置自定义的频次类
    throttle_classes = [MyUser,Myanon]
    # 局部配置自定义分页
    # pagination_class = MyPagination
    # 全局定义过滤字段
    # filterset_fields = ["name"]

    # 局部过滤配置
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["id"]


class GoodViewSets(viewsets.ModelViewSet):
    '''
    分类视图
    继承ModelViewSet 之后拥有 GET POST PATCH DELETE 等HTTP动词操作
    queryset 指明需要操作的模型列表
    serializer_class  指明序列化类
    '''
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    # 定义全局过滤字段
    # filterset_fields = ["name"]


class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerializer


class UserViewSets1(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    """
    声明用户资源类用户操作：获取个人信息 更新个人信息 删除账户
    扩展出action路由  用户操作：创建用户（使用的是注册用户序列化类）
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # 使用 action扩展资源的http方法
    # detail参数传入False时代表没有当前实例的详情路由
    @action(methods=["POST"],detail=False)
    def regist(self,request):
        seria = UserRegistSerializer(data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        # 这个注册路由的设置 因为在序列化时删除了password2 所以在这不能再获取否则会报错,但在 字段配置write_only时课获取
        # 也可以通过单独设置注册接口 实现用户的注册
        return Response(seria.data,status=status.HTTP_201_CREATED)


class UserViewSets(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    """
    声明用户资源类用户操作：获取个人信息 更新个人信息 删除账户
    扩展出action路由  用户操作：创建用户（使用的是注册用户序列化类）
    """
    queryset = User.objects.all()
    # serializer_class = UserSerializer

    def get_serializer_class(self):
        print("action代表Http方法",self.action)
        if self.action == "create":
            return UserRegistSerializer
        return UserSerializer


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [mypermissions.OrdersPermission]

    def get_permissions(self):
        """
        超级管理员只可以展示所有订单
        普通用户 可以创建修改订单 不可以操作其他用户订单
        :return:
        """
        print("http方法为",self.action)
        if self.action == "create":
            # 登录认证后能创建订单
            return [permissions.IsAuthenticated()]
        elif self.action == "update" or self.action == "partial_update" or self.action == "retrieve" or self.action == "destroy":
            # 订单对象所属用户与请求的用户为同一个 才能操作自己的订单
            return [mypermissions.OrdersPermission()]
        else:
            # 除上面的http方法外请求 需要是超级管理员权限
            return [permissions.IsAdminUser()]

# http方法                          混合类关键字             action关键字
# GET列表                           List                     get
# POST创建对象                      Create                   create
# GET单个对象                       Retrieve                  retrieve
# PUT 修改对象提供全属性             Update                    update
# PATCH修改对象提供部分属性          Update                     partial_update
# DELETE 删除对象                   Destroy                    destroy


from urllib import request
from urllib import parse
import urllib.request
import time
import hashlib
import random


def getnums():
    s = ""
    for i in range(6):
        s += str(random.randrange(0,9))
    return s


@api_view(["POST"])
def sendmsg(req):
    try:
        print(req.data)
        """
        向数据库中写入数据
        手机号 验证码 发送时间 
        """

        print("python demo starting...")

        url = "https://openapi.miaodiyun.com/distributor/sendSMS"
        accountSid = "cdc1aabbf2d445108cc13271eexxxxxx"
        to = req.data["telephone"]  # 注册人的手机号
        templateid = "3284"
        param = getnums()  # 发送的验证码
        print("发送的验证码为",param)
        auth_token = "5ecbeaa30b6c477cb77c2bedb5xxxxxx"

        t = time.time()
        timestamp = str((int(round(t * 1000))))
        sig = accountSid + auth_token + timestamp
        m1 = hashlib.md5()
        m1.update(sig.encode("utf-8"))
        sig = m1.hexdigest()

        data = "accountSid=" + accountSid + "&to=" + to + "&templateid=" + templateid + "&param=" + param + "&timestamp=" + timestamp + "&sig=" + sig;
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
        }
        data = str.encode(data);

        print("data sent to SMS server is:")
        print(data);
        req = request.Request(url, headers=headers, data=data)  # POST方法
        page = request.urlopen(req).read()
        page = page.decode('utf-8')
        print("response from SMS server is:")
        print(page)

        print("python demo finished")
        ver = Verfiy()
        ver.code = param
        ver.telephone = to
        ver.save()



        return Response("发送成功")
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

