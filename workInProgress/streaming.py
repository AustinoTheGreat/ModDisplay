 
 
from subprocess import Popen, check_call
import os
import time
import keyboard


# rc = Popen("DISPLAY=:0 chromium 'file:///home/pi/ftp/files/image.jpg' --kiosk", shell = True)

# rc = Popen("streamlink -p omxplayer --timeout 20 --player-fifo https://www.youtube.com/watch?v=MCkTebktHVc 720p", shell = True)
global rc
global current_time

exit = False
def stream(x1, y1, x2, y2, link):

#     rc = Popen("streamlink -p 'omxplayer --timemout 20" + " --crop " + str(x1) + "," + str(y1) + ',' + str(x2) + "," + str(y2) + "' --player-fifo https://www.youtube.com/watch?v=MCkTebktHVc 720p", shell = True)
    
     
    rc = Popen("streamlink -p 'omxplayer --timeout 20 --crop " + str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2) + "' --player-fifo " + link + " 720p", shell = True)
    
#     rc = subprocess.Popen("exec streamlink -p 'omxplayer --timeout 20 --crop " + str(x1) + "," + str(y1) + "," + str(x2) + "," + str(y2) + "' --player-fifo " + link + " 720p", stdout=subprocess.PIPE, shell =True)    

    current_time = time.time()
    
    print("hello")

stream(0,0,1280,480, 'https://www.youtube.com/watch?v=MCkTebktHVc')

# while (keyboard.is_pressed('a') == False):
#     x = x + 1
while (exit == False):
    
    if (time.time() - current_time > 15):
        
        exit = True

Popen("killall -s 9 omxplayer.bin", shell = True)

time.sleep(10)
    


print("hello")

# dim of stream

# height = 720
# width = 1280
