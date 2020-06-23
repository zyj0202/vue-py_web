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
# sum函数求1-100的和
# print(sum(range(1, 101,1)))
# str1 = "qwertyuiop"
# for i in range(len(str1)):
#     print(str1[i])
# print(sum((2, 4, 6), 1)) sum求和函数,将可迭代对象的每一个元素相加,再在计算总和后加后面一个参数1


# *****2.在函数内部修改全局变量,需要在函数内部使用global声明变量
# a = 5
# def fn1():
#     global a
#     a=4
# fn1()
# print(a)

# *****3.python 5个标准库
# os： 提供了与操作系统相关联的函数
# sys: 常用于命令行参数
# re：正则匹配
# math：数学运算
# datetime：处理日期时间

# 4.字典操作删除和合并 字典的键是不可变数据类型(字符串，数字，元组)且唯一 字典是可变容器模型
# 如果同一键被赋值两次 则后一次赋值有效
# dict1 = {'a':1,'b':2,'c':3}
# del dict1['b']  # 删除字典的某个键
# print("删除键b后",dict1)
# dict1['b'] = 2 # 给字典添加一个键
# print("增加键b后",dict1)
# dict1['a'] = 11 # 修改字典的一个键
# print(dict1)
# dict1.clear() # 清空字典内的所有键值对
# print(dict1)
# del dict1 # 删除字典
# print(dict1)
# for i,j in dict1.items(): # 取到字典的所有键值
#     print(i,j) # i为键 j为值
# x = dict1.pop('a') # 删除一个键，并将这个键原来的值返回
# print(x)
# del dict1['a']
# for i in dict1.keys(): # 取到字典的所有键
#     print(i)


# *****5.enumerate() 将一个可遍历的数据对象(list、tuple、或着字符串)同时列出数据和数据索引,参数start为指定索引为多少开始
# ls1 = [1,2,3,4]
# for i,j in enumerate(ls1,start=0):
#     print(i,j)


# 6.python的GIL锁
# GIL是python的全局解释器锁，同一进程如果有多个线程运行，一个线程运行python程序的时候会霸占python解释器(加了一把锁即GIL)
# 导致该进程内的其他线程无法运行，等该线程运行完成后其他线程才能运行。  如果线程运行过程遇到耗时操作，则解释器锁解开，使其他
# 线程运行，所以多线程中，线程的运行仍是有先后顺序的，并不是同时运行。
#
# 多进程中能因为每个进程都能分配系统资源，即每个进程都有一个python解释器，多进程能实现多个进程同时运行，缺点是进程消耗系统资源大


# 7.python实现列表去重的方法
# ls1 = [1,1,2,3,4,2]
# ls1 = set(ls1) #set集合去重
# print(ls1)
# ls1 = [x for x in ls1]  # 列表生成式
# print(ls1)


# 8.fun(*args,**kwargs)中 *args和**kwargs什么意思？
# *args和**kwargs主要用于函数的定义，可以将不定数量的参数传递给一个函数。
# 因为*能拆开一个数列中的所有值，并且将这些数值作为位置参数传给函数调用
# *args将参数打包成元组给函数体调用

# **kwargs 作用是将参数打包成字典给函数体调用
# args，*args，**kwargs 三个参数的位置是一定的必须是这个顺序


# 9.py2和py3的range(100)区别
# py2返回列表，py3返回迭代器节约了内存。

# py2的  print是一个类 py3的print() 是个函数
# py3的input得到的是str，py2的input得到的数据为int，raw_input得到的是str类型数据


# *****10.python内建数据类型
# 整形，int
# 字符串，str
# 列表，list
# 字典，dict
# 元组，tuple
# 布尔，bool


# *****11. __init__  和 __new__区别？
# __init__ 是实例的初始化方法，即将new方法开辟出的内存空间进行初始化操作，创建对象后，就立刻默认调用了，可接受参数
# __new__ 创建类实例的方法，实例化对象(开辟出新的内存空间),是类级别的方法,是个静态方法，必须要有返回值，返回实例化出来的实例


# 12.with方法干了啥？
# 打开文件在进行读写的时候可能会出现一些异常状况，如果按照常规的f.open写法，我们需要try,except,finally，做异常判断，
# 并且文件最终不管遇到什么情况，都要执行finally f.close()关闭文件，with方法帮我们实现了finally中f.close
# with open('./with_test.txt','w') as f:
#     f.write("with_test")


# 13. 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
# map()的第一个参数是函数，第二个一般是list，第三个可以写列表也可不写。py2返回列表，py3返回迭代器
# list1 = [1, 2, 3, 4, 5]
# def fn(x):
#     return x**2
#
# result = map(fn,list1)
# result = map(lambda x:x**2,list1) # 使用lambda匿名函数
# # print(result) # 返回迭代器
# result = [x for x in result if x > 10] # 列表推导式生成列表
# print(result)


# 14.python生成随机整数、随机小数、0-1之间小数方法
# import random
# random.randint(a,b)生成区间的整数能取到a，b的值
# x = random.randint(1,3)
# print(x)
# x = random.random() # 在0-1之间的小数可不写参数
# print(x)
# import numpy as np
# res = np.random.randn(5) # 使用numpy库生成五个随机小数


# 15.去转义的字母
# r'' 表示需要原始字符，不转义特殊字符


# 16.<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
# import re
# finall() 是匹配所有，match和search是匹配一次
# str = '<div class="nam">中国</div>'
# res = re.findall(r'<div class=".*">(.*?)</div>',str)
# print(res)


# 17.一行代码实现9*9乘法表
# print ("\n".join("\t".join(["%s*%s=%s" %(x,y,x*y) for y in range(1, x+1)]) for x in range(1, 10)))


# 18.数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句
# select distinct name from student


# *****19.Linux常用命令
# ls 显示当前路径下的文件或目录
#     -l 列出文件详细信息l(list)
#     -a 列出当前目录下所有文件及目录，包括隐藏的a(all)
# pwd 显示当前目录路径
# cd 切换目录
# touch 创建空文件
# rm 删除文件
#     -r 递归删除，可删除子目录及文件
#     -f 强制删除
# rmdir 删除空目录
# mkdir 创建目录
#     -p 创建目录，若无父目录，则创建p(parent)
# tree 树形结构显示目录
# cp 拷贝
# mv 移动或重命名
# cat 查看文件内容
# more 分页显示文本文件内容
# grep   在文本文件中查找某个字符
# echo 创建带有内容的文件
# find 在文件系统中搜索某文件

