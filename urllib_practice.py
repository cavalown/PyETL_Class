from urllib import request

#擷取PTT_NBA版
url = 'https://www.ptt.cc/bbs/NBA/index.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
#headers為紀錄使用者端的瀏覽器資訊，在network裡面任一項可找到useragent

#對網頁提出request
req = request.Request(url, headers=headers)
#將接收到網頁的response打開
res = request.urlopen(req)
#印出response並轉成可讀的，解碼成utf-8
print(res.read().decode('utf-8'))
