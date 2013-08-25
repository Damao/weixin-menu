# encoding: utf-8

# author hzlzh
# must be python 2.x

import json
import urllib
import urllib2

appid = ""
secret = ""
access_url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"
menu_url = "https://api.weixin.qq.com/cgi-bin/menu/create?%s"


def get_access_token():
    f = urllib.urlopen(access_url % (appid, secret))
    resp = json.loads(f.read())
    print resp
    return resp['access_token']


def generate_menu(token):
    menus = {
        "button": [
            {
                "type": "click",
                "name": "这是什么？",
                "key": "helpMenu"
            },
            {
                "type": "view",
                "name": "(miao.in)",
                "url": "http://miao.in/"
            }]
    }
    params = {'access_token': urllib.quote(token)}
    url = menu_url % urllib.urlencode(params)
    request = urllib2.Request(url, json.dumps(menus, ensure_ascii=False))
    response = urllib2.urlopen(request)
    print response.read()


def main():
    token = get_access_token()
    generate_menu(token)


if __name__ == '__main__':
    main()