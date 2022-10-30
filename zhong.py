import os

import requests,re

from bs4 import BeautifulSoup
from my_fake_useragent import UserAgent
ua=UserAgent(family='chrome')
res=ua.random()
header={"User-Agent":res}
url='https://gdcgdfger.cc/thread-996554-1-1.html'
url_zheader='http://82thz.com/imc_attachad-ad.html?'
page=requests.get(url,headers=header).text
soup=BeautifulSoup(page,'lxml')
# page_img=soup.find_all(class_='zoom')
page_zhongzi=soup.find_all(class_='attnm')
print(page_zhongzi[0])
re_math=re.compile(r'(href=")(.*)?" id=')
url_zhong=re_math.search(page_zhongzi[0])
print(url_zhong)
