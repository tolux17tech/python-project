#!/usr/bin/bash

HOSTNAME=$(hostname)
THRESHOLD=90
TS=$(date "+%Y-%m-%d-%H:%M:%S")
LOG_DIR="/home/${USER}/log/log_$TS"
LOG_FILE="/home/${USER}/log/log_$TS/cpu_usage.log"

disk_usage(){
    mkdir -p ${LOG_DIR}
    touch ${LOG_FILE}
    DISK_USAGE=$(df -Ph|grep '/dev/mapper/cs-root'|awk '{print $5}'|sed 's/%//')
    echo "The current the disk usage for server ${HOSTNAME} is ${DISK_USAGE}%" >> ${LOG_FILE}
    if [[ ${DISK_USAGE} -ge THRESHOLD ]]
    then 
        echo "Disk for server ${HOSTNAME} is greater than or equal to 90% >> ${LOG_FILE}
         ACTION REQUIRED!!!"
    else
        echo "Disk for server ${HOSTNAME} is normal" >> ${LOG_FILE}
    fi


}
disk_usage