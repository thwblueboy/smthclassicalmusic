# coding=utf-8

import sys, urllib2
from datetime import datetime
import time
from myauth2 import MyAuth2

try:
    # init the auth client
    ma2 = MyAuth2(1193184550)

    # extract funds information from the web page
    wp = urllib2.urlopen(urllib2.Request('http://www.newsmth.net/nForum/board/classicalmusic?ajax', headers={"X-Requested-With":"XMLHttpRequest"}))
    content = wp.read(10000)
    content = content[0 : content.rindex('b-content')]
    contentutf8 = content.decode('gbk').encode('utf-8')
    ind1 = contentutf8.index('版面积分:')
    ind1 = contentutf8.index(':', ind1)
    ind2 = contentutf8.index('</span>', ind1)
    boardfund = contentutf8[ind1 + 1 : ind2]
    f = open('/home/caq/smthcm/fundshistory.txt', 'a')
    f.write(str(datetime.now()) + '\t' + str(boardfund) + '\n')
    f.close()
    msg = '[' + time.strftime('%H:%M', time.localtime(time.time())) + '] 目前本版积分是' + boardfund + '，感谢版友们的支持，欢迎大家多多灌水，有条件的来捐献积分哦～'

    # store the funds to local file
    f = open('/home/caq/smthcm/smthcm.config')
    cks = f.readline().strip().split('\t')
    tks = f.readline().strip().split('\t')
    f.close()

    # post to weibo
    ma2.client.post.statuses__update(status=msg)
except:
    raise
    # pass
