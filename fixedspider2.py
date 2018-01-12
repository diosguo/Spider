#coding: utf-8
#import urllib3
import urllib
from bs4 import BeautifulSoup
from urllib import request
import requests

url='http://www.epei.net.cn/xg/48953.html'
i=0

while(1):
    if(i>5000):
        break
    requestss = request.Request(url)
    wb_data = urllib.request.urlopen(requestss)
    soup = BeautifulSoup(wb_data,'lxml')
    image=soup.select('body > div.mainer > div.picmainer > div > center > a > img')
    nextpages=soup.select('body > div.mainer > div.picmainer > div > center > a ')
    if(len(image)==0):
        print(type(image))
        print('img==0')
        print(len(nextpages))
        continue
    for img in image:
        print('          ' + str(i))
        imgsrc='http://www.epei.net.cn'+img.get('src')
        i+=1
        with open('F:\\Photo\\images\\'+str(i)+'.jpg','wb') as f:
            f.write(requests.get(imgsrc).content)

    nexturl=nextpages[0].get('href')
    if(str(nexturl).find('http')!= -1):
        url=str(nexturl)
    else:
        url='http://www.epei.net.cn'+ nexturl
    print(url)
