counter = 100
miles = 100.0
name = "lyh"

print(counter)
print(miles)
print(name)

'''
多个变量赋值
'''
a = b = c = 1
print(a, b, c)
a,b,c = 1,2,"lyh"
print(a, b, c)


'''
字符串
'''

s = 'abcdef'
print(s)
print(s[0]) #第0位
print(s[1:3])#第1位到第3位（不包含第3位）
print(s[1:])#第1位到最后一位
print(s[:3])#第0位到第3位（不包含第3位）
print(s[:])#第0位到最后一位
print(s * 2)#重复2次
print(s + '123')#拼接字符串
d = s + '123'
print(d)