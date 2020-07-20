import time

from time import time, sleep

import vlc # pip install python-vlc 

player = vlc.MediaPlayer('/home/pi/ftp/files/cropped_video10.mp4')

player.play()

sleep(2)

print(player.get_length())


def pause():

    player.pause()

    current_time = player.get_time() # as a percentage of the length of the video

    print(current_time)
    
    return (current_time)


def play (current_time):
    
    player.set_time(current_time)

    player.play()


current_time = pause()

sleep(5)

play(current_time)


# player.toggle_fullscreen can be used to switch between full screen and window size 