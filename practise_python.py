#!/usr/bin/python
import os
# def check_word():
#     a="Hello cloud engineering"
#     if a[0]=='Y':
#         print("The first letter of the word is %s" %(a[0]))
#     else:
#         print("The rest of the letters string is:  %s" %(a[1:]))
        
        
# check_word()


file=open("logging_python_log", "w+")
file.write("I love engineering")
file.close()

file=open("logging_python_log", "r+")
file_mi=file.read()
print(file_mi)
file.close

