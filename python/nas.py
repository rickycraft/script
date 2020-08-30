#!/usr/bin/env python3

import subprocess
from os import path
import argparse


class Options:
    source = "/Volumes/CROCCANTE/OnePlus/"
    dest = "/Volumes/rick/OP6/sdcard/"
    sync_folder = [
        "DCIM/Camera/",
        "WhatsApp/Media/WhatsApp\\ Images/",
        "WhatsApp/Media/WhatsApp\\ Video/",
        "Pictures/",
        "TitaniumBackup/",
    ]
    dry_run = True
    quiet = False

    def __init__(self, dry_run, quiet):
        self.dry_run = dry_run
        self.quiet = quiet
        self.check_path()

    def sync(self):
        cmd = "rsync -ahzP %s %s"
        _pipe = subprocess.DEVNULL if self.quiet else None

        for f in self.sync_folder:
            _cmd = cmd % (self.source + f, self.dest + f)
            None if self.quiet else print(_cmd)
            if not self.dry_run:
                subprocess.run(_cmd, shell=True, stdout=_pipe, stderr=_pipe)

    def check_path(self):
        if not path.exists(self.source):
            print("Invalid source path")
            exit(1)

        if not path.exists(self.dest):
            print("Invalid dest path")
            exit(1)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--quiet", help="quiet", action="store_true")
    parser.add_argument("-n", "--dry-run", help="dry run", action="store_true")
    return parser


def parse_arguments():
    parser = create_parser()
    args = vars(parser.parse_args())
    return Options(args["dry_run"], args["quiet"])


if __name__ == "__main__":
    opt = parse_arguments()
    opt.sync()
