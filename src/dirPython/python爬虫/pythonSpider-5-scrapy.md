# Scrapy

## 概述
结构性数据：爬取到的数据以多组相同结构的部分组成，具有清晰的结构性（购物网站的商品列表）
概述：
- 爬取数据的同时可以提取结构性数据的应用框架，相比非框架爬虫程序，代码编写更加方便更加快速
- 可以理解为专门用于爬虫业务的业务框架 vitejs之于前端 django之于pythonweb

## 基本使用
创建scrapy爬虫框架：`scrapy startproject 项目名称`
框架目录(例爬虫框架名称为scrapy)
- **scrapy**
  - **spiders** ：在其中自定义爬虫文件，构成一个spider包
    - 定义爬虫文件方式：`scrapy genspider 文件名 爬取网页`
    > `scrapy gensipider baidu http://www.baidu.com` 构建
  - *items*：定义数据结构，即定义爬取的数据类型
  - *middlewares* 中间件：进行代理
  - *pipelines*：管道 用于处理下载数据
  - *settings*：配置文件 设置标头，开关robots协议

运行爬虫代码：`scrapy crawl 爬虫名`

## 爬虫文件统一格式
```python
import scrapy

# 爬虫类统一命名
class BaiduSpider(scrapy.Spider):
    # 运行爬虫时所使用的爬虫名
    name = "baidu"
    # 允许访问的域名
    allowed_domains = ["www.baidu.com"]
    # 最先访问的完整域名 
    start_urls = ["http://www.baidu.com"]

    def parse(self, response):
        # 在这里写爬取代码
    # 在执行了start_urls后执行的方法
    # response 可以类比为 urllib.request.urlopen() ，即响应对象
    # 在遵守反爬虫协议的情况下，该函数无法执行，
```

## 爬取方法（在parse函数中）以下只是很小的一部分
scrapy作为爬虫框架，为了完整一套完整的爬虫流程，有自己的解析方法，集成了xpath
- `response.text` 字符串形式返回响应的字符串
- `response.body` 二进制形式返回响应的字符串(html形式)
因为xpath的集成，源码不再重要，并不推荐使用css选择器方式
- `response.xpath('解析字符串')` 返回xpath解析字符串匹配的元素（常用）
  - response.extract() 提取selector对象的data属性值
  - response.extract_first() 提取selector列表的第一个数据

## 架构组成(要加入一个图，之后在搞)
scrapy框架主要由以下部分组成
- 引擎： 组织所有的请求对象
- 下载器：
- 爬虫类
- 调度器
- 管道

## scrapyshell
目的：在未启动spider的情况下调试爬取代码  
用于测试xpath和css表达式，查看工作方式以及爬取的网页中提取的数据  
推荐先安装ipython
语法：`scrapy shell 访问url`
在scrapy shell中可以直接使用类似shell的指令模式，输入爬取方法，实现类似交互的效果

## 实例1. 懒加载反爬
懒加载反爬现象体现为未加载完成的数据大片判null  

原因：网站结构化数据因为懒加载的原因，在暂时没浏览到的时候填在src中的数据没有意义，真正的路径存储在data_original属性中，系统在监听到滚轮滚到对应位置时才会对懒加载数据进行加载  
对应的，第一张图片往往不用设置data-original属性，因此在爬取时要进行一定的判断  
以下为案例：  
```python
def parse(self, response, **kwarg):
    # selector对象可以再次调用xpath方法，基于此，可以对最终的循环进行代码优化
    li_list = response.xpath('//ul[@id="component_59"]/li')
    for li in li_list:
        src = li.xpath('.//img/@data-original').extract_first()
        if src:
            src = src
        else:
            src = li.xpath('.//img/@src').extract_first()

        name = li.xpath('.//img/@alt')
        price = li.xpath('.//p[@class="price"]/span[1]/text()')
        print(src, name, price)
```

