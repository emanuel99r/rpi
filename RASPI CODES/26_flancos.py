import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin_1 = 11
pinMAS_1 = 40
pinMENOS_1 = 38
pin_2 = 3
pinMAS_2 = 33
pinMENOS_2 = 35

GPIO.setup(pin_1,GPIO.IN)
GPIO.setup(pinMAS_1,GPIO.OUT)
GPIO.setup(pinMENOS_1,GPIO.OUT)
GPIO.setup(pin_2,GPIO.IN)
GPIO.setup(pinMAS_2,GPIO.OUT)
GPIO.setup(pinMENOS_2,GPIO.OUT)

contador=0
dato=0
datoanterior=0
flag=0
try:
        #op = str(raw_input("OPCION:"))
	x = float(raw_input("angulo:"))
	y = float(raw_input("angulo:"))



	if x>= 0:
                GPIO.output(pinMAS_1,GPIO.HIGH)
                GPIO.output(pinMENOS_1,GPIO.LOW)
                num_1 = (11058*x)/310        
	elif x< 0 :
        	GPIO.output(pinMAS_1,GPIO.LOW)
                GPIO.output(pinMENOS_1,GPIO.HIGH)
                num_1=(11065*x)/310

        

        contador=0
        dato=0
        datoanterior=0
        while(True):
                #flag=flag+1
                dato = GPIO.input(pin_1)
		if dato==1 and datoanterior==0:
                	contador=contador+1
			print(contador)
			flag = contador
		datoanterior=dato
			#time.sleep(0.0005)
		if contador>=abs(num_1)-1 :
                        print('LLego')
                        GPIO.output(pinMAS_1,GPIO.LOW)
                        GPIO.output(pinMENOS_1,GPIO.LOW)

                        break

		#if flag>contador+100000:
                 #       print('detenido')
                  #      GPIO.output(pinMAS,GPIO.LOW)
                   #     GPIO.output(pinMENOS,GPIO.LOW)
                    #    break
                    

	if y>= 0:
                GPIO.output(pinMAS_2,GPIO.HIGH)
                GPIO.output(pinMENOS_2,GPIO.LOW)
                num_2 = (4545*y)/165        
	elif y< 0 :
        	GPIO.output(pinMAS_2,GPIO.LOW)
                GPIO.output(pinMENOS_2,GPIO.HIGH)
                num_2=(4545*y)/165


        contador=0
        dato=0
        datoanterior=0
        while(True):
                #flag=flag+1
                dato = GPIO.input(pin_2)
		if dato==1 and datoanterior==0:
                	contador=contador+1
			print(contador)
			flag = contador
		datoanterior=dato
			#time.sleep(0.0005)
		if contador>=abs(num_2)-1 :
                        print('LLego')
                        GPIO.output(pinMAS_2,GPIO.LOW)
                        GPIO.output(pinMENOS_2,GPIO.LOW)
                        break


except KeyboardInterrupt:
        GPIO.output(pinMAS_1,GPIO.LOW)
        GPIO.output(pinMENOS_1,GPIO.LOW)
        GPIO.output(pinMAS_2,GPIO.LOW)
        GPIO.output(pinMENOS_2,GPIO.LOW)
 #   GPIO.cleanup()
