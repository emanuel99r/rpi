import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Asignacion Pines

pin_1 = 3
pinMAS_1 = 5
pinMENOS_1 = 7

pin_2 = 11
pinMAS_2 = 13
pinMENOS_2 = 15
#ciclo_util=19

pin_3 = 21
pinMAS_3 = 23
pinMENOS_3 = 29
#ciclo_util = 31

pin_4 = 33
pinMAS_4 = 35
pinMENOS_4 = 37
#ciclo_util = 8

pin_5 = 10
pinMAS_5 = 12
pinMENOS_5 = 16
#ciclo_util = 18

pin_6 = 22
pinMAS_6 = 24
pinMENOS_6 = 26

#Declaracion I/O
GPIO.setup(pin_1,GPIO.IN)
GPIO.setup(pinMAS_1,GPIO.OUT)
GPIO.setup(pinMENOS_1,GPIO.OUT)
GPIO.setup(pin_2,GPIO.IN)
GPIO.setup(pinMAS_2,GPIO.OUT)
GPIO.setup(pinMENOS_2,GPIO.OUT)
GPIO.setup(pin_3,GPIO.IN)
GPIO.setup(pinMAS_3,GPIO.OUT)
GPIO.setup(pinMENOS_3,GPIO.OUT)
GPIO.setup(pin_4,GPIO.IN)
GPIO.setup(pinMAS_4,GPIO.OUT)
GPIO.setup(pinMENOS_4,GPIO.OUT)
GPIO.setup(pin_5,GPIO.IN)
GPIO.setup(pinMAS_5,GPIO.OUT)
GPIO.setup(pinMENOS_5,GPIO.OUT)
GPIO.setup(pin_6,GPIO.IN)
GPIO.setup(pinMAS_6,GPIO.OUT)
GPIO.setup(pinMENOS_6,GPIO.OUT)

#Inicializar variables
contador = 0
dato = 0
datoanterior = 0
j = 0
t = 0



#Inicio Programa

