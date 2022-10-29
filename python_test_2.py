import random
import logging
import time

time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S", time_string)

#logging.info a random number between 1 and 10
logging.info(random.randrange(1,10))

word="python"

# logging.info(word[0])

# hostname=commands.getoutput('hostname')

#logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='python_test.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S", time_string)
logging.info("Starting the code run at %s" %TS)

hostname="grafana"
logging.info(hostname)
logging.info("The hostname is %s" %(hostname))

servers={
    "grafana":"patchprod"
    }

def patchprod():
        logging.info("This is the patch prod fucntion")


if hostname in servers:
    logging.info("Calling the " + servers[hostname] + "function")
    if servers[hostname] == "patchprod":
        patchprod()
else: 
    logging.error("Server not found in the list")
                
                
time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S", time_string)
logging.info("Starting the code run at %s" %(TS))
