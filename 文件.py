import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

"""
\n换行符
\t制表符 tab
\b退格符
\\表示一个\
"""
#相对路径
#test.txt
#绝对路径
path = r"E:\PycharmProjects\learn-test\test.txt"
f = open(path, 'rt',encoding='utf-8')
#s = f.read() #读取文件所有内容，读取完成后再次读取，是无法读取到内容的，因为文件指针已经指向了文件末尾
#f.seek(0) #将文件指针指向文件开头
#print(s)

# s = f.readline() #读取文件一行内容，参数控制读取几个字符
# print(s,end=(""))
# s = f.readline() #读取文件一行内容
# print(s)

# s = f.readlines() #以每行为一个元素，读取整个文件，形成一个列表,参数控制读取几行
# print(s)

path2 = r"E:\PycharmProjects\learn-test\test2.txt"
f2 = open(path2, 'w',encoding='utf-8')  #"a"z追加写入，"w"覆盖写入
# f2.write("铁甲将军夜渡关，\n")
# f2.write("朝臣待露五更寒。\n")
# f2.write("山寺日高僧不起，\n")
# f2.write("看来名利不如闲。\n")  
ls = ["铁甲将军夜渡关，\n","朝臣待露五更寒。\n","山寺日高僧不起，\n","看来名利不如闲。\n"]
f2.writelines(ls)



f.close()
f2.close()
"""
文件的读操作
f.read(size) : 读取文件所有内容
f.readline(size) : 读取文件一行内容
f.readlines(hint) : 读取文件所有内容，返回一个列表，每个元素是一行内容
f.seek(offset[, whence]) : 设置文件指针位置
"""