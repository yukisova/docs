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
  - **spiders** ：在其中定义爬虫文件，构成一个spider包
    - 定义爬虫文件方式：`scrapy genspider 文件名 爬取网页`
    > `scrapy gensipider baidu http://www.baidu.com` 构建
  - *items*
  - *middlewares*
  - *pipelines*
  - *settings*

运行爬虫代码：`scrapy crawl 爬虫名`