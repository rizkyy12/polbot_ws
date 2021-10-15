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

x2 = 0
y2 = 0
z2 = 0

x3 = 0
y3 = 0
z3 = 0


def printOdom():
    global x1, y1, z1
    global x2, y2, z2
    global x3, y3, z3

    # print('openbase1 :', 'x1', x1, 'y1', y1 )
    # print('openbase2:' , 'x2', x2, 'y2', y2 ) 
    # print('openbase3 :', 'x3 ', x3, 'y3', y3)
    print('openbase1 ke 3: ', 'x', (x3-x1), 'y', (y3-y1) )
    print('')
    print('openbase2 ke 3: ', 'x', (x3-x2), 'y', (y3-y2) ) 
    print('')
    print('openbase1 ke 2: ', 'x', (x1-x2), 'y', (y1-y2) )
    print('')


def getOdomR1(msg):
    global x1, y1, z1

    x1 = msg.x
    y1 = msg.y
    z1 = msg.theta

def getOdomR2(msg):
    global x2, y2, z2

    x2 = msg.x
    y2 = msg.y
    z2 = msg.theta

    # print('x1=', x1, 'y1=', y1)

def getOdomR3(msg):
    global x3, y3, z3

    x3 = msg.x
    y3 = msg.y
    z3 = msg.theta


def open_base1():
    global x3,y3

    movePub1 = rospy.Publisher('/open_base1/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 0
    vel.generic.frame = 3
    vel.generic.target.x = x3 - 0.5
    vel.generic.target.y = y3 - 0.25
    movePub1.publish(vel)


def open_base2():
    global x3,y3

    movePub1 = rospy.Publisher('/open_base2/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 0
    vel.generic.frame = 3
    vel.generic.target.x = x3 - 0.5
    vel.generic.target.y = y3 + 0.25
    movePub1.publish(vel)

def open_base3():
    movePub1 = rospy.Publisher('/open_base3/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 0
    vel.generic.frame = 3
    vel.generic.target.x = 1.0
    vel.generic.target.y = 0.25
    movePub1.publish(vel)


if __name__ == '__main__':
    try:
        while (True):
            while not rospy.is_shutdown():
                rospy.init_node('OpenbaseJOSSSSSS')

                rospy.Subscriber('/open_base1/pose/world', Pose2D, getOdomR1)
                rospy.Subscriber('/open_base2/pose/world', Pose2D, getOdomR2)
                rospy.Subscriber('/open_base3/pose/world', Pose2D, getOdomR3)

                open_base1()
                open_base2()
                open_base3()
                printOdom()


                # printOdom()
                # rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
        print('masuk except')
