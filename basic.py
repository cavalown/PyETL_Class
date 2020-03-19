######### 匯入request/requests #########
#from urllib import request   ## urllib是Python內建的
import requests  ## requests是第三方套件，用pip3安裝

######### 匯入BeautifulSoup #########
from bs4 import BeautifulSoup  ## 將html的response轉換成BeautifulSoup和定位

######### url 和 headers #########
url = "https://www.ptt.cc/bbs/cat/index.html"  ## 網址
headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
       ## headers是紀錄使用著的瀏覽器資訊，可做為網站判定是否為機器人

######### urllib #########
# req = request.Request(url, headers=headers)  ## 對網頁提出request
# res = request.urlopen(req).read().decode('utf-8')  ## 將網頁回傳的response打開
#
# soup = BeautifulSoup(res.text, 'html.parser')
         ## 將回傳值轉為BeautifulSoup物件;text是將回傳內容轉為字串;
         ##html.parser是Python內部默認的 html 和 xhml 解析器
# print(soup.prettify())  ## prettify()將 html 排版

######### requests #########
res = requests.get(url, headers=headers)  ## get是獲取網頁資訊
#res = requests.post(url, headers=headers)  ## post用在有夾帶資料時獲取網頁

soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.prettify())

######### find/findAll #########
# artile_title = soup.findAll('div', id="topbar")
# print(artile_title[0].text)

# first_article_title = soup.find('div', class_='title')
# print(first_article_title.text)

# article_author = soup.findAll('div', class_='author')
# print(article_author[5].text)
#
#
# ########## select/select_one #########
article_title = soup.select('div[id="topbar"]')
print(article_title[0].text)

first_article_title = soup.select_one('div[class="title"]')
print(first_article_title.text)

article_title = soup.select('div[class="title"]')
print(article_title)

article_author = soup.select('div[class= "author"]')
print(article_author[5].text)







