import requests
import json
import time

code = input("请输入城市代码：")
request_url = [[0 for col in range(1)] for row in range(26)]
for i in range(1,10):
    request_url[i-1] = "https://www.cnss.com.cn/u/cms/www/tideJson/{0}_2019-09-0{1}.json?v={2}".format(code,int(i),int(round(time.time() * 1000)))
#     # r = random.randint(0, 9)
#     # time.sleep(r)
#     print("{0}号生成完成".format(i))
for i in range(10,27):
    request_url[i-1] = "https://www.cnss.com.cn/u/cms/www/tideJson/{0}_2019-09-{1}.json?v={2}".format(code,int(i),int(round(time.time() * 1000)))
#     # r = random.randint(0, 9)
#     # time.sleep(r)
#     print("{0}号生成完成".format(i))
print(request_url)

# request_url = "https://www.cnss.com.cn/u/cms/www/tideJson/168_2019-09-01.json?v={0}".format(int(round(time.time() * 1000)))
for i in range(1,27):
    data = requests.get(request_url[i-1])
    data_price = json.loads(data.text)
    with open('D:\py prj\CNSS\json\%d.json'%i, 'w') as f:
        json.dump(data_price, f)

print("生成完毕！可关闭窗口执行下一步")
input("please input any key to exit!")
