# Tomcat 
----
> 自动化Tomcat 包含(安装/配置/更新)

**注意:**
选择版本为8安装时需要需要更改 server.xml

```bash
  # 更改为一下配置
  <!--<Listener className="org.apache.catalina.core.JasperListener" />-->
  <Listener className="org.apache.catalina.startup.VersionLoggerListener" />
```

## 安装示例

`ansible-playbook tomcat.yml --extra-vars "hosts_name=${hosts_name} tomcat_version=${tomcat_version} project_name=${project_name} deploy_name=${deploy_name} parameter=${parameter} run_way=${run_way}" --tags ${tags}`

**${hosts_name}**---hosts 里的主机标签
**${tomcat_version}**---选择 tomcat 版本
**${project_name}**---输入部署的名字
**${deploy_name}**---需要添加部署的项目
**${parameter}**---检测使用的 url 需要手动填写
**${run_way}**---选择安装方式
**${tags}**---选择方式(当更新是跳过创建部署目录操作)