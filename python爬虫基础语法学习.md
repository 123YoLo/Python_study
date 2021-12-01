# Python 爬虫基本语法学习



```python
# -*-coding = utf-8 -*-
# @Time : 2021/12/1 14:08
# @Author :123YoLo
# @File : python_easy.py
# @Software: PyCharm

#1.python注释
# print('Hello, world!')
#2.python的行与缩进
'''
if True:
    print("True")
else:
    print("False")
'''
#3.多行语句
'''
weekdays="Little Robert asked his mother for two cents.\
         'What did you do with the money I gave you yesterday?'"
print(weekdays)
'''
#4.等待用户输入
'''
print("Who are you?")
you = input()
print("Hello!")
print(you)
'''
#1.3 Python数据类型
#python拥有6大数据类型：number(数字)、string(字符串)、list(列表)、tuple(元组)、sets(集合)、dictionary(字典)

#数字类型
#支持四种数字类型：int(整数类型)、float(浮点类型)、bool(布尔类型)、complex(复数类型)
'''
a = 1
print(type(a))
查看数字类型
'''
#支持运算类型（+ - * / //整除 %取余 **乘方 ）
'''
print(2**3)乘方
print(3%2)取余
print(15//4)整除
'''

#字符串
'''
1
print('welcome to changsha')
print("what's you name?")
或者用三引号
'''

#print(r"Newlines are indicated by \n")
#2 开头用r或R可以使得转移符失效

#3 字符串的截取
'''
str = 'Lingyi'
print(str[0]) #输出结果为L
print(str[1:4])#输出结果为ing
print(str[-2]) #输出为y
'''

#4 字符运算

'''
num = 1
string = '1'
num2 = int(string)
print(num2)
print(num + num2)
'''
'''
a = 1
b = 2
c ='a'+'b'
print(c)
'''

#列表
'''
#python列表为任意对象的有序集合，列表卸载中括号里，元素之间用逗号隔开

list=["Python",12,[1,2,3],3.14,True]
print(list)
#运行结果 ['Python', 12, [1, 2, 3], 3.14, True]
#列表元素的切片
list2 = [1,2,3,4]
print(list2[0])

list2.remove(3)
print(list2)#删除第三个元素，并用print打印出来

'''

# 元组
#与列表相似，不同之处在于元组的元素不能修改
'''
tuple = ('abc',76,'ly',898,5.2)
print(tuple[1:3])

'''
#集合
#创建可以使用大括号或者是set()函数创建集合。需要注意空集必须使用set函数创建
'''
age = {23,45,46,46,575,453,65}
print(age)
'''

#字典
#字典是一种可变容器模型
'''
information={
    'name':'liming',
    'age':'24'
}
print(information)
#(1)对字典增加数据
information['sex']='boy'
print(information)
#(2)对字典删除数据
del information['age']
print(information)
'''


#python 语句与函数
#(1)条件语句
'''
password = '12345'
if password == '12345':
    print('login sucess!')
else:
    print('wrong password')
'''
#(2)循环语句
'''
sum = 0
for i in range(1,10,1):    #注：不包括10，实际上是1-9
    sum = i + sum
print(sum)

#对于列表或者字典
list=[1,2,3,4]
for i in list:
    print(i)
dictionary={
    'name':'liyuzheng',
    'age':'20'
}
for i in dictionary:
    print(i)

'''

#函数
'''
def y(x):
    y = 5*x+2
    return y
#下面调用自定义函数y
d = y(5)
print(d)
'''
```

