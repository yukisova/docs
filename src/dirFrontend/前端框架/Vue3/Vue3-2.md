---
title: Vue-模版语法基础
---

Vue整个框架都使用模版语法来区分各种实例元素。
目的：将DOM以与渲染模版的形式与HTML内的实例标签/元素进行绑定与使用。


### 文本插值
形式：`{{}}`  
目的：绑定组件实例中包装对象的参数，可在Html节点内任意使用，将数据解释为纯文本  
特性：会自动指定ref()所定义的包装对象的value属性
```html
<!-- msg.value == 12 -->
<p>Message: { { msg } }</p>

<!-- 最终显示： Message:12 -->
```
### 插入HTML语法
形式：指令`v-html=`
目的：文本插值的基础上在节点内插入HTML语句
缺陷：Vue不是基于字符串的模板引擎，还是要使用组件作为重用和组合基本单元
隐患：动态渲染任意HTML很危险，容易出现xss漏洞
```html
<!-- rawHtml.value == "<span>abc</span>" -->
<p>Using v-html directive: <span v-html="rawHtml"></span></p>

<!-- 最终：Using v-html directive: abc -->
```
### 属性绑定
形式：
- 单值：指令`v-bind:` 简写`:`
- 多值：指令`v-bind`
目的：将标签的特定属性与组件的包装属性保持一致  
```html
<div v-bind:id="dynamicId"></div>
```
特性：
- 同名简写：如果两个属性名称相同，可以简写为一个属性名称
- 布尔属性：布尔属性值为真时才会渲染，假时直接忽略
- 多值绑定：包装对象中包含多个属性时，可以一口气绑定到单个元素上
  ```ts
    //
    const objectOfAttrs = {
    id: 'container',
    class: 'wrapper',
    style: 'background-color:green'
    }
  ```
  ```html
     <div v-bind="objectOfAttrs"></div>
  ```

## JS表达式
Vue在所有的数据绑定中都支持完整的JS表达式

## 指令
即带有`v-`前缀的特殊属性，可包含参数与值
### 参数
某些指令要一个参数，用冒号`:`进行标识
```html
<a v-bind:href="url"> ... </a>
```
以上：指令为v-bind, 参数为href，绑定属性为url
  
### 动态参数
指令的值可以进行绑定，参数也可以进行绑定，用`[]`括起
```html
<a :[attributeName]="url"> ... </a>
```
以上：参数以属性attributeName的值来确定
- 约束：绑定属性名时对应的包装对象值得是字符串，进行拼接等表达式操作时不能有空格

### 修饰符
在参数后以`.`开头的特殊后缀，表明指令需要以特殊的方式进行绑定
```html
<form @submit.prevent="onSubmit">...</form>
```