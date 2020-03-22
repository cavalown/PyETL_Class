import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
ss = requests.session()
ss.cookies = {"over18":"1"}
#ss.cookies["over18"] = 1

res = requests.get(url, headers=headers, cookies=ss.cookies)
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.prettify())

article_title = soup.select('div[class="title"]')   #文章列表區的標題
#print(article_title)
# print(article_title)
# print(t for t in article_title)



for t in article_title:
    try:
        ar_title = t.a.text  #title的文字擷取
        print(ar_title)
        ar_url = "https://www.ptt.cc"+t.a['href']  #title的 url擷取
        print(ar_url)
        
        print("-ARTICLE-: ")
        article_res = requests.get(ar_url, headers=headers, cookies=ss.cookies)
        article_soup = BeautifulSoup(article_res.text, "html.parser")
        article_content = article_soup.select('div[id="main-content"]')[0].text.split('--')[0]
        print(article_content)
        print('______________')
    except AttributeError as e:
        print('===========')
        print(t)
        print(e.args)   #
        print('===========')
#url = 'https://www.ptt.cc' + soup.select('a[class="btn wide"]')[1]['href']   #執行下一頁!
