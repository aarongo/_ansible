#!/bin/bash
# 处理云端是本地磁盘(百度云)
umount /mnt
sed -i '/^\/dev\/vdb/d' /etc/fstab
echo "n
p
1


w
" | fdisk /dev/vdb && mkfs.xfs /dev/vdb1
mkdir /software
echo "/dev/vdb1       /software       xfs     defaults        1 1" >> /etc/fstab
mount -a