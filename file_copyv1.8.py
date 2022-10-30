#!/usr/bin/python

import sys,os

#threshold=input("Please enter the server's threshold: ")
threshold=sys.argv[1]

if (len(sys.argv)) != 2:
    print("You entered the wrong number of command line argument")
    exit()
else:
    threshold=sys.argv[1]
    print("You entered the threshold of %s" %(threshold))
    
    
    
disk_check=os.popen["du -h /home/admin/lv |egrep '^[0-9]+\.[0-9]+G'"]
disk_size=os.system[du -h /home/admin/lv |egrep '^[0-9]+\.[0-9]+G'|awk '{print $1}'|sed 's/G//']