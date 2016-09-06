Role Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).

Ansible 流程介绍
------------------
1.使用ansible-galaxy init -p playbooks/roles nginx生成 Roles-->nginx
2.目录介绍
```
├── README.md
├── files
│   ├── nginx-1.8.0.tar.gz
│   ├── openssl-1.0.2f.tar.gz
│   ├── pcre-8.39.tar.gz
│   └── zlib-1.2.8.tar.gz
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── tasks
│   └── main.yml
├── templates
│   ├── index.html.j2
│   ├── log_cut.sh.j2
│   ├── nginx.conf.j2
│   ├── nginx.sh.j2
│   └── nginx_install.sh.j2
└── vars
    └── main.yml
```
defaults: 配置默认变量的目录,可以被 vars 内配置的变量覆盖掉

files: 文件存放位置
handlers: Handlers里面的每一个handler，也是对module的一次调用。而handler与tasks不同的是，handlers不会默认的按顺序执行 只有当TASKS种的action的执行状态是changed时，才会触发notify handler的执行

meta: 其中列出的 “角色依赖” 将被添加到 roles中,(判断系统,从而安装软件)
tasks: 所有的任务列表

templates: 所有j2文件存放位置

site.yml: 执行 playbook 文件入口

```
---
- hosts: nginx
  sudo: True
  roles:
    - nginx #调取角色的名称(目录名)
```
vars:变量存放位置,优先级高于 defaults

所有 copy tasks 可以引用 roles/x/files/ 中的文件，不需要指明文件的路径。

所有 script tasks 可以引用 roles/x/files/ 中的脚本，不需要指明文件的路径。

所有 template tasks 可以引用 roles/x/templates/ 中的文件，不需要指明文件的路径。

所有 include tasks 可以引用 roles/x/tasks/ 中的文件，不需要指明文件的路径
