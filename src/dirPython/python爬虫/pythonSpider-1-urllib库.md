# urllib
前提：爬虫的基础功能就是爬取，urllib就是python自带的爬虫库，用来模拟浏览器访问url并获取响应信息

## 基本使用

- 获取某个网页的源码
- 0. 导入依赖
```python
import urllib.request
```
- 1. 定义一个url字符串 
```python
url = 'http://www.baidu.com'
```
- 2. 模拟浏览器向服务器发送网页请求
```python
response = urllib.request.urlopen(url或者request对象)
```
- 3. 获取服务器响应的页面源码
- 4. 将源码二进制数转换为可读的字符串——解码
```python
content = response.read().decode('utf-8')
```

### 基本类型
HTTPResponse 服务器请求响应数据

### 对应的基本方法
- read(读取字节数)
- readline(读取行数)
- readlines()
以上与文件读取相同
- getcode() 返回状态码 200才是正常
- geturl()  返回url地址
- getheaders()  返回响应头（状态信息）

### 爬虫下载
爬虫所能下载的：网页，图片，视频（所有对应网页引用到的静态资源与媒体资源），网页数据要利用ajax和文件操作
```python
# 下载
urllib.request.urlretrieve(url=url,filename='baidu.html')
```
上例将变量url指定的路径对应的下载到当前目录，名为'baidu.html' 如果要下载图片或者别的媒体文件的话要确保正确定位到页面元素所链接的地址。并将后缀名改为对应格式

## urllib：请求对象的定制 防止UA反爬
url组成当中的协议对应了不同的端口号（计网知识点）
1. http 80
2. https 443
3. mysql 3306
4. oracle 1521
5. redis 6379
6. mongodb 27017  

UA用户代理机制让服务器可以识别客户使用的操作系统与版本、CPU类型、浏览器与版本等等细致信息  
若爬虫程序没有确定好这些信息，就无法逃过UA的法眼，当UA不能识别出客户端的指定信息时，便会进行反爬
反爬机制会导致爬虫无法爬到指定的部分或爬到的部分不完整
  
应对策略：随便用浏览器访问一个网页，在开发者工具中的Network-> Headers中找到字段User-Agent，记录对应的UA值，写在要伪装成响应头的Json字典对象中
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15'
}
```
问题提出: 虽然可以记录到UA值，但是urlopen方法中不可以存储字典。只能传字符串和响应对象
问题解决：进行请求对象定制，在请求相应之前就设定好响应对象的特定值
```python
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)
# ...
```
上例中，在模拟浏览器之前指定了

## urllib: get方式-转码
get方式用于单纯地通过查询字符串方式返回指定的数据，并且不会进行验证或者筛选
问题提出：url默认使用ascii格式进行编解码，而在爬取时所需的url很多事需要有包含中文字符的查询字符串，为了能够顺利读取查询字符串中的数据，要专门修改读取url的方式
1. 导入依赖
```python
import urllib.parse
```
1. 使用编码方法quito将对应字符转编为万国码，万国码可以被url识别出来
```python
# 期望url='https://www.baidu.com/s?wd=周杰伦'
url_pre = 'https://www.baidu.com/s?wd='
data_name = urllib.parse.quito('周杰伦')
url = url_pre+data_name
```
2. 当查询字符串包含多个参数时，quote方法非常不方便，可以通过urlencode传入一个json字典，一次性编码一整串查询字符串
```python
data_origin = {
    'wd':'周杰伦',
    'sex':'男'
}
data = urllib.parse.urlencode(data_origin)
```

## urllib: post方式-编码
post方式主要用于爬虫程序模拟浏览器传输数据并获取服务器指定的响应结果  
有一个交互的过程。
网页开发者工具——Network会记录实际网页的数据传输，基于Network记录来确定网页中实现一个功能真正起作用的节点与真正有用的数据是哪个。
交互后，用户在指定起作用的节点的Preview中可以看到服务器的有效的响应信息  
post请求参数不可显示在url字符串中，为此必须进行转码  
最后还要使用确保post参数为字节形式，使用`encode()`方法进行编码，并放在请求对象定制方法中（Request方法中的data参数）
最后读出的响应信息也会是字节形式，要进行转码转为json字符串才能获取到可用的信息
```python
data = urllib.parse.urlencode(data_pre).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers)

