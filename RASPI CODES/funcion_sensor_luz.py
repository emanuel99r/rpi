import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def sensor(motor,veces):
	contador=0
	acum=0
	if motor==1:
		ENC_MOTOR=3
		PIN_MOTOR = 7
		umbral=5.4
	GPIO.setup(PIN_MOTOR,GPIO.OUT)
	GPIO.setup(ENC_MOTOR, GPIO.OUT)
	GPIO.output(ENC_MOTOR, GPIO.LOW)
	time.sleep(1)
	while True:
		contador+=1
		GPIO.setup(ENC_MOTOR, GPIO.OUT)
		GPIO.output(ENC_MOTOR, GPIO.LOW)
		time.sleep(0.1)
		GPIO.output(PIN_MOTOR, GPIO.HIGH)
		GPIO.setup(ENC_MOTOR, GPIO.IN)
		currentTime = time.time()
		diff = 0
		while(GPIO.input(ENC_MOTOR) == GPIO.LOW):
			diff  = time.time() - currentTime
		x=diff * 1000    
		if x<umbral:
			acum+=1
        	print(x)
        	time.sleep(1)
        	GPIO.output(PIN_MOTOR, GPIO.LOW)
        	time.sleep(1)
        	if contador == veces:
			break
	return acum            
try:
    z = int(input("Digite:"))
    n=sensor(1,z)
    print("Encendido "+str(n)+" veces")
except KeyboardInterrupt:
	GPIO.output(PIN_MOTOR,GPIO.LOW)
