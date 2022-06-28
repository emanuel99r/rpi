#from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
pin=29
pinMAS=3
pinMENOS=5

#GPIO.setup(pin,GPIO.IN)
GPIO.setup(pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(pinMAS,GPIO.OUT)
GPIO.setup(pinMENOS,GPIO.OUT)


try:
    GPIO.output(pinMAS,GPIO.LOW)
    GPIO.output(pinMENOS,GPIO.LOW)


    op = str(raw_input("sentido:"))
    #x = int(raw_input("angulo:"))
    #num = (750*x)/310
    if op == "cw":
        GPIO.output(pinMAS,GPIO.HIGH)
        GPIO.output(pinMENOS,GPIO.LOW)
    elif op == "ccw":
        GPIO.output(pinMAS,GPIO.LOW)
        GPIO.output(pinMENOS,GPIO.HIGH)

    k = 0
    #flag = 0
    while (True):
        
        #flag = flag+1
        lec = GPIO.input(pin)
        if lec == 1:
            k = k+1
            print(k)
            #flag = k
        #time.sleep(0.01)
        '''
        if k >= num:
            print("Llego a su poscion")
            GPIO.output(pinMAS,GPIO.LOW)
            GPIO.output(pinMENOS,GPIO.LOW)
            break
        if flag >= k+100:
            print("Llego a un limite")
            GPIO.output(pinMAS,GPIO.LOW)
            GPIO.output(pinMENOS,GPIO.LOW)
            break
        '''                   
except KeyboardInterrupt:
    GPIO.cleanup()