# content为最终读取
import json
obj = json.loads(content)
```

## urllib: 请求对象关键参数定制 Cookie反爬
网页针对一个重要的功能，会要求客户端传递post详细且关键的的data参数，与完整有效的Cookie请求头参数(json字典)，否则网页会以数据不全或数据验证错误来进行反爬验证（相关数据参考）  

## urllib: ajax-get/post
目的：ajax用于让服务器返回指定的数据，即让爬虫程序通过发出请求的方式爬取网站返回响应的数据。
爬虫程序模拟的环境对网站进行ajax请求，并对请求响应的数据进行get操作。  
> 误区：在浏览器中Network会记录下浏览器ajax请求所返回的响应数据，这些数据可以让爬虫爬取，但它们是**静态**的，本质上还是标准的get请求，没有使用ajax技术  
最重要的地方是分辨出ajax请求对应的接口，并根据接口的用处，设置定制请求对象  
分辨Network元素ajax请求：检查RequestHeaders中是否有X-Requested-With:XMLHttpRequest  
ajax的get请求，请求所需的参数都包含在查询字符串中，可以通过url拼接来搞定  
ajax的post请求，所需的参数一般都是通过表单来传递，对应的表单 数据在**载荷**选项卡  

这也是爬虫用的最广泛的一处，正式框架中，会将每个步骤都以函数方式封装，并允许用户以交互的形式指定一部分ajax请求，以下为示例：
```python
# 请求对象定制
def create_request(page):
    url_base = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&'

    data = {
        'start': (page - 1) * 20,
        'limit': '20'
    }
    data = urllib.parse.urlencode(data)

    base_url = url_base + data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36'
    }
    return urllib.request.Request(url=base_url, headers=headers)

# 爬取内容
def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')

# 进行下载
def download(data, page):
    filename = f"douban_{page}.md"
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(data)

# 主函数
if __name__ == '__main__':
    start_page = int(input('起始页码'))
    end_page = int(input('结束页码'))

    for page in range(start_page, end_page + 1):
        download(get_content(create_request(page)), page)
```

## urllib: 异常
导包：
```python
import urllib.error
```
urllib发送请求有可能会失败，为此需要通过捕获异常语句来让代码健壮：
相关的异常：
1. URLError
   异常原因集中于代码连接阶段，比如无网络、url值不存在、无法连接服务器这种
2. HTTPError
   是URLError的子类，会返回状态码和异常原因，异常原因主要集中于请求的阶段，因此不能被URLError代替  

## urllib: Cookie登录
问题提出：很多网页的数据都需要用户在登陆之后才能进行请求，即登录验证。不然即使输入正确的url，系统也会将浏览器重定向到登录页面  
体现在爬虫程序中就会出现编码错误(登录界面并没有进行编码)，即使避免了编码错误，也因为重定向而无法定位到对应网页，进而无法爬取到指定数据。  
方案：在Request请求头中加入携带了登录信息的cookie在数据采集时绕过登录，获取数据  
- referer: 判断当前url路径请求是否源于上一级url。例如请求url为www.a.com/f/a，该参数判断请求是否来自www.a.com/f，
  - 一般情况下做图片防盗链
- cookie：携带了用户相关信息的缓存数据，用于给网页提供用户账户的信息，在用户在浏览器通过登录验证后便可以利用cookie数据在爬虫程序中绕过登录阶段，破解cookie反爬
  - 但cookie信息仅用于破解60%的反爬，当遇到需要验证码的动态cookie时，要通过别的手段破解反爬（requests库）

## urllib: handler处理器
问题提出：urrlib.request.Request方法可以在一定程度上定制请求头解决cookie和UA反爬，但无法定制针对使用动态cookie和代理的反爬手段  
handler用处：基于已有的定制请求头，去扩展出更高级的请求头（重点在扩展，因此要先定制好请求）
- 可以结合代理服务器
重点方法（每一步都是连着的）：
- handler：有多种handler，根据要求初始化
- build_opener：基于初始化的handler，构建opener对象
- open：基于opener，将handler处理器扩展进已有的请求头
以下为实例，说明三个步骤顺序
```python
# 
handler = urllib.request.HTTPHandler()

opener = urllib.request.build_opener(handler)

request = opener.open(request)

response = request.read().decode('utf-8')
```

### urllib：handler：代理配置
问题提出：在验证失败或者反爬程序成功的情况下，服务器可能会将客户端的IP加入黑名单，让当前计算机自身的IP在短时间内无法再请求数据
代理：用别人的IP访问网站，在真实IP被网站反爬程序禁止访问的情况仍旧能够接入服务器
常用功能：
- 突破自身IP限制，访问国外站点
- 访问单位或团体的内部资源
- 提高访问速度
- 隐藏真实IP，防止攻击
  真实IP只用来访问代理服务器获取地址，真正的请求是由代理服务器来做的
配置方式：
1. 定制请求对象
2. 创建ProxyHandler处理器对象，并传入代理服务器的字典类型配置数据
   代理服务器信息自己找
3. 创建出opener对象
4. 使用opener.open函数发送请求
```python
request = urllib.request.Request(url, headers=headers)

proxies ={
    'http': '172.16.17.32:80',
}

handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

request = opener.open(request)
```

### urllib: handler: 代理池
问题：即使有了代理服务器，在短时间内多次重复访问同一url也不能排除代理服务器也被加入黑名单
方案：配置代理池，其中有一堆高密的代理IP，实际开发中按照特定规则(一般是随机)使用代理IP，最大程度降低同IP重复访问被Ban的风险
下例则为定义代理池与选择代理池的过程，重点只在于选择代理地址
```python
proxies_pool = [
    {'http': '172.16.17.32:80'},
    {'http': '172.16.12.22:88'}
]
proxies = random.choice(proxies_pool)
```