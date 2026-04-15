s1 = "How are you donging?"
s2 = "are"
s3 = "aa"
print(s2 in s1)
print(s3 in s1)#"in"表示判断前一个字符串是否是后一个字符串的子集，若是返回True，不是返回False
print(s1[3])
print(s1[1:6])#输出s1字符串第1个到第5个字符,左闭右开
print(s1[1:])#第一到最后
print(s1[:8])#开始到第八
print(s1[:])#取全部
print(s1[0:11:1])#步长为1
print(s1[0:11:2])#步长为2
print(s1[::-1])#步长为-1逆序排列
print(s1[-1])
print(s1[-2])#索引倒数是从后往前数的
print(s1[:-2])