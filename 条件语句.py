while(1):
    try:
        a = int(input("请选择判断序号:"))
        if a == 1:
            flag = False
            name = input("请输入用户名:")
            if name == "lyh":
                flag = True
                print('welcome', name)
            else:
                print("who are you")
        elif a == 2:
            num = int(input("请输入数字(1-3):"))
            if num == 3:
                print("boss")
            elif num == 2:
                print("user")
            elif num == 1:
                print("worker")
            elif num <= 0:
                print("error")
            else:
                print("roadman")
        elif a == 3:
            num = int(input("输入一个用于判断大小的数"))
            if num >= 0 and num <= 10:
                print("0<=x<=10")
            elif num < 0 or num > 10:
                print("<0 or >10")
            elif (num >= 0 and num <= 5) or (num >= 0 and num <= 5):
                print("0<=x<=5 or 5<=x<=10")
            else:
                print("underfine")
        elif a == 0:
            break
    except ValueError:
        print("输入错误，请输入一个整数！")