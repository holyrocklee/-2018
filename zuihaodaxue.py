#python3
# encoding=utf-8

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
response = requests.get(url,'html.parser')
response.raise_for_status()
response.encoding = response.apparent_encoding
data = response.text

soup = BeautifulSoup(data,'html.parser')
Datadetails = soup.find('tbody',attrs={'class':"hidden_zhpm"})
name = []
score = []
for i in Datadetails.find_all('tr'):
    school_name = i.find('div', attrs={'align': 'left'}).get_text()
    name.append(school_name)
    tds = i('td')
    school_score = tds[3].string
    score.append(school_score)
#print(name)
#print(score)
tplt="{0:^4}\t{1:{3}^10}\t{2:8}"
print(tplt.format("排名","学校","总分",chr(12288)))
for (a,b) in zip(name,score):
    print(tplt.format(name.index(a)+1,a,b,chr(12288)))

wb = Workbook()
ws1 = wb.active
#ws1 = wb.get_active_sheet()  旧版，现在不建议使用
ws1.title = "中国大学排名"
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
# 然后返回由这些元组组成的列表。如果各个迭代器的元素个数不一致，
# 则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
for (o,m) in zip(name,score):
    col_A = 'A%s' % (name.index(o) + 1)
    col_B = 'B%s' % (name.index(o) + 1)
    ws1[col_A] = o
    ws1[col_B] = m
wb.save(filename='软科中国最好大学排名2018.xlsx')