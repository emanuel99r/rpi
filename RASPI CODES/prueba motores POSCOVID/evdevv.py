'''
from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')
print(gamepad)
for event in gamepad.read_loop():
	if event.type == ecodes.EV_KEY:
		print(categorize(event))
'''
# Rotary encoder using evdev
# Add to /boot/config.txt
#  dtoverlay=rotary-encoder,pin_a=20,pin_b=21,relative_axis=1,steps-per-period=2
# Tweak pins and steps to match the encoder
 
import evdev
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
d = evdev.InputDevice('/dev/input/event0')
print('Rotary encoder device: {}'.format(d.name))
GPIO.setup(31,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(29,GPIO.IN, pull_up_down=GPIO.PUD_UP) 
position = 0
 
for e in d.read_loop():
    print('Event: {}'.format(e))
    if e.type == evdev.ecodes.EV_REL:
        position += e.value
        print('Position: {}'.format(position))
