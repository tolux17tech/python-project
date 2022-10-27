import time

time_string=time.localtime()
TS=time.strftime("%d%m%y%M%S", time_string)
print(TS)

SOURCE="NEW"

Z=SOURCE+str(TS)
print(Z)