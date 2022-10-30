import os

import requests
from bs4 import BeautifulSoup
from my_fake_useragent import UserAgent
ua=UserAgent()
res=ua.random()
h={"User-Agent":res}
url='https://hgjhghjgh.y78r6.com/thread-1027355-1-1.html'
url_a='https://fdsafdsaf.co/'
page=requests.get(url,headers=h)
html=page.text
# print(html)
soup=BeautifulSoup(html,'lxml')
page_list=soup.find_all(class_='zoom')
# print(page_list)
for i in page_list:
    print(i['file'],i['id'])
    try:
        content_a = requests.get(i['file'],headers=h).content
        with open('c:/th.cc-0911/'+i['id']+'.jpg','wb') as ff:
            ff.write(content_a)
            ff.flush()
            ff.close()
    except:
        print('下载失败')
# for i in page_list:
#     page_url=url_a+i.a['href']
#     print(i.getText()[1:-1],page_url)
#     if os.path.exists('c:/th.cc-0911/'+i.getText()[1:-1])==False:
#         os.mkdir(r'c:/th.cc-0911/'+i.getText()[1:-1])
#         page_a=requests.get(page_url)
#         html_a=page_a.text
#         soup=BeautifulSoup(html_a,'lxml')
#         page_list_a=soup.find_all('img',class_='zoom')
#         for i_a in page_list_a:
#             print(i_a['id'],i_a['file'])
#             content_a=requests.get(i_a['file']).content
#             try:
#                 with open('c:/th.cc-0911/'+i.getText()[1:-1]+'/'+i_a['id']+'.jpg','wb') as ff:
#                     ff.write(content_a)
#                     ff.flush()
#                     ff.close()
#             except:
#                 print('下载失败')