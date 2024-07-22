### <Component>
Vue适合制作SPA，例如选项卡，为了方便在单页中切换组件，会使用内置组件component来代表一组可以动态变化的组件。component对应的组件通过is属性确定，因为是动态组件，往往需要借助指令来设定动态参数
```html
<!-- curCom为变量名，代表对应的组件名，可通过其他事件来修改curCom，来实现切换组件的效果 -->
<component :is='curCom'></component>
```
注意，因为默认情况component组件下传给is的变量值不是响应式的，要将变量对应的值通过markRaw函数返回，或者在动态组件外用内置组件keepAlive包裹
### <Trasition>

### <TransitionGroup>

### <KeepAlive>

### <Teleport>
有些时候子组件需要在不改变父组件基础布局的情况下将自身某些部分的模版显示在父组件的某些部分下，teleport可以实现这一点，主要要借助to属性  
to属性指向父组件的选择器，因此使用时要注意编译时的顺序，要确保传送的位置先被系统读取到
```html
<!-- 子组件 -->
<teleport to='.main'>
    要传送到父组件特定部分的子组件元素
</teleport>

<!-- 父组件 -->
<div class='main'></div>
```
上例中，子组件内被teleport包装的元素被指定显示在父组件或祖父文件的class名为main的div标签下

### <Suspense>

## 非组件特殊元素
### <component>
### <slot>
### <template>

## 特殊属性
### key
### ref
### is