import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN)

while True:
    
    sensor = GPIO.input(11)
    if sensor == 1:
        print("Nothing is there")
        sleep(1)
    elif sensor == 0:
        print("Something is there....")
        sleep(1)