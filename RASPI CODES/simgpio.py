import socketio
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pinMAS_1=5
pinMENOS_1=7
pin_enc_1=3

pinMAS_2=10
pinMENOS_2=12

pinMAS_3=11
pinMENOS_3=15

pinMAS_4=18
pinMENOS_4=22

pinMAS_5=21
pinMENOS_5=23

pinMAS_6=38
pinMENOS_6=40
GPIO.setup(pinMAS_1,GPIO.OUT)
GPIO.setup(pinMENOS_1,GPIO.OUT)
GPIO.setup(pin_enc_1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinMAS_2,GPIO.OUT)
GPIO.setup(pinMENOS_2,GPIO.OUT)
GPIO.setup(pinMAS_3,GPIO.OUT)
GPIO.setup(pinMENOS_3,GPIO.OUT)
GPIO.setup(pinMAS_4,GPIO.OUT)
GPIO.setup(pinMENOS_4,GPIO.OUT)
GPIO.setup(pinMAS_5,GPIO.OUT)
GPIO.setup(pinMENOS_5,GPIO.OUT)
GPIO.setup(pinMAS_6,GPIO.OUT)
GPIO.setup(pinMENOS_6,GPIO.OUT)

sio = socketio.Client()

sio.connect('http://18.224.252.113:8080/')
@sio.event
def connect():
    print('connection established')
print('my sid is', sio.sid)
contador = 0
p1=0
p2=0
p3=0
p4=0
p5=0
p6=0

posicion=[0,0,0,0,0,0] 
matriz = []
gra1 = []
gra2 = []
gra3 = []
gra4 = []
gra5 = []
gra6 = []
sio.emit('contador1', contador)
sio.emit('contador2', contador)
sio.emit('contador3', contador)
sio.emit('contador4', contador)
sio.emit('contador5', contador)
sio.emit('contador6', contador)

