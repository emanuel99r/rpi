import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
pinMAS_1=7
resistorPin = 3
GPIO.setup(pinMAS_1,GPIO.OUT)

GPIO.setup(resistorPin, GPIO.OUT)
GPIO.output(resistorPin, GPIO.LOW)
time.sleep(1)
try:
    valor = int(input("Digite:"))
    contador=0
    c=0
    while True:
        contador+=1
        GPIO.setup(resistorPin, GPIO.OUT)
        GPIO.output(resistorPin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(pinMAS_1, GPIO.HIGH)
        GPIO.setup(resistorPin, GPIO.IN)
        currentTime = time.time()
        diff = 0
        while(GPIO.input(resistorPin) == GPIO.LOW):
            diff  = time.time() - currentTime
        x=diff * 1000    
        if x<5.4:
            c+=1
        print(x)
        time.sleep(1)
        GPIO.output(pinMAS_1, GPIO.LOW)
        time.sleep(1)
        if contador == valor:
            print("Encendido "+str(c)+" veces")
            break
except KeyboardInterrupt:
	GPIO.output(pinMAS_1,GPIO.LOW)
