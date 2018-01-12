# encoding=utf8
from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib import request
import requests
import urllib
print()
url='https://baike.baidu.com/item/姚明'
print(quote(url))
url=url[:10]+quote(url[10:])
requestss=request.Request(url)
wb_data=urllib.request.urlopen(requestss)

soup = BeautifulSoup(wb_data,'lxml')
info=soup.select('body > div.body-wrapper.feature.feature_small.starSmall > div.content-wrapper > div > div.main-content > div > div.basic-info.cmn-clearfix > dl.basicInfo-block.basicInfo-right > dt')
value=soup.select('body > div.body-wrapper.feature.feature_small.starSmall > div.content-wrapper > div > div.main-content > div > div.basic-info.cmn-clearfix > dl.basicInfo-block.basicInfo-right > dd')

for item,name in zip(info,value):
    if item.text=='老    婆':
        print(name.select('a')[0].text)

# print(soup)