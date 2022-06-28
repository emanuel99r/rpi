import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Asignacion Pines

pinMAS_3 = 12
pinMENOS_3 = 16



GPIO.setup(pinMAS_3,GPIO.OUT)
GPIO.setup(pinMENOS_3,GPIO.OUT)

try:
	GPIO.output(pinMAS_3,GPIO.LOW)
	GPIO.output(pinMENOS_3,GPIO.LOW)

	while True:
		sent = str(raw_input("SENTIDO:"))
		if sent == "cw":
			GPIO.output(pinMAS_3,GPIO.HIGH)
			GPIO.output(pinMENOS_3,GPIO.LOW)
		elif sent == "ccw":
			GPIO.output(pinMAS_3,GPIO.LOW)
			GPIO.output(pinMENOS_3,GPIO.HIGH)
		elif sent == "c":
			GPIO.output(pinMAS_3,GPIO.LOW)
			GPIO.output(pinMENOS_3,GPIO.LOW)


except KeyboardInterrupt:
	GPIO.output(pinMAS_3,GPIO.LOW)
	GPIO.output(pinMENOS_3,GPIO.LOW)
	GPIO.cleanup()
