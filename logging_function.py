#!/usr/bin/python
import logging
import time
import socket


# logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='python_test.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S", time_string)
logging.info("Starting the code run at %s" %TS)



# hostname="MacBook-Pro.local"
# logging.info(hostname)
# logging.info("The hostname is %s" %(hostname))


hostname=(socket.gethostname())
logging.info(hostname)
logging.info("The hostname is %s" %(hostname))



servers={
    "MacBook-Pro.local":"patchprod"
    }

def patchprod():
        logging.info("This is the patch prod fucntion")


if hostname in servers:
    logging.info("Calling the " + servers[hostname] + " function")
    if servers[hostname] == "patchprod":
        patchprod()
else: 
    logging.error("Server not found in the list")
                
                
time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S", time_string)
logging.info("Ending the the code run at %s" %(TS))
