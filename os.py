import os
from datetime import datetime

#print current directory
print(os.getcwd())

#change directory
os.chdir("/Users/dc/Mike_Python")

#Listing the content of a directory
print(os.listdir())  #You can optional pass a directory like this "print(os.listdir("/Users/dc/Downloads"))""


#Creating a directory
os.mkdir("test-os-module")  #Create a directory
os.makedirs("father/daughter") #Creates directory and sub directory

#Removing directories
os.rmdir("test-os-module")
os.removedirs("father/daughter")

#Renaming a folder
os.rename("test-os-module", "test-passed")

Getting information about a directory
print(os.stat('os.py'))
print(os.stat('os.py').st_atime) #You need to import datetime like [from datetime import datetime]
mode = (os.stat('os.py').st_atime)

print(datetime.fromtimestamp(mode))


Shows the directory tree

for dirpath, dirnames, filenames in os.walk("/Users/dc/Mike_Python"):   #This prints the directory, path and files in a directory recursively
    print ("Current directory is: ",  dirnames)
    print ("Current path is: ", dirpath)
    print ("Filenames are: ",  filenames)
    print ("")

#Get the home directory
print(os.environ.get('HOME')) 

#Joins a path with another
file_path = os.path.join(os.environ.get('HOME'), "tolu.txt")
print (file_path)

#Getting a  exact file name out of a path
print(os.path.basename("/Users/dc/Mike_Python"))

#Getting a directory name out of a path
print(os.path.dirname("/Users/dc/Mike_Python"))

#Splitting dir name from file name
print(os.path.split("/Users/dc/Mike_Python"))

#Checking if a path exists, it gives true of false
print(os.path.exists("/Users/dc/Mike_Python"))

#checking if a path is directory or file name
print(os.path.isdir("/Users/dc/Mike_Python"))
print(os.path.isfile("/Users/dc/Mike_Python"))

#Print inforamtion about the os module
#print(dir(os))
print(os.uname())




