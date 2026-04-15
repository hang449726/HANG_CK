"""
元组一旦定义不能修改
x in s : 判断x是否在元组s中
x not in s : 判断x是否不在元组s中
s.len(s) : 获取元组s的长度
s.min(s) : 获取元组s中的最小值
s.max(s) : 获取元组s中的最大值
s.count(x) : 获取元组s中x的个数
s.index(x) : 获取元组s中x的索引
"""
from telnetlib import TLS


t = (1,2,3,4,5)
print(t)
print(len(t))
print(type(t))
print(t[1])#索引
print(t[::-1])#倒序
print(t[-1]) #倒数第一个

for i in t:
    print(i)