# 打包压缩相关命令
# gzip
# bzip2
# tar: #打包压缩
#      -c  归档文件
#      -x  解档文件
#      -z  gzip压缩文件
#      -j  bzip2压缩文件
#      -v  显示压缩或解压缩过程 v(view)
#      -f  使用档名
# tar -cvf /home/abc.tar /home/abc      只打包，不压缩
# tar -zcvf /home/abc.tar.gz /home/abc   打包，并用gzip压缩
# tar -jcvf /home/abc.tar.bz2 /home/abc   打包，并用bzip2压缩
# 解压缩将上面压缩命令中的参数c换成x
#
# vim 使用
# vim三种模式：命令模式、插入模式、编辑模式。使用Esc或着i或着：来切换模式
# 命令模式下：
    # :q  退出
    # :q! 强制退出，但是不保存修改
    # :wq 保存修改并退出
    # :set number 显示行号
    # :set nonumber 隐藏行号
    # /apache 在文档中搜索apache 按n跳到下一个，shift+n上一个
    # yyp 复制光标所在行，并粘贴


# *****20. 可变与比不可变数据类型
# 不可变数据类型： 数值型,str,tuple 其中元组tuple型是tuple的引用不可变，而不是里面的值不可变
# 不可变数据类型的相同值的对象在内存中只有一个地址，改变了原变量的值相当于新创建了一个对象
# a = 3
# b = 3
# print("a的内存地址为：%s,b的内存地址为：%s"%(id(a),id(b)))

# 可变数据类型： 列表list、字典dict
# 允许变量的值发生变化，如果对变量进行append、+=等这种操作后，只是改变了变量的值，而不会新创建对象，变量引用的
# 对象的地址也不会发生变化，但对于相同的值的对象会分配不同的内存地址。


# 21.s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
# set集合对字符串进行去重处理，再转换成列表进行排序
# s = "ajldjlajfdljfddd"
# s = set(s)
# print("去重后的字符串为",s)
# s = list(s)
# print('原列表',id(s))
# print("转成列表",s)
# sort() #是list的方法返回值是在原来列表上进行操作，sorted()是可以对所有的可迭代对象的方法返回新的list对象
# s.sort(reverse=False)  #默认情况下reverse=False 升序   =True是降序
# print('id',id(s))
# print('id:',id(sorted(s)))
# string.join(seq) 将string作为分隔符，将seq中的所有元素(的字符串表示)合并成一个新的字符串，这里是将排序的列表的每个元素用''合并
# res = ''.join(s)
# print(res)


# 22.字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"
# import re
# a = "not 404 found 张三 99 深圳"
# list1 = a.split(" ")
# print(list1)
# res = re.findall('\d+|[a-zA-Z]+',str(list1))
# print(res,type(res))
# for i in res:
#     list1.remove(i)
# print('new_list',list1)
# str = ''.join(list1)
# print("正确输出",str)


# 23.filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter()第一个参数为方法，第二个参数是可迭代对象，该方法返回的是一个迭代器对象
# a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def fn(s):
    # return s % 2 == 1
# new_list = filter(fn,a)
# new_list = list(new_list) # 可以将迭代器对象转换成列表
# new_list = [i for i in new_list] # 也可以使用列表推导式
# print(new_list)


# 24.列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list1 = [i for i in a if i%2==1]
# print(list1)


# 25.re.compile作用
# re.compile是将正则表达式编译成一个对象，加快速度，并且重复使用


# 26.a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
# a = (1,) # 元组类型
# b = (1) # int类型
# print(type(b))
# c = ("1") # str类型
# print(type(c))


# 27.两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,5,6,7,8,9]
# extend() 可以将另一个集合的元素逐一从列表的末尾添加到列表中，区别于append整体添加
# list1 = [1,5,7,9]
# list2 = [2,2,6,8]
# list1.extend(list2) # 合并两个列表
# list1.sort() # 排序两个列表
# print(list1)


# 28.用python删除文件和用linux命令删除文件方法
# python： os.remove(文件名)
# linux： rm 文件名


# 29.log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
# import datetime
# a = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' 星期：'+str(datetime.datetime.now().isoweekday())
# print(a)


# *****30.数据库的优化方法
# 外键、索引、联合查询、选择特定字段等等
# 尽量避免使用select * 能用字段名就用字段名。避免查询无用字段
# select count(*)会查全表 尽量避免
# 建表时字段类型能用varchar/nvarchar就不要用char/ncahr
# 避免频繁的创建和删除临时表 会耗费性能资源 产生大量log
# 如果使用临时表 在使用的最后一定要显示删除 先trancate table 再drop table
# 尽量避免大事务操作，提高并发效率
# 避免向客户端返回大数据量 数据量过大 应考虑需求是否合理
# 比如你在一个在线网站使用delete和update操作。必然会引发数据库锁


# *****31.自定义一段异常代码
# 当触发异常后在异常代码后的代码将不再执行了
# def fn():
#     try:
#         for i in range(5):
#             print("进入循环")
#             if i>2:
#                 raise Exception("数字大于2了")
#     except Exception as e: # 常规错误的基类
#         print(e)
#     except SyntaxError as e:  # 语法错误异常
#         print(e)
#     except ZeroDivisionError as e: # 取模
#         print(e)
#     except AttributeError as e: #对象没有这个属性
#         print(e)
#
# fn()


# 32.正则表达式匹配中，（.*）和（.*?）匹配区别？
# （.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配
# （.*?）是非贪婪匹配，会把满足正则的尽可能少匹配
# s = "<a>哈哈</a><a>呵呵</a>"
# import re
# res1 = re.findall("<a>(.*)</a>",s)
# print("这是贪婪模式",res1)
# res2 = re.findall("<a>(.*?)</a>",s)
# print("这是去贪婪模式",res2)


