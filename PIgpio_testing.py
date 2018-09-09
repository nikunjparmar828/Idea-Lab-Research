
#Author : Nikunj Parmar

import time
import pigpio

servos = 11 #gpio no

pigpio.start()

try:
    while True:
        pigpio.set_servo_pulsewidth(servos, 500)
        print("servo {} {} micro pulses".format(servos, 1000))
        time.sleep(1)
        pigpio.set_servo_pulsewidth(servos, 1500)
        print("servo {} {} micro pulses".format(servos, 1500))
        time.sleep(1)
        pigpio.set_servo_pulsewidth(servos, 2500)
        print("servo {} {} micro pulses".format(servos, 2500))
        time.sleep(1)
        pigpio.set_servo_pulsewidth(servos, 1500)
        print("servo {} {} micro pulses".format(servos, 1500))
        time.sleep(1)
except KeyboardInterrupt:
    pigpio.set_servo_pulsewidth(servos, 0)

pigpio.stop()
