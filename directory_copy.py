import os, time, shutil

SRC="/Users/dc/Mike_Python/python-scripts"
SRC2=os.path.basename("/Users/dc/Mike_Python/python-scripts")
DEST="/Users/dc/Mike_Python/backup"
DEST2=os.path.join(DEST, SRC2)


shutil.copytree(SRC, DEST2)
