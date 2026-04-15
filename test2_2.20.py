try:
    a = 5
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("除数不能为零")
except:
    print("出错了")