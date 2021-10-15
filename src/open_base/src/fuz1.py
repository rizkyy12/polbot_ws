#!/usr/bin/env python3


import time
import numpy as np
import math
from math import atan2
from geometry_msgs.msg import Point, Twist
from tf.transformations import euler_from_quaternion
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose2D
from open_base.msg import Movement, MovementGeneric
from std_msgs.msg import Float64, UInt8
import rospy
from numpy.core.fromnumeric import var

# ____ Tambah Coba Konsensus  BWLOM BERES


targetX1 = 0.0
beginX1 = 0.0
targetY1 = 0.0
beginY1 = 0.0

targetX2 = 0.0
beginX2 = 0.0
targetY2 = 0.0
beginY2 = 0.0

targetX3 = 0.0
beginX3 = 0.0
targetY3 = 0.0
beginY3 = 0.0

consenX = 0.0
consenY = 0.0

varA = 0
varB = 0
varC = 0
x1 = 0.0
y1 = 0.0
z1 = 0.0

x2 = 0.0
y2 = 0.0
z2 = 0.0

x3 = 0.0
y3 = 0.0
z3 = 0.0

value_small_12x = 0.0
value_small_12y = 0.0
value_safe_12x = 0.0
value_safe_12y = 0.0
value_big_12x = 0.0
value_big_12y = 0.0

x_distance = input('masukkan nilai distance = ')
distance12x = float(x_distance)
x_distance = input('masukkan nilai distance = ')
distance12y = float(x_distance)


def printOdom():
    global x1, y1, z1
    global x2, y2, z3
    global x3, y3, z3

    print('x1= ', x1, 'y1= ', y1, 'x3= ', x3, 'y3= ', y3)


def getOdomR1(msg):
    global x1, x2, x3, y1, y2, y3, z1, z2, z3, varA

    x1 = msg.x
    y1 = msg.y
    z1 = msg.theta

    if(varA == 0):
        beginX1 = x1
        beginY1 = y1
        varA = 1


def getOdomR2(msg):
    global x1, x2, x3, y1, y2, y3, z1, z2, z3, varB

    x2 = msg.x
    y2 = msg.y
    z2 = msg.theta

    if(varB == 0):
        beginX2 = x2
        beginY2 = y2
        varB = 1


def getOdomR3(msg):
    global x1, x2, x3, y1, y2, y3, z1, z2, z3, varC

    x3 = msg.x
    y3 = msg.y
    z3 = msg.theta

    if(varC == 0):
        beginX3 = x3
        beginY3 = y3
        varC = 1


