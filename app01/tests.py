from django.test import TestCase

# Create your tests here.

import urllib.request
import re
import requests
# ret=requests.get('http://news.cnhubei.com/ctjb/ctjbsgk/ctjb40/200808/W020080822221006461534.jpg')
# print(ret.content)
# with open('wb') as f:
#     f.write(ret.content)
#     f.close()
# #

#
import selenium#驱动浏览器的一个库，让js能够渲染页面,可以打开浏览器
from selenium import webdriver
# driver=webdriver.PhantomJS()

#


#下载phantomjs，将bin目录下的文件放到环境变量下


#安装lxml
#安装beautifulsoup4
#安装pyquery
from pyquery import PyQuery

from bs4 import BeautifulSoup

import urllib.request
res=urllib.request.urlopen('http://www.baidu.com')
# print(res.read().decode('utf-8'))
print(type(res))
print(res.status)