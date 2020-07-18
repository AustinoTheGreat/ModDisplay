from subprocess import Popen, check_call
import os
import time

rc = Popen("DISPLAY=:0 chromium 'file:///home/pi/ftp/files/image.jpg' --kiosk", shell = True)
# rc = Popen("start http://www.facebook.com/")
time.sleep(10)
print("hello")

Popen("killall -KILL chromium", shell = True)

print("hello")
