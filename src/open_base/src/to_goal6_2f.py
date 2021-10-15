#!/usr/bin/env python

# 3 robot

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2
import math
import numpy as np
import time

x3=0
y3=0
z3=0
yaw3=0

x1=0
y1=0
z1=0
yaw1=0

x2=0
y2=0
z2=0
yaw2=0

varA=0
x1a = 0
y1a = 0

def move1Callback (pose_message): #gerak ke 1
    global x1
    global y1, z1, yaw1
    global x1a, y1a
    global varA

    x1=pose_message.pose.pose.position.x
    y1=pose_message.pose.pose.position.y

    rot_q1 = pose_message.pose.pose.orientation 
    (roll1, pitch1, yaw1) = euler_from_quaternion([rot_q1.x, rot_q1.y, rot_q1.z, rot_q1.w])

    #simpan posisi robot2
    if (varA == 0):
        x1a = x1 
        y1a = y1
        varA = 1
        

def goal1Callback (pose_message): #tujuan 1
    global x_goal1
    global y_goal1
    x_goal1=pose_message.pose.pose.position.x
    y_goal1=pose_message.pose.pose.position.y

def go_to_goal1 (x_goal1, y_goal1):
    global x1
    global y1, z1, yaw1

    velocity_message = Twist()
    # cmd_vel_topic='/tb3_1/cmd_vel'

    while (True):
        e_x = abs(x_goal1-x1)
        e_y = abs(y_goal1-y1)

        distance = abs(math.sqrt(((x_goal1-x1) ** 2) + ((y_goal1-y1) ** 2)))
        K_angular = 4.0 
        desired_angle_goal = math.atan2(y_goal1-y1, x_goal1-x1)         # tetha 

        v = 0.8
        vx = v*(math.cos(desired_angle_goal))
        vy = v*(math.sin(desired_angle_goal))
        
        # resultan
        # linear_speed = abs(math.sqrt((vx**2)+(vy**2)+(2*vx*vy*(math.cos(desired_angle_goal)))))
        # omega
        angular_speed = (desired_angle_goal-yaw1)*K_angular
        
        # velLinear = (v - linear_speed)*K_linear   # <--
        # velocity_message.linear.x = velLinear     # <--
        
        velocity_message.linear.x = abs (0.6*(math.cos(desired_angle_goal)))
        velocity_message.linear.y = abs (0.6*(math.sin(desired_angle_goal)))
        velocity_message.angular.z = angular_speed
        
        velocity_publisher.publish(velocity_message)
        print 'x1=',x1, 'y1=',y1
        # print 'distance = ',distance, 'speed =', linear_speed
        
        if (4 > distance > 2):
            velocity_message.linear.x = abs(2.0* e_x *(math.cos(desired_angle_goal)))
            velocity_message.linear.y = abs(2.0* e_y *(math.sin(desired_angle_goal)))
     	    velocity_message.angular.z= angular_speed
        elif (distance < 1):
            velocity_message.linear.x = 0.0
            velocity_message.linear.y = 0.0
            velocity_message.angular.z = 0.0
            velocity_publisher.publish(velocity_message)
            break

#################################

def move2Callback (pose_message): #gerak ke 2
    global x2
    global y2, z2, yaw2
    x2=pose_message.pose.pose.position.x
    y2=pose_message.pose.pose.position.y

    rot_q2 = pose_message.pose.pose.orientation 
    (roll2, pitch2, yaw2) = euler_from_quaternion([rot_q2.x, rot_q2.y, rot_q2.z, rot_q2.w])

def goal2Callback (pose_message): #tujuan 2
    global x_goal2
    global y_goal2
    x_goal2=pose_message.pose.pose.position.x
    y_goal2=pose_message.pose.pose.position.y    

def go_to_goal2 (x_goal2, y_goal2):
    global x2
    global y2, z2, yaw2

    velocity_message = Twist()
    # cmd_vel_topic='/tb3_1/cmd_vel'

    while(True):
        e_x= abs(x_goal2-x2)
        e_y= abs(y_goal2-y2)
        distance = abs(math.sqrt(((x_goal2-x2) ** 2) + ((y_goal2-y2) ** 2)))
        K_angular = 4.0 
        desired_angle_goal = math.atan2(y_goal2-y2, x_goal2-x2)         # tetha 

        v = 0.8
        vx = v*(math.cos(desired_angle_goal))
        vy = v*(math.sin(desired_angle_goal))

        #resultan
        # linear_speed = abs(math.sqrt((vx**2)+(vy**2)+(2*vx*vy*(math.cos(desired_angle_goal)))))
        #omega
        angular_speed = (desired_angle_goal-yaw2)*K_angular
        
        # velLinear = (v - linear_speed)*K_linear   # <--
        # velocity_message.linear.x = velLinear     # <--
        
        velocity_message.linear.x = abs(0.6 *(math.cos(desired_angle_goal)))
        velocity_message.linear.y = abs(0.6 *(math.sin(desired_angle_goal)))
        velocity_message.angular.z = angular_speed
        
        velocity_publisher1.publish(velocity_message)
        print 'x2=',x2, 'y2=',y2
        # print 'distance = ',distance, 'speed =', linear_speed
    
        if (4 > distance > 2):
            velocity_message.linear.x = abs(2.0 * e_x *(math.cos(desired_angle_goal))) 
            velocity_message.linear.y = abs(2.0 * e_y *(math.sin(desired_angle_goal)))
            velocity_message.angular.z= angular_speed
        elif (distance < 1):
            velocity_message.linear.x = 0.0
            velocity_message.linear.y = 0.0
            velocity_message.angular.z = 0.0
            velocity_publisher1.publish(velocity_message)
            break
        
