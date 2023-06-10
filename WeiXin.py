#!/usr/bin/env  python
import requests
import json
import urllib
import urllib2

def get_token():
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    data = eval(res)
    return data['access_token']



#a = get_token()
def send_msg(data):
    url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+get_token()
    values = """{"touser" : "@all" ,
            "toparty":"@all",
            "msgtype":"text",
            "agentid":"@all",
            "text":{
                "content": "%s"
            },
            "safe":"0"
            }""" %data

    data = json.loads(values)
    req = requests.post(url, values)

for i in range(2):
    send_msg(i)
