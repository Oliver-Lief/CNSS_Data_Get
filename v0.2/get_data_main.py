import calendar
import os
import random
import sys
import requests
import json
import time

from sklearn.preprocessing import PolynomialFeatures


def delete(list):
    resultList = []
    for item in list:
        if not item in resultList:
            resultList.append(item)
    return resultList


def readjson(num, file):
    with open(file+"%d.json" % num, 'r') as load_f:
        load_dict = json.load(load_f)
        D = load_dict[0]["data"]
    return D


def process(Data):
    # 创建一个二维矩阵
    a = [[0 for col in range(2)] for row in range(30)]

    for i in range(len(Data)):
        # 去除不整点
        if ((Data[i][0] / 1000) % 3600) != 0:
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


def save(b, n, Name, file):
    # 保存为txt
    file = open(file+Name+'%d.txt' % n, 'w')
    for i in range(len(b)):
        s = str(b[i]).replace("'", '').replace('[', '').replace(']', '') + '\n'
        file.write(s)
    file.close()


year = int(input('year:'))
month = int(input('month:'))

number = calendar.monthrange(year, month)[1]
month=str(month).rjust(2,'0')
# print(month)
ls = [0]*number
for i in range(1,number+1):
    ls[i-1] = str(i).rjust(2, '0')

code = input("请输入城市代码：")
request_url = [0]*number
for i in range(number):
    request_url[i] = "https://www.cnss.com.cn/u/cms/www/tideJson/{0}_{1}-{2}-{3}.json?v={4}".format(
        code, year, month, ls[i], int(round(time.time() * 1000)))
    # r = random.randint(0, 9)
    # time.sleep(r)
    print("{0}号生成完成".format(i+1))
# print(request_url)
meragefiledir = os.path.split(os.path.realpath(sys.argv[0]))[0]
file1 = meragefiledir+'\\'+'json'+'\\'
file2 = meragefiledir+'\\'+'txt'+'\\'
for i in range(number):
    data = requests.get(request_url[i])
    data_price = json.loads(data.text)
    with open(file1+'%d.json' % i, 'w') as f:
        json.dump(data_price, f)

with open(file1+"1.json", 'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)
    # 打印地点
    name = load_dict[0]["name"]
    # print("地点：", name)
    Data = load_dict[0]["data"]

P1 = process(Data)
save(P1, 0, name, file2)

for i in range(1, number+1):
    Di = readjson(i, file1)
    Pi = process(Di)
    save(Pi, i, name, file2)
