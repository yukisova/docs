---
title: ES实操心得2024.7.16
---

## Element元素
.classList对象包含对应的html元素对应的class列表，可通过修改classList的值来修改对应的样式
- .add("c1","c2") 
  在class列表中添加c1与c2两个类
- .contains("c1")
  检查元素是否绑定了c1类，返回布尔值
- .item(1)
  返回class列表中指定索引的类名
- .remove("c1","c2")
  尝试删除class列表中的类c1和c2
- .toggle("c1")
  若c1存在，则删除c1，若不存在，则添加c1，类似开关

## css-变形
- translate     位移
- scale         缩放
- rotate        旋转
- perspective   透视
- skew          倾斜
- matrix        变换矩阵

## document方法
.querySelector方法，可以在基于css选择器语法的情况下选中指定的元素，并根据情况返回元素列表或单个元素

#