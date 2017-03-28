#!/usr/bin/python3
## me@danielpeluso.com
#
import subprocess

for ping in range(1,10):
    address = "192.168.24." + str(ping)
    res = subprocess.call(['ping', '-c', '3', address])
    if res == 0:
        print ("ping to", address, "OK")
    elif res == 2:
        print ("no response from", address)
    else:
        print ("ping to", address, "failed!")
