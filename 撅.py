from sys import *

print("要开始撅哩！")

# 你是一个一个文件啊！

readlines = []
try :
    with open(argv[1],"r+") as fr:
        for i in fr.readlines():
            readlines.append(i)
except Exception as e:
    print("撅不了哩：没有文件可撅哩！（悲）")
    print("文件不能撅罢！（悲）")
    exit()


# 你是一个一个解释器啊！

try:
    if ((readlines)[0].split())[0] == "":
        pass
except Exception as e:
    print("撅不了哩：怎么是空的啊！（悲）")
    print("文件不能撅哩！（悲）")
    exit()

if ((readlines)[0].split())[0] != "要":
    print("撅不了哩：怎么没有孔啊！（悲）")
    print("文件不能撅哩！（悲）")
    exit()
elif ((readlines)[-1].split())[0] != "脱出来哩！（喜）":
    print("撅不了哩：怎么脱不出来啊！（悲）")

n = 0
num = 0
file = []

for i in readlines:
    command = i.split()
    if command[0] == "要":
        if n == 1:
            print("撅不了哩：已经有孔哩（恼）")
            print("文件不能撅罢（悲）")
            exit()
        file.append("char 孔["+command[1]+"] = {0};")
        file.append("int 撅 = 0;")
        n = 1
    elif command[0] == "你是":
        for i in command:
            if i == "一个":
                num += 1
            elif i == "啊！（悲）":
                for i in range(num):
                    file.append("孔[撅] += 1;")
                num = 0
            elif i == "什么啊！（恼）":
                for i in num:
                    file.append("孔[撅] -= 1;")
                num = 0
    elif command[0] == "哼！":
        file.append("撅 += 1;")
    elif command[0] == "哼哼！":
        file.append("撅 -= 1;")
    elif command[0] == "是0要被撅罢！（悲）":
        file.append("while(孔[撅]!=0){")
    elif command[0] == "撅完哩！（喜）":
        file.append("}")
    elif command[0] == "进来罢！（喜）":
        file.append("孔[撅] = getchar();");
    elif command[0] == "脱出哩！（喜）":
        file.append('putchar(孔[撅]);')

# 你是一个一个输出文件啊！

try:
    name = argv[2]
except Exception as e:
    name = "事雪罢.c"

with open(name,"w") as fw:
    fw.write('''
// 要开始撅哩！（喜）
#include <stdio.h>
void main(int args,char** argv){
''')
    for i in file:
        fw.write(i)
        fw.write("\n")
    fw.write("}\n// 撅完哩！")

print("撅完哩！")
