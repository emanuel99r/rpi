import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Asignacion Pines

pinMAS_4 = 18
pinMENOS_4 = 22


GPIO.setup(pinMAS_4,GPIO.OUT)
GPIO.setup(pinMENOS_4,GPIO.OUT)

try:
	GPIO.output(pinMAS_4,GPIO.LOW)
	GPIO.output(pinMENOS_4,GPIO.LOW)

	while True:
		sent = str(raw_input("SENTIDO:"))
		if sent == "cw":
			GPIO.output(pinMAS_4,GPIO.HIGH)
			GPIO.output(pinMENOS_4,GPIO.LOW)
		elif sent == "ccw":
			GPIO.output(pinMAS_4,GPIO.LOW)
			GPIO.output(pinMENOS_4,GPIO.HIGH)
		elif sent == "n":
			GPIO.output(pinMAS_4,GPIO.LOW)
			GPIO.output(pinMENOS_4,GPIO.LOW)


except KeyboardInterrupt:
	GPIO.output(pinMAS_4,GPIO.LOW)
	GPIO.output(pinMENOS_4,GPIO.LOW)
	GPIO.cleanup()
