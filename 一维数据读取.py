import sys
import io

# 改变标准输出的默认编码，强制使用 utf-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ls = ["北京","上海","深圳","广州","成都"]
# f = open("city.csv","w",encoding = "utf-8")
# s = ",".join(ls)
# f.write(s)
# f.close()

f = open("city.csv","r",encoding = "utf-8")
info = f.read()
print(info)
f.close()
ls = info.split(",")
print(ls)