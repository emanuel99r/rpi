import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Asignacion Pines

pinMAS_5 = 38
pinMENOS_5 = 40


GPIO.setup(pinMAS_5,GPIO.OUT)
GPIO.setup(pinMENOS_5,GPIO.OUT)

try:
	GPIO.output(pinMAS_5,GPIO.LOW)
	GPIO.output(pinMENOS_5,GPIO.LOW)

	while True:
		sent = str(raw_input("SENTIDO:"))
		if sent == "cw":
			GPIO.output(pinMAS_5,GPIO.HIGH)
			GPIO.output(pinMENOS_5,GPIO.LOW)
		elif sent == "ccw":
			GPIO.output(pinMAS_5,GPIO.LOW)
			GPIO.output(pinMENOS_5,GPIO.HIGH)
		elif sent == "n":
			GPIO.output(pinMAS_5,GPIO.LOW)
			GPIO.output(pinMENOS_5,GPIO.LOW)


except KeyboardInterrupt:
	GPIO.output(pinMAS_5,GPIO.LOW)
	GPIO.output(pinMENOS_5,GPIO.LOW)
	GPIO.cleanup()
