#!/usr/bin/python
from pydoc import describe
import sys, shutil, os, time



#USAGE:    python3 file_copy.py /Users/dc/Mike_Python/python-scripts /Users/dc/Mike_Python/backup/aws_jul

#Varible declaration
SOURCE=sys.argv[1]
DESTINATION=sys.argv[2]
RUNNER=sys.argv[3]
#BACKUP_TYPE=sys.argv[4]
time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S", time_string)



#DEST_DIR=("%s/%s/%s/%s/%s" %(DESTINATION,RUNNER,BACKUP_TYPE,TS,os.path.basename(SOURCE)))
#FILE_DEST=("%s/%s/%s/%s" %(DESTINATION,RUNNER,BACKUP_TYPE,TS))


def backup():
    
    
    if os.path.isfile(SOURCE):
        BACKUP_TYPE="FILE"
        FILE_DEST=("%s/%s/%s/%s" %(DESTINATION,RUNNER,BACKUP_TYPE,TS))
        print ("The file or directory to copy is %s" %(SOURCE))
        print ("The backup directory is %s" %(DESTINATION))
        print("")
        print ("Creating a backup up of %s into %s" %(SOURCE,FILE_DEST))
        print("Backing up file")
        print(FILE_DEST)
        os.makedirs(FILE_DEST)
        shutil.copy(SOURCE,FILE_DEST)
    else:
        BACKUP_TYPE="DIRECTORY"
        DEST_DIR=("%s/%s/%s/%s/%s" %(DESTINATION,RUNNER,BACKUP_TYPE,TS,os.path.basename(SOURCE)))
        print ("The file or directory to copy is %s" %(SOURCE))
        print ("The backup directory is %s" %(DESTINATION))
        print("")
        print ("Creating a backup up of %s into %s" %(SOURCE,DEST_DIR))
        print("Backing up directory")
        shutil.copytree(SOURCE,DEST_DIR)
        
        
backup()