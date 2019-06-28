from urllib import request, error, parse
from http import cookiejar
# Python 2.7.9 之后引入了一个新特性，当你使用urllib.urlopen一个 https 的时候会验证一次 SSL证书。当目标使用的是自签名的证书时就会报urllib.error.URLError错误。解决方法如下：
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 创建cookiejar实例
cookie = cookiejar.CookieJar()

# 生成coookie的管理器
cook_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 生成https请求管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cook_handler)


def login():
    '''
    初次登录需要用户名和密码
    '''

    # 登录请求的地址,form的 action属性
    url = 'https://www.zhihu.com/api/v3/oauth/sign_in'

    # key的值需要从登录form对应的name属性获取
    data = {
        'username': 'hedongshu@foxmail.com',
        'password': 'hds1512>zhihu'
    }
    # 把数据进行编码
    data = parse.urlencode(data)

    headers = {
        'cookie': '''_zap = 49c6536d-a924-40fd-9971-031f27e6cca1
        _xsrf = ilhzJ17ALSEKFpEjs8L5bsKcVLFDKF7p
        d_c0 = "APAuWHPWpQ-PTtWzP6VYLI3yt1lat9j7-Qk=|1561607217"
        tgw_l7_route = 7c109f36fa4ce25acb5a9cf43b0b6415
        capsion_ticket = "2|1:0|10:1561607349|14:capsion_ticket|44:ZWI2NjYxNDI3NmY4NDc0ZjkyMGJhM2IwZmRiMGFkYTE=|51ec6e117296496a6e7ed300cb8e7c3035c20c499997e6c9fe99af653b119782''',
        'user-agent': '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36''',
        "origin": 'https://www.zhihu.com'
    }

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener发送请求,获取响应
    res = opener.open(req)

    print(res.read().decode())


def getPage():
    url = 'http://message.bilibili.com/#/reply'

    res = request.Request(headers=headers)
    html = res.read().decode()
    request
    with open('res.html', 'w') as f:
        f.write(html)


if __name__ == "__main__":
    login()
    # getPage()
