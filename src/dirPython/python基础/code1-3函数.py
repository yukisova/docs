# python有内置函数，
len("ith")

# 此处说的是自定义函数
"""
def 函数名(形参):
    函数说明文档（一般采用多行注释，使用特定格式来让鼠标悬停时显示信息）
    函数体
    return 返回值

# 函数区分了局部变量和全局变量
"""
def Student(x,y):
    """
    Student函数大体功能
    :param x:   形参x功能
    :return:    返回值含义
    """
    # 在函数内定义全局变量：global关键字先声明变量，再给变量赋值
    global then
    then = "这是函数内定义的全局变量"

# 无返回值函数返回None 等同于false 也可用于暂时不给变量赋初值办法

