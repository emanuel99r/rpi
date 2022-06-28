import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Asignacion Pines

pinMAS_6 = 32
pinMENOS_6 = 36


GPIO.setup(pinMAS_6,GPIO.OUT)
GPIO.setup(pinMENOS_6,GPIO.OUT)

try:
	GPIO.output(pinMAS_6,GPIO.LOW)
	GPIO.output(pinMENOS_6,GPIO.LOW)

	while True:
		sent = str(raw_input("SENTIDO:"))
		if sent == "cw":
			GPIO.output(pinMAS_6,GPIO.HIGH)
			GPIO.output(pinMENOS_6,GPIO.LOW)
		elif sent == "ccw":
			GPIO.output(pinMAS_6,GPIO.LOW)
			GPIO.output(pinMENOS_6,GPIO.HIGH)
		elif sent == "n":
			GPIO.output(pinMAS_6,GPIO.LOW)
			GPIO.output(pinMENOS_6,GPIO.LOW)


except KeyboardInterrupt:
	#GPIO.output(pinMAS_6,GPIO.LOW)
	#GPIO.output(pinMENOS_6,GPIO.LOW)
	GPIO.cleanup()
