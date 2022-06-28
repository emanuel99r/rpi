import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pinMAS_1 = 3
pinMENOS_1 = 5
GPIO.setup(pinMAS_1,GPIO.OUT)
GPIO.setup(pinMENOS_1,GPIO.OUT)


A_pin = 31
B_pin = 29
GPIO.setup(A_pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(B_pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	
	outcome = [0,1,-1,0,-1,0,0,1,1,0,0,-1,0,-1,1,0]
	last_AB = 0b00
	counter = 0
	
	sent = str(input("SENTIDO:"))
	if sent == "cw":
		GPIO.output(pinMAS_1,GPIO.HIGH)
		GPIO.output(pinMENOS_1,GPIO.LOW)
	elif sent == "ccw":
		GPIO.output(pinMAS_1,GPIO.LOW)
		GPIO.output(pinMENOS_1,GPIO.HIGH)
	
	while True:
		A = GPIO.input(A_pin)
		B = GPIO.input(B_pin)
		current_AB = (A << 1) | B
		position = (last_AB << 2) | current_AB
		counter += outcome[position]
		last_AB = current_AB
		#print(counter)
except KeyboardInterrupt:
	GPIO.output(pinMAS_1,GPIO.LOW)
	GPIO.output(pinMENOS_1,GPIO.LOW)
	GPIO.cleanup()
