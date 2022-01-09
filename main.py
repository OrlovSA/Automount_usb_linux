#!/bin/python3
import os
import subprocess
from time import sleep


DEFAULT_PATH_MOUNT_USB = '/opt/usb'
PATH_NAME = DEFAULT_PATH_MOUNT_USB.split('/')[-1]


def mount_check():
    resault = subprocess.check_output('lsblk -o mountpoint -lpn', shell = True).decode()
    return True if PATH_NAME in resault else False

def path_check():
    if not os.path.isdir(DEFAULT_PATH_MOUNT_USB):
        os.mkdir(DEFAULT_PATH_MOUNT_USB)

def automount():
    while True:
        if mount_check == False:
            out = subprocess.run(
                'ls /dev/sd*', 
                shell = True, 
                stdout=subprocess.PIPE,
                encoding='utf-8')
            result = out.stdout[-5:-1] if out.returncode != 2 else 'usb_out'

            if 'sd' in result and '/' not in result:
                path_check()
                subprocess.run(f'sudo mount /dev/{result} {DEFAULT_PATH_MOUNT_USB}', shell = True) 
                sleep(5)
        sleep(1)

        
if __name__ == "__main__":
    automount()
