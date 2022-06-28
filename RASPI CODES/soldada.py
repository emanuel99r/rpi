
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)









GPIO.setup(3, GPIO.OUT)


GPIO.output(3, GPIO.HIGH)
