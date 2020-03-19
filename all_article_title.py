import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/movie/index.html"
headers = {"User_Agent":"ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

#print(soup.prettify())

article_title = soup.findAll("div", class_ = "title")
#print(article_title)

# article_title = soup.select('div[class="title"]')
# print(article_title)

for t in article_title:
    print('------')
    try:
        #print(t)
        #ar_title = t.select('a')[0].text
        ar_title = t.a.text
        #ar_url = 'https://www.ptt.cc' + t.select('a')[0]['href']
        ar_url = 'https://www.ptt.cc' + t.a['href']
        print(ar_title)
        print(ar_url)
    except:
        print(t)    #被刪除的文章沒有 title和 url了
