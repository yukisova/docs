# 函数可以通过逗号分隔返回多个返回值(相当于返回一个元组)
# 因此接收时也要用多个变量进行接收才能接收到所有值
def function_1():
    return 1,2
x,y = function_1()  # x==1 ,y==2

# 函数传参方式
def function_2(m,n,o):
    print(f'{m},{n},{o}')
# 缺省参数：函数形参内定义，当没有传递对应参数时，形参默认为该值
def function_3(a,b=0):
    print(f'{a},{b}')

# 位置参数：根据函数定义形参位置传递参数（最常见）
function_2(1,2,3)
# 关键字参数：在调用时通过键值对方式传递（可以不考虑顺序）
function_2(n=3,m=2,o=5)
# 两者若混合使用，位置参数必须在关键字参数前。

# 不定长参数:不确定会传多少个参数
# 位置传递*
# 所有参数会被args收集，并合并成一个元组，使用时索引使用
def function_4(*args):
    print(args)
# 关键字传递*
# 参数需要是键值对，所有参数被kargs收集，并合并为字典
def function_4_1(**kargs):
    print(kargs)

# 函数传递（不传递返回值，直接传递本身，也可说是传递代码的执行逻辑）
def func_1(x,y):    # 被作为参数的函数，实际中一般是传递匿名函数
    return x+y

def function_5(func):
    func(1,2)
function_5(func_1)

# 匿名函数
"""
def关键字定义有名称的函数（可重复使用）
lambda关键字定义匿名函数（临时使用一次）

匿名函数定义语法
lambda 参数: 函数体（只有一行代码且会直接返回值） 
"""

function_5(lambda x,y : x+y)