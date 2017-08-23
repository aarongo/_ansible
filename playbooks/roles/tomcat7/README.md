Tomcat7
=========

自动化运维: 使用 Ansible 进行程序的配置安装

Requirements
------------
系统分区划分准确

Role Variables
--------------

运行时需要填入 tomcat version

Dependencies
------------
1. jdk1.7
2. 定制远端服务器文件源

Example Playbook
----------------

- hosts: "{{ hosts_name }}"
  roles:
    - tomcat7

License
-------

BSD

Author Information
------------------

Author: EdwardLiu
E-Mail: liuyulong@co-mall.com
