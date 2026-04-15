import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

""" import turtle
d = 0
turtle.speed(1)
for i in range(8):
    turtle.fd(200)
    d += 90
    turtle.seth(d)
 """

ls = ["综合", "理工", "综合", "综合", "综合", "综合", "综合", "综合", "综合", \
      "综合", "师范", "理工", "综合", "理工", "综合", "综合", "综合", "综合", \
      "综合", "理工", "理工", "理工", "理工", "师范", "综合", "农林", "理工", \
      "综合", "理工", "理工", "理工", "综合", "理工", "综合", "综合", "理工", \
      "农林", "民族", "军事"]

# print("理工:",ls.count("理工"))
# print("综合:",ls.count("综合"))
# print("师范:",ls.count("师范"))
# print("农林:",ls.count("农林"))
# print("民族:",ls.count("民族"))
# print("军事:",ls.count("军事"))

d = {}
for word in ls:
    d[word] = d.get(word,0) + 1

for key in d:
    print(f"{key}:{d[key]}")
