print("{}说今天天气不错！".format("小明"))
print("{}说今天天气{}！".format("小明","不好"))
print("{0}说今天天气{1}！".format("小明","不好"))
print("{1}说今天天气{0}！".format("小明","不好"))
print("{0}说今天天气{0}！".format("小明"))

# :<填充><对齐><宽度><,><精度><类型>

s = "二级考试"
y = "o"
print("{:25}".format(s))
print("{:1}".format(s)) #当输出宽度小于字符串长度时，原样输出字符串
print("{:^25}".format(s))#居中
print("{:>25}".format(s))#右对齐
print("{:<25}".format(s))#左对齐，默认

print("{:*^25}".format(s))
print("{:+^25}".format(s))
print("{0:{1}^25}".format(s,y))
print("{0:{1}^{2}}".format(s,y,28))
print("{0:{1}{3}{2}}".format(s,y,28,"^"))

print("{:-^25,}".format(23456789))

print("{:.2f}".format(3.1415926))
print("{:.2f}".format(3.1455266))
print("{:>25.2f}".format(3.1415926))
print("{:.5}".format("全国二级计算机等级考试"))

"""
b:整数二进制形式
c:输出整数对应的Unicode字符
d:整数十进制形式
o:整数八进制形式
x:整数小写十六进制形式
X:整数大写十六进制形式
"""
print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(255))


"""
e:浮点数对应的小写字母e的指数形式
E:浮点数对应的大写字母e的指数形式
f:标准浮点数形式
%:输出浮点数百分比形式
"""

print("{0:e},{0:E},{0:f},{0:%}".format(3.141))