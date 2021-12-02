import json
import time

def delete(list):
    resultList = []
    for item in list:
        if not item in resultList:
            resultList.append(item)
    return resultList
def readjson(num):
    with open("D:\py prj\CNSS\json\%d.json"%num, 'r') as load_f:
        load_dict = json.load(load_f)
        D = load_dict[0]["data"]
    return D
def process(Data):
    # 创建一个二维矩阵
    a = [[0 for col in range(2)] for row in range(30)]

    for i in range(len(Data)):
        # 去除不整点
        if ((Data[i][0] / 1000)%3600) != 0:
            i += 1
        # 避免最后溢出
        if i >= len(Data):
            break
        # 时间戳转换
        timeStamp = Data[i][0] / 1000
        timeArray = time.localtime(timeStamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        # i+1行的一二列
        a[i][0] = otherStyleTime
        a[i][1] = Data[i][1]

    # 去除零
    for i in a[:]:
        if i[0] == 0:
            a.remove(i)

    b = delete(a)
    return b
def save(b,n):
    #保存为txt
    file = open('D:\\py prj\\CNSS\\txt\\%d.txt'%n, 'w')
    for i in range(len(b)):
        # s = str(a[i]).replace('{', '').replace('}', '').replace("'", '').replace(':', ',') + '\n'
        s = str(b[i]).replace("'",'').replace('[','').replace(']','') + '\n'
        file.write(s)
    file.close()
with open("D:\\py prj\\CNSS\\json\\1.json", 'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)
    #打印地点
    name = load_dict[0]["name"]
    print("地点：",name)
    Data = load_dict[0]["data"]

P1 = process(Data)
save(P1,1)

for i in range(2,27):
    Di = readjson(i)
    Pi = process(Di)
    save(Pi,i)

print("保存txt成功!")

input("please input any key to exit!")