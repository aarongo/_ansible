角色名称 setup_logstash
=========

安装supervisor,logstash.配置使用supervisor 方式启动logstash

要求
------------

使用方式需要确定目标主机为 centos 系统,并且拥有 sudo 权限

角色的参数
--------------

后续可更新参数
	1. 配置文件的名称
	2. 抓取的日志路径
	3. redis的服务器地址
	4. elash服务器地址

依赖
------------
角色间的依赖目前没有涉及,但是tasks是有依赖,先安装 meld3 然后安装 supervisor 否则不能成功

实例
----------------
cat setup_logstash.yml
    - hosts: servers
      sudo: True
      roles:
         - Rolename

License
-------

BSD

Author Information
------------------

Name: EdwardLiu
EMAIL: lonnyliu@126.com