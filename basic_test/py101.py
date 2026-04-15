#print(round(((3**2+5*(6**7))/8)**0.5, 3))

import jieba
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

""" s = "中国特色社会主义进入新时代，我国社会主要矛盾已经转化为人民日益增长的美\
        好生活需要和不平衡不充分的发展之间的矛盾。"
n = len(s)
m = len(jieba.lcut(s))
print("中文字符数为{},中文词语数为{}".format(n,m)) """


""" print("二进制{0:b},八进制{0:o},十进制{0:d},十六进制{0:x}".format(0x4DC0 + 50))
m = 0x4DC0 + 50
print(f"二进制{m:b},八进制{m:o},十进制{m:d},十六进制{m:x}")
 """