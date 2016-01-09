#-*-coding:utf8-*-
from lxml import etree
import requests
import re

def GetImgLink(url):
    html = requests.get(url)
    html = re.sub(r'charset=(/w*)', 'charset=UTF-8', html.text)
    ImgFilter = etree.HTML(html)
    ImgLink = ImgFilter.xpath('//div[@class="l_post j_l_post l_post_bright  "]')
    ImgItem = {}
    for each in ImgLink:
        #links = each.xpath('//div[@class="d_author"]/ul/li/div[@class="icon_relative j_user_card"]/a/img/@src')
        links = each.xpath('//*[@id="j_p_postlist"]/div[24]/div[2]/ul/li[1]/div/a/img/@src')
        #//*[@id="j_p_postlist"]/div[24]/div[2]/ul/li[1]/div/a/img
        #links = each.xpath('//div[@class="d_author"]/ul/li/div[@class="icon_relative j_user_card"]/a/img/[[@src and [not @src="http://tb2.bdstatic.com/tb/static-pb/img/head_80.jpg"]] or @data-tb-lazyload]')
        print(links)

pagelink = 'http://tieba.baidu.com/p/3522395718?pn=1'
GetImgLink(pagelink)

