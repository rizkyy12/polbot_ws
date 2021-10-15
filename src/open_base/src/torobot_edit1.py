#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64, UInt8
from open_base.msg import Movement, MovementGeneric
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist, Quaternion, Pose2D
from math import atan2, cos, sin
import math
import numpy as np
import time

x, x1 =0,0
y, y1 =0,0
z, z1 =0,0
yaw, yaw1 =0,0

ex, ex1 =0,0
ey, ey1 =0,0

varA=0
x1a = 0
y1a = 0 

def posisiawal(pasan):
    global x
    global y, z, yaw
    global x1a, y1a
    global varA

    x= pasan.pose.pose.position.x
    y= pasan.pose.pose.position.y

    rot_q = pasan.pose.pose.orientation
    (roll, pitch, yaw) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

    #simpan posisi robot1
    if (varA == 0):
            x1a = x
            y1a = y
            varA += 1
    
def posisi1(pasan):
    global x_goal
    global y_goal

    x_goal=pasan.pose.pose.position.x
    y_goal=pasan.pose.pose.position.y


def dari1ke2(x_goal, y_goal):
    global x
    global y, z, yaw
    global ex, ey
    
    velocity_publisher = rospy.Publisher('/open_base1/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 2
    vel.generic.frame = 3
    #vel.generic.target.x = 0.5
    #vel.generic.target.y = 0.0
    #movePub1.publish(vel)
    #print ('openbase1')
    #velocity_message = Twist()
    #cmd_vel_topic = '/open_base1/command'

    while(True):
        K_linear = 0.1
        distance = abs(math.sqrt(((x_goal-x)**2) + ((y_goal-y)**2)))
        ex = x_goal-x
        ey = y_goal-y
        K_angular = 4.0 
        desired_angle_goal = math.atan2(y_goal-y, x_goal-x)
        angular_speed = (desired_angle_goal - yaw)*K_angular
	
	#linear_speed = distance * K_linear

        vel.generic.target.x = abs(K_linear*ex*math.cos(desired_angle_goal)) - (K_linear*ey*math.sin(desired_angle_goal))
        vel.generic.target.y = (K_linear*ex*math.sin(desired_angle_goal)) + (K_linear*ey*math.cos(desired_angle_goal))
        vel.generic.target.theta = angular_speed

        velocity_publisher.publish(vel)
        print('x', x, 'y=',y)
	
        if(distance<0.5):
                vel.generic.target.x=0.0
                vel.generic.target.theta=0.0
                velocity_publisher.publish(vel)
                break



if __name__ == '__main__':
    try:
	
        rospy.init_node('Openbase', anonymous = True)

	#Robot 1 ke Robot2
        velocity_publisher = rospy.Publisher('/open_base1/command', Movement, queue_size=1)   
        odom_subscriber = rospy.Subscriber("/open_base1/pose/world", Odometry, posisiawal)
        time.sleep(1)
        odim_subscriber = rospy.Subscriber('/open_base2/pose/world', Odometry, posisi1)
        time.sleep(1)
        dari1ke2(x_goal, y_goal)
        time.sleep(1)
        
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")

