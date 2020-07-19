import subprocess
import sys

def main(library_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])

main(paho-mqtt)
main(keyboard)
main(mpu6050-raspberrypi)
main(gpiozero)
main(python-opencv)


