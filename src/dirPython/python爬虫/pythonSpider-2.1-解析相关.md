# 解析
问题提出：虽然urllib可以根据含参数的ajax请求在一定程度上筛选出部分数据，但无法在参数的基础上进行更加细致的数据解析，爬取的数据往往还是眼花缭乱
解析：说白了就是查找筛选数据，解析方式有多种

xpath插件(lxml库)：
jsonpath
beautifulSoup(bs4)
re

## xpath
xpath要分别在浏览器下安装xpath扩展，代码框架下安装lxml库  
可以解析本地文件与服务器响应数据

### xpath基本语法
- 导入：`from lxml import etree`
- 引入解析源：
  - 本地文件：
    ```python
    tree = etree.parse('html.html')
    ```
  - 服务器响应数据
    ```python
    tree = etree.HTML(request)
    ```
- 解析：`tree.xpath(解析字符串)` 字符串由以下格式组成
1. 路径查询
   - //: 查找所有后代节点
   - /: 查找直接子节点
2. 谓词查询
   - `div[@id="123"]`：查找所有设置了id属性，且id属性参数为123的div标签
3. 属性查询
   - `@class`：查找设置了class属性的标签
4. 模糊查询
   - `div[contain(@id,"he")]`：查找包含id属性且包含字符"he"的div标签
5. 内容查询
   - `text()`：获取查找到的标签中的内容，
6. 逻辑运算
   - 解析字符串可包含and or not或| & !逻辑运算符
以下为使用解析字符串解析的例子
```python
tree = etree.HTML(request)
tree.xpath('//body/div[@class="boxes"]/main[starts-with(@id,"12")]/text() | //body/div[@id="12"]/section[contain(@id,"123")]')
```
上例可以解析出：  
body下class属性为boxes的div标签中id属性和"12"字符开头的main标签的内容  
或者body下id属性为12的div标签中包含id属性与"123"字符的section标签  

## jsonpath
问题提出：xpath主要解析的是网页代码，而很多时候都需要针对一串获取到的json数据进行解析
jsonpath: 专注于解析json数据，不过只能解析已经爬取下载到了本地的json文件

## BeautifulSoup

