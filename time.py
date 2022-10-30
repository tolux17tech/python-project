import time, os, getpass

my_time=time.localtime()
print(my_time)
TS=time.strftime("%m%d%y%M%S", my_time)
print(TS)
DEST="tolu" + "/" + TS
os.makedirs(DEST)
os.mkdir("%s_%s" %("tolu",TS))

#d=day m=month y=year M=minute and S=seconds

# print(os.name)
# print(os.uname())
# print(os.geteuid())
# print(os.getgid())
# print(getpass.getuser())
# print(os.putenv("NAMES", "TOLUX17"))

# print(os.path.basename("/home/user"))
# print(os.path.exists("/home/user"))