# 33.简述django的orm
# ORM，全拼Object-Relation Mapping，意为对象-关系映射
# 实现了数据模型和数据库的解耦，通过简单配置就能轻松更换数据库，而不需要修改代码只需要面向对象编程。
# orm的本质是会根据对接的数据库引擎，翻译成对应的sql语句，如果数据迁移，只需要更换django的数据库引擎即可。

#         models.py             ORM                  数据库
# 定义模型类，通过属性      在orm中根据模型类生成        mysql
# 体现对象间的关系           与表的对应关系             sqlite等关系型数据库
#
# 调用模型类对象的save()      生成update、insert语句
# 调用模型类对象的Delete()    生成delete语句
# 调用模型类对象的all()、get()    生成select语句


# 33.[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
# ls = [[1,2],[3,4],[5,6]]
# res = [j for i in ls for j in i]
# print(res)


# 34.x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
# join()括号里面的是可迭代对象，x插入可迭代对象中间
# x="abc"
# y="def"
# z=["d","e","f"]
# print(x.join(y)) # 输出结果为 dabceabcf
# print(x.join(z)) # 输出结果为 dabceabcf
# os.path.join("root","test","test.txt") # 将文件个目录合成一个路径
# os.path.spilt("root/text.txt")  # 分割该路径的目录和文件名


# *****35.举例说明异常模块中try except else finally的相关意义
# try..except..else没有捕获到异常，执行else语句
# try..except..finally不管是否捕获到异常，都执行finally语句


# 36.python交换两个数值
# 方法一：
# a,b = 3,4
# print(a,b)
# b,a = a,b
# print("a:",a,"b:",b)

# 方法二：
# a,b = 3,4
# temp = a
# a = b
# b = temp
# print("a:",a,"b:",b)

#方法三：
# a,b = 3,4
# a = a+b
# b = a-b
# a = a-b # 等价于 a = a+b-a
# print(a,b)

# 方法四：
# 异或运算，将两值互换。  二进制异或门原理 全1出0  全0出1 有1出1
# a,b = 3,4
# a = a^b
# b = a^b # a^b^b
# a = a^b
# print(a,b)


# 37.a="张明 98分"，用re.sub，将98替换为100
# import re
# a="张明 98分"
# res = re.sub(r"\d+","100",a)
# print(res)


# 38.五条常用sql语句
# show databases; 查看数据库
# use 数据库名; 选择该数据库
# show tables; 查看当前数据库下的表
# desc 表名; 降序
# select 字段名 from 表名;  从表中查某字段
# delete from 表名 where id=5 删除当前表中的id=5 的记录
# update 表名 set 字段1=xx,字段2=xx where id=5  更新表中id=5的记录的信息


# 39.a="hello"和b="你好"编码成bytes类型
# a = "hello"
# b = "你好"
# a = b'hello'
# b = b.encode()  # encode() 默认编码格式为utf-8进行编码
# decode() 传入encoding='编码格式'  指定编码格式进行解码
# print(a,type(a),b,type(b))


# 40.两个列表相加相当于 extends() list1+list2 相当于list1.extend(list2)


# 41.提高python运行效率的方法
# 1、使用生成器，因为可以节约大量内存
# 2、循环代码优化，避免过多重复代码的执行
# 3、核心模块用Cython  PyPy等，提高效率
# 4、多进程、多线程、协程
# 5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率


# 49、简述mysql和redis区别
# redis： 内存型非关系数据库，数据保存在内存中，速度快
# mysql：关系型数据库，数据保存在磁盘中，检索的话，会有一定的Io操作，访问速度相对慢


# 50.遇到bug如何处理？
# 1、细节上的错误，通过print（）打印，能执行到print（）说明一般上面的代码没有问题，分段检测程序是否有问题，如果是js的话可以alert或console.log
# 2、如果涉及一些第三方框架，会去查官方文档或者一些技术博客。
# 3、对于bug的管理与归类总结，一般测试将测试出的bug用teambin等bug管理工具进行记录，然后我们会一条一条进行修改，修改的过程也是理解业务逻辑和提高自己编程逻辑缜密性的方法，我也都会收藏做一些笔记记录。
# 4、导包问题、城市定位多音字造成的显示错误问题


# 51.list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
# 利用min()方法求出最小值，原列表删除最小值，新列表加入最小值，递归调用获取最小值的函数，反复操作。
# import time
# start_t = time.time()
# list1 = [2,3,5,4,9,6]
# new_list = []
# def get_min(list):
    # 获取列表的最小值
    # a = min(list)
    # 将原列表的最小值删除
    # list.remove(a)
    # 将最小值添加进列表
    # new_list.append(a)
    # 保证列表里有值，递归调用最小值函数，直到所有的值获取完，并加入新列表返回
#     if len(list)>0:
#         get_min(list)
#     return new_list
# time.sleep(1)
# new_list = get_min(list1)
# end_t = time.time()
# t = end_t-start_t
# print(new_list,t)


# ******52.常见状态码即意义
# 200 OK 请求正常处理完毕
# 204 No Content 请求成功处理，没有实体的主体返回
# 206 Partial Content GET范围请求已成功处理
# 301 Moved Permanently 永久重定向，资源已永久分配新URI
# 302 Found 临时重定向，资源已临时分配新URI
# 303 See Other 临时重定向，期望使用GET定向获取
# 304 Not Modified 发送的附带条件请求未满足
# 307 Temporary Redirect 临时重定向，POST不会变成GET
# 400 Bad Request 请求报文语法错误或参数错误
# 401 Unauthorized 需要通过HTTP认证，或认证失败
# 403 Forbidden 请求资源被拒绝
# 404 Not Found 无法找到请求资源（服务器无理由拒绝）
# 500 Internal Server Error 服务器故障或Web应用故障
# 503 Service Unavailable 服务器超负载或停机维护


