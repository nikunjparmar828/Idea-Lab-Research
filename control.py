#Author : Nikunj Parmar , Abhimanyu Shanbhag
import pandas as pd
import numpy as np

import RPi.GPIO as GPIO
import time

#setting up GPIO  
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
p=GPIO.PWM(7,207)
GPIO.setup(11,GPIO.OUT)
q=GPIO.PWM(11,207)

#reading data and creating data table
control_data=pd.read_csv("control.csv")


control_data['r']= ((control_data.x)**2+(control_data.y)**2)**0.5


control_data['theta']=np.rad2deg(np.arctan(control_data.y/control_data.x))

control_data['del_r']=control_data.r
control_data['del_theta']=control_data.theta

for i in range(28):
    control_data.iloc[i+1,5]=control_data.iloc[i+1,3]-control_data.iloc[i,3]
    control_data.iloc[i+1,6]=control_data.iloc[i+1,4]-control_data.iloc[i,4]
 
print("Data Table:")
control_data  
    
#function to perform linear actuation
def actuate(d_r):
    
    
    if (d_r>0):
        p.start(0)
        i=(d_r/(0.33))*1
        for j in range (0,i):
            p.changeDutyCycle(100)
        p.stop()
        print("Forward actuation = %2.3f",d_r)
        
    
    if (d_r<0):
        q.start(0)
        i=(d_r/(0.33))*1
        for j in range (0,i):
            q.changeDutyCycle(100)
        q.stop()
        print("Reverse actuation = %2.3f",d_r)
    
  

#function to perform rotation using L293D IC and DC Motor
def rotate(d_theta):
    
    if (d_theta>0):
        p.start(0)
        i=(d_theta/(4.2))*1
        for j in range (0,i):
            p.changeDutyCycle(100)
        p.stop()    
        print("Clockwise rotation = %2.3f",d_r)    
    
    if (d_theta<0):
        q.start(0)
        i=(d_theta/(4.2))*1
        for j in range (0,i):
            q.changeDutyCycle(100)
        q.stop()
        print("Anti-Clockwise rotation = %2.3f",d_r)
    
        
#commence operation        
for i in range(1,29,1):
    d_r=control_data.iloc[i,5]
    d_theta=control_data.iloc[i,6]
    
    actuate(d_r)
    rotate(d_theta)    
GPIO.cleanup()
