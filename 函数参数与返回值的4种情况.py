"""
def fun(a):
    a = 5
    print(a)

m = 10
fun(m)
print(m)
"""
#输出1-100的和
#无参数，无返回值
def fun1():
    sum = 0
    i = 1
    while i<= 100:
        sum += i
        i += 1
    print(sum)

#计算1-100的和，并返回
#无参数，有返回值
def fun2():
    sum = 0
    i = 1
    while i <= 100:
        sum += i
        i += 1
    return sum

#传入一个成绩，判断该成绩是否合格，合格输出“合格”，不合格输出“不合格”
#有参数，无返回值
def fun3(s):
    if s >= 60:
        print("合格")
    else :
        print("不合格")

#传入一个成绩，判断该成绩是否合格，合格返回True，不合格返回False
#有参数，有返回值
def fun4(s):
    if s >= 60:
        return True
    else :
        return False

