#!/usr/local/bin/python3

from pynput.keyboard import Key
from pynput import keyboard
from sys import exit
from typing import Union
from subprocess import run, PIPE, DEVNULL
from time import sleep

IDENTITY_FILE = "/Users/rick/.ssh/id_rsa"
MEDIA_KEY = [Key.media_volume_up, Key.media_volume_down, Key.media_volume_mute]


class Listener:
    volume = '0'

    def __init__(self):
        pass

    def on_press(self, key: Union[keyboard.Key, keyboard.KeyCode]):
        if key not in MEDIA_KEY:
            return

        self.get_volume()
        self.notify_remote()

    def start(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def notify_remote(self):
        cmd = "ssh -i {0} root@192.168.1.100 'echo {1} > /home/hassio/homeassistant/mac_volume'".format(
            IDENTITY_FILE, self.volume)
        run(cmd, shell=True)

    def stop(self):
        pass

    def get_volume(self):
        cmd = ["/bin/sh", "/Users/rick/Git/script/bash/get_volume"]
        out = run(cmd, stdout=PIPE, universal_newlines=True).stdout.strip()
        self.volume = out


if __name__ == "__main__":
    listener = Listener()
    try:
        listener.get_volume()
        listener.notify_remote()
        listener.start()
    except KeyboardInterrupt:
        listener.stop()
        exit(1)
