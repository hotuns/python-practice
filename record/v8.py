# import requests

# url = 'https://www.baidu.com'

# data = {
#     'wd': '比我帅的人'
# }
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36", "X-Requested-With": "XMLHttpRequest"
# }
# res = requests.get(url, params=data, headers=headers)

# #  post方法
# # res = requests.post(url, data=data)

# print('text', res.text)
# print('content', res.content)
# print('url', res.url)
# print('encodeing', res.encoding)
# print('code', res.status_code)


'''
requests - 有道词典
'''
import requests
from urllib import request, parse
from time import time
import random
import hashlib


def get_salt():
    '''
    (ts, salt) 的生成算法'''
    ts = str(int(time()*1000))
    return (ts, ts + str(random.randint(0, 10)))


def get_sign(kw, salt):
    '''
    (sign, bv) 的生成算法'''
    i = salt
    str = 'fanyideskweb{}{}@6f#X3=cCuncYssPsuRUE'.format(kw, i)
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    sign = m.hexdigest()

    navigator_appVersion = "5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    m.update(navigator_appVersion.encode('utf-8'))
    bv = m.hexdigest()
    return (sign, bv)


def youdao(key):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    # 这里数据是从network里面复制的
    # 通过查找js代码, 找到 salt 的生成算法
    # r = "" + (new Date).getTime(),
    # i = r + parseInt(10 * Math.random(), 10);
    # 查找js代码, 找到 sign 的生成算法
    # md5("fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE")
    hash_data = get_salt()
    bs_data = get_sign(key, hash_data[1])
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": hash_data[1],
        "sign": bs_data[0],
        "ts": hash_data[0],
        "bv": bs_data[1],
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    headers_data = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "keep-alive",
        "Content-Length": str(len(data)),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-1087722047@115.153.153.238; _ntes_nnid=44f9263774968ccb7a63d538bc4a90dc,1502864018176; _ga=GA1.2.72994830.1543999386; JSESSIONID=aaaYwg1bHeJE16OwXXxUw; OUTFOX_SEARCH_USER_ID_NCOO=1704243123.1780095; ___rl__test__cookies=1561702259843",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36", "X-Requested-With": "XMLHttpRequest"
    }

    try:
        res = requests.post(url, data=data, headers=headers_data)
        print(res.json())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    youdao(input('请输入要翻译的文字'))
