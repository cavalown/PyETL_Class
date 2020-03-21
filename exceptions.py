import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
cookies = {"over18":"1"}

res = requests.get(url, headers=headers, cookies=cookies)
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.prettify())

article_title = soup.select('div[class="title"]')
#print(article_title)
# print(article_title)
# print(t for t in article_title)


# 要考慮到有些文章被刪除後，內部的html程式已經和我們擷取的不相同，會造成執行錯誤而停止。

for t in article_title:
    try:
        ar_title = t.a.text  #title的文字擷取
        print(ar_title)
        ar_url = "https://www.ptt.cc"+t.a['href']  #title的url擷取
        print(ar_url)
        print('______________')
    except AttributeError as e:
        print('===========')
        print(t)
        print(e.args)   #
        print('===========')



