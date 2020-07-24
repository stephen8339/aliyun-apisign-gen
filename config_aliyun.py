# -*- coding: utf-8 -*-
import datetime
import random

endpoint = 'https://tds.aliyuncs.com'
accesskey = 'testid'
securitykey = 'testkey'
timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
url = {
    'Action': 'SasInstallCode',
    'Version': '2018-12-03',
    'Format': 'JSON',
    'Timestamp': timestamp,
    'AccessKeyId': accesskey,
    'SignatureMethod': 'HMAC-SHA1',
    'SignatureNonce': random.randint(10000, 99999999999999),
    'SignatureVersion': '1.0'
}