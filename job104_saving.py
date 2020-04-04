######下載104工作並存成txt檔######

### mac os ###
import ssl
import os
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
##############

import requests
from bs4 import BeautifulSoup
import pprint
import json
import os
import time
import random



headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

###使用者輸入
jobKeyword = input('請輸入工作關鍵字：')
searchPage = int(input('請輸入要查詢頁數：'))


###Create a directory to save files
job_path = r'./job104_list'
if not os.path.isdir(job_path):
    os.mkdir(job_path)


##104 searching page##
url = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword={}&order=15&asc=0&page={}&mode=s&jobsource=2018indexpoc'.format(jobKeyword, searchPage)

###cookies
cookies_str = '''luauid=1387271567; __auc=56e58f951712bd1178300419ac7; _gid=GA1.3.82735965.1585578056; _gaexp=GAX1.3.zUavRTm-RA6qcZHj3g_CfA.18433.2; _hjid=1ac1a15c-70de-462d-8c6e-ca6ca59422e1; ALGO_EXP_6019=C; lup=1387271567.5001489413863.4623532291991.1.4640712161167; lunp=4623532291991; TS016ab800=01180e452d56c88fa507dc578a2a3171481c39e6d98e1ef5a7d2e88260861a1b6bf4df57b31abd8967a7c8156bf7737116783029e00dff5d3f8b09609877f764cd0ba5d131; __asc=06f79ea61712bf29c20b5e55c38; _ga_W9X1GB1SVR=GS1.1.1585580247.2.1.1585580252.55; _ga_FJWMQR9J2K=GS1.1.1585580247.2.1.1585580252.0; _ga=GA1.3.1136539556.1585578056'''
ss = requests.session()
ss.cookies = {i.split('=')[0]:i.split('=')[1] for i in cookies_str.split('; __')}
#print(ss.cookies)


# print('【擷取『'+jobKeyword+'』相關工作，共'+str(searchPage)+'頁內容】:')

### pages
while searchPage > 0 :

    ###對搜尋頁request
    res = requests.get(url, headers=headers, cookies=ss.cookies)
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.prettify())

    ###all job list in a page
    job_list = soup.select('div[class="b-block__left"] ')
    #pprint.pprint(job_list)
    ###pick up all jobs from a page
    for j in job_list:
        try:
            ###all pages content
            #print(j)   #all job column
            job = j.h2.a
            #print(job)
            job_name = job.text #job name
            #print(job_name)
            job_url = "https:" + job['href'] #job content url
            #print(job_url)
            company = j.ul.a
            #print(company)
            company_name = company.text #company name
            #print(company_name.strip())
            company_url = "https:" + company['href'] #company content url
            #print(company_url)

            ###job content page in json file
            job_code = job_url.split('job/')[-1].split('?')[0]  #job code
            # print(job_code)
            job_js_url = 'https://www.104.com.tw/job/ajax/content/' + '{}'.format(job_code) #job js url
            # print(job_js_url)

            ###request json file page###
            res_j = requests.get(job_js_url, headers=headers)
            soup_j = BeautifulSoup(res_j.text, 'html.parser')
            js_str = str(soup_j)
            js = json.loads(js_str)

            ###job content
            jsdata = js['data']
            # pprint.pprint(jsdata)

            ###job skill
            job_skill = jsdata['condition']['specialty']
            # print(job_skill)
            # print('Skills:')

            skills = ''
            for jsk in job_skill:
                skills += str(jsk['description']) + ' '
            #print(skills)

            # for jsk in job_skill:
            #     print(jsk['description'])
            #skills = list(jsk['description'] for jsk in job_skill)
            # print(skills)

            ###job content
            job_content = '---Job Content---\n'
            #job_content = '{}\n'.format('Company Name:')
            job_content += '{}\n'.format(company_name.strip())
            #job_content += '{}\n'.format('Link of the Company:')
            job_content += '{}\n'.format(company_url)
            #job_content += '{}\n'.format('Job Name:')
            job_content += '{}\n'.format(job_name)
            #job_content += '{}\n'.format('Link of the Job:')
            job_content += '{}\n'.format(job_url)
            #job_content += '{}\n'.format('Skills for the Job:')
            job_content += '{}'.format(skills)

            print(job_content)
            print()
            try:
                with open('{}/{}_{}.txt'.format(job_path, company_name.strip().replace('/','_'), job_name.replace('/','_')), 'w', encoding='utf-8') as f:
                    f.write(job_content)
            except FileExistsError:
                pass

        except AttributeError:
            time.sleep(2)
            pass

    searchPage -= 1
    url = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword={}&order=15&asc=0&page={}&mode=s&jobsource=2018indexpoc'.format(jobKeyword, searchPage)



