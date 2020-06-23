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
from rest_framework import serializers
from .models import *


class CustomSerializer(serializers.RelatedField):
    """
    自定义序列化类
    """

    def to_representation(self, value):
        """
        重写字段的输出格式
        :param value: 需要序列化的对象
        :return: 显示的格式
        """
        return str(value.id) + value.name + "--" + value.desc


class GoodImgsSerializer(serializers.Serializer):
    img = serializers.ImageField()
    good = serializers.CharField(source='good.name')

    # # 校验对应的 商品存在与否
    # def validate_good(self, good):
    #     print('good为:',good)
    #     try:
    #         # 对应的商品存在
    #         g = Good.objects.get(name=good)
    #     except:
    #         raise serializers.ValidationError("输入的商品不存在")
    #     return g
    #

    def validate(self, attrs):
        print("原始值",attrs,type(attrs))
        try:
            # 找到对应的商品实例
            g = Good.objects.get(name=attrs["good"]["name"])
            print("修改了商品",g)
            # 将对应的商品实例赋给图片的good字段
            attrs["good"] = g
            print(type(attrs["good"]))
        except:
            raise serializers.ValidationError("输入的商品不存在")
        return attrs

    def create(self, validated_data):
        instance = GoodImgs.objects.create(**validated_data)
        return instance


class GoodSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=20, error_messages={
        "min_length": "最少两个字",
        "max_length": "最多20个字"
    })
    # category = CategorySerializer(label="分类") 关系字段有一方写就可以
    # 使用imgs序列化字段需要将图片的序列化类放在商品序列化类上面
    imgs = GoodImgsSerializer(label="图片",many=True, read_only=True)

    #当权限只有按已有分类添加商品时用这方法验证分类是否是已有
    def validate_category(self, category):
        """
        处理category
        :param category: 处理的原始值
        :return: 处理的新值
        """
        print('category原始值为：', category)
        try:
            Category.objects.get(name=category['name'])
        except:
            raise serializers.ValidationError("输入的分类名不存在")

        return category

    def validate(self, attrs):
        # print("收到的数据为", attrs)
        # 提交的分类存在
        try:
            c = Category.objects.get(name=attrs['category']['name'])

        # 当提交的分类不存在时
        except:
            c = Category.objects.create(name=attrs['category']['name'])
        attrs['category'] = c
        print('更改之后的实例', attrs)

        return attrs

    def create(self, validated_data):
        print("创建good参数", validated_data)
        instance = Good.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        print("原始值", instance.name, instance.category)
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance


class CategorySerializer(serializers.Serializer):
    """
    自定义序列化类，指定了序列化的细节
    """
    # read_only=True get显示 post不显示,只读
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, min_length=3, error_messages={
        "max_length": "最多10个字",
        "min_length": "最少三个字"
    })
    goods = GoodSerializer(many=True, read_only=True)

    def create(self, validated_data):
        """
        通过重写create方法 来定义模型创建方式
        :param validated_data:
        :return:
        """
        print("重写创建方法", validated_data)
        # Category.objects.create() 创建一个分类 这个方法只能传入一个参数  当前是传入字典的引用
        instance = Category.objects.create(**validated_data)
        print("创建模型实例", instance)
        return instance

    def update(self, instance, validated_data):
        """
        通过重写update，来定义模型的更新方法
        :param instance: 更改之前的实例
        :param validated_data: 更改参数
        :return: 返回的新实例
        """
        # print("原实例对象", instance, type(instance))
        # print("更改参数", validated_data)
        # 当取不到这个name键的值，使用原来的name的值
        instance.name = validated_data.get("name", instance.name)
        print("更改之后的实例", instance)
        # 将内存中的更改后的实例进行保存到数据库中
        instance.save()
        return instance


class CategorySerializer1(serializers.ModelSerializer):
    """
    编写针对category的序列化类
    本类指明了category的序列化细节
    需要继承ModelSerializer(高级类) 才可以针对模型进行序列化
    在Meta类中 model指明序列化的模型  fields 指明序列化的字段
    """
    # goods和related_name 的值一致

    # StringRelatedField可以显示关联模型中的 __str__ 返回值 many=True 代表多个对象，只有一对一时不写其他模型关关联关系时要写
    # goods = serializers.StringRelatedField(many=True)

    # 使用主键字段 要设置read_only=True 因为改商品信息一般在商品里面改
    # goods = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # 显示自定义字段值
    # goods = serializers.SlugRelatedField(slug_field="name", many=True, read_only=True)

    # 显示资源RestFulApi 资源的超链接
    # goods = serializers.HyperlinkedRelatedField(view_name="good-detail", read_only=True, many=True)

    # 自定义序列化类
    goods = CustomSerializer(many=True, read_only=True, )

    class Meta:
        model = Category
        # fields 指明序列化哪些字段，__all__ 代表模型中所有字段
        # fields = "__all__"
        fields = ("name", "goods")








class GoodSerializer1(serializers.ModelSerializer):
    # 在序列化时指定字段 在多方！使用source=关联的模型名(小写).字段名 read_only=True表示不能更改这个指定字段
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Good
        # fields = "__all__"
        fields = ("name", "desc", "category")


class UserSerializer(serializers.ModelSerializer):
    # 传到前端时 前端看不见password字段  但是前端可以传递password字段进行修改
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        # fields = "__all__"
        # 定义不想显示的用户字段名
        exclude = ["user_permissions","groups",]

    def validate(self, attrs):
        print("原生创建",attrs)
        from django.contrib.auth import hashers
        if attrs.get('password'):
            attrs["password"] = hashers.make_password(attrs["password"])
        # print("当用户更改密码，对密码进行加密成密文存到数据库")
        return attrs


class UserRegistSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10,min_length=3,error_messages={"required":"用户名必填"})
    password = serializers.CharField(max_length=10,min_length=3,error_messages={"required":"密码必填"},write_only=True)
    password2 = serializers.CharField(max_length=10,min_length=3,error_messages={"required":"重复密码必填必填"},write_only=True)
    # code = serializers.CharField(max_length=6) # 验证码校验
    # def validated_password2(self,data): #针对于单个进行判断
    #     if data != self.initial_data['password']:
    #         raise serializers.ValidationError("密码不一致")
    #     else:
    #         return data

    def validate(self, attrs):  # 能得到所有请求的数据
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("密码不一致")
        del attrs['password2']
        return attrs

    def create(self, validated_data):
        # print("提交数据",validated_data)
        return User.objects.create_user(username=validated_data.get("username"),email=validated_data.get("email"),password=validated_data.get("password"))
        # return User.objects.create(**validated_data) # 这个创建密码没加密 建议对加密的使用是上方的


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
