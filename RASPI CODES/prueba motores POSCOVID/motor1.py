import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Asignacion Pines


pinMAS_1 = 3
pinMENOS_1 = 5



GPIO.setup(pinMAS_1,GPIO.OUT)
GPIO.setup(pinMENOS_1,GPIO.OUT)


try:
	GPIO.output(pinMAS_1,GPIO.LOW)
	GPIO.output(pinMENOS_1,GPIO.LOW)

	while True:
		sent = str(input("SENTIDO:"))
		if sent == "cw":
			GPIO.output(pinMAS_1,GPIO.HIGH)
			GPIO.output(pinMENOS_1,GPIO.LOW)
		elif sent == "ccw":
			GPIO.output(pinMAS_1,GPIO.LOW)
			GPIO.output(pinMENOS_1,GPIO.HIGH)
		elif sent == "n":
			GPIO.output(pinMAS_1,GPIO.LOW)
			GPIO.output(pinMENOS_1,GPIO.LOW)


except KeyboardInterrupt:
	GPIO.output(pinMAS_1,GPIO.LOW)
	GPIO.output(pinMENOS_1,GPIO.LOW)
	GPIO.cleanup()
