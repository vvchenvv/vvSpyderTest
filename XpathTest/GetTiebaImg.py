#-*-coding:utf8-*-
from lxml import etree
import SaveLinkIntoFile
import requests
import json
import re

def GetTiebaImg(links):
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

if __name__ == '__main__':
    htmlUrl = ['http://tieba.baidu.com/p/4076991537']
    GetTiebaImg(htmlUrl,"vv")