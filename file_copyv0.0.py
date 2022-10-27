#!/usr/bin/python
from pydoc import describe
import sys, shutil, os, time


#USAGE:    python3 file_copy.py /Users/dc/Mike_Python/python-scripts /Users/dc/Mike_Python/backup/aws_jul

#Varible declaration
SOURCE=sys.argv[1]
DESTINATION=sys.argv[2]
time_string=time.localtime()
time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S", time_string)
NEW_DEST2=DESTINATION +"_"+ TS

print(NEW_DEST2)



def backup():
    print ("The file or directory to copy is %s" %(SOURCE))
    print ("The backup directory is %s" %(DESTINATION))
    print("")
    print ("Creating a backup up of %s into %s" %(SOURCE,NEW_DEST2))
    
    if os.path.isfile(SOURCE):
        print("Backinh up file")
        shutil.copy(SOURCE,DESTINATION)
    else:
        print("Backing up directory")
        shutil.copytree(SOURCE,NEW_DEST2)
        
        
backup()