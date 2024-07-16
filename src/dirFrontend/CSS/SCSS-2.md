---
title: Sass新增样式规则
---
## 选择器嵌套
嵌套规则允许sass简化重复选择器定义的同时，呈现出清晰的层次结构
### 针对选择器列表
选择器列表之间嵌套，最后呈现出的效果就是列表之间分别嵌套

### 针对选择器组合符
选择器组合符之间的嵌套，可以将组合符单独作为嵌套的元素，只要确保最后能够组成一个双目就行

### 插值选择器
`@include`关键字可以让选择器结合mixin、变量等玩意定义一个指定值的选择器

## 高级嵌套

## 属性声明
在Sass中，与CSS一样，属性声明定义了与选择器匹配的元素如何被样式化。  
但Sass增加了额外的特性，使编写和自动化变得更容易。首先，声明的值可以是任何SassScript表达式，这些表达式将被计算并包含在结果中。

### 插值
属性的名称可以由插值`#{}`组成
```scss
@mixin prefix($property, $value, $prefixes) {
  @each $prefix in $prefixes {
    -#{$prefix}-#{$property}: $value;
  }
  #{$property}: $value;
}

.gray {
  @include prefix(filter, grayscale(50%), moz webkit);
}
```

### 嵌套思想
许多CSS属性都以相同的前缀开始，这个前缀作为一种命名空间。例如，font-family、font-size和font-weight都以font-开头。因此Sass通过允许属性声明嵌套来使这一过程更加简单且减少冗余。外部属性名称被添加到内部，之间用连字符分隔。
而部分属性拥有简写的方式，若要包含简写形式，要用如下写法：  
```scss
.info-page {
  margin: auto {
    bottom: 10px;
    top: 2px;
  }
}
```
### 根据情况声明样式
有时候，事后只想在某些时候显示属性声明。如果声明的值为null或未加引号的空字符串，Sass根本不会将该声明编译成CSS。
```scss
$rounded-corners: false;

.button {
  border: 1px solid black;
  border-radius: if($rounded-corners, 5px, null);
}
```

### CSS自定义属性
CSS自定义属性，也被称为CSS变量，它们允许在其声明值中使用几乎所有的文本。CSS变量可以由JavaScript访问，因此任何值都可能对用户有潜在的相关性。甚至包括通常会被解析为SassScript的值。
因此，Sass对自定义属性声明的解析与其他属性声明的解析方式不同。所有标记（包括那些看起来像SassScript的标记）都会原封不动地传递给CSS（视为静态值）。只能由插值方式传递动态值。  
但插值方式一般情况下会去除引号，因此为了传递字符串，需要使用`meta.inspect()`函数

## 父选择器
`&`是Sass发明的一种特殊选择器，专门用于选择器嵌套，用来引用父类选择器。它能够更加方便地添加伪类或在外部选择器名字基础上添加选择器。  
因为容易被类型选择器替换，因此只允许在复合选择器之前使用

### 引用父类选择器
```scss
.alert {
  // The parent selector can be used to add pseudo-classes to the outer
  // selector.
  &:hover {
    font-weight: bold;
  }

  // It can also be used to style the outer selector in a certain context, such
  // as a body set to use a right-to-left language.
  [dir=rtl] & {
    margin-left: 0;
    margin-right: 10px;
  }

  // You can even use it as an argument to pseudo-class selectors.
  :not(&) {
    opacity: 0.8;
  }
}
```

### 在外部选择器名称基础上添加选择器
可以使用父选择器为外部选择器添加额外的后缀。这在使用像BEM这样的高度结构化类名的方法论时特别有用。只要外部选择器以字母数字名称结尾（如类选择器、ID选择器和元素选择器），你就可以使用父选择器来附加额外的文本。
```scss
.accordion {
  max-width: 600px;
  margin: 4rem auto;
  width: 90%;
  font-family: "Raleway", sans-serif;
  background: #f4f4f4;

  &__copy {
    display: none;
    padding: 1rem 1.5rem 2rem 1.5rem;
    color: gray;
    line-height: 1.6;
    font-size: 14px;
    font-weight: 500;

    &--open {
      display: block;
    }
  }
}
```

### SassScript中的父选择器
父选择器也可以在SassScript中使用。它是一个特殊的表达式，返回当前父选择器，其格式与选择器函数使用的格式相同：一个逗号分隔的列表（选择器列表），其中包含空格分隔的列表（复合选择器），这些复合选择器又包含未加引号的字符串（复合选择器）。  
如果&表达式在任何样式规则之外使用，它将返回null。这意味着你可以很容易地使用它来确定一个mixin是在样式规则中被调用，还是没有被调用。  
既然&可以用作普通的SassScript表达式，这意味着它可以将父选择器名传递给函数，或在插值中包含它——甚至在其他选择器中！将它与选择器函数和@at-root规则结合使用，可以以非常强大的方式嵌套选择器。  
例如，假设你想编写一个选择器，该选择器匹配外部选择器和元素选择器。你可以编写一个像这样的混入（mixin），它使用selector.unify()函数将&与用户的选择器结合起来。  

## 占位符选择器
Sass有一种特殊的选择器，称为“占位符选择器”。它的外观和行为与类选择器非常相似，但它以%开头，并且其内容不会包含在CSS输出中。实际上，任何包含占位符选择器的复杂选择器（即逗号分隔的选择器）都不会包含在编译后的CSS中
它出现的目的，就是为了方便开发者使用@extend关键字没有后顾之忧地对其他选择器进行扩展。  
个人理解，占位符选择器可以看成一团被封装起来的样式，可以像插值对于变量一样，扩展原本的选择器内容
