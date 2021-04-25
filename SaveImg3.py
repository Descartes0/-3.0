#模拟基于Win10 x64的Microsoft Edge浏览器访问
#
#github:https://github.com/Descartes0
#
#4月24更新  //    修复了第二版本由于第一次获取图片字段会为None导致的无法运行的bug
#               提供更好的可读性
#               后续更新将提供更改爬取页数和爬取地址的接口


import requests
import time
import os
import bs4

weihao = 1631507 #当前图片域名的HTML尾号
root = "E://PIC//4-24第三版//"

kv = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.42'}

url0 = "https://www.4ddzlf7hz7o6lv7x.com/home/pic/9/799_"
for i in range(10):
    cishu = 0
    weihao = weihao - i
    url = url0 + str(weihao)+".html"
    html = requests.get(url,headers=kv)
    html = html.text
    soup = bs4.BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div', class_="nbodys"):
        for item in soup.find_all('div', class_="nbodys"):
            img_ = item.find_all()
            for each in img_:
                img = each.get('src')
                if (img != None):
                    path = root + img.split('/')[-2] + img.split('/')[-1]
                try:
                    start_time = time.time()    #开始保存此次图片的时间
                    if not os.path.exists(root):
                        os.mkdir(root)

                    if not os.path.exists(path):
                        r = requests.get(img)
                        with open(path, 'wb') as f:
                            cishu += 1
                            f.write(r.content)
                            f.close()
                            print("尾号为"+str(weihao)+"的图片保存成功*"+str(cishu))
                    else:
                        print("文件已存在")
                except:
                    print("失败")




