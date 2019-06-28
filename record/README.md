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



## cookie & session

- 由于http协议的无记忆性，人们为了弥补，采用的一个补充协议
- cookie是发放给用户（http浏览器）的一段信息， session是保存在服务器上对应的另一半信息，用来记录用户信息
- 区别：
  - 存放位置不同
  - cookie不安全
  - session会保存在服务器上一段时间
  - 单个cookie保存数据不超过4k，很多浏览器限制一个站点最多保存20个
- session的存放位置
  - 存在服务器端
  - 一般情况，session是放在内存或者数据库中
- 使用cookie登录
  - 直接把cookie复制下来
  - http模块包含关于cookie的模块，通过他们可以自动使用cookie
    - CookieJar
      - 管理存储cookie，向http请求添加cookie。
      - cookie存在内存中CookieJar实例回收后cookie消失
    - FileCookieJar(filename, delayload=None, policy=None)
      - 使用文件管理cookie
    - MozillaCookieJar(filename, delayload=None, policy=None)
      - 创建mocilla浏览器cookie.text兼容的FileCookieJar 实例
    - LwpCookieJar(filename, delayload=None, policy=None)
      - 创建于libwww-pel标准兼容的Set-Cookie3 格式的FileCookieJar实例
- 流程
  - 打开登录页面后自动通过用户名密码登录
  - 自动提取反馈回来的cookie
  - 利用提取的cookie登录隐私页面
- **案例`v6.py`**



## SSL（https）

- SSL证书，就是指蹲守SSL安全套阶层协议的服务器证书
- 美国网景公司开发
- CA 是数字证书认证中心，是 发放、管理、废除数字证书的收信人的第三方机构





## js加密

- 有的反爬虫策略采用js对需要传输的数据进行加密（通常取md5值）
- 经过加密，传输的就是密文。但是加密过程（函数）是在浏览器完成的，也就是一定会把代码暴露给使用者，可以通过阅读加密算法，模拟过程，从而达到破解。
- 