#################################

def move3Callback (pose_message): #gerak ke 3
    global x3
    global y3, z3, yaw3
    x3=pose_message.pose.pose.position.x
    y3=pose_message.pose.pose.position.y

    rot_q3 = pose_message.pose.pose.orientation 
    (roll3, pitch3, yaw3) = euler_from_quaternion([rot_q3.x, rot_q3.y, rot_q3.z, rot_q3.w])

def goal3Callback (pose_message): #tujuan 3
    global x_goal3
    global y_goal3
    x_goal3=pose_message.pose.pose.position.x
    y_goal3=pose_message.pose.pose.position.y    

# def go_to_goal3 (x_goal3, y_goal3):
def go_to_goal3 (x1a,y1a):
    global x3
    global y3, z3, yaw3

    velocity_message = Twist()
    # cmd_vel_topic='/tb3_1/cmd_vel'

    while (True):
        e_x = abs(x1a-x3)
        e_y = abs(y1a-y3)
        
        distance = abs(math.sqrt(((x1a-x3) ** 2) + ((y1a-y3) ** 2)))
        K_angular = 4.0 
        desired_angle_goal = math.atan2(y1a-y3, x1a-x3)         # tetha 

        v = 0.8
        vx = v*(math.cos(desired_angle_goal))
        vy = v*(math.sin(desired_angle_goal))

        #resultan
        # linear_speed = abs(math.sqrt((vx**2)+(vy**2)+(2*vx*vy*(math.cos(desired_angle_goal)))))
        #omega
        angular_speed = (desired_angle_goal-yaw3)*K_angular
        
        # velLinear = (v - linear_speed)*K_linear   # <--
        # velocity_message.linear.x = velLinear     # <--
        
        velocity_message.linear.x = abs(0.6*(math.cos(desired_angle_goal)))
        velocity_message.linear.y = abs(0.6*(math.sin(desired_angle_goal)))
        velocity_message.angular.z = angular_speed
        
        velocity_publisher2.publish(velocity_message)
        print 'x3=',x3, 'y3=',y3
        print 'distance = ',distance
        print 'x1a =', x1a, 'y1a =',y1a
	
        if (4 > distance > 2):
            velocity_message.linear.x = abs(2.0* e_x *(math.cos(desired_angle_goal))) 
            velocity_message.linear.y = abs(2.0* e_y *(math.sin(desired_angle_goal)))
     	    velocity_message.angular.z= angular_speed 
        elif (distance < 1):
            velocity_message.linear.x = 0.0
            velocity_message.linear.y = 0.0
            velocity_message.angular.z = 0.0
            velocity_publisher2.publish(velocity_message)
            break
#===============================================================================

if __name__ == '__main__':
    try:

        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        #declare velocity publisher
        # cmd_vel_topic = '/tb3_0/cmd_vel'
        velocity_publisher = rospy.Publisher('/tb3_0/cmd_vel',Twist,queue_size=10)
        # position_topic = '/tb3_0/odom'
        pose_subscriber = rospy.Subscriber('/tb3_0/odom', Odometry, move1Callback)

        # position_topic1 = '/tb3_2/odom'
        pose_subscriber1 = rospy.Subscriber('/tb3_2/odom', Odometry, goal1Callback)

        time.sleep(2)

        go_to_goal1(x_goal1 ,y_goal1) # tujuan 1

        time.sleep(2)

        # cmd_vel_topic1 = '/tb3_2/cmd_vel'
        velocity_publisher1 = rospy.Publisher('/tb3_2/cmd_vel',Twist,queue_size=10)
        # position_topic1 = '/tb3_2/odom'
        pose_subscriber2 = rospy.Subscriber('/tb3_2/odom', Odometry, move2Callback)

        # position_topic2 = '/tb3_1/odom'
        pose_subscriber3 = rospy.Subscriber('/tb3_1/odom', Odometry, goal2Callback)

        time.sleep(2)

        go_to_goal2(x_goal2 ,y_goal2) # tujuan 2

        time.sleep(2)

        # cmd_vel_topic2 = '/tb3_1/cmd_vel'
        velocity_publisher2 = rospy.Publisher('/tb3_1/cmd_vel',Twist,queue_size=10)
        # position_topic2 = '/tb3_1/odom'
        pose_subscriber4 = rospy.Subscriber('/tb3_1/odom', Odometry, move3Callback)

        # position_topic3 = '/tb3_0/odom'
        # pose_subscriber5 = rospy.Subscriber(position_topic3, Odometry, goal3Callback)

        time.sleep(2)

        # go_to_goal3(-3.0 ,-1.0) # tujuan 3
        go_to_goal3(x1a,y1a)

        time.sleep(2)

        
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated")    
            
