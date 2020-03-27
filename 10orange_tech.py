### 下滑會慢慢增加頁面內容的網頁 ###

import requests
from bs4 import BeautifulSoup
import json
import pprint

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
url = "https://buzzorange.com/techorange/wp-admin/admin-ajax.php"

data_str = '''action: fm_ajax_load_more
nonce: 38e95bb951
page: 2'''

data = {i.split(': ')[0]:i.split(': ')[1] for i in data_str.split('\n')}

res = requests.post(url, headers=headers, data=data)
#print(res.text)

jdata = json.loads(res.text) #把外部的字串轉成json物件
#pprint.pprint(jdata)   #把json檔案排版印出(pprint排版)

html = jdata['data']  #取出html
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())   #印出BeautifulSoup的html

title_list = soup.select('h4.entry-title a')  #取出標題
#print(title_list)

for i in title_list:
    article_title = i.text
    article_url = i['href']
    print(article_title)
    print(article_url)
    print('---')
