#-*-coding:utf8-*-
from lxml import etree
import SaveLinkIntoFile
import requests
import re
import os
import GetTiebaImg

def GetArticleLinks(url):
    TiebaUrlprefix = 'http://tieba.baidu.com'
    html = requests.get(url)
    html = re.sub(r'charset=(/w*)', 'charset=UTF-8', html.text)
    AirticleFilter = etree.HTML(html)
    #print(html)
    LinkSelector = AirticleFilter.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
    for i in range(len(LinkSelector)):
        foldername = LinkSelector[i].strip().lstrip().rstrip('/').replace('/','')
        print(foldername)
        MakeDir("D:\Python_Cache",foldername)
        LinkSelector[i] = TiebaUrlprefix + LinkSelector[i]
        GetTiebaImg.GetTiebaImg([LinkSelector[i]])
        os.chdir("../")

    print(LinkSelector)
    return LinkSelector
    # print("the number of links:{0}".format(len(LinkSelector)))
    # for each in LinkSelector:
    #     print("The links:{0}".format_map(each[0]))

def MakeDir(TargetDir,FolderName):
    new_path = os.path.join(TargetDir,FolderName)
    if(not os.path.isdir(new_path)):
        os.makedirs(new_path)
    os.chdir(new_path)
    # print("the Current dir is:{0}".format(os.getcwd()))
    # os.chdir("../")
    # print("the Current dir is:{0}".format(os.getcwd()))


if __name__ == '__main__':
    MakeDir("D:\Python_Cache","Cache1")
    TiebaUrl = 'http://tieba.baidu.com/f?kw=%E5%A3%81%E7%BA%B8&ie=utf-8'
    GetArticleLinks(TiebaUrl)
    # htmlUrl = ['http://tieba.baidu.com/p/3774712708','http://tieba.baidu.com/p/3774712709']
    # SaveLinkIntoFile.SaveLinkIntoFile(htmlUrl,'Html',"html")

#//*[@id="thread_list"]/li[5]/div/div[2]/div[1]/div[1]/a