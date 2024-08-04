# 集合-遍历

## 单列集合遍历
在集合中，只有有序的集合才能够进行普通for遍历，为了泛用性，还是推荐其他三种遍历的方式
- 迭代器遍历：在遍历的时候如果需要删除或者添加元素，只能使用迭代器进行遍历
- 增强for和Lambda遍历：只需要遍历的时候用这两种遍历方式更加方便

### 迭代器遍历
概念：迭代即为将原本集合中的内容进行一定的处理再以返回值的形式返回给指定的集合变量。  
迭代遍历即为利用迭代器Iterator类，将集合中每一个元素依次迭代返回，实现遍历效果。 
Iterator类特点：
- 不依赖索引
- 是单列集合的内部类

常用方法：
- `.hasNext()`：判断当前位置是否有元素，返回布尔值
- `.next()`：返回当前位置元素，并将迭代器对象移至下一位置
```java
Iterator<String> it = list.iterator();
while(it.hasNext()){
    String str = it.next();
    System.out.println(str);
}
```
注意点：
- 当尝试在迭代器遍历完毕后强行使用next方法时，会报错`NoSuchElementException`
- 当迭代器遍历完毕，指针是不会复位的
- 在使用迭代器操作集合的时候，不能对集合对象进行增加和删除，只能使用迭代器对象对集合进行相关操作

### 增强for遍历
目的：简化迭代器代码的书写，所谓的增强for内部原理就是迭代器。只有数组和单列集合才能使用增强for  
格式：
```java
for(String a:list){
    // 每一次迭代，a都会接收对应集合或数组的元素，类比为其他语言中的for..of..
}
```
注意点：
- 修改接收变量，并不会改变集合中原本的数据。

### Lambda遍历(集合的forEach方法)
目的：进一步简化增强for，Lambda本身可以看成是箭头函数（py里说的很明白，就是匿名函数）
```java
list.forEach(new Consumer<String>(){
    // forEach中支持传入的是实现了Consumer接口的类对象，一般以内部类的形式呈现，并由此定义其中的方法accept，因为函数式接口只有一种方法，可以简写为箭头函数
    @Override
    public void accept(String s){
        // s对应函数中的每一个数据
        System.out.println(s);
    }
})
// 以下为简写形式
list.forEach(s -> System.out.println(s))
```

## 双列集合
因为双列集合是由键值对组成的，遍历分为以下三种
- 键找值
- 键值对
- Lambda表达式

### 键找值
即先获取集合中所有的键，然后利用get方法依次找值
```java
Set<String> keys = map.keySet();
keys.forEach(key -> {
    String value = map.get(key);
    System.out.println(value);
})
```

### 键值对
即先获取集合中所有的Entry对象，然后遍历返回每个键值对的值。需要注意Entry对象是在Map包中的，需要导入
```java
Set<Entry<String,String>> entries = map.entrySet();
entries.forEach(entry -> {
    String key = entry.getKey();
    String value = entry.getValue();
    System.out.println(key+"="+value);
})
```

### Lambda表达式
Map对象中的forEach方法同样可以实现类似单列集合一样的箭头函数遍历效果
```java
map.forEach(new BiConsumer<String,String>(){
    @Override
    public void accept(String key,String value){
        // s对应函数中的每一个数据
        System.out.println(key+"="+value);
    }
})
// 以下为简写形式
map.forEach((key,value) -> System.out.println(key+"="+value))
```