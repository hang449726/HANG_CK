import sys
import io
# 改变标准输出的默认编码，强制使用 utf-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
students = [
    ["学号","姓名","性别","年龄"],
    ["1001","张三","男","17"],
    ["1002","王五","男","14"],
    ["1003","李四","男","19"],
    ["1004","赵六","女","21"]
    ]
#print(students[1][2])

# for s in students:
#     for i in s:
#         print(i,end=" ")
#     print("\n")



# f = open("students.csv","w+",encoding = "utf-8")
# for row in students:
#     s = ",".join(row) + "\n"
#     f.write(s)

# f.seek(0)
# s = f.read()
# print(s)
# f.close()

f = open("students.csv","r",encoding = "utf-8")
ans = []
for line in f:
    line = line.strip("\n") #去掉换行符\
    temp = line.split(",")
    ans.append(temp)

print(ans)
f.close()
