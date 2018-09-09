import RPi.GPIO as GPIO
from numpy import linspace

import time

GPIO.setmode(GPIO.BOARD)

pin_number = 13
GPIO.setup(pin_number, GPIO.OUT)
  
frequency_hertz = 50
pwm = GPIO.PWM(pin_number, frequency_hertz) 

# I'll store a sequence of positions for use in a loop later on
pwm.start(0)

while True:
        pwm.ChangeDutyCycle(2.5)
        time.sleep(1)
        pwm.ChangeDutyCycle(12.5)
        time.sleep(1)
        
	

pwm.stop()


GPIO.cleanup()
