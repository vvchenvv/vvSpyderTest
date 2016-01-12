#-*-coding:utf8-*-
from lxml import etree
#import GetArticleLink
import SaveLinkIntoFile
import requests
import json
import re

def GetTiebaImg(links,folder):
    for article in links:
        html = requests.get(article)
        html = re.sub(r'charset=(/w*)', 'charset=UTF-8', html.text)
        BackGroundFilter = etree.HTML(html)
        #BackGroundLink = BackGroundFilter.xpath('//div[@class="p_content "]/cc/div/img[@class="BDE_Image"]/@src')
        BackGroundLink = BackGroundFilter.xpath('//div[@class="l_post l_post_bright j_l_post clearfix  "]')
        imgnum = 0
        for each in BackGroundLink:
            reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot',''))
            ImgSrc = etree.HTML(reply_info['content']['content'])
            ImgLink = ImgSrc.xpath('//img[@class="BDE_Image"]/@src')

            if(len(ImgLink) > 0):
                print(ImgLink)
                SaveLinkIntoFile.SaveLinkIntoFile(ImgLink,'IMG'+str(imgnum),'jpg')
            imgnum = imgnum + 1


            #print(ImgSrc)
        #ImgSrc = BackGroundLink['content']['src']


htmlUrl = ['http://tieba.baidu.com/p/3774712708']
GetTiebaImg(htmlUrl,"vv")