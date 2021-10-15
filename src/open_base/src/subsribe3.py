#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import pyfirmata
import time
import math

board = pyfirmata.Arduino('/dev/ttyACM0')
print("Communication Successfully started")

it = pyfirmata.util.Iterator(board)
it.start()

motor1r = board.get_pin('d:9:p')
motor1l = board.get_pin('d:10:p')

motor2r = board.get_pin('d:11:p')
motor2l = board.get_pin('d:3:p')

motor3r = board.get_pin('d:5:p')
motor3l = board.get_pin('d:6:p')

def motorpub_callback(msg):
    print ("velocity linear x = " + str(msg.linear.x))
    print ("velocity linear y = " + str(msg.linear.y))    
    print ("velocity angular z = "+ str(msg.angular.z))
    V_m_x = msg.linear.x
    V_m_y = msg.linear.y
    L_omega_p = msg.angular.z
    
    V1 = (-V_m_x / 2.0) - (math.sqrt(3) * V_m_y / 2.0) + L_omega_p
    V2 = V_m_x + L_omega_p
    V3 = (-V_m_x / 2.0) + (math.sqrt(3) * V_m_y / 2.0) + L_omega_p
    
    print ("nilai V1 = "+ str(V1))
    print ("nilai V2 = "+ str(V2))
    print ("nilai V3 = "+ str(V3))
          
    if V1 >= 0.0:
        motor1r.write(V1)
        motor1l.write(0)
    else:
        motor1r.write(0)
        motor1l.write(-V1)
        
    if V2 >= 0.0:
        motor2r.write(V2)
        motor2l.write(0)
    else:
        motor2r.write(0)
        motor2l.write(-V2)

    if V3 >= 0.0:
        motor3r.write(V3)
        motor3l.write(0)
    else:
        motor3r.write(0)
        motor3l.write(-V3)
   
def motor():
    rospy.init_node('motorsub', anonymous=False)
    rospy.Subscriber("cmd_vel", Twist, motorpub_callback)
    rospy.spin()
    
if __name__ == '__main__':
    motor()