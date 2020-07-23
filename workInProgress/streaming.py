 
from subprocess import Popen, check_call
import os
import time
import keyboard


# rc = Popen("DISPLAY=:0 chromium 'file:///home/pi/ftp/files/image.jpg' --kiosk", shell = True)

# rc = Popen("streamlink -p omxplayer --timeout 20 --player-fifo https://www.youtube.com/watch?v=MCkTebktHVc 720p", shell = True)

def stream(x1, y1, x2, y2):

#     rc = Popen("streamlink -p 'omxplayer --timemout 20" + " --crop " + str(x1) + "," + str(y1) + ',' + str(x2) + "," + str(y2) + "' --player-fifo https://www.youtube.com/watch?v=MCkTebktHVc 720p", shell = True)
    
     
    rc = Popen("streamlink -p 'omxplayer --timeout 20 --crop " + str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2) + "' --player-fifo https://www.youtube.com/watch?v=MCkTebktHVc 720p", shell = True)
    
#     time.sleep(20)

    print("hello")

    if (keyboard.is_pressed('ctrl+space') == True):
        
        Popen("killall -s 9 omxplayer.bin", shell = True)

    print("hello")
        
    


stream(0,0,1280,480)

exit()

# dim of stream

# height = 720
# width = 1280