## 实例2. 爬虫程序与items、pipeline文件
### items相关
在爬虫框架中，保存爬取内容会使用管道pipeline，而管道pipeline针对数据往往还要进行类型判断（可能要与数据库对接），因此针对爬取内容解析后的有用数据要用items文件中定义的数据结构进行包装  
下例为items文件中定义的解析后的数据的包装类
```python
# items文件
class SpiderPythonItem(scrapy.Item):
    # 图片
    src = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()

# 示例一parse函数内
    book = SpiderpythonItem(src=src, name=name, price=price)
    yield book
```
上例.items中的类里，使用Field方法开辟一个字段（类比Django中的Model Field） 
yield关键字，可以理解为迭代return：return一个值，并记录返回的位置，下一次迭代就从该位置下一行开始 
parse函数值是返回给管道pipeline的，管道功能要实现在settings文件夹内开启
```python
# settings文件
# 对应pipelines文件夹中的管道类，数字为优先级，值越小优先级越高。可以类比为注册
ITEM_PIPELINES = {
   "Spider_python.pipelines.SpiderPythonPipeline": 300,
}
```
### pipelines相关 - 管道类的使用
管道用于保存爬取后解析的内容，保存在数据库中或者保存在数据表中，或者以其他文件形式保存在某一个路径当中。  
pipeline类默认只会定义一个process_item方法，用于接收在爬虫程序parse函数里返回的数据。但因为一个管道可能对应多个爬虫程序与多个数据结构，同时爬虫程序在运行时会分多次将数据传递进入管道，因为一个对象都要经历打开-关闭文件的操作，另外还要定义open_spider方法和close_spider方法，类比为钩子函数，对应开启爬虫与关闭爬虫的时候执行的语句  
以下为优化的pipeline类
```python
class SpiderPythonPipeline:
    fp = None

    def open_spider(self, spider):
        self.fp = open('book.json','a',encoding='utf-8')
        
    # 函数内的item形参对应在parse函数中通过yield返回的解析数据(本例中为book)
    def process_item(self, item, spider):
        # item形参对应的book解析数据由多个
        self.fp.write(str(item))

        return item

    def close_spider(self, spider):
        self.fp.flush()
        self.fp.close()
```

### pipelines相关 - 多条管道同时处理业务
可以使用多条管道，针对爬取到的数据实现不同的业务（例如一边下载文件，一边下载图片）  
关键在于管道的注册  
步骤：
1. 定义新的管道类
2. 将管道类加入到settings文件中的ITEM_PIPELINES中

### pipelines相关 - 多页数据同时请求同时爬取
当想要一次性将一个网页的多页数据全部爬取时，可以针对将要执行的页再次调用parse方法，url要根据不同页的规律来总结出拼接方式  
关键在于yield关键字的自我迭代特性，与重新调用parse函数的方式
yield关键字相当于迭代return：通俗点讲就是return之后，下一次执行函数的时候从yield下第一个语句开始，不再从函数体开头开始  
以下语句为实例2parse函数部分后段添加  
```python
if self.page < 100:
    self.page = self.page + 1
    url = self.base_url + str(self.page) + '-cp01.04.03.00.00.00.html'

    yield scrapy.Request(url=url, callback=self.parse)
```
为了对其他网站进行爬取，爬虫程序要包装另一个请求对象，第一次请求对象是由框架自动创建的，但之后的请求对象都要让用户来创建。为了将请求对象切实记录进parse函数，parse函数要在请求对象得到相应时调用，因此作为callback参数的值。  
另外，为了保证多页下载正常进行，allowed_domains变量必须只写域名的形式  

## 链接提取器 CrawlSpider
CrawSpider是继承自scrapy.Spider的一个功能
目的：可以直接自定义规则，在解析html内容的时候，根据自定义的规则提取出指定的链接，再向链接发送请求；在需要爬取多重链接时非常好用（例如爬取网页之后提取其中链接再此爬取新的网页，或者爬取未显示全部页跳转按钮的数据）  
下例概括了使用链接提取器的方式
```python
# 开头导入
import scrapy.linkExtractor from LinkExtractor

# 在parse函数中定义链接提取器类，有多种形参，使用时只需要使用一种就行
link = LinkExtractor(
    # allow=r'正则表达式',
    # deny=r'~',
    # allow_domains=r'允许的域名',
    # deny_domains=r'~',
    # restrict_xpaths=r'解析字符串',
    # restrict_css=r'css选择器',
    # restrict_text=r'文本内容',
)

# 在需要使用自定义的规则解析相应数据时使用链接提取器类的extract_link方法
link.extract_links(response)
```