from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#button code variables (change to suit your device)
pin3=3
pin5=5
pin11=11
pin13=13
pin19=19
pin21=21
pin29=29
pin31=31
pin33=33
pin35=35
pin38=38
pin40=40

GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin5, GPIO.OUT)
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


GPIO.setup(pin3, GPIO.OUT)
p=GPIO.PWM(pin3,1000)
p.start(0)



btn1 = 288
btn2 = 289
btn3 = 290
btn4 = 291
btnR1 = 293
btnR2 = 295
btnL1 = 292
btnL2 = 294

k = 0

#prints out device info at start
print(gamepad)

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == btnL1:
                print("Presionaste L1")
                for event in gamepad.read_loop():
                    if event.type == ecodes.EV_KEY:
                       if event.value == 1:
                            
                            if event.code == btn1:
                                print("L1+1 --- Gira la Pinza Sentido Horario")
                                GPIO.output(pin11, GPIO.HIGH)#Motor 4
                                GPIO.output(pin13, GPIO.LOW)
                                GPIO.output(pin19, GPIO.HIGH)#Motor 5
                                GPIO.output(pin21, GPIO.LOW)
                        

                       if event.value == 0:
                            if event.code == btnL1:
                                print("soltaste L1")
                                break
