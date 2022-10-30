#!/bin/bash
#Script to check CPU, DISK, MEMORY UTILIZATION

HOSTNAME=$(hostname)
DATE=$(date "+%Y-%m-%d %H:%M:%S")
CPU_USAGE=$(top -b -n 2 -d1|grep "Cpu(s)"|awk '{print $2}'|awk -F. '{print $1}') #-b means to run in bash mode and -n means run twice
MEMORY_USAGE=$(free -m|grep Mem|awk '{print $3/$2*100}'|awk -F. '{print $1}')
DISK_USAGE=df -hP |grep '/dev/mapper/cs-root'|awk '{print $5}'|sed 's/%//'

q