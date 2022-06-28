import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin=11
pinMAS=40
pinMENOS=38

GPIO.setup(pin,GPIO.IN)
GPIO.setup(pinMAS,GPIO.OUT)
GPIO.setup(pinMENOS,GPIO.OUT)

contador=0
dato=0
datoanterior=0

j = 0

try:
        #op = str(raw_input("OPCION:"))
	#x = float(raw_input("angulo:"))
    	n = int(input("Digite Cantidad de Movimientos:"))
        mov = []
        for i in range(1,n+1):
            mov.append(int(input("Digite movimiento numero %d:"%(i))))	



        

        #while(True):
               
        for grados in mov:
                #time.sleep(0.00000000000000000000000001)
                print("Movimiento %d Giro %d Grados:" % (j,grados))
                print("En Movimiento...")
                j=j+1     
                flag=0 
                contador=0
                if grados>= 0:
                    GPIO.output(pinMAS,GPIO.HIGH)
                    GPIO.output(pinMENOS,GPIO.LOW)
                num = (11058*grados)/310        
                if grados < 0 :
                    GPIO.output(pinMAS,GPIO.LOW)
                    GPIO.output(pinMENOS,GPIO.HIGH)
                    num = (11065*grados)/310
                while(True):
                    flag = flag+1    
                    dato = GPIO.input(pin)
                    if dato==1 and datoanterior==0:
                        contador=contador+1
                        #print(contador)
                        flag = contador
                    datoanterior=dato
		
                    if contador>=abs(num)-1 :
                        print('LLego')
                        #GPIO.output(pinMAS,GPIO.LOW)
                        #GPIO.output(pinMENOS,GPIO.LOW)
                        break
                    if flag>contador+10000:
                        #if j==n or :
                        print('detenido')
                        GPIO.output(pinMAS,GPIO.LOW)
                        GPIO.output(pinMENOS,GPIO.LOW)
                        break
         #   break        
        print("Finalizo el movimiento")
        GPIO.output(pinMAS,GPIO.LOW)
        GPIO.output(pinMENOS,GPIO.LOW)
                      
except KeyboardInterrupt:
        GPIO.output(pinMAS,GPIO.LOW)
        GPIO.output(pinMENOS,GPIO.LOW)
 #   GPIO.cleanup()
