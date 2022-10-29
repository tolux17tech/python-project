#!/usr/bin/python
from pydoc import describe
import sys, shutil, os, time, logging

logging.basicConfig(filename='python_test.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.basicConfig(filename='python_test.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.WARNING)
logging.basicConfig(filename='python_test.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.CRITICAL)
logging.basicConfig(filename='python_test.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.ERROR)

#USAGE:    python3 file_copy.py /Users/dc/Mike_Python/python-scripts /Users/dc/Mike_Python/backup/aws_jul
##LOGGING DETAILS
time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S", time_string)
logging.info("Starting the code run at %s" %TS)

if len(sys.argv) != 5:
    print("Incomplete arugments")
    exit()
else:
    print("Calling the file copy function")

#Varible declaration
SOURCE=sys.argv[1]
DESTINATION=sys.argv[2]
RUNNER=sys.argv[3]
BACKUP_TYPE=sys.argv[4]
time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S", time_string)
DEST_DIR=("%s/%s/%s/%s/%s" %(DESTINATION,RUNNER,BACKUP_TYPE,TS,os.path.basename(SOURCE)))
FILE_DEST=("%s/%s/%s/%s" %(DESTINATION,RUNNER,BACKUP_TYPE,TS))




def backup():
    try:
        
            print ("The file or directory to copy is %s" %(SOURCE))
            print ("The backup directory is %s" %(DESTINATION))
            print("")
            print ("Creating a backup up of %s into %s" %(SOURCE,DEST_DIR))
            
            if os.path.isfile(SOURCE):
                print("Backing up file")
                print(FILE_DEST)
                os.makedirs(FILE_DEST)
                shutil.copy(SOURCE,FILE_DEST)
            else:
                print("Backing up directory")
                shutil.copytree(SOURCE,DEST_DIR)
                
    except:
        print ("The copy function failed")
        
time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S", time_string)
logging.info("Ending the code run at %s" %TS)
        
        
backup()