# 53.分别从前端、后端、数据库阐述web项目的性能优化？
# 前端优化：
# 1、减少http请求、例如制作精灵图
# 2、html和CSS放在页面上部，javascript放在页面下面，因为js加载比HTML和Css加载慢，所以要优先加载html和css,以防页面显示不全，性能差，也影响用户体验差
#
# 后端优化：
# 1、缓存存储读写次数高，变化少的数据，比如网站首页的信息、商品的信息等。应用程序读取数据时，一般是先从缓存中读取，如果读取不到或数据已失效，再访问磁盘数据库，并将数据再次写入缓存。
# 2、异步方式，如果有耗时操作，可以采用异步，比如celery
# 3、代码优化，避免循环和判断次数太多，如果多个if else判断，优先判断最有可能先发生的情况
#
# 数据库优化：
# 1、如有条件，数据可以存放于redis，读取速度快
# 2、建立索引、外键等


# 54.字典的删除键操作，del 和 pop()
# dic ={"name":"zs","age":12}
# x=dic.pop("name")  # pop()删除指定键的值，并返回该值
# print(dic,x)
# del dic['name']
# print(dic)


# 55.列出常见MYSQL存储引擎
# InnoDB：支持事务处理，支持外键，支持崩溃修复能力和并发控制。如果需要对事务的完整性要求比较高（比如银行），
# 要求实现并发控制（比如售票），那选择InnoDB有很大的优势。如果需要频繁的更新、删除操作的数据库，也可以选择InnoDB，
# 因为支持事务的提交（commit）和回滚（rollback）。 

# MyISAM：插入数据快，空间和内存使用比较低。如果表主要是用于插入新记录和读出记录，那么选择MyISAM能实现处理高效率。
# 如果应用的完整性、并发性要求比 较低，也可以使用。

# MEMORY：所有的数据都在内存中，数据的处理速度快，但是安全性不高。如果需要很快的读写速度，
# 对数据的安全性要求较低，可以选择MEMOEY。它对表的大小有要求，不能建立太大的表。所以，这类数据库只使用在相对较小的数据库表。


# 56.简述同源策略
# 同源策略需要同时满足以下三点要求： 
# 1）协议相同 
# 2）域名相同 
# 3）端口相同 
#  http:www.test.com与https:www.test.com 不同源——协议不同 
#
#  http:www.test.com与http:www.admin.com 不同源——域名不同 
#
#  http:www.test.com与http:www.test.com:8081 不同源——端口不同
#  只要不满足其中任意一个要求，就不符合同源策略，就会出现“跨域”


# 57.简述cookie和session的区别
# 1，session 在服务器端，cookie 在客户端（浏览器）
# 2、session 的运行依赖 session id，而 session id 是存在 cookie 中的，也就是说，如果浏览器禁用了 cookie ，
# 同时 session 也会失效，存储Session时，键与Cookie中的sessionid相同，值是开发人员设置的键值对信息，进行了base64编码，过期时间由开发人员设置
# 3、cookie安全性比session差


# 58.多进程多线程
# 进程：
# 1、操作系统进行资源分配和调度的基本单位，多个进程之间相互独立
# 2、稳定性好，如果一个进程崩溃，不影响其他进程，但是进程消耗资源大，开启的进程数量有限制
#
# 线程：
# 1、CPU进行资源分配和调度的基本单位，线程是进程的一部分，是比进程更小的能独立运行的基本单位，一个进程下的多个线程可以共享该进程的所有资源
# 2、如果IO操作密集，则可以多线程运行效率高，缺点是如果一个线程崩溃，都会造成进程的崩溃
#
# 应用：
# IO密集的用多线程，在用户输入，sleep 时候，可以切换到其他线程执行，减少等待的时间
# CPU密集的用多进程，因为假如IO操作少，用多线程的话，因为线程共享一个全局解释器锁，当前运行的线程会霸占GIL，其他线程没有GIL，就不能充分利用多核CPU的优势


# 59.IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常
# IOError：输入输出异常
# AttributeError：试图访问一个对象没有的属性
# ImportError：无法引入模块或包，基本是路径问题
# IndentationError：语法错误，代码没有正确的对齐
# IndexError：下标索引超出序列边界
# KeyError:试图访问你字典里不存在的键
# SyntaxError:Python代码逻辑语法出错，不能执行
# NameError:使用一个还未赋予对象的变量


# 60.python中copy和deepcopy区别
# 1、在处理可变数据时，赋值是默认浅拷贝传递对象的引用，被赋值的对象会随着原对象的改变而改变。
#   浅copy，开辟出新的内存空间，并且只copy父级对象,对于子对象的内存空间是源对象的内存引用
#   深copy，开辟出新的内存空间，拷贝对象里的所有对象即父级对象和子对象。
#   如果源对象只有顶级对象时，源做任何改动，都不影响深浅拷贝。
#   如果源对象，不止顶级对象时，还有嵌套的对象时，源做任何改动，都会影响浅拷贝，但不影响深拷贝。
# import copy
# a=["haha",'1']
# a=[['a'],'b','c']
# b=a
# c=copy.copy(a)
# d=copy.deepcopy(a)
# print("a的id：%s，b的id：%s，c的id：%s，d的id：%s"%(id(a),id(b),id(c),id(d)))
# a[0].append('a')
# print(a,b,c,d)
# print("a的id：%s，b的id：%s，c的id：%s，d的id：%s"%(id(a),id(b),id(c),id(d)))


# 61.列出几种魔法方法并简要介绍用途
# __init__:对象初始化方法
# __new__:创建对象时候执行的方法，单例模式会用到
# __str__:当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
# __del__:删除对象执行的方法


# 62.请将[i for i in range(3)]改成生成器
# 生成器是特殊的迭代器，
# 1、列表表达式的[]改为()即可变成生成器
# 2、函数在返回值得时候出现yield就变成生成器，而不是函数了；


# 63.a = "  hehheh  ",去除首尾尾空格
# 去除首尾空格方法 strip(), strip("x1")只要头尾 包含x1字符就删除
# a = "  hehheh  "
# print(a.strip())
# b="xx1xassx1xx"
# print(b.strip("x1"))


# 64.使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为
# [0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# a = sorted(foo,key=lambda x:(x<0,abs(x)))  # abs() 取绝对值函数
# print(a)


# 65.列表嵌套字典的排序，分别根据年龄和姓名排序
# foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]
# res = sorted(foo,key=lambda x:x["age"],reverse=True)  # reverse为True时降序排序，sorted()返回新列表
# print(res)
# res = sorted(foo, key=lambda x:x["name"],reverse=False)
# print(res)


