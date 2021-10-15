#!/usr/bin/env python3

# -------- Gerakin dr R1 ke R3

import rospy
from std_msgs.msg import Float64, UInt8
from open_base.msg import Movement, MovementGeneric
from geometry_msgs.msg import Pose2D

from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2, sin
import math
import numpy as np
import time

x1 = 0
y1 = 0
z1 = 0


def printOdom():
    global x1, y1, z1

    # print('openbase1 :', 'x1', x1, 'y1', y1 )
    # print('openbase2:' , 'x2', x2, 'y2', y2 ) 
    # print('openbase3 :', 'x3 ', x3, 'y3', y3)
    print('x:', x1, 'y:', y1 )


def getOdomR1(msg):
    global x1, y1, z1

    x1 = msg.x
    y1 = msg.y
    z1 = msg.theta


def open_base1():

    movePub1 = rospy.Publisher('/open_base1/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 0
    vel.generic.frame = 3
    vel.generic.target.x = 1
    vel.generic.target.y = 1
    movePub1.publish(vel)



if __name__ == '__main__':
    try:
        while (True):
            while not rospy.is_shutdown():
                rospy.init_node('OpenbaseJOSSSSSS')

                rospy.Subscriber('/open_base1/pose/world', Pose2D, getOdomR1)

                open_base1()
                printOdom()


                # printOdom()
                # rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
        print('masuk except')
