#!/bin/bash

export JAVA_HOME=/software/jdk1.7.0_51
script_path=/software/script/monitor
out_dir=/tmp
Now=$(date +%Y-%m-%d_%H-%M)
IP_ADDR=$(/sbin/ifconfig eth1 | grep "inet addr" | awk '{print $2}' | awk -F ":" '{print $2}')
hostname=$(/bin/hostname)
dnsname="f.cdc.carrefour.com"
FNQ=${hostname}${dnsname}
upload_dir=/software/picture_upload/log_analysis/


at_tomcat(){
	${script_path}/java.sh
	${script_path}/linux.sh
}
at_tomcat_handle(){
	cd ${out_dir}
	tar czvf ${FNQ}_${Now}_tomcat.tar.gz jstack linux
	mv ${FNQ}_${Now}_tomcat.tar.gz ${upload_dir}
	cd ${out_dir};rm -rf jstack linux
}

at_memcached(){
	${script_path}/memcache.sh
	cd ${out_dir}
	tar czvf ${FNQ}_${Now}_memcacehd.tar.gz memcached
	mv ${FNQ}_${Now}_memcacehd.tar.gz ${upload_dir}
	cd ${out_dir};rm -rf memcached
}

at_mongodb(){
	${script_path}/mongodb.sh
	cd ${out_dir}
	tar czvf ${FNQ}_${Now}_mongodb.tar.gz mongodb
	mv ${FNQ}_${Now}_mongodb.tar.gz ${upload_dir}
	cd ${out_dir};rm -rf mongodb

}

at_mysql(){
	${script_path}/mysql.sh
	cd ${out_dir}
	tar czvf ${FNQ}_${Now}_mysql.tar.gz mysql
	cd ${out_dir};rm -rf mysql
}

case $1 in
	tomcat )
		at_tomcat
		at_tomcat_handle
		;;
	memcache )
		at_memcached
		;;
	mongodb )
		at_mongodb
		;;
	mysql )
		at_mysql
		;;
	* )
        echo "Usage:$0(tomcat|memcached|mongodb|mysql)"
        exit 1
esac
