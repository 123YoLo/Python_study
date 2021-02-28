# -*-coding = utf-8 -*-
# @Time : 2021/2/28 8:15
# @Author :123YoLo
# @File : demo z2.py
# @Software: PyCharm
#方法一
'''
for i in range(1,10):
    for j in range(1,10):
        k = i * j
        if i>j:
            print("%d*%d=%d" % (i, j, k), end="\t")
        elif i==j:
            print("%d*%d=%d" % (i, j, k), end="\n")
'''
#方法二
'''
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(i,j,i*j),end=" ")
    print("\n")
'''
#方法三
'''
#从他人博客上摘抄
# 答案3 for+字符串转换
for i in range(1, 10):
    for j in range(1, i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j), end=" ")  # end=" "作用①不换行②间隔
    print()  # 换行
'''