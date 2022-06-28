import socketio
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pinMAS_1=21
#pinMENOS_1=13
pinMAS_2=19
#pinMENOS_2=13
pinMAS_3=13
#pinMENOS_3=13
pinMAS_4=11
#pinMENOS_4=13
pinMAS_5=5
#pinMENOS_5=13
pinMAS_6=3
#pinMENOS_6=13
GPIO.setup(pinMAS_1,GPIO.OUT)
#GPIO.setup(pinMENOS_1,GPIO.OUT)
GPIO.setup(pinMAS_2,GPIO.OUT)
#GPIO.setup(pinMENOS_2,GPIO.OUT)
GPIO.setup(pinMAS_3,GPIO.OUT)
#GPIO.setup(pinMENOS_3,GPIO.OUT)
GPIO.setup(pinMAS_4,GPIO.OUT)
#GPIO.setup(pinMENOS_4,GPIO.OUT)
GPIO.setup(pinMAS_5,GPIO.OUT)
#GPIO.setup(pinMENOS_5,GPIO.OUT)
GPIO.setup(pinMAS_6,GPIO.OUT)
#GPIO.setup(pinMENOS_6,GPIO.OUT)

sio = socketio.Client()

sio.connect('http://192.168.100.10:10000/')
@sio.event
def connect():
    print('connection established')
