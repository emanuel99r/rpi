import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#pinMAS_1=5
#pinMENOS_1=7
pin_enc_1=35

GPIO.setup(pinMAS_1,GPIO.OUT)
GPIO.setup(pinMENOS_1,GPIO.OUT)
GPIO.setup(pin_enc_1,GPIO.IN)
#GPIO.setup(pin_enc_1,GPIO.IN, pull_up_down=GPIO.PUD_UP)

x=int(input("Valor"))
acum=0
dato=0
datoanterior=0
try:  
	while True:

		if x>= 0:
			GPIO.output(pinMAS_1,GPIO.HIGH)
		elif x < 0 :
			GPIO.output(pinMENOS_1,GPIO.HIGH)
		time.sleep(0.5)    
		dato = GPIO.input(pin_enc_1)
		if dato==1:
			acum=acum+1
			print(acum)
		datoanterior=dato
		GPIO.output(pinMAS_1,GPIO.LOW)
		GPIO.output(pinMENOS_1,GPIO.LOW)
		time.sleep(0.5)
		if acum==abs(x):
			print("Llego")
			break 
except KeyboardInterrupt:
        GPIO.output(pinMAS_1,GPIO.LOW)
        GPIO.output(pinMENOS_1,GPIO.LOW)		
