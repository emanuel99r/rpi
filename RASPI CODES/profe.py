from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#button code variables (change to suit your device)
pin3=3    #boton1, motor1
pin5=5    #boton2, motor1

pin11=11  #boton3, motor2
pin13=13  #boton4, motor2

pin19=19  #botonR1,motor3
pin21=21  #botonR2,motor3

pin29=29  #botonL1,motor4
pin31=31  #botonL2,motor4

pin33=33  #start, motor5
pin35=35  #select, motor5

pin38=38  #analogo derecho, motor6
pin40=40  #analogo izquierdo, motor6

en=23     #pwm motor2

GPIO.setup(en,GPIO.OUT)
GPIO.setup(pin5, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin11, GPIO.OUT)
GPIO.setup(pin13, GPIO.OUT)
GPIO.setup(pin19, GPIO.OUT)
GPIO.setup(pin21, GPIO.OUT)
GPIO.setup(pin29, GPIO.OUT)
GPIO.setup(pin31, GPIO.OUT)
GPIO.setup(pin33, GPIO.OUT)
GPIO.setup(pin35, GPIO.OUT)
GPIO.setup(pin38, GPIO.OUT)
GPIO.setup(pin40, GPIO.OUT)
p=GPIO.PWM(en,1000)

btn1 = 288
btn2 = 289
btn3 = 290
btn4 = 291
btnR1 = 293
btnR2 = 295
btnL1 = 292
btnL2 = 294
btnstart=297
btnselect=296
anaizq=298
anader=299
p.start(100)

#prints out device info at start
print(gamepad)

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
                
            if event.code == btn1:
                print("Presionaste 1")
                GPIO.output(pin3, GPIO.HIGH)
                
            elif event.code == btn2:
				GPIO.output(pin5, GPIO.HIGH)
				print("Presionaste 2")
                
                  
            elif event.code == btn3:
                print("Presionaste 3")
                p.ChangeDutyCycle(100)
                GPIO.output(pin11, GPIO.HIGH)
                GPIO.output(pin13, GPIO.LOW)
                
            elif event.code == btn4:
                print("Presionaste 4")    
                p.ChangeDutyCycle(100)
                GPIO.output(pin13, GPIO.HIGH)
                
            elif event.code == btnR1:
				GPIO.output(pin19, GPIO.HIGH)
				print("Presionaste R1")
                
                    
            elif event.code == btnR2:
				GPIO.output(pin21, GPIO.HIGH)
				print("Presionaste R2")
                       
            elif event.code == btnL1:
				GPIO.output(pin29, GPIO.HIGH)
				print("Presionaste L1")
                 
                
            elif event.code == btnL2:
				GPIO.output(pin31, GPIO.HIGH)
				print("Presionaste L2")
                
            elif event.code == btnstart:
				GPIO.output(pin33, GPIO.HIGH)
				print("Presionaste start")
                
                
            elif event.code == btnselect:
				GPIO.output(pin35, GPIO.HIGH)
				print("Presionaste select")
                  
                
            elif event.code == anader:
				GPIO.output(pin38, GPIO.HIGH)
				print("Presionaste analogo derecho")
                   
                       
            elif event.code == anaizq:
				GPIO.output(pin40, GPIO.HIGH)
				print("Presionaste analogo izq")
                      
                              
        if event.value == 0:
                
            if event.code == btn1:
                print("soltaste 1")
                GPIO.output(pin3, GPIO.LOW)
                
            elif event.code == btn2:
                print("soltaste 2")    
                GPIO.output(pin5, GPIO.LOW)
                
            elif event.code == btn3:
                print("soltaste 3")
                p.ChangeDutyCycle(30)
                GPIO.output(pin11, GPIO.LOW)
                GPIO.output(pin13, GPIO.HIGH)
                
            elif event.code == btn4:
                print("soltaste 4")
                p.ChangeDutyCycle(30)    
                GPIO.output(pin11, GPIO.LOW)
                GPIO.output(pin13, GPIO.HIGH)   
                
            elif event.code == btnR1:
				GPIO.output(pin19, GPIO.LOW)
				print("soltaste R1")
                
                    
            elif event.code == btnR2:
				GPIO.output(pin21, GPIO.LOW)
				print("Presionaste R2")
                 
                
            elif event.code == btnL1:
				GPIO.output(pin29, GPIO.LOW)
				print("soltaste L1")
                 
                
            elif event.code == btnL2:
				GPIO.output(pin31, GPIO.LOW)
				print("soltaste L2")
                
                
            elif event.code == btnstart:
				GPIO.output(pin33, GPIO.LOW)
				print("soltaste start")
                
                
            elif event.code == btnselect:
				GPIO.output(pin35, GPIO.LOW)
				print("soltaste select")
                  
                
            elif event.code == anader:
				GPIO.output(pin38, GPIO.LOW)
				print("soltaste analogo derecho")
                   
                       
            elif event.code == anaizq:
				GPIO.output(pin40, GPIO.LOW) 
				print("soltaste analogo izq")
                       
