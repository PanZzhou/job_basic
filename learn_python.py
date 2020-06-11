import sys#导入sys模块,最后面得必须是包
from sys import path,argv#导入sys模块成员，最后面得可以是包，函数，变量
import math
import pickle

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
tuple1 = 'abcd', 786 , 2.23, 'runoob', 70.2 #与typle效果一致
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
 
for x in f:
    print(x, end=' ')
else:
    print()

#函数定义,参数包含必需参数、关键字参数、默认参数和不定长参数
#必需参数须以正确的顺序传入函数，print_welcome("Runoob")
#关键字参数允许函数调用时参数的顺序与声明时不一致
#*vartuple是以元组的形式传入的，若变为**vardict，则是以字典的形式传入,示例见print_welcome1函数
def print_welcome(name='PanZzhou',age=36,*vartuple, mate='Tang'):
    print("Welcome:", name, 'age:',age,'mate:',mate,end=' ')
    print(vartuple)

name="Runoob"
age=20
print_welcome(name,age)              #必需参数调用，顺序必须一致
print_welcome(age=age,name=name)     #关键字参数调用，顺序可以不一致
print_welcome()                      #name,age使用默认参数
print_welcome(name,age,1,2,3)        #可变参数，以元组(1,2,3)的形式传入
print_welcome(name,age,1,2,mate='Ya')#可变参数后面的参数必须是关键字参数,这样才能标记可变参数的结束

#age必须是指定位置参数，不能是关键位置参数,/代表其前面的参数必须是指定位置参数
def print_welcome1(age,/,name='PanZzhou',**vardict):
    print(name,vardict)
print_welcome1(name,a=1,b=2,c=3)     #后三个数据会转换成字典形式
#print_welcome1(age=20,'Pan',a=1)    age使用了关键字参数，报错

#lambda 表达式
sum = lambda x,y:x**y
print('sum:',sum(2,3))

#列表推导式
vec = [2, 4, 6]
list = [3*x for x in vec if x>3]
print(list)
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
print([[row[i] for row in matrix] for i in range(4)]) #实现矩阵的转置

#del
del matrix[:] #删除列表中的所有元素
del matrix    #删除matrix变量

#遍历技巧
#在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,':',v, end='  ')
print()
#在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,':',v,end='  ')
print()
#反向遍历一个序列，首先指定这个序列，然后调用 reversed() 如:for i in reversed(range(1, 10)):
#同时遍历两个或更多的序列，可以使用 zip() 组合

#类
class people:
    name='' #基本属性
    age=0  #基本属性
    __weight=0  #__表示此为私有属性
    def __init__(self,n,a,w):#构造函数，实例化对象时自动调用此函数
        self.name=n
        self.age=a
        self.__weight=n
    def speak(self):
        print(f'{self.name}说:我{self.age}岁')#使用fstring格式化输出
p=people('Pan',24,60)
p.speak()

#继承
class student(people):
    grade=''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)#调用父类的构造函数
        self.grade=g
    def speak(self):
        print(f'{self.name}说:我{self.age}岁，{self.grade}年级')
s=student('Pan',24,60,13)
s.speak()

#多重继承与私有方法
class speaker:
    name=''
    topic=''
    def __init__(self,n,t):
        self.name=n
        self.topic=t
    def speak(self):
        print(f'大家好，我是{self.name}，我演讲的题目是{self.topic}')

class sample(speaker,student):
    def __init__(self,n,a,w,g,t):
        speaker.__init__(self,n,t)
        student.__init__(self,n,a,w,g)
    def __foo(self):     #函数名前带"__"，表示此函数是私有函数
        print("这是私有方法")
    def foo(self):
        print('这是公有方法')
        self.__foo()     #类方法内调用其他类函数，不能是__foo(self),应该是self.__foo()
s=sample('Pan',24,60,13,'Python')
s.speak()#两个父类都有speak函数，则调用位置靠前的父类的函数;
         #当然也可以在子类中重写此函数，则调用时调用的就是子类重写的函数
s.foo()
#s.__foo(),调用报错，不能直接在外部调用私有方法

#类的专有方法
#__init__ : 构造函数,__del__ : 析构函数,__len__: 获得长度,
#_cmp__: 比较运算,__call__: 函数调用,__add__: 加运算等

#__name__属性， 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，
#否则是被引入。当其他模块import此模块时，__name__就不是__main__
if __name__ == '__main__':
    print("此模块自身在运行")

L=dir(sys)   #dir()函数是内置的，返回被引入模块所包含定义的所有名称，以列表返还
print(L[0])

#包，管理组织不同模块的目录，只有包含__init__.py文件的目录才是一个包
#__init__.py中可以有一个__all__变量，当使用from package import *时，就会
#读取__all__列表变量，导入其中添加的模块，包作者增加删除模块后，得更新__all__

#输出
name='Pan'
age=24
print(f'{name}说:我{age}岁')#使用fstring格式化输出
print("%s说:我%d岁"%(name,age))#使用操作符符格式化输出
print("{0}说:我{1:3d}岁".format(name,age))#使用format函数，此方法应多代替上述两种方法
print("{name}说:我{age:5d}岁".format(name=name,age=age))#age:5d表示age输出占5位
print('PI等于{:.3f}'.format(math.pi)) #小数输出

#输入,交互窗口输入:Tools->SublimeREPL->Python->Python:RUN current file
#str=input("请输入:")

#读写文件
f=open('learn_git.cpp','r',encoding="utf-8")
#str=f.read()，读整个文件
#f.write()
#f.tell(), 返回文件对象当前所处得位置
#f.seek(offset,from_what), 改变文件当前位置,offset是偏移，from_what为0表示文件开头，1表示当前位置，2表示文件结尾
#file.flush()，直接把内部缓冲区的数据立刻写入文件
str=f.readline()#读其中一行
print(str)
f.close()

#pickle 模块，python的pickle模块实现了基本的数据序列和反序列化。
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
output=open('obj.txt','wb')
pickle.dump(data1,output)  #序列化后保存到文件
output.close()
pkl_file=open('obj.txt','rb')
data1=pickle.load(pkl_file)
print(data1)
pkl_file.close()