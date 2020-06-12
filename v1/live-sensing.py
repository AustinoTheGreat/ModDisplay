import RPi.GPIO as GPIO
import time
from PIL import Image
from crop import main

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
    
GPIO.output(11, GPIO.HIGH)

GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    
    main(GPIO.input(19), GPIO.input(15))
    
    time.sleep(10)
    
    