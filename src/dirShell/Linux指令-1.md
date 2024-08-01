# Linux指令

## 最最最基础
### 目录操作
- mkdir
  创建目录
- cd
  目录跳转
- ls
  目录展示
- mv
  
- cp
  
- pwd
  当前路径
### 文件操作
- rm
  删除
- touch
  创建文件
- cat
  预览文件
- tail
  查看文件末尾
- less
  翻页预览
- more
### 其他操作
- find
  检索文件
- whereis
- which
- sudo
  用户临时权限
- service
- free
- df
- mount
- uname
- scp
- ftp
### 权限相关
- useradd
  新建用户
- groupadd
  新建用户组，所有用户组信息存在/etc/group下
- chgrp
  修改指定用户所在的组
- chown
  修改文件的所有者u的身份，让文件只能由根用户和指定用户访问
  chown sora file.txt 将文件分配给sora，这个sora默认是root组下的
  chown sora:abc file.txt 将文件分配给abc组下的sora
- chmod
  增加和解除文件权限
  文件用户：u-文件所有者 g-文件所有者同组用户 o-其他用户 (数字写法每一位都对应一个用户) a-所有用户
  文件权限：r-读4 w-写2 x-执行1 
  命令参数：-R 地柜改变文件夹下所有文件的权限
  包含两种写法
  chmod u+rw file.txt
  chmod 600 file.txt    
- chattr
- cksum
- cmp
- diff
- diffstat
- file
- wc

- grep
- sed
- awk
- cut


通配符  
- 

快捷

- top
  用来查看进程并进行相关操作，类似任务管理器
  - 
