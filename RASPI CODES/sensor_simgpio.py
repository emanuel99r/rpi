import socketio
import time
import RPi.GPIO as GPIO
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
try:
        def sensor(motor,veces):
                contador=0
                acum=0
                global p1
                global p2
                global p1
                global p2   
                global p3
                global p4
                global p5
                global p6
                global p 
                while st == 1:
                        
                        if contador == abs(veces):
                                break
                        contador+=1
                        @sio.on('stop')
                        def stp():
                                global st 
                                print('Stop')   
                                GPIO.output(5,GPIO.LOW)
                                GPIO.output(7,GPIO.LOW)
                                GPIO.output(10,GPIO.LOW)
                                GPIO.output(12,GPIO.LOW)
                                GPIO.output(11,GPIO.LOW)
                                GPIO.output(15,GPIO.LOW)
                                GPIO.output(21,GPIO.LOW)
                                GPIO.output(23,GPIO.LOW)
                                GPIO.output(18,GPIO.LOW)
                                GPIO.output(22,GPIO.LOW)
                                GPIO.output(38,GPIO.LOW)
                                GPIO.output(40,GPIO.LOW)
                                st = 0                         
                                
                        if motor=="pinMAS_1":
                                ENC_MOTOR=3
                                PIN_MOTOR = 5
                                umbral=5
                                chanel='contador1'
                                k = 0
                                cha_p='pos1'
                                s=1
                        elif motor=="pinMENOS_1":
                                ENC_MOTOR = 3 
                                PIN_MOTOR = 7
                                umbral = 5
                                chanel = 'contador1'
                                k = 0
                                cha_p='pos1'
                                s=-1                                
                        elif motor=="pinMAS_2":
                                ENC_MOTOR= 8
                                PIN_MOTOR = 10
                                umbral=900
                                chanel='contador2'
                                k = 1
                                cha_p='pos2'
                                s=1
                        elif motor=="pinMENOS_2":
                                ENC_MOTOR = 8 
                                PIN_MOTOR = 12
                                umbral = 200
                                chanel = 'contador2'
                                k = 1
                                cha_p='pos2'
                                s=-1
                        elif motor=="pinMAS_3":
                                ENC_MOTOR= 13
                                PIN_MOTOR = 11
                                umbral=150
                                chanel='contador3'
                                k = 2
                                cha_p='pos3'
                                s=1
                        elif motor=="pinMENOS_3":
                                ENC_MOTOR = 13 
                                PIN_MOTOR = 15
                                umbral = 25
                                chanel = 'contador3'
                                k = 2
                                cha_p='pos3'
                                s=-1
                        elif motor=="pinMAS_4":
                                ENC_MOTOR= 16
                                PIN_MOTOR = 18
                                umbral=850
                                chanel='contador4'
                                k = 3
                                cha_p='pos4'
                                s=1
                        elif motor=="pinMENOS_4":
                                ENC_MOTOR = 16 
                                PIN_MOTOR = 22
                                umbral = 40
                                chanel = 'contador4'
                                k = 3
                                cha_p='pos4'
                                s=-1
                        elif motor=="pinMAS_5":
                                ENC_MOTOR= 19
                                PIN_MOTOR = 21
                                umbral=100
                                chanel='contador5'
                                k = 4
                                cha_p='pos5'
                                s=1
                        elif motor=="pinMENOS_5":
                                ENC_MOTOR = 19
                                PIN_MOTOR = 23
                                umbral = 25
                                chanel = 'contador5'
                                k = 4
                                cha_p='pos5'
                                s=-1
                        elif motor=="pinMAS_6":
                                ENC_MOTOR= 36
                                PIN_MOTOR = 38
                                umbral=200
                                chanel='contador6'
                                k = 5
                                cha_p='pos6'
                                s=1
                        elif motor=="pinMENOS_6":
                                ENC_MOTOR = 36
                                PIN_MOTOR = 40
                                umbral = 200
                                chanel = 'contador6'
                                k = 5
                                cha_p='pos6'
                                s=-1                                                                                                                                                            
                        GPIO.setup(PIN_MOTOR,GPIO.OUT) 
                        GPIO.setup(ENC_MOTOR, GPIO.OUT)
                        GPIO.output(ENC_MOTOR, GPIO.LOW)
                        #time.sleep(0.6)
                        time.sleep(0.06)
                        #time.sleep(0.1)
                        GPIO.output(PIN_MOTOR, GPIO.HIGH)
                        GPIO.setup(ENC_MOTOR, GPIO.IN)
                        currentTime = time.time()
                        diff = 0
                        while(GPIO.input(ENC_MOTOR) == GPIO.LOW):
                                diff  = time.time() - currentTime
                        x=diff * 1000    
                        if x<umbral:
                                acum+=1
                                p[k]=p[k]+s
                                
                        print(x)
                        sio.emit(chanel, acum)
                        sio.emit(cha_p, p[k])
                        #time.sleep(0.5)
                        time.sleep(0.05)
                        #time.sleep(0.1)
                        GPIO.output(PIN_MOTOR, GPIO.LOW)                 
       
                return acum
        sio = socketio.Client()
        sio.connect('http://18.224.252.113:8080/')
        @sio.event
        def connect():
            print('connection established')
        print('my sid is', sio.sid)
        contador = 0
        orden = 0
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
        p = [0,0,0,0,0,0]
        sio.emit('contador1', contador)
        sio.emit('contador2', contador)
        sio.emit('contador3', contador)
        sio.emit('contador4', contador)
        sio.emit('contador5', contador)
        sio.emit('contador6', contador)
        while True:
            time.sleep(0.01)
            lim_1_inf =-170-posicion[0]
            lim_1_sup =140-posicion[0]
            lim_2_inf =-165-posicion[1]
            lim_2_sup =165-posicion[1]
            lim_3_inf =-130-posicion[2]
            lim_3_sup =130-posicion[2]
            lim_4_inf =-130-posicion[3]
            lim_4_sup =130-posicion[3]
            lim_5_inf =-360-posicion[4]
            lim_5_sup =360-posicion[4]
            lim_6_inf =-100-posicion[5]
            lim_6_sup =100-posicion[5]
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
                global orden
                orden = 1
                try:
                    if float(arreglo[0]) < lim_1_inf  or float(arreglo[0]) > lim_1_sup or float(arreglo[1]) < lim_2_inf or float(arreglo[1]) > lim_2_sup or float(arreglo[2]) < lim_3_inf  or float(arreglo[2]) > lim_3_sup or float(arreglo[3]) < lim_4_inf  or float(arreglo[3]) > lim_4_sup or float(arreglo[4]) < lim_5_inf  or float(arreglo[4]) > lim_5_sup or float(arreglo[5]) < lim_6_inf  or float(arreglo[5]) > lim_6_sup:
                        #print("Introduzca un valor dentro del rango indicado")
                        #sio.emit('outRange')   
                            if float(arreglo[0]) < lim_1_inf  or float(arreglo[0]) > lim_1_sup:
                                print("Fuera del rango para el eje 1")
                                sio.emit('outRange1')    
                            elif float(arreglo[1]) < lim_2_inf or float(arreglo[1]) > lim_2_sup:
                                print("Fuera del rango para el eje 2")
                                sio.emit('outRange2')
                            elif float(arreglo[2]) < lim_3_inf  or float(arreglo[2]) > lim_3_sup:
                                print("Fuera del rango para el eje 3")
                                sio.emit('outRange3')     
                            elif float(arreglo[3]) < lim_4_inf  or float(arreglo[3]) > lim_4_sup:
                                print("Fuera del rango para el eje 4")
                                sio.emit('outRange4')     
                            elif float(arreglo[4]) < lim_5_inf  or float(arreglo[4]) > lim_5_sup:
                                print("Fuera del rango para el eje 5")
                                sio.emit('outRange5')
                            elif float(arreglo[5]) < lim_6_inf  or float(arreglo[5]) > lim_6_sup:
                                print("Fuera del rango para el eje 6")
                                sio.emit('outRange6')      

                    else:
                        sio.emit('arregloTabla',arreglo)    
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
                global orden
                
                if orden == 1 :
                        sio.emit('deshabilitar')    
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
                        global st
                        st=1
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
                            if grado1> 0 and st == 1:
                                sensor("pinMAS_1",grado1)
                            elif grado1 < 0 and st == 1:
                                sensor("pinMENOS_1",grado1)
                            print("En Movimiento...") 
                            if grado2> 0 and st == 1:
                                sensor("pinMAS_2",grado2)
                            elif grado2 < 0 and st == 1:
                                sensor("pinMENOS_2",grado2)               
                            print("En Movimiento...") 
                            if grado3> 0 and st == 1:
                                sensor("pinMAS_3",grado3)
                            elif grado3 < 0 and st == 1:
                                sensor("pinMENOS_3",grado3) 
                            print("En Movimiento...") 
                            if grado4> 0 and st == 1:
                                sensor("pinMAS_4",grado4)
                            elif grado4 < 0 and st == 1:
                                sensor("pinMENOS_4",grado4)         
                            print("En Movimiento...") 
                            if grado5> 0 and st == 1:
                                sensor("pinMAS_5",grado5)
                            elif grado5 < 0 and st == 1:
                                sensor("pinMENOS_5",grado5)                      
                            print("En Movimiento...") 
                            if grado6> 0 and st == 1:
                                sensor("pinMAS_6",grado6)
                            elif grado6 < 0 and st == 1:
                                sensor("pinMENOS_6",grado6)                     
                            r=r+1
                            sio.emit('habilitar')
                     
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
                global p
                global orden   
                orden = 0
                p=[0,0,0,0,0,0]
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
except KeyboardInterrupt:
        GPIO.output(5,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(11,GPIO.LOW)
        GPIO.output(15,GPIO.LOW)
        GPIO.output(21,GPIO.LOW)
        GPIO.output(23,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
        GPIO.output(38,GPIO.LOW)
        GPIO.output(40,GPIO.LOW)
