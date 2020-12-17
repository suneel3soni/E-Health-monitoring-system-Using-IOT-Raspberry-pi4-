
#import RPi.GPIO as GPIO
import time
from time import sleep
import smbus
while True:
    def ultra_sonic():
        GPIO.setmode(GPIO.BOARD)

        TRIG = 16
        ECHO = 18
        i=0

        GPIO.setwarnings(False)
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)

        GPIO.output(TRIG, False)
        print ("Calibrating.....")
        time.sleep(2)

        print ("Place the object......")


        try:
            
               GPIO.setwarnings(False)
               GPIO.output(TRIG, True)
               time.sleep(0.00001)
               GPIO.output(TRIG, False)

               while GPIO.input(ECHO)==0:
                    pulse_start = time.time()

               while GPIO.input(ECHO)==1:
                  pulse_end = time.time()

               pulse_duration = pulse_end - pulse_start

               distance = pulse_duration * 17150

               distance = round(distance+1.15, 2)
 
               if distance<=20 and distance>=5:
                  print ("distance:",distance,"cm")
                  i=1
         
               if distance>20 and i==1:
                  print ("place the object....")
                  i=0
               time.sleep(2)

        except KeyboardInterrupt:
            pass
            #GPIO.cleanup()
    #ultra_sonic()





    def proximity():

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(11, GPIO.IN)

        #while True:
   
        sensor = GPIO.input(11)
        if sensor == 1:
            print("i seee 11111111111")
            sleep(0.1)
        elif sensor == 0:
            print("This was 0 in my code....")
   


#    proximity()
    def IR_temp():
        print("------------------")
 
        class MLX90614():

            MLX90614_RAWIR1=0x04
            MLX90614_RAWIR2=0x05
            MLX90614_TA=0x06
            MLX90614_TOBJ1=0x07
            MLX90614_TOBJ2=0x08
 
            MLX90614_TOMAX=0x20
            MLX90614_TOMIN=0x21
            MLX90614_PWMCTRL=0x22
            MLX90614_TARANGE=0x23
            MLX90614_EMISS=0x24
            MLX90614_CONFIG=0x25
            MLX90614_ADDR=0x0E
            MLX90614_ID1=0x3C
            MLX90614_ID2=0x3D
            MLX90614_ID3=0x3E
            MLX90614_ID4=0x3F
 
            def __init__(self, address=0x5a, bus_num=1):
                self.bus_num = bus_num
                self.address = address
                self.bus = smbus.SMBus(bus=bus_num)
 
            def read_reg(self, reg_addr):
                return self.bus.read_word_data(self.address, reg_addr)
 
            def data_to_temp(self, data):
                temp = (data*0.02) - 273.15
                return temp
 
            def get_amb_temp(self):
                data = self.read_reg(self.MLX90614_TA)
                return self.data_to_temp(data)
 
            def get_obj_temp(self):
                data = self.read_reg(self.MLX90614_TOBJ1)
                return self.data_to_temp(data)
 
           # IR_temp()



#import RPi.GPIO as GPIO
#import time

    def relay_moter():
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
    #  relay_moter()


    if __name__ == "__main__":
            ultra_sonic()
            proximity()
            relay_moter()
            sensor = MLX90614()
            print(sensor.get_amb_temp())
            print(sensor.get_obj_temp())
