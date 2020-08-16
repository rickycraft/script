#!/usr/bin/env python3

import subprocess
import os
import argparse
import sys
from subprocess import PIPE, DEVNULL, STDOUT
from datetime import date


EXIT_ERROR = 0
JUNK_FILES = [
    "/Android",
    "/data",
    "/DCIM/.thumbnails",
    "/Pictures/.thumbnails",
    "/Movies/.thumbnails",
]
BLACKLIST_DIR = [
    "amap",
    "android",
    "backups",
    "beam",
    "data",
    "mipush",
    "notifications",
    "ringtones",
    "telegram",
    "tencent",
]
SDCARD = "/sdcard"
TITANIUM_BACK = "/TitaniumBackup"
DEBUG = False

dir_to_sync = []
options = {
    "delete": False,
    "titanium": False,
    "junk": False,
    "device_id": "",
    "sync_dir": False,
    "dry_run": False,
}
_pipe = DEVNULL


def create_parser():
    parser = argparse.ArgumentParser(description="BetterBack for android on Linux")
    parser.add_argument("-d", help="Delete file on dest", action="store_true")
    parser.add_argument("-f", help="Dirs file", metavar="FILE")
    parser.add_argument("-o", help="Outdir", metavar="OUT")
    parser.add_argument(
        "-e", help="Get from env outdir (ADB_SYNC_DEST)", action="store_true"
    )
    parser.add_argument("-j", help="Clean junk files", action="store_true")
    parser.add_argument("-t", help="Update titanium", action="store_true")
    parser.add_argument("-i", help="Specify device id", metavar="DEVICE_ID")
    parser.add_argument("-D", help="Debug mode", action="store_true")
    parser.add_argument("-l", help="Sync by list dir", action="store_true")
    parser.add_argument("-n", help="Dry run", action="store_true")
    return parser


def parse_args():
    parser = create_parser()
    arg = vars(parser.parse_args())
    # if debug flag is set
    if arg["D"]:
        print("DEBUG IS ACTIVE")
        print("Args:", arg)
        global DEBUG
        DEBUG = arg["D"]
        global _pipe
        _pipe = None
    # check that at leas one output is valid
    if not (arg["e"] ^ bool(arg["o"])):
        sys.stderr.write("Both -o and -e specified or none\n")
        exit(EXIT_ERROR)
    # read all arguments
    read_destination(arg)
    read_flags(arg)
    read_syncdir(arg)

    print("Parsed Arg:", options) if DEBUG else None


# check if a device is connected
def check_device():
    subprocess.run(["adb", "start-server"], stdout=DEVNULL, stderr=DEVNULL)
    out = subprocess.run(
        ["adb", "get-serialno"], stdout=PIPE, stderr=DEVNULL, universal_newlines=True,
    ).stdout.strip()

    if out != "":
        if options["device_id"] != "":
            return options["device_id"] in out
        else:
            return True
    else:
        return False


# read output destination folder
def read_destination(arg: dict):
    path = None
    # take path from env
    if arg["e"]:
        path = os.getenv("ADB_SYNC_DEST")
        if not path:
            sys.stderr.write("no env var is set\n")
            exit(EXIT_ERROR)
    # take path form argument
    elif arg["o"]:
        path = arg["o"]
    # check path validity
    if path:
        path = os.path.abspath(path)
        if os.path.exists(path):
            options["out_dir"] = path
        else:
            sys.stderr.write("path does not exist\n")
            exit(EXIT_ERROR)
    else:
        sys.stderr.write("File path error\n")
        exit(EXIT_ERROR)


# read option from the passed arguments
def read_flags(arg: dict):
    options["delete"] = arg["d"]
    options["junk"] = arg["c"]
    options["titanium"] = arg["t"]
    options["sync_dir"] = arg["l"]
    options["dry_run"] = arg["n"]
    options["device_id"] = arg["i"] if arg["i"] else ""


# read file w/ folder to sync
def read_syncdir(arg: dict):
    if arg["f"]:
        with open(arg["f"], "r") as f:
            for line in f.readlines():
                dir_to_sync.append(line.strip())
        print("Sync", dir_to_sync) if DEBUG else None
    else:
        print("Sync all dirs") if DEBUG else None


# remove folder/file from device
def adb_shell_rm(cmd: str):
    # check that is somewhat valid
    if len(cmd) < 2:
        return
    f = SDCARD + cmd
    _cmd = ["adb", "shell", "rm", "-rf", f]
    if options["dry_run"]:
        print(" ".join(_cmd))
    else:
        print("shell rm", f) if DEBUG else None
        subprocess.run(_cmd, stdout=_pipe)


def del_junk():
    if options["junk"]:
        for f in JUNK_FILES:
            adb_shell_rm(f)


def del_titanium():
    if check_titanium_date() or options["titanium"]:

        _cmd = ["rm", "-rf", options["out_dir"] + TITANIUM_BACK]
        if options["dry_run"]:
            print(" ".join(_cmd))
        else:
            print("Removing Titanium")
            subprocess.run(_cmd, stdout=_pipe)
            if len(dir_to_sync) > 0 and TITANIUM_BACK not in dir_to_sync:
                dir_to_sync.append(TITANIUM_BACK)


def check_titanium_date():
    titanium_dir = options["out_dir"] + TITANIUM_BACK
    if not os.path.exists(titanium_dir):
        return False
    m_date = date.fromtimestamp(os.path.getmtime(titanium_dir))
    today = date.today()
    return m_date < today


def adb_sync():
    folder_list()
    del_junk()
    del_titanium()
    # create command
    cmd = ["adb-sync", "-R", "-t"]
    cmd.append("-d") if options["delete"] else None
    # either some folder or all the sdcard
    if len(dir_to_sync) > 0:
        adb_sync_folders(cmd)
    else:
        adb_sync_all(cmd)


def adb_sync_all(cmd: list):
    cmd.append(SDCARD + "/")
    cmd.append(options["out_dir"])
    if options["dry_run"]:
        print(" ".join(cmd))
    else:
        print("running:", cmd) if DEBUG else print("Pulling", cmd[-2], "->", cmd[-1])
        subprocess.run(cmd, stderr=DEVNULL, stdout=_pipe)


def adb_sync_folders(cmd: list):
    for f in dir_to_sync:
        _cmd = cmd.copy()
        # trailing slash to open dir like rsync
        _cmd.append(SDCARD + f + "/")
        _cmd.append(options["out_dir"] + f)
        if options["dry_run"]:
            print(" ".join(_cmd))
        else:
            print("running:", _cmd) if DEBUG else print(
                "Pulling", _cmd[-2], "->", _cmd[-1]
            )
            subprocess.run(_cmd, stderr=DEVNULL, stdout=_pipe)


def folder_list():
    if not options["sync_dir"]:
        return

    cmd = ["adb", "shell", "ls", "/sdcard"]
    out = (
        subprocess.run(cmd, stderr=DEVNULL, stdout=PIPE, universal_newlines=True)
        .stdout.strip()
        .split("\n")
    )
    for f in out:
        if f.lower() not in BLACKLIST_DIR:
            dir_to_sync.append("/" + f)


if __name__ == "__main__":
    try:
        parse_args()
        if not check_device():
            sys.stderr.write("No device connected\n")
            # exit(EXIT_ERROR)
        print("#" * 20) if DEBUG else None
        adb_sync()
    except KeyboardInterrupt:
        print("Stopping")
        exit(EXIT_ERROR)
