"""
字典Dictionary
字典是一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
d = {key1 : value1, key2 : value2 }

字典常用操作函数：
1.len(d)  #返回字典长度
2.d.keys()  #返回字典所有键
3.d.values()  #返回字典所有值
4.d.items()  #返回字典所有键值对
5.d.get(key)  #返回字典指定键的值
6.d.clear()  #清空字典
7.d.pop(key)  #删除字典指定键
8.min(d) : 获取字典d中的最小值
9.max(d) : 获取字典d中的最大值

"""
import sys
import io
# 改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

d = {"20010101":"刘备","20010102":"关羽","20010103":"张飞"}
print(d)
print(len(d))
print(type(d))
print(d["20010101"])
d["20010102"] = "赵云"
print(d)
d["20010104"] = "马超"
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(min(d))
print(max(d))
for i in d:
    print(i)
for i in d.values():
    print(i)
for i in d.items():
    print(i)
for i,j in d.items():
    print(i,j)
print(d.get("20010103"))
print(d.get("20010105","没找到"))
print(d.items())
tmpe = d.pop("20010103")
print(d.items())
print(tmpe)