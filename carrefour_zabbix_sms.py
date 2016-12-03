#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Author EdwardLiu


import os
from subprocess import Popen, PIPE
import sys
import datetime


os.environ["JAVA_HOME"] = "/software/jdk1.7.0_51"
os.environ["PATH"] = "$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH"
sms_logs_path = "/software/zabbix_server/logs/sms.log"


def send_sms(mobile, message1, message2):
    sendsms_command = """/software/jdk1.7.0_51/bin/java -jar /software/script/TestSMS23.jar "%s %s" "%s" """ % (
        message1, message2, mobile)
    proc = Popen(sendsms_command, stdin=PIPE, stdout=PIPE, universal_newlines=True, shell=True)
    exit_code = proc.wait()
    result = ""
    if exit_code != 0:
        for line in proc.stderr:
            result = result + line
    else:
        for line in proc.stdout:
            result = result + line
    return result


def main():
    mobile = sys.argv[1]
    message1 = sys.argv[2]
    if len(sys.argv) == 3:
        message2 = ''
    elif len(sys.argv) == 4:
        message2 = sys.argv[3]
    send_sms(mobile, message1, message2)
    NOW = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    send_messages = '----------Stdout----------' + "\n"+NOW + "\n"\
                    u'手机号-->%s'.encode(encoding='utf-8')%mobile + "\n"\
                    u'Frist信息-->%s'.encode(encoding='utf-8')%message1 + "\n"\
                    u'sencend信息-->%s'.encode(encoding='utf-8')%message2 + "\n"+"----------Stdout End----------"+"\n"
    with open(sms_logs_path, "a") as text_file:
        text_file.write(send_messages)
    text_file.close()

if __name__ == '__main__':
    main()

