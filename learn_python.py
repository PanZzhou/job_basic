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
#数字类型（ int、float、bool、complex）
2/4 #除法，得到浮点数
2//4#除法，得到整数
2 ** 5 # 乘方，2的5次幂

#字符串类型，Python中的字符串不能改变，如word[0] = 'm'会导致错误
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

#列表，[],基本操作与字符串类似，但与字符串不一样，列表中的数据是可以变的
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
print(list[-1::-1])#可接收第三个参数，表示步长,-1 表示逆向

#元组，(),与列表类似，但元组中的元素不能修改
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )

#集合，{}或set()创建，基本功能是进行成员关系测试和删除重复元素。
#创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
a = set('abracadabra')
b = set('alacazam')
print(a)#会自动去除重复元素
a|b #求并集
a&b #求交集
a-b #求差集
a^b #求a和b中不同时存在的元素

#字典，{}
dict = {}#创建空字典
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

#逻辑运算符，and与，or或，not非
#成员运算符，in在序列中返回True, not in不在序列中返回True