while True:
    
    #contador=contador+1
    #sio.emit('message', matriz)
    time.sleep(0.01)

    
    
    lim_1_inf =-165-posicion[0]
    lim_1_sup =165-posicion[0]
    lim_2_inf =-165-posicion[1]
    lim_2_sup =165-posicion[1]
    lim_3_inf =-165-posicion[2]
    lim_3_sup =165-posicion[2]
    lim_4_inf =-165-posicion[3]
    lim_4_sup =165-posicion[3]
    lim_5_inf =-165-posicion[4]
    lim_5_sup =165-posicion[4]
    lim_6_inf =-165-posicion[5]
    lim_6_sup =165-posicion[5]
    lim=[lim_1_inf,lim_1_sup,lim_2_inf,lim_2_sup,lim_3_inf,lim_3_sup,lim_4_inf,lim_4_sup,lim_5_inf,lim_5_sup,lim_6_inf,lim_6_sup]
    sio.emit('limites',lim)
       
    
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
        
    


    @sio.on('accionar')
    def accionar():
        contador=0
        sio.emit('contador1', contador)
        sio.emit('contador2', contador)
        sio.emit('contador3', contador)
        sio.emit('contador4', contador)
        sio.emit('contador5', contador)
        sio.emit('contador6', contador)
        matriz.append(gra1)
        matriz.append(gra2)
        matriz.append(gra3)
        matriz.append(gra4)
        matriz.append(gra5)
        matriz.append(gra6)
        print(matriz)
        global p1
        global p2   
        global p3
        global p4
        global p5
        global p6
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
    
            
            print("En Movimiento...") 
            contador=0 
            acum=0 
            dato=0
            datoanterior=0  
            while(True):
                contador=contador+1
                sio.emit('contador1', contador)
                p1=p1+1
                sio.emit('pos1', p1)
                
                if grado1>= 0:
                    GPIO.output(pinMAS_1,GPIO.HIGH)
                elif grado1 < 0 :
                    GPIO.output(pinMENOS_1,GPIO.HIGH)
                time.sleep(0.5)    
                
                dato = GPIO.input(pin_enc_1)
                if dato==1 and datoanterior==0:
                    acum=acum+1
                    print(acum)
                    datoanterior=dato

                GPIO.output(pinMAS_1,GPIO.LOW)
                GPIO.output(pinMENOS_1,GPIO.LOW)
                time.sleep(0.5)


                if contador==abs(grado1):
                    print("Llego")
                    break                         

                

            
            print("En Movimiento...") 
            contador=0    


            while(True):
                contador=contador+1
                sio.emit('contador2', contador)
                p2=p2+1
                sio.emit('pos2', p2)
                if grado2>= 0:
                    GPIO.output(pinMAS_2,GPIO.HIGH)
                elif grado2 < 0 :
                    GPIO.output(pinMENOS_2,GPIO.HIGH)
                time.sleep(0.5)    
                GPIO.output(pinMAS_2,GPIO.LOW)
                GPIO.output(pinMENOS_2,GPIO.LOW)
                time.sleep(0.5)
                if contador==abs(grado2):
                    print("Llego")
                    break                         
                

            
            print("En Movimiento...") 
            contador=0    

            while(True):
                contador=contador+1
                sio.emit('contador3', contador)
                p3=p3+1
                sio.emit('pos3', p3)
                if grado3>= 0:
                    GPIO.output(pinMAS_3,GPIO.HIGH)
                elif grado3 < 0 :
                    GPIO.output(pinMENOS_3,GPIO.HIGH)
                time.sleep(0.5)    
                GPIO.output(pinMAS_3,GPIO.LOW)
                GPIO.output(pinMENOS_3,GPIO.LOW)
                time.sleep(0.5)
                if contador==abs(grado3):
                    print("Llego")
                    break                         

                

            
            print("En Movimiento...") 
            contador=0    

            while(True):
                contador=contador+1
                sio.emit('contador4', contador)
                p4=p4+1
                sio.emit('pos4', p4)
                if grado4>= 0:
                    GPIO.output(pinMAS_4,GPIO.HIGH)
                elif grado4 < 0 :
                    GPIO.output(pinMENOS_4,GPIO.HIGH)
                time.sleep(0.5)    
                GPIO.output(pinMAS_4,GPIO.LOW)
                GPIO.output(pinMENOS_4,GPIO.LOW)
                time.sleep(0.5)
                if contador==abs(grado4):
                    print("Llego")
                    break                         

                

            
            print("En Movimiento...") 
            contador=0    

            while(True):
                contador=contador+1
                sio.emit('contador5', contador)
                p5=p5+1
                sio.emit('pos5', p5)
                if grado5>= 0:
                    GPIO.output(pinMAS_5,GPIO.HIGH)
                elif grado5 < 0 :
                    GPIO.output(pinMENOS_5,GPIO.HIGH)
                time.sleep(0.5)    
                GPIO.output(pinMAS_5,GPIO.LOW)
                GPIO.output(pinMENOS_5,GPIO.LOW)
                time.sleep(0.5)
                if contador==abs(grado5):
                    print("Llego")
                    break                         

                

            
            print("En Movimiento...") 
            contador=0    

            while(True):
                contador=contador+1
                sio.emit('contador6', contador)
                p6=p6+1
                sio.emit('pos6', p6)
                if grado6>= 0:
                    GPIO.output(pinMAS_6,GPIO.HIGH)
                elif grado6 < 0 :
                    GPIO.output(pinMENOS_6,GPIO.HIGH)
                time.sleep(0.5)    
                GPIO.output(pinMAS_6,GPIO.LOW)
                GPIO.output(pinMENOS_6,GPIO.LOW)
                time.sleep(0.5)
                if contador==abs(grado6):
                    print("Llego")
                    break                         

                
            r=r+1


    @sio.on('limpiar')
    def lim():
        print("Limpio")
        global posicion
        global matriz
        global gra1
        global gra2
        global gra3
        global gra4
        global gra5
        global gra6
        global p1
        global p2   
        global p3
        global p4
        global p5
        global p6
        posicion=[0,0,0,0,0,0]
        matriz=[]
        print(matriz)
        p1=0
        p2=0
        p3=0
        p4=0
        p5=0
        p6=0
        gra1=[]
        gra2=[]
        gra3=[]
        gra4=[]
        gra5=[]
        gra6=[]
        contador=0
        sio.emit('contador1', contador)
        sio.emit('contador2', contador)
        sio.emit('contador3', contador)
        sio.emit('contador4', contador)
        sio.emit('contador5', contador)
        sio.emit('contador6', contador)
        sio.emit('pos1', p1)
        sio.emit('pos2', p2)
        sio.emit('pos3', p3)
        sio.emit('pos4', p4)
        sio.emit('pos5', p5)
        sio.emit('pos6', p6)

                

