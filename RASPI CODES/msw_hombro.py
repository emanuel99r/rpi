import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


pin=5
pinMAS=19
pinMENOS=21
en2=15

GPIO.setup(pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(en2,GPIO.OUT)
GPIO.setup(pinMAS,GPIO.OUT)
GPIO.setup(pinMENOS,GPIO.OUT)
p2=GPIO.PWM(en2,1000)
p2.start(100)

contador=0
dato=0
datoanterior=0
flag=0
posicion=0
try:
    print("HOMING...")
    p2.ChangeDutyCycle(100)
    GPIO.output(pinMAS,GPIO.HIGH)
    GPIO.output(pinMENOS,GPIO.LOW)
        
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
        if flag>contador+100:
            print('HOME')
            GPIO.output(pinMAS,GPIO.LOW)
            GPIO.output(pinMENOS,GPIO.LOW)
            break
                
                        
    for i in range(4):
        x = float(raw_input("angulo:"))
        if x>= 0:
                p2.ChangeDutyCycle(100)
                GPIO.output(pinMAS,GPIO.HIGH)
                GPIO.output(pinMENOS,GPIO.LOW)
                num = (4169*x)/165
                posicion=posicion+x
        elif x< 0 :
                p2.ChangeDutyCycle(100)
                GPIO.output(pinMAS,GPIO.LOW)
                GPIO.output(pinMENOS,GPIO.HIGH)
                posicion=posicion+x    
                num=(4000*x)/165
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
                if contador>=abs(num)-5 :
                        print('LLego')
                        if posicion<-40:
                            p2.ChangeDutyCycle(30)
                            GPIO.output(pinMAS,GPIO.HIGH)
                            GPIO.output(pinMENOS,GPIO.LOW)
                            break
                        elif posicion>-40:
                            p2.ChangeDutyCycle(30)
                            GPIO.output(pinMAS,GPIO.LOW)
                            GPIO.output(pinMENOS,GPIO.HIGH)
                            break
                        elif posicion==-40:
                            GPIO.output(pinMAS,GPIO.LOW)
                            GPIO.output(pinMENOS,GPIO.LOW)
                            break
                if flag>contador+100:
                        print('detenido')
                        GPIO.output(pinMAS,GPIO.LOW)
                        GPIO.output(pinMENOS,GPIO.LOW)
                        break                
    GPIO.output(pinMAS,GPIO.LOW)
    GPIO.output(pinMENOS,GPIO.LOW)
            

except KeyboardInterrupt:
    GPIO.output(pinMAS,GPIO.LOW)
    GPIO.output(pinMENOS,GPIO.LOW)

 #   GPIO.cleanup()
