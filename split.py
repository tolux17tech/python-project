import os

my_dir=os.getcwd()
print(my_dir)

my_dir_new=my_dir.split("/")
print(my_dir_new[1])
print(my_dir_new[2])
print(my_dir_new[3])
print(my_dir_new[4].split("-")[1])

