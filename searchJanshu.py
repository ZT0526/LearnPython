#-*- coding: utf-8 -*-
import re
import urllib2
import json
import requests
import time

# userlink = []
# neadAirtcles = []
# currentPageCount = 1
# authorname = ' '
# total_pages = 1
# def getUrl():
#     global userlink
#     global  neadAirtcles
#     global  currentPageCount
#     global  authorname
#     global  total_pages
#
#     # while len(userlink) == 0:
#     if(authorname == ' '):
#         authorname = raw_input('请输入想检索的内容： ')
#
#     url = 'http://www.jianshu.com/search/do?q=' + authorname + '&type=note&page=' + str(
#         currentPageCount) + '&order_by=default'
#     headers = {
#         # '(Request - Line)' : 'POST / search / do?q = ios & type = note & page = 1 & order_by = default HTTP / 1.1',
#         'Host': 'www.jianshu.com',
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0',
#         'Accept': 'application/json',
#         'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
#         'Accept-Encoding': 'gzip, deflate',
#         'X-CSRF-Token': 'AaptezFCpyFRqRuLfUNSec2sXezPdSkevhSOumWdjmQBwcsqtFj7Y4++9C7q1KNYcdDeKYPYSx2LF8TOv/yraw==',
#         'Referer': 'http://www.jianshu.com/search?q=ios&page=' + str(
#         currentPageCount) + '&type=note',
#         'Cookie': '_ga=GA1.2.1123264411.1477987596; _m7e_session=ca00c4a06553d05d9582f8608cec77d6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215f90ad001a20-0dec543cc50fda-485960-1024000-15f90ad001b249%22%2C%22%24device_id%22%3A%2215f90ad001a20-0dec543cc50fda-485960-1024000-15f90ad001b249%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; sajssdk_2015_cross_new_user=1; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1509960778,1509981445; _gid=GA1.2.809709895.1509960780; signin_redirect=http%3A%2F%2Fwww.jianshu.com%2Fsearch%3Fq%3Dios%26page%3D1%26type%3Dnote; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1509982101'
#     }
#     page = requests.post(url=url, headers=headers)  # 获取网页中的json文件。
#     json_data = json.loads(page.text)
#     if(currentPageCount == 1):
#         total_pages = json_data['total_pages']
#
#     if (total_pages > 0 and json_data.has_key('entries')):
#         for airtcle in json_data['entries']:
#             # 标题
#             airtcleTile = airtcle['title']
#             dr = re.compile(r'<[^>]+>', re.S)
#             airtcleTile = dr.sub('', airtcleTile)
#             # 链接
#             slug = airtcle['slug']
#             airtcleUrl = 'http://www.jianshu.com/p/' + slug
#
#             likeCount = airtcle['likes_count']
#             if (likeCount > 50):
#                 neadAirtcles.append(airtcle)
#                 titleAdnUrl = airtcleTile + ' ' + airtcleUrl + '  like: ' + str(likeCount)
#                 print  titleAdnUrl
#         currentPageCount += 1
#         if (currentPageCount < total_pages):
#             time.sleep(2)
#             getUrl()
#     elif(json_data.has_key('error')):
#         time.sleep(3)
#         getUrl()
#
#
#
#
# getUrl()


class JianShuSearch:

    def __init__(self):
        self.total_pages = 1
        self.userlink = []
        self.neadAirtcles = []
        self.currentPageCount = 1
        self.searchContent = ' '
        self.sleepCount = 2

    def getUrl(self):

        # while len(userlink) == 0:
        if (self.searchContent == ' '):
            self.searchContent = raw_input('请输入想检索的内容： ')

        url = 'http://www.jianshu.com/search/do?q=' + self.searchContent + '&type=note&page=' + str(
            self.currentPageCount) + '&order_by=default'
        headers = {
            # '(Request - Line)' : 'POST / search / do?q = ios & type = note & page = 1 & order_by = default HTTP / 1.1',
            'Host': 'www.jianshu.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0',
            'Accept': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'X-CSRF-Token': 'AaptezFCpyFRqRuLfUNSec2sXezPdSkevhSOumWdjmQBwcsqtFj7Y4++9C7q1KNYcdDeKYPYSx2LF8TOv/yraw==',
            'Referer': 'http://www.jianshu.com/search?q=ios&page=' + str(
                self.currentPageCount) + '&type=note',
            'Cookie': '_ga=GA1.2.1123264411.1477987596; _m7e_session=ca00c4a06553d05d9582f8608cec77d6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215f90ad001a20-0dec543cc50fda-485960-1024000-15f90ad001b249%22%2C%22%24device_id%22%3A%2215f90ad001a20-0dec543cc50fda-485960-1024000-15f90ad001b249%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; sajssdk_2015_cross_new_user=1; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1509960778,1509981445; _gid=GA1.2.809709895.1509960780; signin_redirect=http%3A%2F%2Fwww.jianshu.com%2Fsearch%3Fq%3Dios%26page%3D1%26type%3Dnote; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1509982101'
        }
        page = requests.post(url=url, headers=headers)  # 获取网页中的json文件。
        json_data = json.loads(page.text)
        if (self.currentPageCount == 1):
            self.total_pages = json_data['total_pages']

        if (self.total_pages > 0 and json_data.has_key('entries')):
            for airtcle in json_data['entries']:
                # 标题
                airtcleTile = airtcle['title']
                dr = re.compile(r'<[^>]+>', re.S)
                airtcleTile = dr.sub('', airtcleTile)
                # 链接
                slug = airtcle['slug']
                airtcleUrl = 'http://www.jianshu.com/p/' + slug

                likeCount = airtcle['likes_count']
                if (likeCount > 10):
                    self.neadAirtcles.append(airtcle)
                    titleAdnUrl = airtcleTile + ' ' + airtcleUrl + '  like: ' + str(likeCount)
                    print  titleAdnUrl
                    self.currentPageCount += 1
            if (self.currentPageCount < self.total_pages):
                time.sleep(self.sleepCount)
                self.getUrl()
        elif (json_data.has_key('error')):
            print json_data['error']

            self.sleepCount += 1
            time.sleep(self.sleepCount)
            self.getUrl()


jianshuSearch = JianShuSearch()
jianshuSearch.getUrl()