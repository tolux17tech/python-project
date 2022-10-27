#!/usr/bin/python

#Module
import shutil

#Variable declaration 

SOURCE = "/Users/dc/Library/CloudStorage/OneDrive-Personal/k8s/project/springboot.yaml"
DESTINATION = "/Users/dc/Mike_Python/backup"

print("The source file is %s and the destination directory is %s" %(SOURCE, DESTINATION))
print("The destination directory is %s" %(DESTINATION))


shutil.copy(SOURCE,DESTINATION)