# Automount_usb_linux
Auto mount inspection USB stick

Add this to the system autorun (crontab or systemd) at startup, 

The script starts to monitor /dev/sd*, when USB is detected it will mount in DEFAULT_PATH_MOUNT_USB

I use this on Raspberry PI, it might come in handy for someone.
