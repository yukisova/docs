# Selenium

## 概述
问题提出：先前的爬虫库都是通过模拟浏览器的方式对网站服务器进行请求，模拟浏览器所访问到的网站往往会缺失很多很多页面数据，并且也更容易遭到反爬
概念：
- 直接运行在浏览器中，规避掉了绝大部分因为数据的缺失而遭到的反爬
- 支持通过各种驱动来在真实的浏览器内核中完成测试，以完整的浏览器环境访问网页，能避免数据的缺失

## 基础操作
基础操作
- 下载对应版本的浏览器驱动
- 导入：
  - `from selenium import webdriver`
  - `from selenium.webdriver.chrome.service import Service`
- 创建浏览器操作对象
- 访问网址
```python
# 指定浏览器驱动路径
path = Service(executable_path="chromedriver.exe")

# 创建浏览器操作对象（相当于打开浏览器）
browser = webdriver.Chrome(service=path)

url = 'https://www.jd.com/'

# 浏览器获取到url并跳转
browser.get(url)

# 浏览器获取到url所跳转到的页面的全部内容，不进行元素定位
content = browser.page_source
```
可以将webdriver类比为宏，或者类比为pymysql，起到的作用就是操作实际存在的应用，不再进行模拟  
可以爬取到实际使用浏览器所访问的网页全部内容  

## 元素定位
问题拓展：selenium起到的作用还有自动化，即模拟鼠标和键盘来操作浏览器中的元素。而操作元素的前提就是定位元素，可以类比为pymysql中的光标
导入：`from selenium.webdriver.common.by import By` 导入By中的定位对象，与定位方法配合使用
定位方法：
- `.find_element(定位对象,"对应参数")` element+s后缀的话会将所有符合定位条件的对象以列表形式定位
定位方案: 
  - id属性：By.ID
  - class属性：By.CLASS_NAME
  - name属性：By.NAME
  - xpath-解析字符串：By.XPATH
  - css选择器:By.CSS_SELECTOR
  - 文本完全匹配: By.LINK_TEXT
  - 文本模糊匹配: By.PARTIAL_LINK_TEXT
  - 标签匹配：By.TAG_NAME
```python
# 
content = browser.find_element(By.XPATH, '//*[@id="content"]')
```

## 元素操作
### 访问
问题拓展：在成功定位到元素的时候，可以进行两种操作，即访问和交互  
访问方法：
  - `.get_attribute('属性名')` 获取元素指定属性值
  - `.text` 获取元素文本
  - `.tag_name` 获取元素标签名

### 交互
交互方法：
  -  `click()` 左键点击
  -  `send_keys('123')` 在对应元素文本框中输入123
  -  `forward() back()` 前进和后退
  -  `execute_script('代码')` 执行js代码，执行类似滑动滚轮之类的操作
  -  `page_source`  返回整个网页代码
  -  `current_url`  返回当前url
  -  `context_click()` 右键点击
  -  `move_to_element()` 鼠标悬停
  -  `drag_and_drop()` 拖拽
  -  `set_page_load_timeout(10)` 设置超时等待时间
  -  `close() quit()` 关闭网页和退出浏览器会话
  -  `WebDriverWait(browser, 10).until(条件)` 在10秒内等待指定条件达成
  -  `.implicitly_wait(10)` 隐式等待10秒
  -  `.save_screenshot('保存文件名')` 保存浏览器的快照界面，用于在无界面环境中查看浏览器的状态
## 无界面浏览器
问题提出：原生selenium下因为真的要加载一个完整的浏览器并渲染出网页中全部的数据，会导致很多无用的css与gui占用大量的渲染空间
Chrome handless：
  - 针对chrome环境的无界面浏览器，不会加载css样式和gui界面，支持元素元素查找和js执行，运行效率必原生selenium快很多
  - 交互方面的代码量更少，
导入：`from selenium.webdriver.chrome.options import Options`  
以下为handless固定加载方式，因为格式很标准，可以直接用函数包装
```python
def share_browser():
    chrome = Options()
    chrome.add_argument('--headless')
    chrome.add_argument('--disable-gpu')
    
    path = "电脑本身的chrome浏览器程序所在路径"
    browser = webdriver.Chrome(chrome_options=chrome)
    return browser
```

