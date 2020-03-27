#下載圖片，用dcard為例#

import requests
from bs4 import BeautifulSoup
import json
import pprint
from urllib import request
import time
import random

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

url = "https://www.dcard.tw/service/api/v2/forums/dressup/posts?popular=true&limit=30&before=233349397"

#res = requests.get(url, headers=headers)
#pprint.pprint(res.text)

##Read file (直接把json檔案貼到txt檔後，讀檔)
with open('jsfile.txt', 'r', encoding='utf-8') as f:  #其實就是一班的request,只是怕被鎖ip才先複製在檔案裡
    res = f.read()

jdata = json.loads(res)
#pprint.pprint(jdata[0])

#for k in jdata[0]:
#    print(k)   #找出所有key，再去分析我們要的圖片在哪裡

for t in jdata:
    article_title = t['title']
    article_url = "https://www.dcard.tw/f/dressup/p/" + str(t['id'])
    print(article_title)
    print(article_url)
    for img in t['mediaMeta']:
        img_url = img['url']
        print(img_url)    #列出所有圖片網址
        # 創一個資料夾放下載的圖片
        c = 0
        while c<5:   #設定最多失敗後再試，也只會抓五次
            try:
                request.urlretrieve(img_url, './dcard_img/' + img_url.split('/')[-1])  #圖片網址,存檔位置,圖片檔名
                status = 1
            except:
                time.sleep(random.randint(3,10))
                request.urlretrieve(img_url, './dcard_img/' + img_url.split('/')[-1])  #有誤讓他休息，之後再抓一次
                status = 1
            if status == 1:
                break
            c += 1
#print(jdata[1]['mediaMeta'][0]['url'])  #看一下裡面有什麼`,這次的第0篇剛好沒有內容，所以我才選擇第1篇>jdata[1]


##很多網頁惠所爬蟲，所以要import time讓他休息
##通常會在request url的地方有休息的設置


