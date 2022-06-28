import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
#pin_to_circuit = 37
pinMAS_1=5
pinMENOS_1=7
pin_enc_1=37

GPIO.setup(pinMAS_1,GPIO.OUT)
GPIO.setup(pinMENOS_1,GPIO.OUT)




def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_enc_1, GPIO.OUT)
    GPIO.output(pin_enc_1, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_enc_1, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_enc_1) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interrupted, cleanup correctly
try:
	# Main loop
	x = int(input("Valor:"))
	contador=0
	while (True):
		if x>= 0:
			GPIO.output(pinMAS_1,GPIO.HIGH)
		elif x < 0 :
			GPIO.output(pinMENOS_1,GPIO.HIGH)
		time.sleep(0.5)  		
 		while True:	
			print rc_time(pin_enc_1)
			if rc_time(pin_enc_1)>0:
				print("HIGH")
				
			elif rc_time(pin_enc_1)<=0:
				print("LOW")
			break
		GPIO.output(pinMAS_1,GPIO.LOW)
		GPIO.output(pinMENOS_1,GPIO.LOW)		
		time.sleep(0.5)
		contador += 1
		if contador == abs(x):
			break
		 	
except KeyboardInterrupt:
	GPIO.output(pinMAS_1,GPIO.LOW)
	GPIO.output(pinMENOS_1,GPIO.LOW)
