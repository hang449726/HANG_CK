while(1):
    ans = 0
    try:
        socre = int(input("请输入你的成绩:"))
        print("你的成绩是",socre)
        ans = 1
    except:
        print("你输入的成绩不正确，请重新输入")
    if ans == 1:
        break


