import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Asignacion Pines

#pin_ms_1=
pin_ms_1=37
pin_enc_1=3
pinMAS_1=11
pinMENOS_1=13

pin_enc_2=5
pin_pwm_2=15
pinMAS_2=19
pinMENOS_2=21


#,7,,10
pin_enc_3=8
pin_ms_3=31
pin_pwm_3=18
pinMAS_3=22
pinMENOS_3=16

pin_enc_4=10
pin_ms_4=35
pin_pwm_4=26
pinMAS_4=32
pinMENOS_4=24

pin_enc_5=7
pin_ms_5=29
pin_pwm_5=40
pinMAS_5=38
pinMENOS_5=36

pin_enc_6=12
pinMAS_6=23
pinMENOS_6=33

#Declaracion I/O
GPIO.setup(pin_enc_1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_enc_2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_enc_3,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_enc_4,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_enc_5,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_enc_6,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_ms_1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_ms_3,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_ms_4,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_ms_5,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinMAS_1,GPIO.OUT)
GPIO.setup(pinMENOS_1,GPIO.OUT)
GPIO.setup(pinMAS_2,GPIO.OUT)
GPIO.setup(pinMENOS_2,GPIO.OUT)
GPIO.setup(pin_pwm_2,GPIO.OUT)
GPIO.setup(pinMAS_3,GPIO.OUT)
GPIO.setup(pinMENOS_3,GPIO.OUT)
GPIO.setup(pin_pwm_3,GPIO.OUT)
GPIO.setup(pinMAS_4,GPIO.OUT)
GPIO.setup(pinMENOS_4,GPIO.OUT)
GPIO.setup(pin_pwm_4,GPIO.OUT)
GPIO.setup(pinMAS_5,GPIO.OUT)
GPIO.setup(pinMENOS_5,GPIO.OUT)
GPIO.setup(pin_pwm_5,GPIO.OUT)
GPIO.setup(pinMAS_6,GPIO.OUT)
GPIO.setup(pinMENOS_6,GPIO.OUT)

#Inicializar variables
p2=GPIO.PWM(pin_pwm_2,1000)
p2.start(100)
p3=GPIO.PWM(pin_pwm_3,1000)
p3.start(100)
p4=GPIO.PWM(pin_pwm_4,1000)
p4.start(100)
p5=GPIO.PWM(pin_pwm_5,1000)
p5.start(100)
contador = 0
dato = 0
datoanterior = 0
j = 0
t = 0
flag=0
posicion_1=0
posicion_2=0
posicion_3=0
posicion_4=0
posicion_5=0
posicion_6=0
#Inicio Programa

