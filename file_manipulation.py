#/usr/bin/python

import sys,os

if (len(sys.argv)) != 2:
    print("You entered the wrong number of command line argument")
    exit()
else:
    threshold=sys.argv[1]
    print("You entered the threshold of %s" %(threshold))

#Opening a file
fh=open("json1.py", "w+")
fh.write("I like mike as my teacher")
fh.close()


fh=open("json1.py", "r+")
file_content=fh.read()
print(file_content)
fh.close()

#listing  a directory

sh=os.listdir('.')
for i in sh:
    if  i == "file_manipulation.py":
        print("File available")
print(sh)


# entry=int(input("Enter disk utilization threadhold: "))
# print("You entered %s" %(entry))

# print(f"You entered {entry}")

