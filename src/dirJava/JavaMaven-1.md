# Maven

## 概述
目的：用于管理和构建java项目的工具，基于项目对象模型POM的概念，通过一小段描述信息管理项目构建  
作用：
- 方便管理依赖：方便管理项目依赖的资源（Jar包）避免版本冲突（在pom.xml中简单描述，maven会自动联网下载，避免了手动导入的繁琐）
  - maven会先在计算机本地创建一个仓库，在需要关联jar包的时候，会依次查找本地——私服——官方的仓库，并将jar包拷贝到本地仓库中进行关联，可以与pip对应
- 统一项目结构：Maven提供了标准的项目工程结构，以下为目录结构
  ```
  maven文件
    src
        main：实际项目资源
            java：java源代码目录
            resources：配置文件目录
        test：测试项目资源
            java
            resources
        pom.xml：项目配置文件
  ```

### 仓库
目的：用于存储资源，包含各种jar包。  
分类：
- 本地仓库：设置在本地指定存储位置的仓库，项目最终关联的是本地仓库中的jar包。
- 私服仓库：保存着具有版权的jar包，由企业搭建在服务器中，maven会先尝试在私服仓库中拷贝jar包。
- 中央仓库：官方的仓库，存放着所有开源的jar包，系统会自动识别项目中所需的jar包，并在云端拷贝（类似npm）

### 坐标
目的：方便项目查找，对所需的jar包资源进行定位。简称gav  
定位方式：mvnrepository.com中查找对应jar包的坐标定义格式，粘贴到pom.xml文件中   
作用：作为唯一标识，唯一性地定位资源的位置，让系统得以进行资源识别与下载工作。
组成：
- groupId：定义当前Maven项目隶属的组织名称——域名反写
- artifactId：定义当前Maven项目名称——模块的名称
- version：Maven项目版本号
- packaging：定义该项目的打包方式

### 依赖
目的：提供Maven项目正常运行所必要的支持的jar包，一个插件为了正常使用可能需要多个jar包提供依赖关系。需要maven系统在中央仓库或私服仓库中拷贝而来。  
使用：在pom中通过`dependency`标签，使用gav添加依赖
```xml
<dependencies>
  <dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.5.11</version>
  </dependency>
</dependencies>
```

### 生命周期
概念：项目按照生命周期模型顺序构建，并且对于生命周期每一个阶段都有提供相对应命令插件来完成。  
开发式只需要直接执行相对应命令，maven便会自动构建项目  
对应项目构建的过程，底层是maven命令的调用。  

### 插件
概念：maven本身是插件框架，核心并不执行具体构建任务，任务都交给插件完成。相比于依赖，插件的作用是强化开发的工具，即使不加也不会影响maven正常运行  
使用：在pom中通过`plugin`标签，使用gav添加插件
```xml
<plugins>
  <plugin>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>3.5.11</version>
  </plugin>
</plugins>
```

### 