######將txt檔製成dataFram，並存成csv檔######

import pandas as pd
import os

source_file_path = r'./job104_list'
file_list = os.listdir(source_file_path)
#print(file_list)

df = pd.DataFrame(columns = ['索引', '公司名稱', '公司網址', '職缺名稱', '職缺網址', '所需技能'])
job_info_row_data = []
for n, each_job in enumerate(file_list):
    job_path = source_file_path + '/' + each_job
    with open(job_path, 'r', encoding='utf-8') as f:
        tmp_job_string = f.read().split('---Job Content---\n')[-1]
    tmp_row_data = [str(n + 1)] + tmp_job_string.split('\n')
    job_info_row_data.append(tmp_row_data)
print(job_info_row_data)

df = df.append(pd.DataFrame(job_info_row_data, columns = ['索引','公司名稱', '公司網址', '職缺名稱', '職缺網址', '所需技能']))
df.to_csv(r'./job104_bigData.csv', index=False, encoding = 'utf-8')

