import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin_ms=36
pin=3
pinMAS=40
pinMENOS=38
pinMAS_2=10
pinMENOS_2=12

GPIO.setup(pin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_ms,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinMAS,GPIO.OUT)
GPIO.setup(pinMENOS,GPIO.OUT)
GPIO.setup(pinMAS_2,GPIO.OUT)
GPIO.setup(pinMENOS_2,GPIO.OUT)

contador=0
dato=0
datoanterior=0
flag=0
ms=0

posicion=0
try:
	print("HOMING...")
        GPIO.output(pinMAS,GPIO.HIGH)
        GPIO.output(pinMENOS,GPIO.LOW)
        while(True):
                ms=GPIO.input(pin_ms)
                if ms== 0:
                        print("Home")       
                        break
                flag=flag+1
                dato = GPIO.input(pin)
		if dato==1 and datoanterior==0:
                	contador=contador+1
			#print(contador)
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
			#print(contador)
			flag = contador
                datoanterior=dato
                
		time.sleep(0.0005)
		if contador>=74 :
                        print('LLego')
                        GPIO.output(pinMAS,GPIO.LOW)
                        GPIO.output(pinMENOS,GPIO.LOW)
                        break
                   
        for i in range(4):
            x = float(raw_input("angulo:"))
            if x>= 0:
                    GPIO.output(pinMAS,GPIO.HIGH)
                    GPIO.output(pinMENOS,GPIO.LOW)
                    num = (4900*x)/140
                    posicion=posicion+x
            elif x< 0 :
                    GPIO.output(pinMAS,GPIO.LOW)
                    GPIO.output(pinMENOS,GPIO.HIGH)
                    posicion=posicion+x    
                    num=(6200*x)/170
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

 #   GPIO.cleanup()
