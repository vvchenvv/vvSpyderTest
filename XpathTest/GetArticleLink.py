#-*-coding:utf8-*-
from lxml import etree
import SaveLinkIntoFile
import requests
import re

def GetArticleLinks(url):
    TiebaUrlprefix = 'http://tieba.baidu.com'
    html = requests.get(url)
    html = re.sub(r'charset=(/w*)', 'charset=UTF-8', html.text)
    AirticleFilter = etree.HTML(html)
    #print(html)
    LinkSelector = AirticleFilter.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
    for i in range(len(LinkSelector)):
        LinkSelector[i] = TiebaUrlprefix + LinkSelector[i]
    print(LinkSelector)
    return LinkSelector
    # print("the number of links:{0}".format(len(LinkSelector)))
    # for each in LinkSelector:
    #     print("The links:{0}".format_map(each[0]))


TiebaUrl = 'http://tieba.baidu.com/f?kw=%E5%A3%81%E7%BA%B8&ie=utf-8'
GetArticleLinks(TiebaUrl)
htmlUrl = ['http://tieba.baidu.com/p/3774712708','http://tieba.baidu.com/p/3774712709']
SaveLinkIntoFile.SaveLinkIntoFile(htmlUrl,'Html',"html")

#//*[@id="thread_list"]/li[5]/div/div[2]/div[1]/div[1]/a