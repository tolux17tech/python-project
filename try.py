#!/usr/bin/python
import os

try:
	os.mkdir("BACKUP_LOCATION_TS")
	print("The directory you are trying to create was SUCCESSFUL!!! {}.format(BACKUP_LOCATION_TS")
except OSError:
	print("The directory you are trying to create FAILED!!! {}.format(BACKUP_LOCATION_TS")

