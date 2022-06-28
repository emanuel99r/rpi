from evdev import  categorize, ecodes
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
pin=11
pinMAS=40
pinMENOS=38

GPIO.setup(pin,GPIO.IN)

GPIO.setup(pinMAS,GPIO.OUT)
GPIO.setup(pinMENOS,GPIO.OUT)


try:
    GPIO.output(pinMAS,GPIO.LOW)
    GPIO.output(pinMENOS,GPIO.LOW)


    op = str(raw_input("OPCION:")) 
    x = int(raw_input("angulo:"))
    if op == "CW":
        GPIO.output(pinMAS,GPIO.HIGH)
        GPIO.output(pinMENOS,GPIO.LOW)
        num = (480*x)/130 
    elif op == "CCW":
        GPIO.output(pinMAS,GPIO.LOW)
        GPIO.output(pinMENOS,GPIO.HIGH)
        num = (480*x)/130
    k = 0
    
    while (True):
        #while(True):
        lec = GPIO.input(pin)
        if lec == 1:
            k = k+1
            print(k)
        time.sleep(0.01)
        if k >= num:
            print("Llego a su poscion")
            GPIO.output(pinMAS,GPIO.LOW)
            GPIO.output(pinMENOS,GPIO.LOW)
            break           
except KeyboardInterrupt:
    GPIO.cleanup()


