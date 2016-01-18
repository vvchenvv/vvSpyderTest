#-*-coding:utf8-*-
from lxml import etree
import requests
import re

def GetImgLink(url):
    html = requests.get(url)
    html = re.sub(r'charset=(/w*)', 'charset=UTF-8', html.text)
    ImgFilter = etree.HTML(html)
    ImgLink = ImgFilter.xpath('//div[@class="l_post j_l_post l_post_bright  "]')[0]
    links = ImgLink.xpath('//div[@class="d_author"]/ul/li/div[@class="icon_relative j_user_card"]/a/img/@data-tb-lazyload')
    #links = ImgLink.xpath('//div[@class="d_author"]/ul/li/div[@class="icon_relative j_user_card"]/a/img/@src')
    print(links)
    print("before set list:{0}".format(len(links)))
    links = list(set(links))
    print("after set list:{0}".format(len(links)))
    i = 0
    for each_link in links:
        graphic = requests.get(each_link)
        with open("img{0}.jpg".format(i),"wb") as code:
            code.write(graphic.content)
        i = i + 1
    # for each in ImgLink:
    #     links = each.xpath('//div[@class="d_author"]/ul/li/div[@class="icon_relative j_user_card"]/a/img/@data-tb-lazyload')
    #     print("*********loop*********{0}\n".format(len(links)))
    #     print(links)
        # i = 0
        # for each_link in links:
        #     graphic = requests.get(each_link)
        #     with open("img{0}.jpeg".format(i),"wb") as code:
        #         code.write(graphic.content)
        #     i = i + 1

if __name__ == '__main__':
    pagelink = 'http://tieba.baidu.com/p/3522395718?pn=1'
    GetImgLink(pagelink)

