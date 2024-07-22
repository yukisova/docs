---
title: Vue-VCA方式
---

## Vue主要内容概括一下
- 模版语法
- 指令
  - 自定义指令
- 响应式对象
  - ref和reactive
- 函数
  - 
- 计算属性
  
- 钩子
  - 创建阶段
  - 挂载阶段
  - 更新阶段
  - 销毁阶段
- 监听器
  - 懒更新与普通监听
- 数据传递
  - 数据验证
  - 父传子子传父
  - 提供/注入
- 动画过渡
  - 过渡组
- 插槽
  - 具名插槽
  - 作用域插槽
- 组件
  - 动态组件
  - 异步组件
- VueRouter
- Pinia
- ElementPlus
- Vant

## 创建应用
创建vue最低的运行条件，需要有根组件和配置文件两个文件
```ts
// main.ts
import { createApp } from 'vue'
import App from './App.vue'

const app = create({
   // 根组件设置项，用来确认谁是根组件，一般来讲默认根组件名为App.vue，除此之外也可以直接使用voa写法定义
   data(){
      return{
         // 因为根组件的模版通常作为组件本身的一部分，在这里使用voa更加合适
      }
   }
})
// 只有在调用挂载方法后应用才能够被渲染。
app.mount('#app')
```
app在挂载之前，还可以使用如下进行系统方面的配置与扩展
`app.config`更加细致的配置  
`app.component`全局下注册组件  
``  