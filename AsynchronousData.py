from bs4 import BeautifulSoup
import requests
from urllib import request
import urllib
import time

url='https://weheartit.com/inspirations/taylorswift?page='

i=0
def get_page(url,data=None):
    global i
    requestss=request.Request(url)
    wb_data=urllib.request.urlopen(requestss)
    soup=BeautifulSoup(wb_data,'lxml')

    css='#wrapper > div > section > div:nth-child(9) > div.hits_group-things.clearfix > article:nth-of-type(2) > header > a > img'
    imgs = soup.select('img.entry-thumbnail')

    if data is None:
        for img in imgs:
            data={
                'img':img.get('src'),
            }
            print(data)
            with open('weheartit/'+str(i)+data['img'][-4:],'wb') as f:
                f.write(requests.get(data['img']).content)
            i+=1

def get_more_page(start,end):
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(2)

if __name__=='__main__':
    get_more_page(1,10)