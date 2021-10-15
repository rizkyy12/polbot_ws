#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64, String
from geometry_msgs.msg import Twist
import pyfirmata
import time
import math

board = pyfirmata.Arduino('/dev/ttyACM0')


it = pyfirmata.util.Iterator(board)
it.start()
print("Communication Successfully started")
motor1r = board.get_pin('d:9:p')
motor1l = board.get_pin('d:10:p')

motor2r = board.get_pin('d:11:p')
motor2l = board.get_pin('d:3:p')

motor3r = board.get_pin('d:5:p')
motor3l = board.get_pin('d:6:p')

def motorpub_callback(msg):
    
    V1 = msg.data
    V1 = 0.0
    
    print ("nilai V1 = ", V1)
    #print ("nilai V2 = "+ str(V2))
    #print ("nilai V3 = "+ str(V3))
          
    if V1 >= 0.0:
        motor3r.write(V1)
        motor3l.write(0)
    else:
        motor3r.write(0)
        motor3l.write(-V1)
        
    #if V2 >= 0.0:
    #    motor2r.write(V2)
    #    motor2l.write(0)
    #else:
    #    motor2r.write(0)
    #    motor2l.write(-V2)

    #if V3 >= 0.0:
    #    motor3r.write(V3)
    #    motor3l.write(0)
    #else:
    #    motor3r.write(0)
    #    motor3l.write(-V3)
   
def motor():
    rospy.init_node('motorsub', anonymous=False)
    rospy.Subscriber("/vel_roda1", Float64, motorpub_callback)
    rospy.spin()
    
if __name__ == '__main__':
    motor()
