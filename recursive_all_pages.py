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
###方法 1:  直接設定要列印幾頁
# for i in range(39747):    # 執行3頁
#     for t in article_title:
#         try:
#             ar_title = t.a.text  #title的文字擷取
#             print(ar_title)
#             ar_url = "https://www.ptt.cc"+t.a['href']  #title的url擷取
#             print(ar_url)
#             print('______________')
#         except AttributeError as e:
#             print('===========')
#             print(t)
#             print(e.args)   #
#             print('===========')
#     url = 'https://www.ptt.cc' + soup.select('a[class="btn wide"]')[1]['href']   #執行下一頁!


###方法 2: 根據url變化規律，決定幾頁
page_num = 39746
while page_num >= 1:
    print(page_num)

    for t in article_title:
        try:
            ar_title = t.a.text  # title的文字擷取
            print(ar_title)
            ar_url = "https://www.ptt.cc" + t.a['href']  # title的url擷取
            print(ar_url)
            print('______________')
        except AttributeError as e:
            print('===========')
            print(t)
            print(e.args)  #
            print('===========')
    page_num -= 1
    url = "https://www.ptt.cc/bbs/Gossiping/index{}.html".format(page_num)