# 66.列表嵌套元组，分别按字母和数字排序
# foo = [("zs",19),("ll",54),("wa",17),("df",23)]
# res = sorted(foo,key=lambda x:x[1])
# print("按年龄排序",res)
# res = sorted(foo,key=lambda x:x[0])
# print("按字母排序",res)


# 67.列表嵌套列表排序，年龄数字相同怎么办？
# foo = [("zs",19),("ll",54),("wa",17),("df",23),("xf",23)]
# res = sorted(foo,key=lambda x:(x[1],x[0])) # 先按数字排，如果重复再将重复的按字母排
# print(res)


# 68.s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
# import re
# s="info:xiaoZhang 33 shandong"
# res = re.split(r":| ",s)  # |表示或，按照：或着空格分
# print(res)


# 69.正则匹配以163.com结尾的邮箱
# import re
# email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
# for email in email_list:
#     res = re.match("[\w]{4,20}@163\.com$",email)
#     if res:
#         print(email,res.group())
#     else:
#         print("不是163结尾")


# 70.递归求和
# 递归完成1+2+3+......+100的和
# def get_sum(num):
#     if num>=1:
#         res=num+get_sum(num-1)
#     else:
#         res=0
#     return res
# res=get_sum(100)
# print(res)


# 71.python字典和json字符串相互转化方法
# json.dumps()字典转json字符串，json.loads()json转字典
# json的特点
# 1. 字符串外边有单引号
# 2. json是类字典的形式，里面的键-值对规定必须使用双引号，值如果是数字可以不加双引号，
# 但是键必须是双引号引起来的字符串， json的值可以是普通变量，数组，json对象
# 缺点：
# json只有null、布尔、数字、字符串、数组和对象这几种数据类型,JSON没有日期类型


# 72.用两种方法去空格
# str = "haha hehe qwe r"
# res =str.replace(" ","")
# print("方法一",res)
# res = str.split(" ")
# res = "".join(res)
# print("第二种方法",res)


# 73.python的引用计数机制
# python的垃圾回收主要以引用计数为主，标记-清除和分代清除为辅的机制，其中标记清除和分代回收主要是为了解决处理循环引用的难题
# 引用计数算法
# 当有一个变量保存了对象的引用，则该对象的引用计数就会加1。
# 当使用del删除变量指向的对象时，如果对象的引用计数不为1，则只会使这个对象的引用计数减掉1，直到该对象的引用计数为1时，
# 再调用一次del就会真的把对象进行删除。
# import sys
# class Animal():
#     def __init__(self,name):
#         print("init被调用")
#         self.name=name
#
#     def __del__(self):
#         print("del在对象对删除时调用")
#         print("%s对象被删除了"%self.name)
#
# cat = Animal("中华田园猫")
# c1 = cat
# c2 = cat
# print(id(cat),id(c1),id(c2))
# del c1
# print(id(c2))
# print(sys.getrefcount(cat)) # 显示对象的被引用次数


# 74.在正则中findall结果无需加group()因为该方法返回的是一个列表，,search需要加group()提取
#

# 75.简述乐观锁，悲观锁。
# 悲观锁, 就是很悲观，每次去拿数据的时候都认为别人会修改，所以每次在拿数据的时候都会上锁，这样别人想拿这个数据就会block直到它拿到锁。
# 传统的关系型数据库里边就用到了很多这种锁机制，比如行锁，表锁等，读锁，写锁等，都是在做操作之前先上锁。
#
# 乐观锁，就是很乐观，每次去拿数据的时候都认为别人不会修改，所以不会上锁，但是在更新的时候会判断一下在此期间别人有没有去更新这个数据，
# 可以使用版本号等机制，乐观锁适用于多读的应用类型，这样可以提高吞吐量


# 76.r、r+、rb、rb+文件打开模式区别
# r 以只读方式打开文件
# r+ 打来一个文件可用于读写
# rb 以二进制格式打开一个文件用于只读
# w 打开一个文件只用于写入，如果该文件以存在则将其覆盖，不存在则创建新文件。

# 77.Linux命令重定向 > 和 >>
# Linux 允许将命令执行结果 重定向到一个 文件
# 将本应显示在终端上的内容 输出／追加 到指定文件中
# > 表示输出，会覆盖文件原有的内容
# >> 表示追加，会将内容追加到已有文件的末尾
# 用法示例：
# 将 echo 输出的信息保存到 1.txt 里echo Hello Python > 1.txt
# 将 tree 输出的信息追加到 1.txt 文件的末尾tree >> 1.txt


# 78.正则表达式匹配出<html><h1>www.itcast.cn</h1></html>
# # 前面的<>和后面的<>是对应的，可以用此方法
# import re
# label = ["<html><h1>www.itcast.cn</h1></html>","<html><h1>www.itcast.cn</h2></html>"]
# for i in label:
#     res = re.match(r"<(\w*)><(\w*)>.*?</\2></\1>",i)
#     if res:
#         print(res,type(res),res.group())


# 79.python传参数是传值还是传址？
# Python中函数参数是引用传递（注意不是值传递）。
# 对于不可变类型（数值型、字符串、元组），因变量不能修改，所以运算不会影响到变量自身；
# 而对于可变类型（列表字典）来说，函数体运算可能会更改传入的参数变量。
# b=2
# def fn(a,c):
#     global b
#     b+=1
#     a+=1
#     c+=c
# a = 1
# c=[1,2]
# print("初始变量a",a,"初始变量c",c)
# fn(a,c)
# print("传递到方法里更改后a",a,b,"传递到方法里更改后c",c)


# 80.104、常见的网络传输协议
# UDP、TCP、FTP、HTTP、SMTP等等


# 81.lambda匿名函数好处
# 精简代码，lambda省去了定义函数，map省去了写for循环过程
# a=["x1","x2","","","x3",""]
# res = list(map(lambda x:"填充值" if x=="" else x ,a))
# print(res)


