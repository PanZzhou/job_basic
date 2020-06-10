import sys#导入sys模块
from sys import path,argv#导入sys模块成员

word='这是一个字符串'; sentence="这是一个字符串"
paragraph="""这也是一个字符串，
可以转行"""

#这是一个注释
'''
这是一个
多行注释
'''
"""
这也
是一个
多行注释
"""

a = b = c = 1
a, b, c = 1, 2, "john"
d=a+\
  b   #多行语句
total = ['item_one', 'item_two', 'item_three',   #[],{},()中的数据换行不需要\来连接
        'item_four', 'item_five']
del a  #删除对象引用

print(type(b))#type()不会认为子类是一种父类类型。
print(isinstance(b,int))#isinstance()会认为子类是一种父类类型。
#数字类型（ int、float、bool、complex）,常用函数操作(见菜鸟教程)
2/4 #除法，得到浮点数
2//4#除法，得到整数
2 ** 5 # 乘方，2的5次幂

#字符串类型，Python中的字符串不能改变，如word[0] = 'm'会导致错误；常用函数操作(见菜鸟教程)
str='Runoob'
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
print(r'Ru\noob')          #显示原始字符串，\也显示出来，不表示转义字符
#不换行输出
print(str,end=" ")
print(word)
#格式化输出
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
#f-string,输出时就不用指定s%等
w = {'name': 'Runoob', 'url': 'www.runoob.com'};  print(f'{w["name"]}: {w["url"]}')
name = 'Runoob'
print(f'Hello {name}')

#列表，[],基本操作与字符串类似，但与字符串不一样，列表中的数据是可以变的；常用函数操作(见菜鸟教程)
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
print(list[-1::-1])#可接收第三个参数，表示步长,-1 表示逆向

#元组，(),与列表类似，但元组中的元素不能修改，基本操作与字符串类似
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tup1 = (50);print(type(tup1)),#数字类型
tup2 = (50,);print(type(tup2))#加了逗号后，变成元组类型
#可以对tuple进行连接组合
tup3=(20,30);print(tup2+tup3)

#集合，{}或set()创建，基本功能是进行成员关系测试和删除重复元素。
#创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
a = set('abracadabra')
b = set('alacazam')
c = set({'alacazam'}) #与b不一样
print(a)#会自动去除重复元素
a|b #求并集
a&b #求交集
a-b #求差集
a^b #求a和b中不同时存在的元素

#字典，{}，列表不能当键，常用函数操作(见菜鸟教程)
dict = {}#创建空字典
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

#逻辑运算符，and与，or或，not非
#成员运算符，in在序列中返回True, not in不在序列中返回True
#身份运算符，is 是判断两个标识符是不是引用自一个对象，x is y, 类似 id(x) == id(y)，id() 函数用于获取对象内存地址。；
            #is not 是判断两个标识符是不是引用自不同对象

#条件控制
if a==1:
    print('hh')
elif a==2:
    print('jjj')
else:
    pass

a=1
#循环语句
while a<5:
    print(a,end=' ')
    a+=1
else:
    pass

for x in range(4,9):
    print(x, end=' ')
else:
    print()

#迭代器，字符串，列表或元组对象都可用于创建迭代器，有两个基本的方法：iter() 和 next()。
#把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__()
list=[1,2,3,4]
it=iter(list)
print(next(it),end=' ');print(next(it))

for x in it: #迭代器也可用于遍历
    print(x,end=' ')
print()

#生成器,使用了 yield 的函数被称为生成器,每次遇到 yield 时函数会暂停并保存当前所有的运行信息
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()