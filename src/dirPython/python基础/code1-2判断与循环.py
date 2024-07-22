"""
if 要判断的条件:
    条件成立语句
elif 要判断的条件:
    条件2成立语句
else:
    所有条件不成立语句
# 注意要缩进，嵌套的话以缩进为判断基础
"""
a = int(input("请输入"))
if a==2:
    print(a)
elif a==3:
    print(a)
else:
    print("error")

"""
match 要判断的对象:
    case 匹配值1:
        语句
    ...
    case _ :
        默认匹配语句（_为通配符，若没有匹配值就执行此语句）
"""

"""
while 条件:
    条件满足语句
"""
while a<3:
    print(a)
    a+=1

name = "Kabby"
"""
for 临时变量 in 数据容器:
    循环语句
# for循环跟别的编程语言不一样，只能够进行遍历
"""
for i in name:
    print(i)
# break和continue关键字在py中仍然有效


# 获取数字序列
# range(num)    获取从0开始到num结束（不含num）
for i in range(5):
    print(i)
# range(num1,num2)  获取从num1到num2（不含num2）
# range(num1,num2,step)     获取从num1到num2，步长为step(默认为1) (同样不包含num2)

# 循环变量作用域
# for中的临时变量不应该在for外使用
