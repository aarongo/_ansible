## zabbix server

**Zabbix Server Install And Use Nginx Web**

### Example
cat /path/zabbix_server.yml

```bash
---
- hosts: zabbix
  roles:
    - nginx
    - zabbix_server
```

### Run ES:

`/path/zabbix_server.yml --extra-vars "DB_HOST=x.x.x.x DB_PORT=3306"`

