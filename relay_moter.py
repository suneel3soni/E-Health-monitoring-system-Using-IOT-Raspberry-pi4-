import RPi.GPIO as GPIO
import time

channel = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def moter_on(pin):
    GPIO.output(pin, GPIO.HIGH)
    
    
def moter_off(pin):
    GPIO.output(pin, GPIO.LOW)
    
if __name__ == '__main__':
    try:
        moter_on(channel)
        time.sleep(0.05)
        moter_off(channel)
        time.sleep(0.05)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
        pass