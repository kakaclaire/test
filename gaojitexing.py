# 高级特性

# 切片#
print("-----------------------切片-------------------------------")


# 通过循环取值
def test(*args):
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    r = []
    n = 3
    for i in range(n):
        r.append(L[i])
    print(r)


test()


# 通过切片取值
def test2(*args):
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    l = L[0:3]  # 顺序切片,L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
    l2 = L[-3:-1]  # 倒序切片
    T = (0, 1, 2, 3, 4)
    t1 = T[:3]  # tuple切片
    t2 = T[::2]
    S = "goodgoodstudydaydayup"
    s1 = S[:8]
    s2 = S[::3]

    print(l, l2, t1, t2, s1, s2)


test2()


# 通过切片操作去除首尾空格
def trim(s):
    if s.find('') >= 0:
        s1 = s.strip()
    print(s1)

    if s.isspace() == True:  # 判断字符串是不是全部为空格
        print('不能为空')


trim(" ab ")

print("-----------------------迭代-------------------------------")
# 迭代
import random


# 查找list中的最大最小值
def findMinAndMax(L):
    if L == []:
        return (None, None)
    else:
        min = L[0]
        max = L[0]
        for i in L:
            if i < min:
                min = i
            elif i > max:
                max = i
            t = tuple([min, max])  # 将数列转为元组
    return print(t)


findMinAndMax([1, 4, 56, 9])

print("-----------------------列表生成式-------------------------------")


# 循环的方法生成列表
def list1():
    l1 = list(range(1, 11))
    print(l1)
    for x in range(1, 11):
        l1.append(x * x)
    return print(l1)


list1()


# 列表生成式的方法
def list2():
    l2 = [x * x for x in range(1, 11)]
    print("列表生成式的方法")
    print(l2)
    return


list2()


# for循环后面还可以加上if判断
def list3():
    l3 = [x * x for x in range(1, 11) if x % 2 == 0]
    return print(l3)


list3()


# list 两层循环
def list4():
    l4 = [m + n for m in 'ABC' for n in 'XYZ']
    return print(l4)


list4()


# 两个变量的列表生成式

def list5():
    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    for k, v in d.items():
        print(k, "=", v)
    l5 = [k + "=" + v for k, v in d.items()]
    print(l5)


list5()


# 把一个list中的所有字符串变成小写

def list6():
    L = ['Hello', 'World', 'IBM', 'Apple']
    l6 = [s.lower() for s in L]  # 小写
    print(l6)


list6()


# 列表表达式中的if else的用法

def list7():
    l7 = [x for x in range(1, 11) if x % 2 == 0]  # if是筛选条件
    l8 = [x if x % 2 == 0 else -x for x in range(1, 11)]  # if 是表达式必须带else
    print(l7, l8)


list7()


# 练习
# list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
def list8():
    L8 = ['Hello', 'World', 18, 'Apple', None]
    l9 = [x.lower() for x in L8 if isinstance(x, str) == True]
    return print(l9)


list8()

print("-----------------------生成器-------------------------------")


# 在Python中，这种一边循环一边计算的机制，称为生成器：可迭代对象
def generator():
    g = (x*x  for x in range(10))  # 在Python中，这种一边循环一边计算的机制，称为生成器：
    next(g)  # generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
    next(g)
    print(next(g))
    h = (x for x in range(10))
    for n in h:
        print(n) #通过for循环迭代生成器h

generator()

print("---------------------")
def fiber(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b#相当于t=tuple（b,a+b），a=t(0),b=t(1)
        n=n+1
    return 'done'

fiber(5)

#一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield(b)
        a,b=b,a+b#相当于t=tuple（b,a+b），a=t(0),b=t(1)
        n=n+1
    return 'done'

fib(5)