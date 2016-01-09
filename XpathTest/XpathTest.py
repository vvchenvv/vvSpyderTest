#-*-coding:utf8-*-
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json
import re
import sys

'''重新运行之前请删除content.txt，因为文件操作使用追加方式，会导致内容太多。'''

def towrite(contentdict):
    f.writelines(u'回帖时间:' + str(contentdict['topic_reply_time']) + '\n')
    f.writelines(u'回帖内容:' + str(contentdict['topic_reply_content']) + '\n')
    f.writelines(u'回帖人:' + contentdict['user_name'] + '\n\n')

def spider(url):
    html = requests.get(url)
    html = re.sub(r'charset=(/w*)', 'charset=UTF-8', html.text)
    selector = etree.HTML(html)
    content_field = selector.xpath('//div[@class="l_post j_l_post l_post_bright  "]')
    item = {}
    for each in content_field:
        reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot',''))
        author = reply_info['author']['user_name']
        content = each.xpath('div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content  clearfix"]/text()')
        reply_time = reply_info['content']['date']
        print("content:{0}".format(content))
        print("Reply_time:{0}".format(reply_time))
        print("Author:{0}".format(author))
        item['user_name'] = author
        item['topic_reply_content'] = content
        item['topic_reply_time'] = reply_time
        towrite(item)

if __name__ == '__main__':
    pool = ThreadPool(8)
    f = open('content.txt','a',encoding='UTF-8')
    page = []
    for i in range(1,21):
        newpage = 'http://tieba.baidu.com/p/3522395718?pn=' + str(i)
        page.append(newpage)

    results = pool.map(spider,page)
    pool.close()
    pool.join()
    f.close()
