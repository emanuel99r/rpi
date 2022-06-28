import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

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
#pin_ms_6=
pinMAS_6=23
pinMENOS_6=33


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
GPIO.setup(pinMAS_4,GPIO.OUT)
GPIO.setup(pinMENOS_4,GPIO.OUT)
GPIO.setup(pinMAS_5,GPIO.OUT)
GPIO.setup(pinMENOS_5,GPIO.OUT)
GPIO.setup(pinMAS_6,GPIO.OUT)
GPIO.setup(pinMENOS_6,GPIO.OUT)
#PIO.setup(pinMAS_2,GPIO.OUT)
#GPIO.setup(pinMENOS_2,GPIO.OUT)
p2=GPIO.PWM(pin_pwm_2,1000)
p2.start(100)

contador=0
dato=0
datoanterior=0
flag=0
try:
    x = float(raw_input("angulo:"))
    p2.ChangeDutyCycle(100)
    if x>= 0:
        GPIO.output(pinMAS_2,GPIO.HIGH)
        GPIO.output(pinMENOS_2,GPIO.LOW)
        #GPIO.output(pinMAS_2,GPIO.LOW)
        #GPIO.output(pinMENOS_2,GPIO.HIGH)
        num = (11030*x)/310        
    elif x< 0 :
        GPIO.output(pinMAS_2,GPIO.LOW)
        GPIO.output(pinMENOS_2,GPIO.HIGH)
                #GPIO.output(pinMAS_2,GPIO.HIGH)
                #GPIO.output(pinMENOS_2,GPIO.LOW)
        num=(11030*x)/310
        


    while(True):
        flag=flag+1
        dato = GPIO.input(pin_enc_2)
        if dato==1 and datoanterior==0:
            contador=contador+1
            print(contador)
            flag = contador
        datoanterior=dato
                
        time.sleep(0.0005)
        #if contador>=abs(num)-10 :
                 #       print('LLego')
                  #      GPIO.output(pinMAS,GPIO.LOW)
                   #     GPIO.output(pinMENOS,GPIO.LOW)
                    #    GPIO.output(pinMAS_2,GPIO.LOW)
                     #   GPIO.output(pinMENOS_2,GPIO.LOW)
                      #  break
        #if flag>contador+1000000:
                 #       print('detenido')
                  #      GPIO.output(pinMAS,GPIO.LOW)
                   #     GPIO.output(pinMENOS,GPIO.LOW)
                    #    break
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
#        GPIO.output(pinMAS_2,GPIO.LOW)
 #       GPIO.output(pinMENOS_2,GPIO.LOW)
 #   GPIO.cleanup()
