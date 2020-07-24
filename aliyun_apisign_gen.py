# -*- coding: utf-8 -*-
import base64, hmac, urllib.parse, urllib.request, json
import config_aliyun


class Caculate_Sign(object):

    def __init__(self, url):
        self.url = url

    def sign2sign(self):
        sortedurl = sorted(self.url.items(), key=lambda x: x[0])
        urlencodeParams = urllib.parse.urlencode(sortedurl)
        urlencodeParams = urllib.parse.quote_plus(urlencodeParams)
        sign2sign = "GET" + "&" + urllib.parse.quote_plus("/") + "&" + urlencodeParams
        return sign2sign


def main():
    s2s = Caculate_Sign(config_aliyun.url).sign2sign()
    h = hmac.new((config_aliyun.securitykey + "&").encode(), s2s.encode(), digestmod='sha1')
    hrecode = base64.encodebytes(h.digest()).strip().decode()
    config_aliyun.url["Signature"] = hrecode
    finalurl = config_aliyun.endpoint + "?" + urllib.parse.urlencode(config_aliyun.url)
    response = urllib.request.urlopen(finalurl)
    res = json.load(response)
    print(res['data'])


if __name__ == '__main__':
    main()
