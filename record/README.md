# python 爬虫

## urllib
- 包含模块
    - urllib.requiest: 打开读取urls
    - urllib.error: 包含request产生的常见错误. 使用try捕捉
    - rullib.parse: 包含解析url的方法
    - urllib.robotparser: 解析robots.txt文件  (道德问题)
    - **案例: `v1.py`**

- 网页编码问题解决
    - chardet: 可以自动检测页面文件的编码格式, 可能有误
    - ***案例: `v2.py`***
    
- request.date 的使用

    - 访问网络的两种方法

        - get

            - 用url参数传递，参数为dict， 然后用parse编码

        - post

            - 使用data参数

            - 使用post，http请求头可能需要更改
              - Content-Type: application/x-www.form-urlencode
              - Content-Length: 数据长度
              - 简而言之，一旦更改请求方法，注意修改其他请求头部信息
            - `urllib.parse.urlencode`可以把字符串转换成url的格式
            - ***案例 `v3.py`***

            ​	

- UserAgent

    - 用户代理，简称ua   属于headers的一部分，服务器通过ua来判断访问者身份
    - 设置UA
        - heads
        - add_head
        - **案例`v4.py`**



-  ProxyHandler处理（代理服务器）
  - 使用代理IP，是爬虫常用手段
  - 获取代理服务器的地址：
    - www.xicidaili.com
    - www.goubanjia.com
  - 代理用来伪装成真实用户，代理一定要有很多很多
  - 代理使用：
    1. 设置代理地址
    2. 创建ProxyHandler
    3. 创建Opener
    4. 安装Opener
  - **案例`V5.py`**



- 