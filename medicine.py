from bs4 import BeautifulSoup
import urllib
import requests
from urllib import request
import xlwt

def outToExcel(datas):
    workbook=xlwt.Workbook()
    sheet=workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    sheet.write(0,0,'商品名称')
    sheet.write(0,1,'通用名称')
    sheet.write(0,2,'生产企业')
    sheet.write(0,3, '批准文号')
    sheet.write(0, 4, '适应症')
    sheet.write(0, 5, '剂型')
    sheet.write(0, 6, '规格')
    sheet.write(0, 7, '用法用量')
    sheet.write(0, 8, '不良反应')
    sheet.write(0, 9, '有效期')
    propMap={
        'name':0,
        'gname':1,
        'org':2,
        'license':3,
        'application':4,
        'type':5,
        'spec':6,
        'method':7,
        'effect':8,
        'period':9
    }
    row=1
    for data in datas:
        keys=data.keys()
        for key in keys:
            print(key,type(key))
            sheet.write(row,propMap[key],data[key])
        row+=1
    workbook.save('Medicine.xls')

def getInfo(url):
    print(url)
    data={}
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    medicine = soup.select('#wrap990list1 > ul > li')
    string=str(medicine)
    if(string.find('不良反应')>0):
        data['effect']=string[string.find('不良反应'):string.find('<',string.find('不良反应'))]
    if (string.find('商品名称') > 0):
        data['name'] = string[string.find('商品名称')+5:string.find('<', string.find('商品名称'))]
    if(string.find('规格')>0):
        data['spec']=string[string.find('规格')+3:string.find('<',string.find('规格'))]
    if (string.find('生产企业') > 0):
        data['org'] = string[string.find('生产企业')+5:string.find('<', string.find('生产企业'))]
    if(string.find('通用名称')>0):
        data['gname']=string[string.find('通用名称')+5:string.find('<',string.find('通用名称'))]
    if (string.find('有效期') > 0):
        data['period'] = string[string.find('有效期')+4:string.find('<', string.find('有效期'))]
    if(string.find('剂型')>0):
        data['type']=string[string.find('剂型')+3:string.find('<',string.find('剂型'))]
    if (string.find('批准文号') > 0):
        data['license'] = string[string.find('批准文号')+5:string.find('<', string.find('批准文号'))]
    if (string.find('适应症') > 0):
        data['application'] = string[string.find('适应症')+9:string.find('<', string.find('适应症'))]
    if (string.find('用法用量') > 0):
        data['method'] = string[string.find('用法用量')+5:string.find('<', string.find('用法用量'))]
    return data

def run(url):
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    medicines=soup.select('#YproductList a.name')
    datas=[]
    for med in medicines:
        datas.append(getInfo('http://www.360kad.com'+med.get('href')))
    return datas

def pa():
    numberOfPage=0
    url = 'http://www.360kad.com/Category_842/Index.aspx'
    wb_data=requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    index=soup.select('body > div.Ywrap > div.Yright > div > div > span > span.end > select > option')
    print(len(index))
    datas=[]
    for i in range(1,len(index)+1):
        datas.extend(run(url+'?page='+str(i)))
    return datas

if __name__ =='__main__':
    datas=pa()
    outToExcel(datas)