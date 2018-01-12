#coding: utf-8
import urllib3
import urllib
from bs4 import BeautifulSoup
from urllib import request
import requests
url='http://www.5442.com/meinv/20150530/21538.html'
i=0
while(1):
    if(i>1000):
        break
    requestss = request.Request(url)
    wb_data = urllib.request.urlopen(requestss)
    soup = BeautifulSoup(wb_data,'lxml')
    image=soup.select('#contents > a > img')
    nextpages=soup.select('#contents > a')
    if(len(image)==0):
        nextsections=soup.select('#prenext > a')
        print(len(nextsections))
        url=nextsections[-1].get('href')

        print('img==0')
        print(len(nextpages))
        continue
    for img in image:
        print('          ' + str(i))
        imgsrc=img.get('src')
        i+=1
        with open('images/'+str(i)+'.jpg','wb') as f:
            f.write(requests.get(imgsrc).content)

    nexturl=nextpages[0].get('href')
    if(str(nexturl).find('http')!= -1):
        url=str(nexturl)
    else:
        url=url[0:url.rindex('/')+1]+nexturl
    print(url)