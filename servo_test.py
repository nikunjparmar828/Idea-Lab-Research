'''
Author: Abhimanyu Shanbhag, Nikunj Parmar
'''


import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
p = GPIO.PWM(7, 207)
GPIO.setup(11, GPIO.OUT)
q = GPIO.PWM(11, 207)

# Servo specific action
GPIO.setup(13, GPIO.OUT)
r = GPIO.PWM(13, 50)
 
p.start(0)

##x = [j for j in range(10,110,20)]
##
##
##
##       

x = [3]*100
"""
for i in x:
    lst = range(0, i)
"""

for j in range(5):            
    p.ChangeDutyCycle(100)
    time.sleep(0.02)

    p.ChangeDutyCycle(0)
    print('forward actuation complete')
    p.stop()
    time.sleep(2)
    p.start(0)


q.start(0)

for i in range(5):
   q.ChangeDutyCycle(100)
   time.sleep(0.02)
   
   q.ChangeDutyCycle(0)
   print('reverse actuation complete')
   q.stop()
   time.sleep(2)
   q.start(0)


GPIO.cleanup()
        
    
