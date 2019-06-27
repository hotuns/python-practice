# Python 2.7.9 之后引入了一个新特性，当你使用urllib.urlopen一个 https 的时候会验证一次 SSL证书。当目标使用的是自签名的证书时就会报urllib.error.URLError错误。解决方法如下：
from urllib import request, error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == "__main__":
    url = 'https://www.baidu.com/'
    agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    try:
        # 使用add_header
        # req = request.Request(url)
        # req.add_header('User-Agent', agent)

        headers = {
            'User-Agent': agent
        }
        reqData = request.Request(url, headers=headers)

        req = request.urlopen(reqData)
        html = req.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except Exception as e:
        print(e)
