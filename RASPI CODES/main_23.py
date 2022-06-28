import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Asignacion Pines

pin_1 = 3
pinMAS_1 = 40
pinMENOS_1 = 38
pin_2 = 5
pinMAS_2 = 12
pinMENOS_2 = 10

#Declaracion I/O
GPIO.setup(pin_1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_1,GPIO.IN)
GPIO.setup(pinMAS_1,GPIO.OUT)
GPIO.setup(pinMENOS_1,GPIO.OUT)
GPIO.setup(pin_2,GPIO.IN)
GPIO.setup(pinMAS_2,GPIO.OUT)
GPIO.setup(pinMENOS_2,GPIO.OUT)

#Inicializar variables
contador = 0
dato = 0
datoanterior = 0
j = 0
t = 0
matriz = []
gra1 = []
gra2 = []
gra3 = []
gra4 = []
gra5 = []
gra6 = []


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
                    matriz.append(gra1)
                    matriz.append(gra2)
                    
                            
    
        elif sw == 2:
            r=0#recorremos vector de los movimientos
            p=0#indice eje
            w=len(gra1)
            for indice in range(w):
                gg = matriz[p]
                grado1 = gg[r] 
                gg = matriz[p+1]
                grado2 = gg[r]
                #gg = matriz[p]
                #grado3 = gg[r+2] 
                #gg = matriz[p]
                #grado4 = gg[r+3]
                #gg = matriz[p]
                #grado5 = gg[r+4]
                #gg = matriz[p]
                #grado6 = gg[r+5]
    
                while (True):
            
                    
    
                    print("Movimiento %d Giro %d Grados:" % (j,grado1))
                    print("En Movimiento...")
                    j=j+1     
                    flag=0 
                    contador=0
                    print(grado1)
                    if grado1>= 0:
                        GPIO.output(pinMAS_1,GPIO.HIGH)
                        GPIO.output(pinMENOS_1,GPIO.LOW)
                        num = (11056*grado1)/310
                        
                    if grado1 < 0 :
                        GPIO.output(pinMAS_1,GPIO.LOW)
                        GPIO.output(pinMENOS_1,GPIO.HIGH)
                        num = (11052*grado1)/310
                    while(True):
                        flag = flag+1    
                        dato = GPIO.input(pin_1)
                        if dato==1 and datoanterior==0:
                            contador=contador+1
                            print(contador)
                            flag = contador
                        datoanterior=dato
                        time.sleep(0.0005)
                        if contador>=abs(num)-1 :
                            print('LLego')
                            print("Finalizo el movimiento")
                            GPIO.output(pinMAS_1,GPIO.LOW)
                            GPIO.output(pinMENOS_1,GPIO.LOW)
                            break
                        if flag>contador+100:
                            print('detenido')
                            GPIO.output(pinMAS_1,GPIO.LOW)
                            GPIO.output(pinMENOS_1,GPIO.LOW)
                            break                         

                    break
                
                #time.sleep(1)
                while (True):
            
                    #time.sleep(t)
    
                    print("Movimiento %d Giro %d Grados:" % (j,grado2))
                    print("En Movimiento...")
                    j=j+1     
                    flag=0 
                    contador=0
                    if grado2>= 0:
                        GPIO.output(pinMAS_2,GPIO.HIGH)
                        GPIO.output(pinMENOS_2,GPIO.LOW)
                        num = (4169*grado2)/165        
                    if grado2 < 0 :
                        GPIO.output(pinMAS_2,GPIO.LOW)
                        GPIO.output(pinMENOS_2,GPIO.HIGH)
                        num = (4529*grado2)/165
                    while(True):
                        flag = flag+1    
                        dato = GPIO.input(pin_2)
                        if dato==1 and datoanterior==0:
                            contador=contador+1
                            print(contador)
                            flag = contador
                        datoanterior=dato
                        time.sleep(0.0005)
                        if contador>=abs(num)-1 :
                            print('LLego')
                            break
                        if flag>contador+100:
                            print('detenido')
                            GPIO.output(pinMAS_2,GPIO.LOW)
                            GPIO.output(pinMENOS_2,GPIO.LOW)
                            break                         
                    print("Finalizo el movimiento")
                    GPIO.output(pinMAS_2,GPIO.LOW)
                    GPIO.output(pinMENOS_2,GPIO.LOW)
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
#   GPIO.cleanup()       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
