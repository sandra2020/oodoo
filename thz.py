import os

import requests,time
from bs4 import BeautifulSoup
from my_fake_useragent import UserAgent
ua=UserAgent(family='chrome')
res=ua.random()
header={"User-Agent":res}


n=0
while n<2:
    n=n+1
    url='http://73thz.com/forum.php?mod=forumdisplay&fid=181&filter=typeid&typeid=770&filter=typeid&page='+str(n)
    url_header='http://73thz.com/'
    page=requests.get(url,headers=header)
    html=page.text
    # print(html)
    soup=BeautifulSoup(html,'lxml')
    page_list=soup.find_all(class_='s xst')
    # print(page_list)
    for i in page_list:
        page_img =url_header+i['href']
        print(page_img,i.text)
        if os.path.exists('c:/th.cc-0911/'+i.text):
            pass
        else:
            os.mkdir('c:/th.cc-0911/'+i.text)
        try:
            soup_url=BeautifulSoup(requests.get(page_img,headers=header,timeout=10000).text,'lxml')
            soup_img=soup_url.find_all(class_='zoom')
            for img_url in soup_img:
                print(img_url['file'],img_url['id'])
                content_a=requests.get(img_url['file'],headers=header).content
                with open('c:/th.cc-0911/'+i.text+'/'+img_url['id']+'.jpg','wb')as ff:
                    ff.write(content_a)
                    ff.flush()
                    ff.close()
        except:
            pass