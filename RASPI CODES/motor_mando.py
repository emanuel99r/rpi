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

en=23     #pwm motor2
en2=16
en3=18

GPIO.setup(en,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.setup(en3,GPIO.OUT)
GPIO.setup(pin5, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin11, GPIO.OUT)
GPIO.setup(pin13, GPIO.OUT)
GPIO.setup(pin19, GPIO.OUT)
GPIO.setup(pin21, GPIO.OUT)
GPIO.setup(pin29, GPIO.OUT)
GPIO.setup(pin31, GPIO.OUT)
p=GPIO.PWM(en,1000)
p2=GPIO.PWM(en2,1000)
p3=GPIO.PWM(en3,1000)



btn1 = 288
btn2 = 289
btn3 = 290
btn4 = 291
btnR1 = 293
btnR2 = 295
btnL1 = 292
btnL2 = 294
p.start(100)
p2.start(100)
p3.start(100)

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
                
            elif event.code == btn4:
                print("Presionaste 4")    
                p.ChangeDutyCycle(100)
                GPIO.output(pin13, GPIO.HIGH)
                
                
            elif event.code == btnR1:
                print("Presionaste R1")
                GPIO.output(pin19, GPIO.HIGH)
                GPIO.output(pin29, GPIO.HIGH)
                
            elif event.code == btnR2:
                print("Presionaste R2")    
                GPIO.output(pin21, GPIO.HIGH)
                GPIO.output(pin31, GPIO.HIGH)
                
            elif event.code == btnL1:
                print("Presionaste L1")
                p2.ChangeDutyCycle(99.85)
                p3.ChangeDutyCycle(100)
                GPIO.output(pin29, GPIO.HIGH)
                GPIO.output(pin21, GPIO.HIGH)
                
            elif event.code == btnL2:
                print("Presionaste L2")    
                p2.ChangeDutyCycle(99.93)
                p3.ChangeDutyCycle(100)
                GPIO.output(pin31, GPIO.HIGH)
                GPIO.output(pin19, GPIO.HIGH)
            
        if event.value == 0:
                
            if event.code == btn1:
                print("soltaste 1")
                GPIO.output(pin3, GPIO.LOW)
                
            elif event.code == btn2:
                print("soltaste 2")    
                GPIO.output(pin5, GPIO.LOW)
                
            elif event.code == btn3:
                print("soltaste 3")
                p.ChangeDutyCycle(20)
                GPIO.output(pin11, GPIO.LOW)
                GPIO.output(pin13, GPIO.HIGH)
                
            elif event.code == btn4:
                print("soltaste 4")
                p.ChangeDutyCycle(20)    
                GPIO.output(pin11, GPIO.LOW)
                GPIO.output(pin13, GPIO.HIGH)
                
            elif event.code == btnR1:
                print("soltaste R1")
                GPIO.output(pin19, GPIO.LOW)
                GPIO.output(pin29, GPIO.LOW)
                
            elif event.code == btnR2:
                print("soltaste R2")    
                GPIO.output(pin21, GPIO.LOW)
                GPIO.output(pin31, GPIO.LOW)
                
            elif event.code == btnL1:
                print("soltaste L1")
                GPIO.output(pin29, GPIO.LOW)
                GPIO.output(pin21, GPIO.LOW)
                
            elif event.code == btnL2:
                GPIO.output(pin31, GPIO.LOW)
                GPIO.output(pin19, GPIO.LOW)
                print("soltaste L2")
                        
            
