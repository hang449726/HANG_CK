n = 2

def fun1(a,b):
    n = a * b
    print(n)

fun1(5,6)
print("n没有设置成全局变量",n,end=(" \n"))#end的值默认为\n,若是将end的值赋值成其他的东西，那么就可以print就可以不换行了
def fun2(a,b):
    global n
    n = a * b
    print(n)

fun2(5,6)
print("n设置成全局变量",n)