import RPi.GPIO as GPIO
from time import sleep
import RPi.GPIO as GPIO
import time

while True:
    
    def proximity():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.IN)
        while True:
            sensor = GPIO.input(11)
            if sensor == 1:
                print("Keep your hand again....")
                sleep(1)
            elif sensor == 0:
                print("Thankyou Visit again")
                sleep(1)
        
        
    def relay():

        channel = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel, GPIO.OUT)

        def moter_on(pin):
            GPIO.output(pin, GPIO.HIGH)
    
    
        def moter_off(pin):
            GPIO.output(pin, GPIO.LOW)
    
        if __name__ == '__main__':
            proximity()
            relay()
            try:
                moter_on(channel)
                time.sleep(0.05)
                moter_off(channel)
                time.sleep(0.05)
                GPIO.cleanup()
            except KeyboardInterrupt:
                GPIO.cleanup()
                pass