def leader():
    global targetX1, targetY1

    movePub1 = rospy.Publisher('/open_base1/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    mov = Movement()
    mov.movement = 1
    mov.generic.type = 0
    mov.generic.frame = 3
    mov.generic.target.x = 0.0  # targetX1
    mov.generic.target.y = 3.0  # targetY1
    movePub1.publish(mov)


def fuzzy12():
    global x1, x2, x3, y1, y2, y3, z1, z2, z3, value_small_12y, value_small_12x, value_big_12x, value_big_12y, value_safe_12x, value_safe_12y, distance12x, distance12y

    # distance12x = abs(x1 - x2)
    # distance12y = abs(y1 - y2)

    if distance12x <= 0.2:
        value_small_12x = 1
        value_safe_12x = 0
        value_big_12x = 0
    elif distance12x > 0.2 and distance12x < 0.4:
        value_small_12x = (0.4-distance12x)/(0.4-0.2)
        value_safe_12x = 0
        value_big_12x = 0
    elif distance12x > 0.2 and distance12x < 0.5:
        value_safe_12x = (distance12x - 0.2)/(0.5-0.2)
        value_big_12x = 0
        value_small_12x = 0
    elif distance12x == 0.5:
        value_small_12x = 0
        value_safe_12x = 1
        value_big_12x = 0
    elif distance12x > 0.5 and distance12x < 0.8:
        value_small_12x = 0
        value_safe_12x = (0.8 - distance12x)/(0.8-0.5)
        value_big_12x = 0
    elif distance12x > 0.6 and distance12x < 0.8:
        value_small_12x = 0
        value_big_12x = (distance12x-0.6)/(0.8-0.6)
        value_safe_12x = 0
    elif distance12x >= 0.8:
        value_small_12x = 0
        value_safe_12x = 0
        value_big_12x = 1

    if distance12y <= 0.2:
        value_small_12y = 1
        value_safe_12y = 0
        value_big_12y = 0
    elif distance12y > 0.2 and distance12y < 0.4:
        value_small_12y = (0.4-distance12y)/(0.4-0.2)
        value_safe_12y = 0
        value_big_12y = 0
    elif distance12y > 0.2 and distance12y < 0.5:
        value_safe_12y = (distance12y - 0.2)/(0.5-0.2)
        value_big_12y = 0
        value_small_12y = 0
    elif distance12y == 0.5:
        value_small_12y = 0
        value_safe_12y = 1
        value_big_12y = 0
    elif distance12y > 0.5 and distance12y < 0.8:
        value_small_12y = 0
        value_safe_12y = (0.8 - distance12y)/(0.8-0.5)
        value_big_12y = 0
    elif distance12y > 0.6 and distance12y < 0.8:
        value_small_12y = 0
        value_big_12y = (distance12y-0.6)/(0.8-0.6)
        value_safe_12y = 0
    elif distance12y >= 0.8:
        value_small_12y = 0
        value_safe_12y = 0
        value_big_12y = 1

# def fuzzy13():
#     global x1, x2, x3, y1, y2, y3, z1, z2, z3

#     distance13x = abs(x1 - x3)
#     distance13y = abs(y1 - y3)

#     if distance13x <= 0.2:
#         value_small_13x = 1
#         value_safe_13x = 0
#         value_big_13x = 0
#     elif distance13x > 0.2 and distance13x < 0.4:
#         value_small_13x = (0.4-distance13x)/(0.4-0.2)
#         value_safe_13x = 0
#         value_big_13x = 0
#     elif distance13x > 0.2 and distance13x < 0.5:
#         value_safe_13x = (distance13x - 0.2)/(0.5-0.2)
#         value_big_13x = 0
#         value_small_13x = 0
#     elif distance13x == 0.5:
#         value_small_13x = 0
#         value_safe_13x = 1
#         value_big_13x = 0
#     elif distance13x > 0.5 and distance13x < 0.8:
#         value_small_13x = 0
#         value_safe_13x = (0.8 - distance13x)/(0.8-0.5)
#         value_big_13x = 0
#     elif distance13x > 0.6 and distance13x < 0.8:
#         value_small_13x = 0
#         value_big_13x = (distance13x-0.6)/(0.8-0.6)
#         value_safe_13x = 0
#     elif distance13x >= 0.8:
#         value_small_13x = 0
#         value_safe_13x = 0
#         value_big_13x = 1

#     if distance13y <= 0.2:
#         value_small_13y = 1
#         value_safe_13y = 0
#         value_big_13y = 0
#     elif distance13y > 0.2 and distance13y < 0.4:
#         value_small_13y = (0.4-distance13y)/(0.4-0.2)
#         value_safe_13y = 0
#         value_big_13y = 0
#     elif distance13y > 0.2 and distance13y < 0.5:
#         value_safe_13y = (distance13y - 0.2)/(0.5-0.2)
#         value_big_13y = 0
#         value_small_13y = 0
#     elif distance13y == 0.5:
#         value_small_13y = 0
#         value_safe_13y = 1
#         value_big_13y = 0
#     elif distance13y > 0.5 and distance13y < 0.8:
#         value_small_13y = 0
#         value_safe_13y = (0.8 - distance13y)/(0.8-0.5)
#         value_big_13y = 0
#     elif distance13y > 0.6 and distance13y < 0.8:
#         value_small_13y = 0
#         value_big_13y = (distance13y-0.6)/(0.8-0.6)
#         value_safe_13y = 0
#     elif distance13y >= 0.8:
#         value_small_13y = 0
#         value_safe_13y = 0
#         value_big_13y = 1


speed = []


def fungsiinfslow(variabel_distanceX, variabel_distanceY):
    if variabel_distanceX != 0:
        if variabel_distanceY != 0:
            hasil_output = min(variabel_distanceX, variabel_distanceY)
            speed.append([hasil_output, 1])


def fungsiinfaverage(variabel_distanceX, variabel_distanceY):
    if variabel_distanceX != 0:
        if variabel_distanceY != 0:
            hasil_output = min(variabel_distanceX, variabel_distanceY)
            speed.append([hasil_output, 2])


def fungsiinffast(variabel_distanceX, variabel_distanceY):
    if variabel_distanceX != 0:
        if variabel_distanceY != 0:
            hasil_output = min(variabel_distanceX, variabel_distanceY)
            speed.append([hasil_output, 3])


fungsiinfslow(value_small_12x, value_small_12y)
fungsiinfaverage(value_safe_12x, value_safe_12y)
fungsiinffast(value_big_12x, value_big_12y)

print('Speed ', speed)


if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            rospy.init_node('OPENBASE_TA')

            rospy.Subscriber('/open_base1/pose/world', Pose2D, getOdomR1)
            rospy.Subscriber('/open_base2/pose/world', Pose2D, getOdomR2)
            rospy.Subscriber('/open_base3/pose/world', Pose2D, getOdomR3)

            # rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
