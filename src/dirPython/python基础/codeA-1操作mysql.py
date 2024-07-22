# 通过pymysql第三方库，可以进行mysql数据库的操作
from pymysql import *
# 获取到Mysql数据库的链接
conn = Connection(
    host='localhost',   # 域名（Ip地址）
    port=3306,          # 端口，默认3306
    user='root',        # 账户名
    passwd='123456',    # 密码
    autocommit=True     # 设置自动提交（不设置的话修改数据库必须要执行commit之后才能成功）
)

# 打印mysql数据库的软件信息
# print(conn.get_host_info())

# 操作部分
"""
n-1. 获取游标对象 .cursor()
    必须要获取游标对象才能够对数据库进行定位操作（把这个想象成光标，要赋给某个变量）
n-2. 选择数据库     链接对象.select_db(数据库名)
    必须要先选择所需要操作的数据库，才能进行查询操作
n-3. 执行sql语句    游标对象.execute(sql语句)
    语句为字符串，可以不以分号结尾
n-4. 提交数据更改   链接对象.commit()
    当链接对象中没有设置自动提交时，每次修改数据必须要使用commit来提交才能正常修改sql数据库
n-5. 获取查询结果   游标对象.fetchall()
    返回元组类型（嵌套）
"""

# 关闭与数据库的连接（没有这个语句的话系统会链接会被一直占用——必须要有）
conn.close()    