# 常用API

## Math-进行数学相关运算

## System-与系统相关的方法
- `.exit(返回退出值)`：退出JVM，并显示针对对应的情况的特定值（0：正常停止 非零：异常停止）
- `.currentTimeMillis()`：返回系统时间（毫秒形式）

## Runtime-当前JVM运行环境相关方法
要调用Runtime中`getRuntime()`方法才能获得当前系统的运行环境对象

## Object-Java顶级父类，所有对象的直接间接父类
作为万物皆对象的java，Object类中方法可以被所有的子类所访问

## 超长包装类-BigInteger和BigDecimal

## 正则表达式-字符串中的方法
`.matches(正则表达式字符串)`：针对字符串进行正则匹配，返回布尔值 
`.replaceAll(正则表达式字符串,替换字符串)`：将匹配成功的部分替换成其他字符串

### Pattern类-表示正则表达式
`Pattern.compile(正则表达式字符串)`：返回Pattern对象
### Matcher类-文本匹配器
用处：按照正则匹配的规则去读取字符串，
`Pattern对象.matcher(要读取的字符串)`：返回Matcher对象

`Matcher对象.find()`：正式在字符串中查找匹配子串，找到时返回布尔值，并在Matcher属性中记录位置（底层遍历类似迭代器，可以像next()一样反复查询）
`Matcher对象.group()`：根据find()记录的位置，返回截取到的匹配子串


## 包装类
为了对应java概念中万物皆对象的思想，针对每个基本数据类型都有对应的引用类型——对象

## Lambda表达式
可以理解为匿名函数，基于函数式编程思想，而不是面向对象  
函数式编程：不再强调是谁去做，而是强调要做的事本身  
- Lambda表达式只对应函数式接口，即**有且只有一个抽象方法的接口**，建议为其添加`@FunctionalInterface`注解