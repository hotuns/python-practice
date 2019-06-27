'''
使用urllib.request请求一个网页内容
'''

from urllib import request, parse
import json

# Python 2.7.9 之后引入了一个新特性，当你使用urllib.urlopen一个 https 的时候会验证一次 SSL证书。当目标使用的是自签名的证书时就会报urllib.error.URLError错误。解决方法如下：
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def main():

    # get请求
    def getReq():
        # 打开相应的url
        url = 'https://www.baidu.com/s?'
        wd = input('请输入关键词')
        # date,需要使用字典结构
        qs = {
            'wd': wd
        }
        qs = parse.urlencode(qs)
        target = url + qs
        print('target', target)
        res = request.urlopen(target)
        html = res.read()
        html = html.decode()
        print(html)

    # post请求

    def postReq():
        url = 'https://fanyi.baidu.com/sug'
        kw = input('请输入需要翻译的')
        data = {
            'kw': kw
        }
        data = parse.urlencode(data).encode('utf-8')

        # 构造一个请求头
        headers = {
            # post请求至少包含content-length
            'Content=Length': len(data)
        }

        # 发送请求
        urlArg = request.Request(url, data=data, headers=headers)
        res = request.urlopen(urlArg)

        res_data = json.loads(res.read())['data']
        for i in res_data:
            print('{}: {}'.format(i['k'], i['v']))

    postReq()


if __name__ == '__main__':
    main()