print('my sid is', sio.sid)
contador = 0
posicion=[0,0,0,0,0,0] 
matriz = []
gra1 = []
gra2 = []
gra3 = []
gra4 = []
gra5 = []
gra6 = []
while True:
    

    
    lim_1_inf =-165-posicion[0]
    sio.emit('lim_1_inf', lim_1_inf)
    lim_1_sup =165-posicion[0]
    sio.emit('lim_1_sup', lim_1_sup)
    
    lim_2_inf =-165-posicion[1]
    sio.emit('lim_2_inf', lim_2_inf)
    lim_2_sup =165-posicion[1]
    sio.emit('lim_2_sup', lim_2_sup)    
    
    lim_3_inf =-165-posicion[2]
    sio.emit('lim_3_inf', lim_3_inf)
    lim_3_sup =165-posicion[2]
    sio.emit('lim_3_sup', lim_3_sup) 

    lim_4_inf =-165-posicion[3]
    sio.emit('lim_4_inf', lim_4_inf)
    lim_4_sup =165-posicion[3]
    sio.emit('lim_4_sup', lim_4_sup) 

    lim_5_inf =-165-posicion[4]
    sio.emit('lim_5_inf', lim_5_inf)
    lim_5_sup =165-posicion[4]
    sio.emit('lim_5_sup', lim_5_sup) 

    lim_6_inf =-165-posicion[5]
    sio.emit('lim_6_inf', lim_6_inf)
    lim_6_sup =165-posicion[5]
    sio.emit('lim_6_sup', lim_6_sup)

    @sio.on('grados')
    def mover(arreglo):
        print(arreglo)
        global posicion
        global lim_1_inf
        global lim_1_sup
        global lim_2_inf
        global lim_2_sup        
        global lim_3_inf
        global lim_3_sup
        global lim_4_inf
        global lim_4_sup
        global lim_5_inf
        global lim_5_sup        
        global lim_6_inf
        global lim_6_sup
        global gra1
        global gra2
        global gra3
        global gra4
        global gra5
        global gra6
        global matriz

        try:

            if float(arreglo[0]) < lim_1_inf  or float(arreglo[0]) > lim_1_sup or float(arreglo[1]) < lim_2_inf or float(arreglo[1]) > lim_2_sup or float(arreglo[2]) < lim_3_inf  or float(arreglo[2]) > lim_3_sup or float(arreglo[3]) < lim_4_inf  or float(arreglo[3]) > lim_4_sup or float(arreglo[4]) < lim_5_inf  or float(arreglo[4]) > lim_5_sup or float(arreglo[5]) < lim_6_inf  or float(arreglo[5]) > lim_6_sup:
                print("Introduzca un valor dentro del rango indicado")
                sio.emit('outRange')
            else:
                x=float(arreglo[0])
                gra1.append(x)
                posicion[0]=posicion[0]+x
                print(posicion[0])
                print("Valor correcto")          
                

                x=float(arreglo[1])
                gra2.append(x)
                posicion[1]=posicion[1]+x
                print(posicion[1])
                print("Valor correcto")

                x=float(arreglo[2])
                gra3.append(x)
                posicion[2]=posicion[2]+x
                print(posicion[2])
                print("Valor correcto")                            

                x=float(arreglo[3])
                gra4.append(x)
                posicion[3]=posicion[3]+x
                print(posicion[3])
                print("Valor correcto")          
                

                x=float(arreglo[4])
                gra5.append(x)
                posicion[4]=posicion[4]+x
                print(posicion[4])
                print("Valor correcto")

                x=float(arreglo[5])
                gra6.append(x)
                posicion[5]=posicion[5]+x
                print(posicion[5])
                print("Valor correcto") 

            
        
        
        
        
        
        
        
        
        except ValueError:
            print("Introduzca un numero real")
            sio.emit('typeError')
        
 


    @sio.on('home')
    def home(home):
        print(home)
        matriz.append(gra1)
        matriz.append(gra2)
        matriz.append(gra3)
        matriz.append(gra4)
        matriz.append(gra5)
        matriz.append(gra6)
        print(matriz)   

        
        r=0#recorremos vector de los movimientos
        p=0#indice eje
        w=len(gra1)
        for indice in range(w):
            gg = matriz[p]
            grado1 = gg[r] 
            gg = matriz[p+1]
            grado2 = gg[r]
            gg = matriz[p+2]
            grado3 = gg[r] 
            gg = matriz[p+3]
            grado4 = gg[r]
            gg = matriz[p+4]
            grado5 = gg[r]
            gg = matriz[p+5]
            grado6 = gg[r]
    
            while (True):
                print("En Movimiento...") 
                contador=0    
                if grado1>= 0:
                    GPIO.output(pinMAS_1,GPIO.HIGH)
                if grado1 < 0 :
                    GPIO.output(pinMAS_1,GPIO.LOW)

                while(True):
                    contador=contador+1
                    sio.emit('message_1', contador)
                    GPIO.output(pinMAS_1,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pinMAS_1,GPIO.LOW)
                    time.sleep(0.5)
                    if contador==abs(grado1):
                        break                         

                break

            while (True):
                print("En Movimiento...") 
                contador=0    
                if grado2>= 0:
                    GPIO.output(pinMAS_2,GPIO.HIGH)
                if grado2 < 0 :
                    GPIO.output(pinMAS_2,GPIO.LOW)

                while(True):
                    contador=contador+1
                    sio.emit('message_2', contador)
                    GPIO.output(pinMAS_2,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pinMAS_2,GPIO.LOW)
                    time.sleep(0.5)
                    if contador==abs(grado2):
                        break                         

                break

            while (True):
                print("En Movimiento...") 
                contador=0    
                if grado3>= 0:
                    GPIO.output(pinMAS_3,GPIO.HIGH)
                if grado3 < 0 :
                    GPIO.output(pinMAS_3,GPIO.LOW)

                while(True):
                    contador=contador+1
                    sio.emit('message_3', contador)
                    GPIO.output(pinMAS_3,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pinMAS_3,GPIO.LOW)
                    time.sleep(0.5)
                    if contador==abs(grado3):
                        break                         

                break

            while (True):
                print("En Movimiento...") 
                contador=0    
                if grado4>= 0:
                    GPIO.output(pinMAS_4,GPIO.HIGH)
                if grado4 < 0 :
                    GPIO.output(pinMAS_4,GPIO.LOW)

                while(True):
                    contador=contador+1
                    sio.emit('message_4', contador)
                    GPIO.output(pinMAS_4,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pinMAS_4,GPIO.LOW)
                    time.sleep(0.5)
                    if contador==abs(grado4):
                        break                         

                break

            while (True):
                print("En Movimiento...") 
                contador=0    
                if grado5>= 0:
                    GPIO.output(pinMAS_5,GPIO.HIGH)
                if grado5 < 0 :
                    GPIO.output(pinMAS_5,GPIO.LOW)

                while(True):
                    contador=contador+1
                    sio.emit('message_5', contador)
                    GPIO.output(pinMAS_5,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pinMAS_5,GPIO.LOW)
                    time.sleep(0.5)
                    if contador==abs(grado5):
                        break                         

                break

            while (True):
                print("En Movimiento...") 
                contador=0    
                if grado6>= 0:
                    GPIO.output(pinMAS_6,GPIO.HIGH)
                if grado4 < 0 :
                    GPIO.output(pinMAS_6,GPIO.LOW)

                while(True):
                    contador=contador+1
                    sio.emit('message_6', contador)
                    GPIO.output(pinMAS_6,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(pinMAS_6,GPIO.LOW)
                    time.sleep(0.5)
                    if contador==abs(grado6):
                        break                         

                break
            r=r+1    