# 82.HTTP请求中get和post区别
# GET和POST是HTTP协议的两种请求方法。
# HTTP是基于TCP/IP的关于数据如何在万维网中如何通信的协议。
# 所以HTTP的底层就是TCP/IP。所以GET和POST底层也是TCP/IP
# 但是由于HTTP的规定和浏览器的/服务器的限制，导致我们在应用过程会有不同。
# GET产生一个TCP数据包；POST产生两个TCP数据包。当然有些浏览器还是有点区别的。
# 对于GET方式的请求，浏览器会把http header和data一并发送出去，服务器响应200（返回数据）；
# 而对于POST，浏览器先发送header，服务器响应100 continue，浏览器再发送data，服务器响应200 ok（返回数据）。
# 1、GET请求是通过URL直接请求数据，数据信息可以在URL中直接看到，比如浏览器访问；而POST请求是放在Request body的请求头中的，我们是无法直接看到的；
# 2、GET提交有数据大小的限制，一般是不超过1024个字节，而这种说法也不完全准确，
# HTTP协议并没有设定URL字节长度的上限，而是浏览器做了些处理，所以长度依据浏览器的不同有所不同；POST请求在HTTP协议中也没有做说明，一般来说是没有设置限制的，但是实际上浏览器也有默认值。总体来说，少量的数据使用GET，大量的数据使用POST。
# 3、GET请求因为数据参数是暴露在URL中的，所以安全性比较低，比如密码是不能暴露的，就不能使用GET请求；
# POST请求中，请求参数信息是放在请求头的，所以安全性较高，可以使用。在实际中，涉及到登录操作的时候，尽量使用HTTPS请求，安全性更好。
# 4、GET请求只能进行url编码，而POST支持多种编码方式
# 5、GET请求会被浏览器主动cache，而POST不会，除非手动设置。


# 83.python中读取Excel文件的方法
# 应用数据分析库pandas
# import pandas as pd
# df = pd.read_excel("xx.xlsx")
# print(df)


# 84.对python语言的看法
# python是强类型语言，有很强的可读性，对初学者十分友好
# 因为开源，所以也有很丰富的扩展库、与Linux Unix Windows兼容良好,可移植性好。
# python在ai的应用比较多。
# 但是python语言是解释型语言，运行速度会稍微慢点。

#
# 85.在学习Python过程中有没有令你影响深刻的事
# 有，在自己学习python的过程中经常会让我有一种惊叹，比如django开发的时候，python manage的各种命令 django的filter ORM,
# restframework都省去了很多复杂的工序，大大提高了开发效率,还有我开始对python产生兴趣的首先就是爬虫,我就用爬虫爬过智联，51job等网站上的招聘信息，并把这些数据整合起来方便自己去找工作


# 86.字符串、字典、元组、列表常用方法？
# 字符串常用的是split、replace、join、find、strip、just
# 列表常用 pop 、append、 remove、 insert 、clear 、len 、sort、 reverse
# 字典常用 get、 index、 keys、 values、 update


# 87.函数闭包的理解？
# 是指函数中嵌套函数 且外层函数的返回值也是函数
# 闭包中需要注意的是变量的作用域，内层函数使用外层函数的值需要加nolocal 使用全局变量的值需要加global


# 88.什么是装饰器？应用场景？
# 装饰器的特点是返回值和参数都是函数
# 装饰器的目的就是对已封装函数进行操作，为其加上新的功能或一系列运算 。
# 在django中有middleware中间件，它其实就是高级的装饰器用法，


# *****89.django中间件？应用场景？
# 中间件是服务器端与应用程序的一个中间层，它将个管道一样。将接受到的请求进行一些处理。然后传递到客户端 然后把客户端处理的结果再返回
# 中间件顾名思义，是介于request与response处理之间的一道处理过程，相对比较轻量级，并且在全局上改变django的输入与输出。
# 因为改变的是全局，所以需要谨慎使用
# Django的默认中间件在Django项目下的settings模块中，配置的MIDDLEWARE中每一个元素都是中间件
# 有csrf防止跨站请求伪造中间件，黑名单、白名单、全局用户身份校验、全局用户访问频率校验。
# 应用场景
# 1、根据url把请求给到不同的客户端程序  2、允许多个客户端  3、负载均衡和远程处理  4、应答的过滤处理


# *****90.什么是装饰器？应用场景？
# 装饰器的特点是返回值和参数都是函数
# 装饰器的目的就是对已封装函数进行操作，为其加上新的功能或一系列运算 。
# 在django中有middleware中间件，它其实就是高级的装饰器用法，


# 91.生成器、迭代器和可迭代对象区别和应用？
# 能使用for遍历的就叫迭代对象 ，能用next函数的叫迭代器


# 92.线程、进程和协成？同步异步，阻塞非阻塞？
# 同步与异步区别在于：调用者是否得到了想要的最终结果。
# 同步就是一直要执行到返回最终结果。
# 异步就是直接返回了，但是返回的不是最终的结果，调用者不能通过这种调用得到结果，还要通过被调用者，使用其他方式通知调用者，来取回最终结果。
#
# 阻塞与非阻塞的区别在于，调用者是否还能干其他的事情。
# 阻塞，调用者只能干等。
# 非阻塞，调用者可以先忙一会别的，不用一直等。
#
# 进程、线程
# 进程是资源分配的最小单位，线程是程序执行的最小单位。
# 进程有自己的独立地址空间，每启动一个进程，系统就会为它分配地址空间，建立数据表来维护代码段、堆栈段和数据段，这种操作非常昂贵。而线程是共享进程中的数据的，使用相同的地址空间，因此CPU切换一个线程的花费远比进程要小很多，同时创建一个线程的开销也比进程要小很多。
# 线程之间的通信更方便，同一进程下的线程共享全局变量、静态变量等数据，而进程之间的通信需要以通信的方式（IPC)进行。不过如何处理好同步与互斥是编写多线程程序的难点。
# 但是多进程程序更健壮，多线程程序只要有一个线程死掉，整个进程也死掉了，而一个进程死掉并不会对另外一个进程造成影响，因为进程有自己独立的地址空间。
#
# 协程
# 协程，又称微线程，纤程。英文名Coroutine。
# 协程的概念很早就提出来了，但直到最近几年才在某些语言（如Lua）中得到广泛应用。
# 子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。
# 所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。
# 子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。
# 协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
# 注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。


