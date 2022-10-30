#!/usr/bin/python
import os,sys,logging
# def check_word():
#     a="Hello cloud engineering"
#     if a[0]=='Y':
#         print("The first letter of the word is %s" %(a[0]))
#     else:
#         print("The rest of the letters string is:  %s" %(a[1:]))
        
        
# check_word()


# file=open("logging_python_log", "w+")
# file.write("I love engineering")
# file.close()

# file=open("logging_python_log", "r+")
# file_mi=file.read()
# print(file_mi)
# file.close


# for x in os.listdir("."):
#     if x == "logging_python_log":
#         log_file=open("logging_python_log", "r+")
#         log=log_file.read()
#         print(log)
#         log_file.close()
        
        

# for x in os.listdir("."):
#     if x == "logging_python_log":
#         log_file=open(x, "r+")
#         log=log_file.read()
#         print(log)
#         log_file.close()
        
        
# threshold="85%"
# threshold=threshold.replace('%','')
# print(threshold)

# threshold="95%"
# threshold=threshold.strip("%")
# print(threshold)
    
# a="TOLULOPE"
# print(a.lower())
# print(a.title())
# print(a.upper())

# for x in os.listdir("."):
#     if x == "logging_python_log":
#         log_file=open(x, "r+")
#         log=log_file.read()
#         print(log)
#         log_file.close()
#         with open("logging_python_log", "r+") as file: 
#             x=file.read()
#         with open("logging_python_log", "w+") as file:
#             x=x.replace('cloud','engine')
#             file.write(x)
        
with open("logging_python_log", "r+") as file: 
    x=file.read()
    print(x)
with open("logging_python_log", "w+") as file: 
    x=x.replace('cloud','engine')
    file.write(x)        
with open("logging_python_log", "r+") as file: 
    x=file.read()
    print(x)
    


# with open("logging_python_log", "r+") as file: 
#     x=file.read()
# with open("logging_python_log", "w+") as file:
#     x=x.replace('cloud','engine')
#     file.write(x)


# log=open(x, "r+")
# log2=log.read()
# print(x)      

        


# fh=open("json1.py", "w+")
# fh.write("I like mike as my teacher")
# fh.close()

# fh=open("json1.py", "w+")
# fh.write("I like mike as my teacher".replace("mike", "tolu"))
# fh.close()


    
