from locale import locale_encoding_alias


l = [123,123,3.14,"abc","abc"]
print(l)
print(len(l))
print(type(l))
print(l[1])#索引
print(l[::-1])#倒序
print(l[-1]) #倒数第一个
print(l[1:3])#切片

l2 = [123, 456, [789, 123, 456], "abc"]
print(l2)
print(l2[2])
print(l2[2][2])#嵌套列表索引

"""
列表的一些函数和方法
x in s : 判断x是否在s中,在返回True,否则返回False
x not in s : 判断x是否不在s中,不在返回True,否则返回False
s.len(s) : 返回列表s的长度
s.min(s) : 返回列表s中的最小值
s.max(s) : 返回列表s中的最大值
s.append(x) : 在列表s的末尾添加元素x
s.insert(i,x) : 在列表s的索引i位置插入元素x
s.pop(i) : 弹出列表s中的索引i位置的元素，并返回该元素
s.remove(x) : 从列表s中移除第一个出现的元素x
s.clear() : 清空列表s
s.index(x) : 返回列表s中第一个出现的元素x的索引
s.count(x) : 返回列表s中元素x的出现次数
s.sort() : 对列表s进行排序
s.reverse() : 对列表s进行倒序
"""

print("列表的一些函数和方法")
ls = [123,123,3.14,1,2]
print(len(ls))
print(123 in ls)
print(123 not in ls)
print(min(ls))
print(max(ls))

strls = ["abc","def","ghi","q","a","yui"]
print(min(strls))
print(max(strls))

ls.append(123)
ls.append("abc")
print(ls)
ls.insert(0,"lyh")
print(ls)
a = ls.pop(0)
print(a)
print(ls)
ls.remove(123)
print(ls)
ls.reverse() #倒序
ls.reverse()
print(ls.index(123))
print(ls.count(123))
lsort = [1,3,4,5,7,9,8,4,12]
lsort.sort()
print(lsort)
lsort.sort(reverse=True)
print(lsort)
lsort.clear()
print(lsort)
