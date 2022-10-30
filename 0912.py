import requests
from bs4 import BeautifulSoup
h={'user-agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
url='http://73thz.com/thread-2572923-1-1.html'
url_a='https://fdsafdsaf.co/'
page=requests.get(url,headers=h)
html=page.text
# print(html)
soup=BeautifulSoup(html,'lxml')
page_list=soup.find_all(class_='zoom')
#print(page_list)
for i in page_list:
    print(i['file'],i['id'])

    try:
        content_a = requests.get(i['file'],headers=h,timeout=5000).content
        with open('c:/th.cc-0911/'+i['id']+'.jpg','wb') as ff:
            ff.write(content_a)
            ff.flush()
            ff.close()
    except:
        print('下载失败')