---
title: TS-类型注解
---
## 类型注解
类似python，为变量进行类型约束。此后系统便会进行严格的类型审查，会出现类型以如下格式进行添加
```ts
let count: number = 19
```
上例将变量`count`的类型注解为`number`类型

## 常用基础类型
TS的基础类型分为两类，即JS原生的与TS新增的类型
1. JS原生
   - 原始：数字 字符串 布尔 空 未定义 标志
   - 对象：object(函数，数组等等等)
2. TS新增
   - 联合类型
   - 自定义类型
   - 接口
   - 元祖
   - 字面量
   - 枚举
   - void
   - any

#### 针对函数的类型注解
函数类型分为参数与返回值的类型  
可单独指定每个参数类型，如下所示：  
```ts
function add(num: number, num2: number): number {函数体}
const add = (num: number, num2: number): number => {函数体}
```
也可同时指定参数与返回值类型，但只能用于函数表达式，如下所示：  
```ts
const add: (num1: number, num2: number) => number = (num1,num2) =>{函数体}
```
有点脱裤子放屁，了解就行。
> [!caution]
> TS中函数如果没有返回值，那么就设返回值为void，但要注意void!=null。
#### 函数参数可选
有些时候函数某些参数可以不用上，可传可不传，这些参数称为可选参数（类型注解为`?:`），但一定要放在形参列表最后，如下所示：  
```ts
function add(start: number, end?: number): void {函数体}
```

#### 针对对象类型的类型注解
- 针对数组类型有两种写法，分别为
```ts
let num: number[] = [1, 3, 5]
let num: Array<number> = [1, 3, 5]
```
- 针对普通对象类型，普通对象由属性和方法构成，在类型注解中要以花括号括起一个个注明，之间用分号分隔，如下所示
```ts
let person: {name: string; say(): void} = {
    对象内容
}
```
函数也是一种对象，因此对象类型也可以包含可选的属性或方法

## TS新增类型
- 联合类型
目的：指定变量的包含的值的多个类型
```ts
let abc: (number | string) = "123"
```
上例的abc变量既可以赋`number`变量也可以赋`string`变量

- 自定义类型
目的：为特定的类型其别名来简化使用，因此也称类型别名，可类比为`typeof`语句
```ts
type Custom = (number | boolean)

let a: Custom = true
```
上例将联合类型`(number | boolean)`起了个别名Custom，成功完成自定义  
跟接口相比，自定义类型本身可以对所有类型起别名，但不具备继承的特性

- 接口
目的：对象类型被多次使用时，需要达到复用的目的
```ts
interface IPerson {
    name: string
    age: number
}
```
当一行只用声明一个属性或方法的类型，可不加分号或逗号
声明接口后，可以直接使用接口名称作为变量的类型，某种意义上起到了跟自定义类型一样的作用。
::: danger
接口拥有可继承性
```ts
interface p2d {x: number; y: number}
interface p3d extends p2d {z: number}
```
在上例中，接口类型p3d继承了p2d的所有属性和方法，并在基础上增添了z属性
:::

- 元组类型
有些时候数组在记录数据方面并不严谨，因为在定义时数组是可以包含任意多个数据的。
目的：需要确切标记出元素个数，以及元素的类型  
```ts
let stu: [string, number] =["阿三", 114]
```
上例中元组类型确切地指定了只有两个元素，第一个元素为string类型第二个元素为number类型  

## 类型推论
TS中在==声明变量并初始化时==，或==决定函数返回值时==，可以省略类型注解，此时系统会根据类型转换机制自动推论变量的类型
并不会因此失去类型验证机制，可以用来偷懒