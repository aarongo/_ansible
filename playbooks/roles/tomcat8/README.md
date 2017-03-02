Tomcat7
=========

自动化运维: 使用 Ansible 进行程序的配置安装

Requirements
------------
系统分区划分准确

Role Variables
--------------

运行时需要填入 tomcat 版本 例如: "tomcat_version=7.0.75" 或者 "tomcat_version=8.5.11"

Dependencies
------------
"tomcat_version=7.0.75" 依赖 jdk1.7
"tomcat_version=8.5.11" 依赖 jdk1.8

Example Playbook
----------------

	- hosts: tomcat
	  roles:
	    - { role: tomcat7, when: "tomcat_version=='7.0.75'"}
	    - { role: tomcat8, when: "tomcat_version=='8.5.11'"}

License
-------

BSD

Author Information
------------------

Author: EdwardLiu
E-Mail: liuyulong@co-mall.com
