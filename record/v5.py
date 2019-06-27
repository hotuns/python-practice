'''
使用代理访问网站
'''
from urllib import request, error
if __name__ == "__main__":
    url = 'http://www.baidu.com'

    # 1. 设置代理地址
    proxy = {'http': '182.92.105.136:3128'}
    # 2. 创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3. 创建Opener
    opener = request.build_opener(proxy_handler)
    # 4. 安装Opener
    request.install_opener(opener)

    # 现在如果访问,则使用代理服务器

    try:
        res = request.urlopen(url)
        html = res.read().decode()
        print(html)
    except Exception as e:
        print(e)
