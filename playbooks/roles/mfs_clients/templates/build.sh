#!/bin/bash
cd /tmp/moosefs-3.0.88
./configure --prefix=/usr/local/mfs --with-default-user=mfs --with-default-group=mfs --enable-mfsmount  --disable-mfsmaster  --disable-mfschunkserver
make && make install
