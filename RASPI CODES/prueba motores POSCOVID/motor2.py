import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Asignacion Pines

pinMAS_2 = 7
pinMENOS_2 = 11


GPIO.setup(pinMAS_2,GPIO.OUT)
GPIO.setup(pinMENOS_2,GPIO.OUT)

try:
	GPIO.output(pinMAS_2,GPIO.LOW)
	GPIO.output(pinMENOS_2,GPIO.LOW)

	while True:
		sent = str(raw_input("SENTIDO:"))
		if sent == "cw":
			GPIO.output(pinMAS_2,GPIO.HIGH)
			GPIO.output(pinMENOS_2,GPIO.LOW)
		elif sent == "ccw":
			GPIO.output(pinMAS_2,GPIO.LOW)
			GPIO.output(pinMENOS_2,GPIO.HIGH)
		elif sent == "n":
			GPIO.output(pinMAS_2,GPIO.LOW)
			GPIO.output(pinMENOS_2,GPIO.LOW)


except KeyboardInterrupt:
	GPIO.output(pinMAS_2,GPIO.LOW)
	GPIO.output(pinMENOS_2,GPIO.LOW)
	GPIO.cleanup()