try:
    print("HOMING-1...")
    ms=GPIO.input(pin_ms_1)
    if ms==0:
        print("Home 1")
        GPIO.output(pinMAS_1,GPIO.LOW)
        GPIO.output(pinMENOS_1,GPIO.LOW)        
    else:
        GPIO.output(pinMAS_1,GPIO.LOW)
        GPIO.output(pinMENOS_1,GPIO.HIGH)
        while(True):
            ms=GPIO.input(pin_ms_1)
            if ms== 0:
                print("Home 1")       
                break
            flag=flag+1
            dato = GPIO.input(pin_enc_1)
            if dato==1 and datoanterior==0:
                contador=contador+1
                flag = contador
            datoanterior=dato
                    
            time.sleep(0.0005)
            if flag>contador+100:
                contador=0
                datoanterior=0                        
                GPIO.output(pinMAS_1,GPIO.HIGH)
                GPIO.output(pinMENOS_1,GPIO.LOW)

        time.sleep(0.0005)
        contador=0
        datoanterior=0     
        while True:
            dato = GPIO.input(pin_enc_1)
            if dato==1 and datoanterior==0:
                contador=contador+1
            datoanterior=dato
            time.sleep(0.0005)
            if contador>=74 :
                print('LLego')
                GPIO.output(pinMAS_1,GPIO.LOW)
                GPIO.output(pinMENOS_1,GPIO.LOW)
                break

    print("HOMING-2...")
    p2.ChangeDutyCycle(100)
    GPIO.output(pinMAS_2,GPIO.HIGH)
    GPIO.output(pinMENOS_2,GPIO.LOW)   
    flag=0
    contador=0
    datoanterior=0         
    while(True):
        flag=flag+1
        dato = GPIO.input(pin_enc_2)
        if dato==1 and datoanterior==0:
            contador=contador+1
           
            flag = contador
        datoanterior=dato
        time.sleep(0.0005)
        if flag>contador+100:
            print('HOME 2')
            GPIO.output(pinMAS_2,GPIO.LOW)
            GPIO.output(pinMENOS_2,GPIO.LOW)
            break
        
    print("HOMING-3...")
    p3.ChangeDutyCycle(100)
    ms=GPIO.input(pin_ms_3)
    flag=0
    if ms== 0:
        print("Home 3")       
        GPIO.output(pinMAS_3,GPIO.LOW)
        GPIO.output(pinMENOS_3,GPIO.LOW)
    else:
        GPIO.output(pinMAS_3,GPIO.LOW)
        GPIO.output(pinMENOS_3,GPIO.HIGH)
        while(True):
            ms=GPIO.input(pin_ms_3)
            if ms== 0:
                print("Home 3")       
                break
            flag=flag+1
            dato = GPIO.input(pin_enc_3)
            if dato==1 and datoanterior==0:
                contador=contador+1
                flag = contador
            datoanterior=dato
                
            time.sleep(0.0005)

            if flag>contador+100:
                
                contador=0
                datoanterior=0
                flag=0
                GPIO.output(pinMAS_3,GPIO.HIGH)
                GPIO.output(pinMENOS_3,GPIO.LOW)
        
        flag=0
        contador=0
        datoanterior=0         
                
        while True:
            flag=flag+1
            dato = GPIO.input(pin_enc_3)
            if dato==1 and datoanterior==0:
                contador=contador+1
                flag = contador
            datoanterior=dato
                    
            time.sleep(0.0005)
            if contador>=300 :
                print('LLego')
                GPIO.output(pinMAS_3,GPIO.LOW)
                GPIO.output(pinMENOS_3,GPIO.LOW)
                break        


    print("HOMING-5...")
    
    ms=GPIO.input(pin_ms_5)
    if ms== 0:
        print("Home 5")       
        GPIO.output(pinMAS_4,GPIO.LOW)
        GPIO.output(pinMENOS_4,GPIO.LOW)       
        GPIO.output(pinMAS_5,GPIO.LOW)
        GPIO.output(pinMENOS_5,GPIO.LOW)
        
    else:
        p4.ChangeDutyCycle(100)
        p5.ChangeDutyCycle(100)
        GPIO.output(pinMAS_4,GPIO.HIGH)
        GPIO.output(pinMENOS_4,GPIO.LOW)
        GPIO.output(pinMAS_5,GPIO.HIGH)
        GPIO.output(pinMENOS_5,GPIO.LOW)
        
        while(True):
            ms=GPIO.input(pin_ms_5)
            if ms== 0:
                print("Home 5")       
                break
            flag=flag+1
            dato = GPIO.input(pin_enc_5)
            if dato==1 and datoanterior==0:
                contador=contador+1
                
                flag = contador
            datoanterior=dato
                
            time.sleep(0.0005)

            if flag>contador+100:
                print('detenido')
                contador=0
                datoanterior=0                        
                GPIO.output(pinMAS_4,GPIO.LOW)
                GPIO.output(pinMENOS_4,GPIO.HIGH)
                GPIO.output(pinMAS_5,GPIO.LOW)
                GPIO.output(pinMENOS_5,GPIO.LOW)
                flag=0
        flag=0
        contador=0
        datoanterior=0         
                
        while True:
            flag=flag+1
            dato = GPIO.input(pin_enc_5)
            if dato==1 and datoanterior==0:
                contador=contador+1
                flag = contador
            datoanterior=dato
                    
            time.sleep(0.0005)
            if contador>=50:
                print('LLego')
                GPIO.output(pinMAS_4,GPIO.LOW)
                GPIO.output(pinMENOS_4,GPIO.LOW)
                GPIO.output(pinMAS_5,GPIO.LOW)
                GPIO.output(pinMENOS_5,GPIO.LOW)            
                break 


    print("HOMING-4...")
    ms=GPIO.input(pin_ms_4)
    if ms== 0:
        print("Home 4")       
        GPIO.output(pinMAS_4,GPIO.LOW)
        GPIO.output(pinMENOS_4,GPIO.LOW)       
        GPIO.output(pinMAS_5,GPIO.LOW)
        GPIO.output(pinMENOS_5,GPIO.LOW)
    else:
        p4.ChangeDutyCycle(100)
        p5.ChangeDutyCycle(100)
        GPIO.output(pinMAS_4,GPIO.LOW)
        GPIO.output(pinMENOS_4,GPIO.HIGH)
        GPIO.output(pinMAS_5,GPIO.HIGH)
        GPIO.output(pinMENOS_5,GPIO.LOW)
        
        while(True):
            ms=GPIO.input(pin_ms_4)
            if ms== 0:
                print("Home 4")       
                break
            flag=flag+1
            dato = GPIO.input(pin_enc_5)
            if dato==1 and datoanterior==0:
                contador=contador+1
                flag = contador
            datoanterior=dato
                
            time.sleep(0.0005)

            if flag>contador+50:
                
                contador=0
                datoanterior=0                        
                GPIO.output(pinMAS_4,GPIO.HIGH)
                GPIO.output(pinMENOS_4,GPIO.LOW)
                GPIO.output(pinMAS_5,GPIO.LOW)
                GPIO.output(pinMENOS_5,GPIO.HIGH)
                flag=0
        flag=0
        contador=0
        datoanterior=0         
                
        while True:
            flag=flag+1
            dato = GPIO.input(pin_enc_5)
            if dato==1 and datoanterior==0:
                contador=contador+1
                flag = contador
            datoanterior=dato
                    
            time.sleep(0.0005)
            if contador>=100 :
                print('LLego')
                GPIO.output(pinMAS_4,GPIO.LOW)
                GPIO.output(pinMENOS_4,GPIO.LOW)
                GPIO.output(pinMAS_5,GPIO.LOW)
                GPIO.output(pinMENOS_5,GPIO.LOW)            
                break        
    
    print("HOMING-6...")
    GPIO.output(pinMAS_6,GPIO.HIGH)
    GPIO.output(pinMENOS_6,GPIO.LOW)
    flag=0
    contador=0
    datoanterior=0         
    while(True):
        flag=flag+1
        dato = GPIO.input(pin_enc_6)
        if dato==1 and datoanterior==0:
            contador=contador+1
          
            flag = contador
        datoanterior=dato
        time.sleep(0.0005)
        if flag>contador+100:
            print('HOME 6')
            GPIO.output(pinMAS_6,GPIO.LOW)
            GPIO.output(pinMENOS_6,GPIO.LOW)
            break
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

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
        print("3. HOME")
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
                matriz = []
                gra1 = []
                gra2 = []
                gra3 = []
                gra4 = []
                gra5 = []
                gra6 = []

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
                                print("Subir y bajar el Antebrazo. Digite movimiento numero %d en el rango[-180,80]:"%(i))
                                t = float(input("Digite movimiento numero %d:"%(i)))
                                if t >= -180 and t<=80:
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
                                print("Subir y bajar la Pinza. Digite movimiento numero %d en el rango[-130,130]:"%(i))
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
                                print("Cerrar y Abrir la Pinza. Digite movimiento numero %d en el rango[-360,360]:"%(i))
                                t = float(input("Digite movimiento numero %d:"%(i)))
                                if t >= -100 and t<=100:
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
                        posicion_1=posicion_1+grado1
                    if grado1 < 0 :
                        GPIO.output(pinMAS_1,GPIO.LOW)
                        GPIO.output(pinMENOS_1,GPIO.HIGH)
                        num = (11052*grado1)/310
                        posicion_1=posicion_1+grado1
                    while(True):
                        flag = flag+1    
                        dato = GPIO.input(pin_enc_1)
                        if dato==1 and datoanterior==0:
                            contador=contador+1
 
                            flag = contador
                        datoanterior=dato
                        time.sleep(0.0005)
                        if contador>=abs(num)-1 :
                            print('LLego Grado 1')
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
                p2.ChangeDutyCycle(100)
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
                        posicion_2=posicion_2+grado2        
                    if grado2 < 0 :
                        GPIO.output(pinMAS_2,GPIO.LOW)
                        GPIO.output(pinMENOS_2,GPIO.HIGH)
                        num = (4529*grado2)/165
                        posicion_2=posicion_2+grado2
                    while(True):
                        flag = flag+1    
                        dato = GPIO.input(pin_enc_2)
                        if dato==1 and datoanterior==0:
                            contador=contador+1
                            flag = contador
                        datoanterior=dato
                        time.sleep(0.0005)
                        if contador>=abs(num)-1 :
                            print('LLego Grado 2')
                            p2.ChangeDutyCycle(30)
                            print("Finalizo el movimiento")
                            GPIO.output(pinMAS_2,GPIO.HIGH)
                            GPIO.output(pinMENOS_2,GPIO.LOW)
                            break
                        if flag>contador+100:
                            print('detenido')
                            GPIO.output(pinMAS_2,GPIO.LOW)
                            GPIO.output(pinMENOS_2,GPIO.LOW)
                            break                         
                    break
                #time.sleep(1)
                p3.ChangeDutyCycle(100)
                while (True):
            
                    #time.sleep(t)
    
                    print("Movimiento %d Giro %d Grados:" % (j,grado3))
                    print("En Movimiento...")
                    j=j+1     
                    flag=0 
                    contador=0  
                    if grado3>= 0:
                        GPIO.output(pinMAS_3,GPIO.LOW)
                        GPIO.output(pinMENOS_3,GPIO.HIGH)                 
                        num = (4842*grado3)/180
                        posicion_3=posicion_3+grado3        
                    if grado3 < 0 :
                        GPIO.output(pinMAS_3,GPIO.HIGH)
                        GPIO.output(pinMENOS_3,GPIO.LOW)
                        num = (1117*grado3)/80
                        posicion_3=posicion_3+grado3
                    while(True):
                        flag = flag+1    
                        dato = GPIO.input(pin_enc_3)
                        if dato==1 and datoanterior==0:
                            contador=contador+1
                            flag = contador
                        datoanterior=dato
                        time.sleep(0.0005)
                        if contador>=abs(num)-1 :
                            print('LLego Grado 3')
                            #p2.ChangeDutyCycle(30)
                            print("Finalizo el movimiento")
                            GPIO.output(pinMAS_3,GPIO.LOW)
                            GPIO.output(pinMENOS_3,GPIO.LOW)
                            break
                        if flag>contador+100:
                            print('detenido')
                            GPIO.output(pinMAS_3,GPIO.LOW)
                            GPIO.output(pinMENOS_3,GPIO.LOW)
                            break                         
                    break
                #time.sleep(1)
                p4.ChangeDutyCycle(100)
                p5.ChangeDutyCycle(100)
                while (True):
            
                    #time.sleep(t)
    
                    print("Movimiento %d Giro %d Grados:" % (j,grado4))
                    print("En Movimiento...")
                    j=j+1     
                    flag=0 
                    contador=0
                    datoanterior=0
                    if grado4>= 0:
                        GPIO.output(pinMAS_4,GPIO.LOW)
                        GPIO.output(pinMENOS_4,GPIO.HIGH)                 
                        GPIO.output(pinMAS_5,GPIO.HIGH)
                        GPIO.output(pinMENOS_5,GPIO.LOW) 
                        num = (1605*grado4)/65
                        posicion_4=posicion_4+grado4        
                    if grado4 < 0 :
                        GPIO.output(pinMAS_4,GPIO.HIGH)
                        GPIO.output(pinMENOS_4,GPIO.LOW)
                        GPIO.output(pinMAS_5,GPIO.LOW)
                        GPIO.output(pinMENOS_5,GPIO.HIGH)                         
                        num = (1605*grado4)/65
                        posicion_4=posicion_4+grado4
                    while(True):
                        flag = flag+1    
                        dato = GPIO.input(pin_enc_4)
                        if dato==1 and datoanterior==0:
                            contador=contador+1
                            print(contador)
                            flag = contador
                        datoanterior=dato
                        time.sleep(0.0005)
                        if contador>=abs(num)-1 :
                            print('LLego Grado 4')
                            #p4.ChangeDutyCycle(30)
                            print("Finalizo el movimiento")
                            GPIO.output(pinMAS_4,GPIO.LOW)
                            GPIO.output(pinMENOS_4,GPIO.LOW)
                            GPIO.output(pinMAS_5,GPIO.LOW)
                            GPIO.output(pinMENOS_5,GPIO.LOW)
                            break
                        if flag>contador+100:
                            print('detenido')
                            GPIO.output(pinMAS_4,GPIO.LOW)
                            GPIO.output(pinMENOS_4,GPIO.LOW)
                            GPIO.output(pinMAS_5,GPIO.LOW)
                            GPIO.output(pinMENOS_5,GPIO.LOW)
                            break
                    break                                 
                
                #time.sleep(1)
                p4.ChangeDutyCycle(100)
                p5.ChangeDutyCycle(100)
                while (True):
            
                    #time.sleep(t)
    
                    print("Movimiento %d Giro %d Grados:" % (j,grado5))
                    print("En Movimiento...")
                    j=j+1     
                    flag=0 
                    contador=0  
                    if grado5>= 0:
                        GPIO.output(pinMAS_4,GPIO.HIGH)
                        GPIO.output(pinMENOS_4,GPIO.LOW)                 
                        GPIO.output(pinMAS_5,GPIO.HIGH)
                        GPIO.output(pinMENOS_5,GPIO.LOW) 
                        num = (2250*grado5)/360
                        posicion_5=posicion_5+grado5        
                    if grado5 < 0 :
                        GPIO.output(pinMAS_4,GPIO.LOW)
                        GPIO.output(pinMENOS_4,GPIO.HIGH)
                        GPIO.output(pinMAS_5,GPIO.LOW)
                        GPIO.output(pinMENOS_5,GPIO.HIGH)                         
                        num = (2250*grado5)/360
                        posicion_5=posicion_5+grado5
                    while(True):
                        flag = flag+1    
                        dato = GPIO.input(pin_enc_4)
                        if dato==1 and datoanterior==0:
                            contador=contador+1
                            flag = contador
                        datoanterior=dato
                        time.sleep(0.0005)
                        if contador>=abs(num)-1 :
                            print('LLego Grado 5')
                            print(contador)
                            #p4.ChangeDutyCycle(30)
                            print("Finalizo el movimiento")
                            GPIO.output(pinMAS_4,GPIO.LOW)
                            GPIO.output(pinMENOS_4,GPIO.LOW)
                            GPIO.output(pinMAS_5,GPIO.LOW)
                            GPIO.output(pinMENOS_5,GPIO.LOW)
                            break
                        if flag>contador+100:
                            print('detenido')
                            GPIO.output(pinMAS_4,GPIO.LOW)
                            GPIO.output(pinMENOS_4,GPIO.LOW)
                            GPIO.output(pinMAS_5,GPIO.LOW)
                            GPIO.output(pinMENOS_5,GPIO.LOW)
                            break                         
                    break
                    
                #time.sleep(1)
                
                while (True):
                    print("Movimiento %d Giro %d Grados:" % (j,grado6))
                    print("En Movimiento...")
                    j=j+1     
                    flag=0 
                    contador=0
                    print(grado6)
                    if grado6>= 0:
                        GPIO.output(pinMAS_6,GPIO.HIGH)
                        GPIO.output(pinMENOS_6,GPIO.LOW)
                        num = (414*grado6)/100
                        posicion_6=posicion_6+grado6
                    if grado6 < 0 :
                        GPIO.output(pinMAS_6,GPIO.LOW)
                        GPIO.output(pinMENOS_6,GPIO.HIGH)
                        num = (446*grado6)/100
                        posicion_6=posicion_6+grado6
                    while(True):
                        flag = flag+1    
                        dato = GPIO.input(pin_enc_6)
                        if dato==1 and datoanterior==0:
                            contador=contador+1
                            flag = contador
                        datoanterior=dato
                        time.sleep(0.0005)
                        if contador>=abs(num)-1 :
                            print('LLego Grado 6')
                            print("Finalizo el movimiento")
                            GPIO.output(pinMAS_6,GPIO.LOW)
                            GPIO.output(pinMENOS_6,GPIO.LOW)
                            break
                        if flag>contador+1000:
                            print('detenido')
                            GPIO.output(pinMAS_6,GPIO.LOW)
                            GPIO.output(pinMENOS_6,GPIO.LOW)
                            break                         

                    break
                #time.sleep(1)
                r=r+1                  
    
    
    
    
    
    
        elif sw == 3:
            print("HOMING-1...")
            ms=GPIO.input(pin_ms_1)
            flag=0
            if ms==0:
                print("Home 1")
                GPIO.output(pinMAS_1,GPIO.LOW)
                GPIO.output(pinMENOS_1,GPIO.LOW)        
            else:
                GPIO.output(pinMAS_1,GPIO.LOW)
                GPIO.output(pinMENOS_1,GPIO.HIGH)
                while(True):
                    ms=GPIO.input(pin_ms_1)
                    if ms== 0:
                        print("Home 1")       
                        break
                    flag=flag+1
                    dato = GPIO.input(pin_enc_1)
                    if dato==1 and datoanterior==0:
                        contador=contador+1
                        flag = contador
                    datoanterior=dato
                            
                    time.sleep(0.0005)
                    if flag>contador+100:
                        contador=0
                        datoanterior=0                        
                        GPIO.output(pinMAS_1,GPIO.HIGH)
                        GPIO.output(pinMENOS_1,GPIO.LOW)

                time.sleep(0.0005)
                contador=0
                datoanterior=0     
                while True:
                    dato = GPIO.input(pin_enc_1)
                    if dato==1 and datoanterior==0:
                        contador=contador+1
                    datoanterior=dato
                    time.sleep(0.0005)
                    if contador>=74 :
                        print('LLego')
                        GPIO.output(pinMAS_1,GPIO.LOW)
                        GPIO.output(pinMENOS_1,GPIO.LOW)
                        break

            print("HOMING-2...")
            p2.ChangeDutyCycle(100)
            GPIO.output(pinMAS_2,GPIO.HIGH)
            GPIO.output(pinMENOS_2,GPIO.LOW)   
            flag=0
            contador=0
            datoanterior=0         
            while(True):
                flag=flag+1
                dato = GPIO.input(pin_enc_2)
                if dato==1 and datoanterior==0:
                    contador=contador+1
                    #print(contador)
                    flag = contador
                datoanterior=dato
                time.sleep(0.0005)
                if flag>contador+100:
                    print('HOME 2')
                    GPIO.output(pinMAS_2,GPIO.LOW)
                    GPIO.output(pinMENOS_2,GPIO.LOW)
                    break
                
            print("HOMING-3...")
            p3.ChangeDutyCycle(100)
            ms=GPIO.input(pin_ms_3)
            flag=0
            if ms== 0:
                print("Home 3")       
                GPIO.output(pinMAS_3,GPIO.LOW)
                GPIO.output(pinMENOS_3,GPIO.LOW)
            else:
                GPIO.output(pinMAS_3,GPIO.LOW)
                GPIO.output(pinMENOS_3,GPIO.HIGH)
                while(True):
                    ms=GPIO.input(pin_ms_3)
                    if ms== 0:
                        print("Home 3")       
                        break
                    flag=flag+1
                    dato = GPIO.input(pin_enc_3)
                    if dato==1 and datoanterior==0:
                        contador=contador+1
                        flag = contador
                    datoanterior=dato
                        
                    time.sleep(0.0005)

                    if flag>contador+100:
                            #print('detenido')
                        contador=0
                        datoanterior=0
                        flag=0
                        GPIO.output(pinMAS_3,GPIO.HIGH)
                        GPIO.output(pinMENOS_3,GPIO.LOW)
                
                flag=0
                contador=0
                datoanterior=0         
                        
                while True:
                    flag=flag+1
                    dato = GPIO.input(pin_enc_3)
                    if dato==1 and datoanterior==0:
                        contador=contador+1
                        flag = contador
                    datoanterior=dato
                            
                    time.sleep(0.0005)
                    if contador>=300 :
                        print('LLego')
                        GPIO.output(pinMAS_3,GPIO.LOW)
                        GPIO.output(pinMENOS_3,GPIO.LOW)
                        break        


            print("HOMING-5...")
            
            ms=GPIO.input(pin_ms_5)
            if ms== 0:
                print("Home 5")       
                GPIO.output(pinMAS_4,GPIO.LOW)
                GPIO.output(pinMENOS_4,GPIO.LOW)       
                GPIO.output(pinMAS_5,GPIO.LOW)
                GPIO.output(pinMENOS_5,GPIO.LOW)
                
            else:
                p4.ChangeDutyCycle(100)
                p5.ChangeDutyCycle(100)
                GPIO.output(pinMAS_4,GPIO.HIGH)
                GPIO.output(pinMENOS_4,GPIO.LOW)
                GPIO.output(pinMAS_5,GPIO.HIGH)
                GPIO.output(pinMENOS_5,GPIO.LOW)
                
                while(True):
                    ms=GPIO.input(pin_ms_5)
                    if ms== 0:
                        print("Home 5")       
                        break
                    flag=flag+1
                    dato = GPIO.input(pin_enc_5)
                    if dato==1 and datoanterior==0:
                        contador=contador+1
                        
                        flag = contador
                    datoanterior=dato
                        
                    time.sleep(0.0005)

                    if flag>contador+100:
                        print('detenido')
                        contador=0
                        datoanterior=0                        
                        GPIO.output(pinMAS_4,GPIO.LOW)
                        GPIO.output(pinMENOS_4,GPIO.HIGH)
                        GPIO.output(pinMAS_5,GPIO.LOW)
                        GPIO.output(pinMENOS_5,GPIO.LOW)
                        flag=0
                flag=0
                contador=0
                datoanterior=0         
                        
                while True:
                    flag=flag+1
                    dato = GPIO.input(pin_enc_5)
                    if dato==1 and datoanterior==0:
                        contador=contador+1
                        flag = contador
                    datoanterior=dato
                            
                    time.sleep(0.0005)
                    if contador>=50:
                        print('LLego')
                        GPIO.output(pinMAS_4,GPIO.LOW)
                        GPIO.output(pinMENOS_4,GPIO.LOW)
                        GPIO.output(pinMAS_5,GPIO.LOW)
                        GPIO.output(pinMENOS_5,GPIO.LOW)            
                        break 


            print("HOMING-4...")
            ms=GPIO.input(pin_ms_4)
            if ms== 0:
                print("Home 4")       
                GPIO.output(pinMAS_4,GPIO.LOW)
                GPIO.output(pinMENOS_4,GPIO.LOW)       
                GPIO.output(pinMAS_5,GPIO.LOW)
                GPIO.output(pinMENOS_5,GPIO.LOW)
            else:
                p4.ChangeDutyCycle(100)
                p5.ChangeDutyCycle(100)
                GPIO.output(pinMAS_4,GPIO.LOW)
                GPIO.output(pinMENOS_4,GPIO.HIGH)
                GPIO.output(pinMAS_5,GPIO.HIGH)
                GPIO.output(pinMENOS_5,GPIO.LOW)
                
                while(True):
                    ms=GPIO.input(pin_ms_4)
                    if ms== 0:
                        print("Home 4")       
                        break
                    flag=flag+1
                    dato = GPIO.input(pin_enc_5)
                    if dato==1 and datoanterior==0:
                        contador=contador+1
                        flag = contador
                    datoanterior=dato
                        
                    time.sleep(0.0005)

                    if flag>contador+50:
                        
                        contador=0
                        datoanterior=0                        
                        GPIO.output(pinMAS_4,GPIO.HIGH)
                        GPIO.output(pinMENOS_4,GPIO.LOW)
                        GPIO.output(pinMAS_5,GPIO.LOW)
                        GPIO.output(pinMENOS_5,GPIO.HIGH)
                        flag=0
                flag=0
                contador=0
                datoanterior=0         
                        
                while True:
                    flag=flag+1
                    dato = GPIO.input(pin_enc_5)
                    if dato==1 and datoanterior==0:
                        contador=contador+1
                        flag = contador
                    datoanterior=dato
                            
                    time.sleep(0.0005)
                    if contador>=100 :
                        print('LLego')
                        GPIO.output(pinMAS_4,GPIO.LOW)
                        GPIO.output(pinMENOS_4,GPIO.LOW)
                        GPIO.output(pinMAS_5,GPIO.LOW)
                        GPIO.output(pinMENOS_5,GPIO.LOW)            
                        break        
            
            print("HOMING-6...")
            GPIO.output(pinMAS_6,GPIO.HIGH)
            GPIO.output(pinMENOS_6,GPIO.LOW)
            flag=0
            contador=0
            datoanterior=0         
            while(True):
                flag=flag+1
                dato = GPIO.input(pin_enc_6)
                if dato==1 and datoanterior==0:
                    contador=contador+1
                    #print(contador)
                    flag = contador
                datoanterior=dato
                time.sleep(0.0005)
                if flag>contador+100:
                    print('HOME 6')
                    GPIO.output(pinMAS_6,GPIO.LOW)
                    GPIO.output(pinMENOS_6,GPIO.LOW)
                    break

                            
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
#    GPIO.output(pinMAS_6,GPIO.LOW)
#    GPIO.output(pinMENOS_6,GPIO.LOW)    
#   GPIO.cleanup()       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
