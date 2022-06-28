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

GPIO.output(pin11, GPIO.LOW)
GPIO.output(pin13, GPIO.LOW)
GPIO.output(pin19, GPIO.LOW)
GPIO.output(pin21, GPIO.LOW)
GPIO.output(pin29, GPIO.LOW)
GPIO.output(pin29, GPIO.LOW)
GPIO.output(pin29, GPIO.LOW)
GPIO.output(pin29, GPIO.LOW)






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
                            
                       
                                      
                            if event.code == btnR1:
                                print("L1+R1 --- Sube el Brazo")
                                GPIO.output(pin11, GPIO.HIGH)#Motor 2
                                GPIO.output(pin13, GPIO.LOW)                                        
                            elif event.code == btnR2:
                                print("L1+R2 --- Sube el Antebrazo")    
                                GPIO.output(pin19, GPIO.HIGH)#Motor 3
                                GPIO.output(pin21, GPIO.LOW)    


                        elif event.value == 0:
                            if event.code == btnL1:
                                print("soltaste L1")
                                break
                        
                            elif event.code == btnR1:
                                print("L1+R1 --- Sube el Brazo")
                                GPIO.output(pin11, GPIO.LOW)#Motor 2
                                GPIO.output(pin13, GPIO.LOW)                                        
                            elif event.code == btnR2:
                                print("L1+R2 --- Sube el Antebrazo")    
                                GPIO.output(pin19, GPIO.LOW)#Motor 3
                                GPIO.output(pin21, GPIO.LOW)
            if event.code == btnL2:
                print("Presionaste L2")
                for event in gamepad.read_loop():
                    if event.type == ecodes.EV_KEY:
                        if event.value == 1:
                            
                        
                                    
                            if event.code == btnR1:
                                print("L2+R1 --- Baja el Brazo")
                                GPIO.output(pin11, GPIO.LOW)#Motor 2
                                GPIO.output(pin13, GPIO.HIGH)                                        
                            elif event.code == btnR2:
                                print("L2+R2 --- Baja el Antebrazo")    
                                GPIO.output(pin19, GPIO.LOW)#Motor 3
                                GPIO.output(pin21, GPIO.HIGH)    


                        elif event.value == 0:
                            if event.code == btnL2:
                                break
                            elif event.code == btnR1:
                                print("L1+R1 --- Sube el Brazo")
                                GPIO.output(pin11, GPIO.LOW)#Motor 2
                                GPIO.output(pin13, GPIO.LOW)                                        
                            elif event.code == btnR2:
                                print("L1+R2 --- Sube el Antebrazo")    
                                GPIO.output(pin19, GPIO.LOW)#Motor 3
                                GPIO.output(pin21, GPIO.LOW)
                            
                            
