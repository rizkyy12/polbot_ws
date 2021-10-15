#!/usr/bin/env python3

# ____ bagi jadi 2 orientasi atas bawah
# ____ nambah angle

from numpy.core.fromnumeric import var
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

targetX1 = 0.0
targetY1 = 0.0

targetX2 = 0.0
targetY2 = 0.0

targetX3 = 0.0
targetY3 = 0.0


x1 = 0.0
y1 = 0.0
z1 = 0.0

x2 = 0.0
y2 = 0.0
z2 = 0.0

x3 = 0.0
y3 = 0.0
z3 = 0.0


def getOdomR4(msg):
    global x1, x2, x3, y1, y2, y3, z1, z2, z3, varA

    x1 = msg.x
    y1 = msg.y
    z1 = msg.theta

# def caseFormation():
#     # isi program formasi
#     global x1

def open_base1():
    global targetX1, targetY1
    global x1, y1

    movePub1 = rospy.Publisher('/open_base1/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    mov = Movement()
    mov.movement = 1
    mov.generic.type = 0
    mov.generic.frame = 3

    mov.generic.target.x = targetX1
    mov.generic.target.y = targetY1

    movePub1.publish(mov)
    # print ('openbase1')


def open_base2():
    global targetX2, targetY2
    global x2, y2

    movePub1 = rospy.Publisher('/open_base2/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    mov = Movement()
    mov.movement = 1
    mov.generic.type = 0
    mov.generic.frame = 3

    mov.generic.target.x = targetX2
    mov.generic.target.y = targetY2

    movePub1.publish(mov)
    # print ('openbase2')


def open_base3():
    global targetX3, targetY3
    global x3, y3

    movePub1 = rospy.Publisher('/open_base3/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    mov = Movement()
    mov.movement = 1
    mov.generic.type = 0
    mov.generic.frame = 3

    mov.generic.target.x = targetX3
    mov.generic.target.y = targetY3

    movePub1.publish(mov)
    # print ('openbase3')


if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            rospy.init_node('Followers_Node')

            rospy.Subscriber('/open_base4/pose/world', Pose2D, getOdomR4)

            open_base1()
            open_base2()
            open_base3()


    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