# 93.Python2x与Python3x的区别?
# Unicode. python3是默认utf-8编码的
# 除法运算 两个整数相除返回浮点数 而在2x版本可以整除的返回整数
# 捕获异常机制也从except exc,var 改为 except exc as var
# python3取消了xrange函数。xrange更像是个生成器 它是惰性取值的
# 去掉了long类型。只用int表示整型
# 不等运算符去掉了<> 只存在！=
# 去掉了“repx表达式


# 93.Http协议？列举Http请求方法？列举Http常用请求头？列举Http状态码？
#HTTP：超文本传输协议 (HTTP-Hypertext transfer protocol) 是一种详细规定了浏览器和万维网服务器之间互相通信的规则，
# 通过因特网传送万维网文档的数据传送协议。
# HTTPS：（全称：Hypertext Transfer Protocol over Secure Socket Layer），是以安全为目标的HTTP通道，简单讲是HTTP的安全版。
# 即HTTP下加入SSL层，HTTPS的安全基础是SSL，因此加密的详细内容就需要SSL。 它是一个URI scheme（抽象标识符体系），
# 句法类同http:体系。用于安全的HTTP数据传输。https:URL表明它使用了HTTP，但HTTPS存在不同于HTTP的默认端口
# 及一个加密/身份验证层（在HTTP与TCP之间）。这个系统的最初研发由网景公司进行，提供了身份验证与加密通讯方法，
# 现在它被广泛用于万维网上安全敏感的通讯，例如交易支付方面。


# *****94.Django请求生命周期？
# 浏览器请求url，浏览器生成请求头和请求体发送给服务端，url经过django的WSGI是请求对象创建完成，再经过django中间件，
# 再到路由系统匹配路由，匹配成功后走到相应的视图函数，视图函数执行相关逻辑代码并返回执行结果为符合html复杂字符串，
# 再次通过中间件处理响应，WSGI返回响应，浏览器渲染。


# *****95.什么是wsgi？
#  WSGI:
# web服务器网关接口,是一套协议。用于接收用户请求并将请求进行初次封装，然后将请求交给web框架
# 实现wsgi协议的模块：
#         1.wsgiref,本质上就是编写一个socket服务端，用于接收用户请求(django)
#         2.werkzeug,本质上就是编写一个socket服务端，用于接收用户请求(flask)
# uwsgi:
# 与WSGI一样是一种通信协议，它是uWSGI服务器的独占协议,用于定义传输信息的类型
# uWSGI:
#         是一个web服务器,实现了WSGI协议,uWSGI协议,http协议


# 96.经典类和新式类
# 经典类和新式类在写法上的区别是是否继承了object类。新式的必然有很多新的功能


# 97.什么是cookie，session，有什么区别
# 1、Cookies是服务器在本地机器上存储的小段文本并随每一个请求发送至同一服务器，是在客户端保持状态的方案。
# 2、Session是存在服务器的一种用来存放用户数据的类HashTable结构。
# 区别：
# 1、Cookie和Session都是会话技术，Cookie是运行在客户端，Session是运行在服务器端。
#    2、Cookie有大小限制以及浏览器在存cookie的个数也有限制，Session是没有大小限制和服务器的内存大小有关。
#    3、Cookie有安全隐患，通过拦截或本地文件找得到你的cookie后可以进行攻击。
#    4、Session是保存在服务器端上会存在一段时间才会消失，如果session过多会增加服务器的压力。


# 98. mysql数据引擎myisam与innodb的区别
# MyISAM 适合于一些需要大量查询的应用，但其对于有大量写操作并不是很好。甚至你只是需要update一个字段，
# 整个表都会被锁起来，而别的进程，就算是读进程都无法操作直到读操作完成。另外，MyISAM 对于 SELECT COUNT(*) 这类的计算是超快无比的。

# InnoDB 的趋势会是一个非常复杂的存储引擎，对于一些小的应用，它会比 MyISAM 还慢。他是它支持“行锁” ，
# 于是在写操作比较多的时候，会更优秀。并且，他还支持更多的高级应用，比如：事务。


# 99. 如何在服务器上签署Diango项目流程；
# (1)	Uwsgi django 框架运行依赖wsgi，（本质提供socket服务端）众多模块实现了wsgi规范，而django框架中默认使用wsigiref模块来实现。由于性能比较低，所以用于本地开发和测试，线上部署则需要使用uwsgi。
#     ①	在服务器上安装uwsgi
#         1)	Pip insalluwsgi
#         2)	在服务器端编写一个python文件。
#             def application(env, start_response):
#                 start_response('200 OK', [('Content-Type','text/html')])
#             return [b"Hello World"]
# #       3） 在服务器上执行命令，启动web服务器
#             uwsgi --http :9001 --wsgi-file app.py# 或
#             uwsgi --http :9002 --wsgi-file foobar.py --master --processes 4
#         4） Django 程序使用uwsgi，将开发好的程序拷贝到服务器目录。
#             uwsgi --http :9005 --chdir /data/oldboy/ --wsgi-file oldboy/wsgi.py --master --processes 4
#         5） 配置文件的形式，启动uwsgi
#             1. 创建配置文件 oldboy.ini
#
#             [uwsgi]
#             http = 0.0.0.0:9005
#             chdir = /data/oldboy/
#             wsgi-file = oldboy/wsgi.py
#             processes = 4
#             static-map = /static=/data/oldboy/allstatic
#             2. 根据配置文件启动uwsgi
#
#             uwsigi --ini  oldboy.ini
#         6） 虚拟环境： virtualenv = /env/oldbody_venv
#         7） 静态文件配置。
#             a.	收集静态文件
#             在django的配置文件中添加：STATIC_ROOT = os.path.join(BASE_DIR,"allstatic")
#             执行 python3 manage.py collectstatic 命令，至此django项目所有相关静态文件都会收集到制定目录。
#             b.	设置uwsgi静态文件对应关系
#             uwsgi --http :9005 --chdir /data/oldboy/ --wsgi-file oldboy/wsgi.py --master --processes 4 --static-map /static=/data/oldboy/allstatic
# （2）nginx 上部署
#     1)	安装nginx   pip install nginx
#     2)	配置nginx
#     3)	配置uwsgi
#         为了确保让所有请求均通过80端口来访问网站，将uwsgi的配置文件修改为：
#         [uwsgi]
#         socket = 127.0.0.1:9005
#         chdir = /data/oldboy/
#         wsgi-file = oldboy/wsgi.py
#         processes = 4
#         logto = /tmp/oldboy.log
#     4） 启动uwsgi 和 nginx
#         uwsgi --ini /data/oldboy/oldboy.ini &
#         /etc/init.d/nginx start


