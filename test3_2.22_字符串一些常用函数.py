s = "Hello"
s1 = "asd-fg-gjh-jkl"
name = "张三,李四,王五"
s2 = "==python=="
s3 = "how are you doing?"
print(len(s)) #返回字符串长度
a = 123
a = str(a)   #强制转换类型
print(type(a))
print(chr(97))
print(ord("a"))
print(ord(":"))
print(hex(20))#转换成16进制
print(oct(30))#转化为8进制
print(s.lower())
print(s.upper())
a = s1.split(sep = "-")
nameg = name.split(",")
print(a)
print(nameg)
print(s.count("o")) #统计字母o出现的次数
c = s.replace("l","a")#将s中的l替换成a，并赋值给c，另s没有被改变
print(c)
print(s)

print(s.center(10,"="))
print(s.center(10))#fillchar默认为空格
print(s.center(2,"="))#当width小于字符串长度，直接输出字符串
print(s2.strip("="))#使用strip去掉左右两边的“=”，默认去掉空格
print(",".join("python"))

print(s3.capitalize())  #将字符串的首字母大写

#index(sub,begin,end) 返回sub在当前字符串中第一次出现的位置,如果没找到，报错      （begin和end是指定范围寻找）
#find(sub,begin,end)  返回sub在当前字符串中第一次出现的位置，如果没找到，返回-1

s4 = "I was thinking of taking you somewhere special for dinner tonight!"
print(s4.index("o"))
print(s4.find("o"))
print(s4.index("o",16))
print(s4.find("o",16))
try:
    print(s4.index("o", 16, 20))
except:
    print("index()函数没有在你规定的范围类找到你要找的内容")
print(s4.find("o",16,20))