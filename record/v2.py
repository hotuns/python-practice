'''
使用urllib.request请求一个网页内容
'''

from urllib import request
from targetUrl import url
import chardet

# Python 2.7.9 之后引入了一个新特性，当你使用urllib.urlopen一个 https 的时候会验证一次 SSL证书。当目标使用的是自签名的证书时就会报urllib.error.URLError错误。解决方法如下：
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def main():
    # 打开相应的url
    res = request.urlopen(url)
    # 读取结果, 读取出来类型是bytes
    html = res.read()

    # 使用chardet检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    html = html.decode(cs.get('encoding', 'utf-8'))

    print(html)


if __name__ == '__main__':
    main()
