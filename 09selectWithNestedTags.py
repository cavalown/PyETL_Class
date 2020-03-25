import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/joke/index.html"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

#title = soup.select('div[class="title"]')   ##(1)
title = soup.select('div[class="title"] a')
#print(title)



##(1)##
# for t in title:
#     try:
#         print(t)
#         article_title = t.select('a')[0].text  #(1.1)
#         article_title = t.a.text  #(1.2)
#         article_url = "https://www.ptt.cc" + t.select('a')[0]["href"]
#         print(article_title)
#         print(article_url)
#         print("---")
#     except:
#        print(article_title)


##(2)##
for t in title:
    try:
        #print(t)
        article_title = t.text
        article_url = "https://www.ptt.cc" + t["href"]
        print(article_title)
        print(article_url)
        print("---")
    except:
       print(article_title)