# 99.Django的FBV和CBV
# FBV(function base views):在视图里使用函数处理请求。(对新手很友好)
# CBV(class base views):在视图里使用类处理请求，提高代码复用性，可以面向对象技术比如多继承Mixin类，可以用不同函数针对
# 不同HTTP请求方法处理，不用写很多if判断，提高代码可读性。


# 100.Django信号作用？应用？
# Django 提供一个了“信号分发器”机制，允许解耦的应用在框架的其它地方发生操作时会被通知到。 通俗而讲Django信号的工作原理就是
# 当某个事件发生的时候会发出一个信号(signals), 而监听这个信号的函数(receivers)就会立即执行。
# Django信号的应用场景很多，尤其是用于不同模型或程序间的联动。
# 常见例子包括创建User对象实例时创建一对一关系的UserProfile对象实例，或者每当用户下订单时触发给管理员发邮件的动作。
# Django内置信号包括：
# django.db.models.signals.pre_save & post_save在模型调用 save()方法之前或之后发送。
# django.db.models.signals.pre_init& post_init在模型调用_init_方法之前或之后发送。
# django.db.models.signals.pre_delete & post_delete在模型调用delete()方法或查询集调用delete() 方法之前或之后发送。
# django.db.models.signals.m2m_changed在模型多对多关系改变后发送。
# django.core.signals.request_started & request_finished Django建立或关闭HTTP 请求时发送。


# 101.什么是REST 、RESTful 、RESTful API？
# Rest
# 1、Rest与技术无关，代表的是一种面向资源的架构风格
# 2、Rest是Representational State Transfer的简称，中文翻译为“表征状态转移”。

# Restful
# 遵守了rest风格的应用,简洁明了，

# Restful API
# 1、在RESTful风格的架构中，每个网址代表一种资源，所以网址中不能有动词，只能有名词。而且所用的名词往往与数据库的表名对应。
# 2、HTTP动词设计：GET（获取资源）POST（新建资源）PUT（更新资源，客户端提供改变后的完整资源）DELETE（删除资源）　


# 102.restful framework框架：认证、权限和访问频率?
# 103.IO多路复用？
# 104.with 上下文机制原理？
# 105.Python内存管理?



# redis数据库部分
# 1、为什么使用redis
# 性能：
# 我们在碰到需要执行耗时特别久，且结果不频繁变动的SQL，就特别适合将运行结果放入缓存。这样，
# 后面的请求就去缓存中读取，使得请求能够迅速响应。
# 并发：
# 在大并发的情况下，所有的请求直接访问数据库，数据库会出现连接异常。这个时候，就需要使用redis做一个缓冲操作，
# 让请求先访问到redis，而不是直接访问数据库。

# 2、使用redis有什么缺点
# 分析:大家用redis这么久，这个问题是必须要了解的，基本上使用redis都会碰到一些问题，常见的也就几个。
# 回答:主要是四个问题
# (一)缓存和数据库双写一致性问题
# (二)缓存雪崩问题
# (三)缓存击穿问题
# (四)缓存的并发竞争问题

# 3、redis的数据类型，以及每种数据类型的场景
# (一)String
# 这个其实没啥好说的，最常规的set/get操作，value可以是String也可以是数字。一般做一些复杂的计数功能的缓存。
# (二)hash
# 这里value存放的是结构化的对象，比较方便的就是操作其中的某个字段。博主在做单点登录的时候，就是用这种数据结构存储用户信息，
# 以cookieId作为key，设置30分钟为缓存过期时间，能很好的模拟出类似session的效果。

# (三)list
# 使用List的数据结构，可以做简单的消息队列的功能。另外还有一个就是，可以利用lrange命令，做基于redis的分页功能，性能极佳，用户体验好。

# (四)set
# 因为set堆放的是一堆不重复值的集合。所以可以做全局去重的功能。为什么不用JVM自带的Set进行去重？因为我们的系统一般都是集群部署，使用JVM自带的Set，比较麻烦，难道为了一个做一个全局去重，再起一个公共服务，太麻烦了。
# 另外，就是利用交集、并集、差集等操作，可以计算共同喜好，全部的喜好，自己独有的喜好等功能。

# (五)sorted set
#
# sorted set多了一个权重参数score,集合中的元素能够按score进行排列。可以做排行榜应用，取TOP N操作。另外，参照另一篇《分布式之延时任务方案解析》，该文指出了sorted set可以用来做延时任务。最后一个应用就是可以做范围查找。









































# 1.同母异序题
# def is_Anagram(s1, s2):
#     s1, s2 = s1.lower(), s2.lower()
#     lsts1 = list(s1)
#     lsts2 = list(s2)
#     lsts1.sort()
#     lsts2.sort()
#     for i, char in enumerate(lsts1):
#         if lsts2[i] != char:
#             return False
#     return True
#
#
# def is_Anagram_another(s1, s2):
#     s1, s2 = s1.lower(), s2.lower()
#     lst1 = [0] * 26
#     lst2 = [0] * 26
#     length1, length2 = len(s1), len(s2)
#     for i in range(length1):
#         pos = ord(s1[i]) - ord('a')
#         lst1[pos] += 1
#
#     for i in range(length2):
#         pos = ord(s2[i]) - ord('a')
#         lst2[pos] += 1
#
#     for i in range(26):
#         if lst1[i] != lst2[i]:
#             return False
#     return True
#
# print(is_Anagram("Abbc", "cbaba"))
# print(is_Anagram_another("Abbc", "cbaba"))
# print(is_Anagram("JKwwi", "wkjwi"))
# print(is_Anagram_another("JKwwi", "wkjwi"))