try:

    print("UNIVERSIDAD DEL NORTE ")
    print(" ")
    print("IMPLEMENTACION DE UN SISTEMA DE ACTUACION")
    print("PARA BRAZOS ROBOTICOS ARTICULADOS INDUSTRIALES")
    print("DEL LABORATORIO DE AUTOMATIZACION INDUSTRIAL")
    
    
    while True:
        print(" ")
        print(" ")
        print(" ")
        print(" ")    
        print("Menu:")
        print("1. Lista de comandos")
        print("2. Accionamiento")
        print("3. Configurar robot")
        print("4. Salir")
        
        while True:
            try:
                sw = int(input("Seleccione una opcion:"))
                break
            except ValueError:
                print("Digite opcion valida")
            except NameError:
                print("Digite opcion valida")
            except SyntaxError:
                print("Digite opcion valida")             
                
        if sw == 1:
                matriz = []
                gra1 = []
                gra2 = []
                gra3 = []
                gra4 = []
                gra5 = []
                gra6 = []
            
            
                while True:
                    try:
                        n = int(input("Digite Cantidad de Movimientos:"))
                        break
                    except ValueError:
                        print("Introduzca un numero entero") 
                    except NameError:
                        print("Introduzca un numero entero")
                    except SyntaxError:
                        print("Introduzca un numero entero")                     

                for i in range(1,n+1):
                    while True:
                        try:
                            while True:
                                print("Giro del Brazo. Digite movimiento numero %d en el rango[-310,310]:"%(i))
                                t = float(input("Digite movimiento numero %d:"%(i)))
                                if t >= -310 and t<=310:
                                    gra1.append(t)
                                    break
                                else:
                                    print("Introduzca un valor dentro del rango indicado")
                            break
                        except ValueError:
                            print("Introduzca un numero real")
                        except NameError:
                            print("Introduzca un numero real")
                        except SyntaxError:
                            print("Introduzca un numero real") 
                    while True:
                        try:
                            while True:
                                print("Subir y bajar el Brazo. Digite movimiento numero %d en el rango[-165,165]:"%(i))
                                t = float(input("Digite movimiento numero %d:"%(i)))
                                if t >= -165 and t<=165:
                                    gra2.append(t)
                                    break
                                else:
                                    print("Introduzca un valor dentro del rango indicado")
                            break
                        except ValueError:
                            print("Introduzca un numero real")
                        except NameError:
                            print("Introduzca un numero real")
                        except SyntaxError:
                            print("Introduzca un numero real") 
                    while True:
                        try:
                            while True:
                                print("Subir y bajar el Antebrazo. Digite movimiento numero %d en el rango[-130,130]:"%(i))
                                t = float(input("Digite movimiento numero %d:"%(i)))
                                if t >= -130 and t<=130:
                                    gra3.append(t)
                                    break
                                else:
                                    print("Introduzca un valor dentro del rango indicado")
                            break
                        except ValueError:
                            print("Introduzca un numero real")
                        except NameError:
                            print("Introduzca un numero real")
                        except SyntaxError:
                            print("Introduzca un numero real") 
                    while True:
                        try:
                            while True:
                                print("Subir y bajar Pinza. Digite movimiento numero %d en el rango[-130,130]:"%(i))
                                t = float(input("Digite movimiento numero %d:"%(i)))
                                if t >= -130 and t<=130:
                                    gra4.append(t)
                                    break
                                else:
                                    print("Introduzca un valor dentro del rango indicado")
                            break
                        except ValueError:
                            print("Introduzca un numero real")
                        except NameError:
                            print("Introduzca un numero real")
                        except SyntaxError:
                            print("Introduzca un numero real")
                    while True:
                        try:
                            while True:
                                print("Girar la Pinza. Digite movimiento numero %d en el rango[-360,360]:"%(i))
                                t = float(input("Digite movimiento numero %d:"%(i)))
                                if t >= -360 and t<=360:
                                    gra5.append(t)
                                    break
                                else:
                                    print("Introduzca un valor dentro del rango indicado")
                            break
                        except ValueError:
                            print("Introduzca un numero real")
                        except NameError:
                            print("Introduzca un numero real")
                        except SyntaxError:
                            print("Introduzca un numero real")
                    while True:
                        try:
                            while True:
                                print("Abrir y cerrar la Pinza. Digite movimiento numero %d en el rango[-130,130]:"%(i))
                                t = float(input("Digite movimiento numero %d:"%(i)))
                                if t >= -130 and t<=130:
                                    gra6.append(t)
                                    break
                                else:
                                    print("Introduzca un valor dentro del rango indicado")
                            break
                        except ValueError:
                            print("Introduzca un numero real")
                        except NameError:
                            print("Introduzca un numero real")
                        except SyntaxError:
                            print("Introduzca un numero real")                    
                    matriz.append(gra1)
                    matriz.append(gra2)
                    matriz.append(gra3)
                    matriz.append(gra4)
                    matriz.append(gra5)
                    matriz.append(gra6)                    
                    
                    
                            
    
        elif sw == 2:
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
                j=j+1
                while (True):
            
                    #time.sleep(t)
    
                    print("Movimiento %d Giro %d Grados:" % (j,grado1))
                    print("En Movimiento...")
                         
                    flag=0 
                    contador=0
                    if grado1>= 0:
                        GPIO.output(pinMAS_1,GPIO.HIGH)
                        GPIO.output(pinMENOS_1,GPIO.LOW)
                        num = (11058*grado1)/310        
                    if grado1 < 0 :
                        GPIO.output(pinMAS_1,GPIO.LOW)
                        GPIO.output(pinMENOS_1,GPIO.HIGH)
                        num = (11065*grado1)/310
                    while(True):
                        flag = flag+1    
                        dato = GPIO.input(pin_1)
                        if dato==1 and datoanterior==0:
                            contador=contador+1
                            #print(contador)
                            flag = contador
                        datoanterior=dato
                        if contador>=abs(num)-1 :
                            print('LLego')
                            break
                        if flag>contador+10000:
                            print('detenido')
                            GPIO.output(pinMAS_1,GPIO.LOW)
                            GPIO.output(pinMENOS_1,GPIO.LOW)
                            break                         
                    print("Finalizo el movimiento")
                    GPIO.output(pinMAS_1,GPIO.LOW)
                    GPIO.output(pinMENOS_1,GPIO.LOW)
                    break
                
                
                while (True):
            
                    #time.sleep(t)
    
                    print("Movimiento %d Giro %d Grados:" % (j,grado2))
                    print("En Movimiento...")
                         
                    flag=0 
                    contador=0
                    if grado2>= 0:
                        GPIO.output(pinMAS_2,GPIO.HIGH)
                        GPIO.output(pinMENOS_2,GPIO.LOW)
                        num = (11058*grado2)/310        
                    if grado2 < 0 :
                        GPIO.output(pinMAS_2,GPIO.LOW)
                        GPIO.output(pinMENOS_2,GPIO.HIGH)
                        num = (11065*grado2)/310
                    while(True):
                        flag = flag+1    
                        dato = GPIO.input(pin_2)
                        if dato==1 and datoanterior==0:
                            contador=contador+1
                            #print(contador)
                            flag = contador
                        datoanterior=dato
                        if contador>=abs(num)-1 :
                            print('LLego')
                            break
                        if flag>contador+10000:
                            print('detenido')
                            GPIO.output(pinMAS_2,GPIO.LOW)
                            GPIO.output(pinMENOS_2,GPIO.LOW)
                            break                         
                    print("Finalizo el movimiento")
                    GPIO.output(pinMAS_2,GPIO.LOW)
                    GPIO.output(pinMENOS_2,GPIO.LOW)
                    break
               
                while (True):
            
                    #time.sleep(t)
    
                    print("Movimiento %d Giro %d Grados:" % (j,grado3))
                    print("En Movimiento...")
                         
                    flag=0 
                    contador=0
                    if grado3>= 0:
                        GPIO.output(pinMAS_3,GPIO.HIGH)
                        GPIO.output(pinMENOS_3,GPIO.LOW)
                        num = (11058*grado3)/310        
                    if grado3 < 0 :
                        GPIO.output(pinMAS_3,GPIO.LOW)
                        GPIO.output(pinMENOS_3,GPIO.HIGH)
                        num = (11065*grado3)/310
                    while(True):
                        flag = flag+1    
                        dato = GPIO.input(pin_3)
                        if dato==1 and datoanterior==0:
                            contador=contador+1
                            #print(contador)
                            flag = contador
                        datoanterior=dato
                        if contador>=abs(num)-1 :
                            print('LLego')
                            break
                        if flag>contador+10000:
                            print('detenido')
                            GPIO.output(pinMAS_3,GPIO.LOW)
                            GPIO.output(pinMENOS_3,GPIO.LOW)
                            break                         
                    print("Finalizo el movimiento")
                    GPIO.output(pinMAS_3,GPIO.LOW)
                    GPIO.output(pinMENOS_3,GPIO.LOW)
                    break
                while (True):
            
                    #time.sleep(t)
    
                    print("Movimiento %d Giro %d Grados:" % (j,grado4))
                    print("En Movimiento...")
                         
                    flag4=0
                    flag5=0
                    contador4=0
                    contador5=0
                    dato4=0
                    dato5=0
                    datoanterior4=0
                    datoanterior5=0
                    if grado4>= 0:
                        GPIO.output(pinMAS_4,GPIO.HIGH)
                        GPIO.output(pinMENOS_4,GPIO.LOW)
                        GPIO.output(pinMAS_5,GPIO.HIGH)
                        GPIO.output(pinMENOS_5,GPIO.LOW)
                        num = (11058*grado4)/310        
                    if grado4 < 0 :
                        GPIO.output(pinMAS_4,GPIO.LOW)
                        GPIO.output(pinMENOS_4,GPIO.HIGH)
                        GPIO.output(pinMAS_5,GPIO.LOW)
                        GPIO.output(pinMENOS_5,GPIO.HIGH)
                        num = (11065*grado4)/310
                    while(True):
                        flag4 = flag4+1
                        flag5 = flag5+1
                        dato4 = GPIO.input(pin_4)
                        dato5 = GPIO.input(pin_5)
                        if dato4==1 and datoanterior4==0:
                            contador4=contador4+1
                            #print(contador)
                            flag4 = contador4
                        datoanterior4=dato4
                        if dato5==1 and datoanterior5==0:
                            contador5=contador5+1
                            #print(contador)
                            flag4 = contador4
                        datoanterior4=dato4
                        if contador4>=abs(num)-1 and contador5>=abs(num)-1 :
                            print('LLego')
                            break
                        if flag4>contador4+10 or flag5>contador5+10 :
                            print('detenido')
                            GPIO.output(pinMAS_4,GPIO.LOW)
                            GPIO.output(pinMENOS_4,GPIO.LOW)
                            GPIO.output(pinMAS_5,GPIO.LOW)
                            GPIO.output(pinMENOS_5,GPIO.LOW)
                            break                         
                    print("Finalizo el movimiento")
                    GPIO.output(pinMAS_4,GPIO.LOW)
                    GPIO.output(pinMENOS_4,GPIO.LOW)
                    GPIO.output(pinMAS_5,GPIO.LOW)
                    GPIO.output(pinMENOS_5,GPIO.LOW)
                    break
                while (True):
            
                    #time.sleep(t)
    
                    print("Movimiento %d Giro %d Grados:" % (j,grado5))
                    print("En Movimiento...")
                         
                    flag4=0
                    flag5=0
                    contador4=0
                    contador5=0
                    dato4=0
                    dato5=0
                    datoanterior4=0
                    datoanterior5=0
                    if grado5>= 0:
                        GPIO.output(pinMAS_4,GPIO.HIGH)
                        GPIO.output(pinMENOS_4,GPIO.LOW)
                        GPIO.output(pinMAS_5,GPIO.LOW)
                        GPIO.output(pinMENOS_5,GPIO.HIGH)
                        num = (11058*grado5)/310        
                    if grado5 < 0 :
                        GPIO.output(pinMAS_4,GPIO.LOW)
                        GPIO.output(pinMENOS_4,GPIO.HIGH)
                        GPIO.output(pinMAS_5,GPIO.HIGH)
                        GPIO.output(pinMENOS_5,GPIO.LOW)
                        num = (11065*grado5)/310
                    while(True):
                        flag4 = flag4+1
                        flag5 = flag5+1
                        dato4 = GPIO.input(pin_4)
                        dato5 = GPIO.input(pin_5)
                        if dato4==1 and datoanterior4==0:
                            contador4=contador4+1
                            #print(contador)
                            flag4 = contador4
                        datoanterior4=dato4
                        if dato5==1 and datoanterior5==0:
                            contador5=contador5+1
                            #print(contador)
                            flag4 = contador4
                        datoanterior4=dato4
                        if contador4>=abs(num)-1 and contador5>=abs(num)-1 :
                            print('LLego')
                            break
                        if flag4>contador4+10 or flag5>contador5+10 :
                            print('detenido')
                            GPIO.output(pinMAS_5,GPIO.LOW)
                            GPIO.output(pinMENOS_5,GPIO.LOW)
                            GPIO.output(pinMAS_5,GPIO.LOW)
                            GPIO.output(pinMENOS_5,GPIO.LOW)
                            break                         
                    print("Finalizo el movimiento")
                    GPIO.output(pinMAS_4,GPIO.LOW)
                    GPIO.output(pinMENOS_4,GPIO.LOW)
                    GPIO.output(pinMAS_5,GPIO.LOW)
                    GPIO.output(pinMENOS_5,GPIO.LOW)
                    break
                while (True):
            
                    #time.sleep(t)
    
                    print("Movimiento %d Giro %d Grados:" % (j,grado6))
                    print("En Movimiento...")
                         
                    flag=0 
                    contador=0
                    if grado6>= 0:
                        GPIO.output(pinMAS_6,GPIO.HIGH)
                        GPIO.output(pinMENOS_6,GPIO.LOW)
                        num = (11058*grado6)/310        
                    if grado6 < 0 :
                        GPIO.output(pinMAS_6,GPIO.LOW)
                        GPIO.output(pinMENOS_6,GPIO.HIGH)
                        num = (11065*grado6)/310
                    while(True):
                        flag = flag+1    
                        dato = GPIO.input(pin_6)
                        if dato==1 and datoanterior==0:
                            contador=contador+1
                            #print(contador)
                            flag = contador
                        datoanterior=dato
                        if contador>=abs(num)-1 :
                            print('LLego')
                            break
                        if flag>contador+10000:
                            print('detenido')
                            GPIO.output(pinMAS_6,GPIO.LOW)
                            GPIO.output(pinMENOS_6,GPIO.LOW)
                            break                         
                    print("Finalizo el movimiento")
                    GPIO.output(pinMAS_6,GPIO.LOW)
                    GPIO.output(pinMENOS_6,GPIO.LOW)
                    break              
                r=r+1                  
    
    
    
    
    
    
        elif sw == 3:
            try:
                while True:
                    t = float(input("Digite tiempo de espera entre movimientos(Segundos):"))
                    
                    if t<0:
                        print("Debe ingresar un numero positivo")
                    elif t>=0:
                        print("Hecho...")
                        break
            except ValueError:
                print("Digite tiempo valido")                    
            except NameError:
                print("Digite tiempo valido")
            except SyntaxError:
                print("Digite tiempo valido")
                    
        elif sw == 4:
            print("Finalizado...")
            break
        
        
        
        
        
except KeyboardInterrupt:
    GPIO.output(pinMAS_1,GPIO.LOW)
    GPIO.output(pinMENOS_1,GPIO.LOW)
    GPIO.output(pinMAS_2,GPIO.LOW)
    GPIO.output(pinMENOS_2,GPIO.LOW)
    GPIO.output(pinMAS_3,GPIO.LOW)
    GPIO.output(pinMENOS_3,GPIO.LOW)
    GPIO.output(pinMAS_4,GPIO.LOW)
    GPIO.output(pinMENOS_4,GPIO.LOW)
    GPIO.output(pinMAS_5,GPIO.LOW)
    GPIO.output(pinMENOS_5,GPIO.LOW)
    GPIO.output(pinMAS_6,GPIO.LOW)
    GPIO.output(pinMENOS_6,GPIO.LOW)
#   GPIO.cleanup()       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
