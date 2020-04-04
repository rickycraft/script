#!/usr/local/bin/python3
import os
import sys
import subprocess
from datetime import datetime, timedelta, date
source = "/Volumes/CROCCANTE/OnePlus"
dest = "/Volumes/rick/OP6/sdcard"

Titanium = "/TitaniumBackup/"
syncFolder = ["/DCIM/Camera/", "/Pictures/", "/WhatsApp/Media/WhatsApp Images/", "/WhatsApp/Media/WhatsApp Video/", Titanium]


avoid = ["/Android", "/data", "/DCIM/.thumbnails", "/Pictures/.thumbnails"]
dateFile = "/Volumes/CROCCANTE/date.txt"
today = date.today()

# TODO titanium automatic avoid backup


def titaniumCheck():
    f = open(dateFile, "r")
    d = datetime.strptime(f.readline(), "%Y%m%d").date()
    f.close()
    # if last backup is before today
    return (d < today)


def titaniumSet():
    f = open(dateFile, "w")
    d = today.strftime("%Y%m%d")
    f.write(d)
    f.close()


def syncPhotos():
    print("\nSyncing photos\n")
    for f in syncFolder:
        print("#####\nSyncing",f,"\n#####")
        subprocess.call(["rsync", "-avhzP", "--size-only", source+f, dest+f])
    print("Done syncing")


def shellRm(f):
    f = "/sdcard"+f
    print("removing shell", f)
    subprocess.call(["adb", "shell", "rm", "-rf", f])


def syncDevice():
    if (not titaniumCheck()):
        i = input("Do you want to update Titanium ? [Y/n] ")
        if (i != "n"):
            print("Updating titanium")
            subprocess.call(["rm", "-rf", source+Titanium])
            titaniumSet()
    for a in avoid:
        shellRm(a)
    subprocess.call(["adb-sync", "-R", "-t", "-d", "/sdcard/", source])


def checkMount():
    return (os.path.exists(source) & os.path.exists(dest))


def checkDevice():
    o = subprocess.check_output(["adb", "devices"]).decode("utf-8")
    print(o)
    if ("29d3c130" in o):
        return True
    else:
        return False

# main

if (checkMount() == False):
    print("Dir not mounted")
    exit(0)
if (checkDevice() == False):
    print("Device not connected")
    exit(0)

syncDevice()
syncPhotos()
