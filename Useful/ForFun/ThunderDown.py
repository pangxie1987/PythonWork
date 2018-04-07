# -*- coding:utf-8 -*-
'''
实现迅雷自动下载
'''
import urllib
import os
import base64

def getThunderurl(url):
    # QutoUrl=(('AA'+url+'ZZ').encode('utf-8'))
    # downurl='thunder://'.encode('utf-8')+base64.b64encode(QutoUrl)
    # return downurl

    return ('thunder://'.encode('utf-8')+base64.b64encode(('AA'+url+'ZZ').encode('utf-8')))

#url='magnet:?xt=urn:btih:CF6D363B9BE49927AAD133C95413B8C9C1862382'
url = "magnet:?xt=urn:btih:bd86f3dc32c45861a4e73887f38d2cc8eed5a44e&dn=The.Bold.the.Corrupt.and.the.Beautiful.2017.720p.BluRay.x264-WiKi&tr=http%3A%2F%2Ftracker.trackerfix." \
      "com%3A80%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2710&tr=udp%3A%2F%2F9.rarbg.to%3A2710"

os.chdir("D:\Program Files (x86)\Program")
thunderUrl=getThunderurl(url)

os.system("Thunder.exe -StartType:DesktopIcon \"%s\""%url)

