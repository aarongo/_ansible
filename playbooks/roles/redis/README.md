Redis
=========

单点和集群安装
![未命名](https://lh3.googleusercontent.com/-boleYmBRDb0/WMfebjyDb7I/AAAAAAAAACY/T-s_EpKBFIQ/I/%25255BUNSET%25255D.png)

使用工具管理集群:
redis-trib.rb create --replicas 1 10.200.200.78:6379 10.200.200.78:6380 10.200.200.79:6379 10.200.200.79:6380 10.200.200.81:6379 10.200.200.81:6380

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: "redis_{{roles}}"
      roles:
        - role: redis

License
-------

BSD

Author Information
------------------


