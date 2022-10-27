#!/usr/bin/python

import sys

x=sys.argv[1]
y=sys.argv[2]

print("The first command line argument is %s" %(x))

print("The second command line argument is %s" %(y))

#Function Definitions
def scheduled():
    print ("Hi the scheduled function has been called")

#conditional statement

if x == "scheduled":
    print ("Calling the scheduled function")
    scheduled()
else:
    print ("Calling the interview function")