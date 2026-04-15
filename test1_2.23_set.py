"""
集合的操作符：“-”,"&","^","|"
"""
s = {123,123,3.14,"abc","abc"}
print(s)
print(len(s))
print(type(s))


q = {123,43,45,56,67,89}
t = {123,43,45,11,22,33}
#差集 -
print(q-t)
#交集 &
print(q&t)
#补集 ^
print(q^t)
#并集 |
print(q|t)


"""
集合的一些操作函数
"""
print(len(s))
print(123 in s)
print(123 not in s)
print(s)
s.add(124)
print(s)
s.remove(123)
print(s)
s.clear()
print(s)

p = set()
print(p)