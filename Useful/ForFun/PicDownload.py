#-*- coding:utf-8 -*-
'''
爬取网络上的图片

'''
import requests
import re
import os
from bs4 import BeautifulSoup


path="E:/Pypic/"
passurl="http://gaoqing.la/720p/"

def request(url):

    r=requests.get(url)
    s=BeautifulSoup(r.text,'html.parser')
    #匹配页面中src的标签
    piclinks=s.findAll(src=re.compile('jpg'))

    for links in piclinks:
        print(links)

        #获取src数据
        link=links['src']
        html=requests.get(link)
        print(link)

        #获取电影名称
        moviename=links['alt']
        print(moviename)

        #获取图片名称
        picname = os.path.split(link)[1]
        print(os.path.split(link))

        print('-'*100)

        #将电影名称+图片名称+图片链接保存到文件中
        with open (path+'movie.txt','a+',encoding='utf-8') as h:
            h.write(str(moviename)+'\t'+picname+'\n')


        #保存获取到的图片
        with open(path+picname,'wb') as f:
            f.write(html.content)


#获取第一页的数据
request(passurl)

#获取后面几页的数据
newurl=passurl+'page/'
n=2
while True:
    #实现下一页图片的获取
    url=newurl+str(n)
    print(url)
    n+=1
    request(url)

    response=requests.get(url)
    print(response.status_code)
    if response.status_code==404:
        print('超出页面限制，终止访问')
        break