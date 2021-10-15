#!/usr/bin/env python3

# -------- Gerakin dr R1 ke R3

import rospy
from std_msgs.msg import Float64, UInt8
from open_base.msg import Movement, MovementGeneric
from geometry_msgs.msg import Pose2D

from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2
import math
import numpy as np
import time

x1 = 0
y1 = 0
z1 = 0

x3 = 0
y3 = 0
z3 = 0


def printOdom():
    global x1, y1, z1
    global x2, y2, z2
    global x3, y3, z3

    print('x1= ', x1, 'y1= ', y1, 'x2=', x2, 'y2=',
          y2, 'x3= ', x3, 'y3= ', y3)


def getOdomR1(msg):
    global x1, y1, z1

    x1 = msg.pose.pose.position.x
    y1 = msg.pose.pose.position.y
    z1 = msg.pose.pose.orientation.w

    print('x1=', x1, 'y1=', y1)

def getOdomR3(msg):
    global x3, y3, z3

    x3 = msg.pose.pose.position.x
    y3 = msg.pose.pose.position.y
    z3 = msg.pose.pose.orientation.w


def open_base1():
    global x3,y3

    movePub1 = rospy.Publisher('/open_base1/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 0
    vel.generic.frame = 3
    vel.generic.target.x = x3
    vel.generic.target.y = y3
    movePub1.publish(vel)

def open_base3():
    movePub1 = rospy.Publisher('/open_base3/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 0
    vel.generic.frame = 3
    vel.generic.target.x = 2.0
    vel.generic.target.y = 1.0
    movePub1.publish(vel)


if __name__ == '__main__':
    try:
        while (True):
            while not rospy.is_shutdown():
                rospy.init_node('OpenbaseJOSSSSSS')

                rospy.Subscriber('/my_odom_r1', Odometry, getOdomR1)
                rospy.Subscriber('/my_odom_r3', Odometry, getOdomR3)

                open_base1()
                open_base3()


                # printOdom()
                # rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
        print('masuk except')
