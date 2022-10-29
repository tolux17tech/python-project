#!/usr/bin/bash

HOSTNAME=$(hostname)
WARNING=80
CRITICAL=90
TS=$(date "+%Y-%m-%d-%H:%M:%S")
LOG_DIR="/home/${USER}/log/log_$TS"
LOG_FILE="/home/${USER}/log/log_$TS/cpu_usage.log"


cpu_usage(){
    CPU_IDLE=$(top -b -n1|grep 'Cpu'|awk '{print $8,$9}'|awk '{print $1}'|awk -F. '{print $1}')
    if [[ ${CPU_IDLE} == "id" ]]
    then
        exit
    else
        mkdir -p ${LOG_DIR}
        touch ${LOG_FILE}
        CPU_UTILI=`expr 100 - ${CPU_IDLE}`
        echo "The Cpu(%) utilization for server $HOSTNAME is ${CPU_UTILI}%" >>${LOG_FILE}
        if [[ $CPU_UTILI -gt $WARNING ]]
        then
            echo "WARNING, The Cpu(%) utilization for server $HOSTNAME IS GREATER THAN 80%" >> ${LOG_FILE}
        elif [[ $CPU_UTILI -gt $CRITICAL ]]
        then
            echo "CRITICAL, The Cpu(%) utilization for server $HOSTNAME IS GREATER THAN 90% 
                  ACTION NEEDED" >> ${LOG_FILE}
        else
            echo "The Cpu(%) utilization for server $HOSTNAME is normal" >> ${LOG_FILE}
        fi

    fi
    
   

}

cpu_usage