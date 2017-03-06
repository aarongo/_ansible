system_init
=========

初始化系统工作

要求
------------

需要一个新安装系统的 Linux Server


角色变量
--------------


	limit_conf:
	  - { name: soft, info: "*   soft    nofile  65535" }
	  - { name: hard, info: "*   hard    nofile  65535" }
	DNS_Server:
	  - { name: pubilc, info: "nameserver {{pubilc_adress}}"}
	  - { name: Search_domain, info: "nameserver {{search_adress}}"}

依赖
------------

没有任何依赖

 playbook 例子
----------------

Run: ansible-playbook roles/limit.yml --extra-vars "pubilc_adress=114.114.114.114 search_adress=8.8.8.8 hostname=test01"

    - hosts: servers
      roles:
         - system_init

License
-------

BSD

Author Information
------------------

> Author:EdwardLIu

****

> E-mail: lonnyliu@126.com

