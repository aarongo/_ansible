## controller

> 1. 判断系统是否能够访问外网
> 2. 如果能够访问外网引用`perform`进行安装
> 3. 如果不能访问外网同样引用`perform 执行`进行安装

### Tomcat Program

**注意:** 
**1**. ${TOMCAT_HOME} 所属权限为启动用户和组
**2**. supervisor 日志目录权限为启动用户或者组 如果启动多进程需要细分权限

```
[program:tomcat-process]
directory = /software/tomcat_supervisor
command = /software/tomcat_supervisor/bin/supervisord_wrapper.sh
user = tomcat
autostart= true
autorestart = true
startsecs = 10
```