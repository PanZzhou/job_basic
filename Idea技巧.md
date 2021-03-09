# 快捷键

alt + insert 可以调出”generate”面板，从而选择插入get set toString方法。

Ctr + D 复制光标所在行到下一行。

ctrl + alt+ v 就会补全左侧代码

ctrl + alt+ l 就会代码自动对齐



# 快速coding技巧

list.for可以快速写出一个循环。（list是一个List对象）

“sout”+回车 就等于输入”System.out.printLn()”

“psvm“+回车 就等于输入” public static void main(String[] args) { }”

alt+拖动选中不同行：可以同时编辑选中的行

# web

要新建一个web项目，可以先新建一个普通的maven项目，然后右键项目后点击“add Framework support...”  ,选中java web周点击确定即可。（若直接新建一个maven web项目的话，可能需要改版本，很麻烦）



给web项目添加Tomcat server：选择运行按钮前的“Edit Configurations”  点击右上角"+"号，选中“tomcat server” 选择local。然后该Server页面下的Name(随便改)和Deplement页面下的Application context 为“/”。多个子项目的情况还需要选择运行的子项目。(刚进入server页面可以点击fix按钮)

注意：多个子项目的，在运行不同子项目时都要改变下Tomcat的配置，让Tomcat改为运行此子项目。

![image-20210302151206097](C:\Users\FlameZ\AppData\Roaming\Typora\typora-user-images\image-20210302151206097.png)

 选中之前的子项目，然后点击左下角"-"号，然后再点击fix选择对应子项目即可



可能出现web代码配置都正确，但是结果总是出错的现象，可能是因为打包中web-inf下没有lib文件夹，需要把依赖包手动放到lib文件夹下：Project structure -> Artifacts ->需要配置的项目->Output layout ->在web-inf下新建lib文件夹  ->选中lib->点击上方"+"->在弹出的窗口中选中所有的依赖包即可



# 配置文件



![image-20210309180927646](C:\Users\FlameZ\AppData\Roaming\Typora\typora-user-images\image-20210309180927646.png)

不同语言的不同配置文件设置过程如上。这样可以同时编辑多个文件，使其配置名相同，但是可以设置不同的的值。

# 改bug

![image-20210304173807553](C:\Users\FlameZ\AppData\Roaming\Typora\typora-user-images\image-20210304173807553.png)

