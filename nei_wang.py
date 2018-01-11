#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json

import requests
class DictObj():
    def __init__(self):
        pass

class PostMan ():
    HOST = '10.10.10.4'
    PORT = '9080'
    ZXDJK = 'zxdjk'

    POST_MAN_INFO={}
    TOKEN=''
    app_list = []

    def __init__(self):
        print('new')


    def parse_url(self,url):
        return url.replace('{{host}}',self.HOST).replace('{{port}}',self.PORT).replace('{{zxdjk}}',self.ZXDJK)

    def parse_body(self,body):
        i={}
        for item in body:
            i={**i,**{item['key']:item['value']}}
        return i

    def parse(self,response,*args,**kvargs):
        print('访问请求花费了%s!'%response.elapsed)
        print(response.request.headers)
        print('接口返回的数据是:%s'%response.json())
        res = response.json()
        if self.TOKEN =='':
            self.TOKEN = json.loads(res['content'])['token']
        print('TOKEN is %s'%self.TOKEN)

    def postApi(self,api_list):
        for api in student_api_list:
            ob = DictObj()
            ob.__dict__.update(api)
            print(ob.name)
            url = self.parse_url(ob.request.get('url').get('raw'))
            body = ob.request.get('body').get('formdata')
            body = self.parse_body(body)
            print('TOKEN is %s'%self.TOKEN)
            headers ={'token':self.TOKEN}
            print(url)
            requests.api.request(
                method=ob.request.get('method','post'),
                headers =headers,
                url = url,
                hooks =dict(response=self.parse),
                data = body,
            )



with open('zxt.json','r') as load_file:
    app_list =[]
    POST_MAN_INFO = json.load(load_file)['item']
    for app in POST_MAN_INFO:
        app_item = DictObj()
        app_item.__dict__.update(app)
        app_list.append(app_item)
    student_api_list = app_list[0].item
    x_man = PostMan()
    x_man.postApi(student_api_list)



