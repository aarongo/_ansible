#!/bin/bash
# This Script For Ansible Install Nginx
# set LANG
sudo echo "export LC_ALL=C" >> /etc/profile;source /etc/profile
# Install libary
yum -y install gcc gcc-c++

#Install Pcre
cd /tmp;tar xf pcre-8.39.tar.gz;cd pcre-8.39
./configure \
--prefix=/usr/pcre-8
make && make install

#Install zlib
cd /tmp;tar xf zlib-1.2.8.tar.gz;cd zlib-1.2.8
./configure \
--prefix=/usr/zlib-1.2
make && make install

#Install openssl
cd /tmp;tar xf openssl-1.0.2f.tar.gz;cd openssl-1.0.2f
./configure darwin64-x86_64-cc --prefix=/usr
make && make install

#Install Nginx
yum -y install zlib-devel openssl-devel pcre-devel
groupadd -r nginx
useradd -s /sbin/nologin -g nginx -r nginx
cd /tmp
mkdir /software
tar xf nginx-1.8.0.tar.gz;cd nginx-1.8.0
./configure \
--prefix=/software/nginx \
--with-pcre=/tmp/pcre-8.39 \
--with-zlib=/tmp/zlib-1.2.8 \
--user=nginx \
--group=nginx \
--with-http_stub_status_module \
--with-http_gzip_static_module \
--with-http_sub_module \
--with-http_ssl_module
make && make install