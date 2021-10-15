#!/usr/bin/env python3

#coba pub ke motr dari gazebo

import rospy
from std_msgs.msg import Float64, String
from geometry_msgs.msg import Twist
#import pyfirmata
import time
import math

#board = pyfirmata.Arduino('/dev/ttyACM0')


#it = pyfirmata.util.Iterator(board)
#it.start()
#print("Communication Successfully started")
#motor1r = board.get_pin('d:9:p')
#motor1l = board.get_pin('d:10:p')

#motor2r = board.get_pin('d:11:p')
#motor2l = board.get_pin('d:3:p')

#motor3r = board.get_pin('d:5:p')
#motor3l = board.get_pin('d:6:p')

def motor1pub_callback(msg):
    
    V1 = msg.data
    V1 = float(V1/10)
    
    print ("nilai V1 = ", V1)
          
#    if V1 >= 0.0:
#        motor1r.write(V1)
#        motor1l.write(0)
#    else:
#        motor1r.write(0)
#        motor1l.write(-V1)
    

def motor2pub_callback(msg):
    
    V2 = msg.data
    V2 = float(V2/10)
    
    print ("nilai V2 = ", V2)
          
#    if V2 >= 0.0:
#        motor2r.write(V2)
#        motor2l.write(0)
#    else:
#        motor2r.write(0)
#        motor2l.write(-V2)


def motor3pub_callback(msg):
    
    V3 = msg.data
    V3 = float(V3/10)
    
    print ("nilai V3 = ", V3)
          
#    if V3 >= 0.0:
#        motor3r.write(V3)
#        motor3l.write(0)
#    else:
#        motor3r.write(0)
#        motor3l.write(-V3)              
   

def motor():
    rospy.init_node('Ke_motor', anonymous=False)
    rospy.Subscriber("/data_pid_roda1_from_arduino", Float64, motor1pub_callback)
    # rospy.Subscriber("/data_pid_roda2_from_arduino", Float64, motor2pub_callback)
    # rospy.Subscriber("/data_pid_roda3_from_arduino", Float64, motor3pub_callback)
    rospy.spin()         
    
if __name__ == '__main__':
    motor()
