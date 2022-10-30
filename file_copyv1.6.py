
#!/usr/bin/python
from pydoc import describe
import sys, shutil, os, time,logging


def backup():
    try:
        
        if len(sys.argv) != 4:
            logging.warning("Wrong number of command line arguments entered, Please fix !!!")
            exit
        else:
        
            if os.path.isfile(SOURCE):
                #SOURCE=sys.argv[1]
                DESTINATION=sys.argv[2]
                RUNNER=sys.argv[3]
                BACKUP_TYPE="FILE"
                time_string=time.localtime()
                TS=time.strftime("%d%m%y%M%S", time_string)
                #BACKUP_TYPE="FILE"
                FILE_DEST=("%s/%s/%s/%s" %(DESTINATION,RUNNER,BACKUP_TYPE,TS))
                logging.info("The file or directory to copy is %s" %(SOURCE))
                logging.info("The backup directory is %s" %(DESTINATION))
                logging.info("")
                logging.info("Creating a backup up of %s into %s" %(SOURCE,FILE_DEST))
                logging.info("Backing up file")
                logging.info(FILE_DEST)
                os.makedirs(FILE_DEST)
                shutil.copy(SOURCE,FILE_DEST)
            else:
                #SOURCE=sys.argv[1]
                DESTINATION=sys.argv[2]
                RUNNER=sys.argv[3]
                time_string=time.localtime()
                TS=time.strftime("%d%m%y%M%S", time_string)
                BACKUP_TYPE="DIRECTORY"
                DEST_DIR=("%s/%s/%s/%s/%s" %(DESTINATION,RUNNER,BACKUP_TYPE,TS,os.path.basename(SOURCE)))
                logging.info("The file or directory to copy is %s" %(SOURCE))
                logging.info("The backup directory is %s" %(DESTINATION))
                logging.info("")
                logging.info("Creating a backup up of %s into %s" %(SOURCE,DEST_DIR))
                logging.info("Backing up directory")
                shutil.copytree(SOURCE,DEST_DIR)
    except:
        logging.error("The copy function failed")
            
        




if __name__=="__main__":
    logging.basicConfig(filename='python_test.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.basicConfig(filename='python_test.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.WARNING)
    logging.basicConfig(filename='python_test.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.CRITICAL)
    logging.basicConfig(filename='python_test.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.ERROR)

#USAGE:    python3 file_copyv1.5.py /Users/dc/Mike_Python/python-scripts /Users/dc/Mike_Python/backup/aws_jul tolu
#Varible declaration
SOURCE=sys.argv[1]
DESTINATION=sys.argv[2]

backup()