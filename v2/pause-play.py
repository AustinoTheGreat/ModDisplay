import time

from time import time, sleep

from omxplayer.player import OMXPlayer as omxplayer

video_path = '/home/pi/ftp/files/cropped_video10.mp4'

player = omxplayer(video_path)

player.play()

print(player.duration())


def pause():

    player.pause()

    current_time = player.position() # as a percentage of the length of the video

    print(current_time)
    
    return (current_time)


def play (current_time):
    
    player.seek(current_time)

    player.play()

sleep(2)
    
current_time = pause()

sleep(2)

play(current_time)

player.quit()

# player.toggle_fullscreen can be used to switch between full screen and window size 
