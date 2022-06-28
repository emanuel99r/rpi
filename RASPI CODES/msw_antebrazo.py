import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin_ms=31
pin=8
pinMAS=22
pinMENOS=26
en2=18


GPIO.setup(pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_ms,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(en2,GPIO.OUT)
GPIO.setup(pinMAS,GPIO.OUT)
GPIO.setup(pinMENOS,GPIO.OUT)
p2=GPIO.PWM(en2,1000)
p2.start(100)

contador=0
dato=0
datoanterior=0
flag=0
ms=0

posicion=0
try:
    print("HOMING...")
    p2.ChangeDutyCycle(100)
    GPIO.output(pinMAS,GPIO.HIGH)
    GPIO.output(pinMENOS,GPIO.LOW)
    ms=GPIO.input(pin_ms)
    if ms== 0:
        print("Home")       
        GPIO.output(pinMAS,GPIO.LOW)
        GPIO.output(pinMENOS,GPIO.LOW)            
    else:
        while(True):
            ms=GPIO.input(pin_ms)
            if ms== 0:
                print("Home")       
                break
            flag=flag+1
            dato = GPIO.input(pin)
            if dato==1 and datoanterior==0:
                contador=contador+1
                print(contador)
                flag = contador
            datoanterior=dato
                
            time.sleep(0.0005)

            if flag>contador+100:
                    #print('detenido')
                    contador=0
                    datoanterior=0                        
                    GPIO.output(pinMAS,GPIO.LOW)
                    GPIO.output(pinMENOS,GPIO.HIGH)
                    
    flag=0
    contador=0
    datoanterior=0         
            
    while True:
        flag=flag+1
        dato = GPIO.input(pin)
        if dato==1 and datoanterior==0:
            contador=contador+1
            print(contador)
            flag = contador
        datoanterior=dato
                
        time.sleep(0.0005)
        if contador>=300 :
            print('LLego')
            GPIO.output(pinMAS,GPIO.LOW)
            GPIO.output(pinMENOS,GPIO.LOW)
            break
           
    for i in range(4):
        x = float(raw_input("angulo:"))
        if x>= 0:
                GPIO.output(pinMAS,GPIO.HIGH)
                GPIO.output(pinMENOS,GPIO.LOW)
                num = (1617*x)/80
                posicion=posicion+x
        elif x< 0 :
                GPIO.output(pinMAS,GPIO.LOW)
                GPIO.output(pinMENOS,GPIO.HIGH)
                posicion=posicion+x    
                num=(4842*x)/180
        print(posicion)
        flag=0
        contador=0
        datoanterior=0 
        while(True):
                    
                flag=flag+1
                dato = GPIO.input(pin)
                if dato==1 and datoanterior==0:
                        contador=contador+1
                        #print(contador)
                        flag = contador
                datoanterior=dato
                time.sleep(0.0005)
                if contador>=abs(num)-10 :
                        print('LLego')
                        GPIO.output(pinMAS,GPIO.LOW)
                        GPIO.output(pinMENOS,GPIO.LOW)
                        break
                if flag>contador+100:
                        print('detenido')
                        GPIO.output(pinMAS,GPIO.LOW)
                        GPIO.output(pinMENOS,GPIO.LOW)
                        break                


except KeyboardInterrupt:
        GPIO.output(pinMAS,GPIO.LOW)
        GPIO.output(pinMENOS,GPIO.LOW)
