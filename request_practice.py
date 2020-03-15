import requests
from bs4 import BeautifulSoup

#擷取PTT_NBA版
url = 'https://www.ptt.cc/bbs/NBA/index.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
#headers為紀錄使用者端的瀏覽器資訊，在network裡面任一項可找到useragent

#對網頁提出request
req = requests.get(url, headers=headers)
print(req.text)  #用.text把內容轉成字串list

#把response轉成BeautifulSoup形式，html.parser為Python默認解析器
soup = BeautifulSoup(req.text, 'html.parser')
print(soup.prettify())


