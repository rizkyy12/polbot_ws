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


def printOdom():
    global x1, y1, z1
    global x2, y2, z3
    global x3, y3, z3

    print('x1=', x1, 'y1=', y1, 'x2=', x2, 'y2=', y2, 'x3=', x3, 'y3=', y3)


def getOdomR1(msg):
    global targetX1, targetY1, targetX2, targetY2, targetX3, targetY3
    global beginX1, beginX2, beginX3, beginY1, beginY2, beginY3, consenX, consenY
    global x1, x2, x3, y1, y2, y3, z1, z2, z3, varA

    x1 = msg.x
    y1 = msg.y
    z1 = msg.theta

    if(varA == 0):
        beginX1 = x1
        beginY1 = y1
        # kasih delay
        varA = 1


def getOdomR2(msg):
    global targetX1, targetY1, targetX2, targetY2, targetX3, targetY3
    global beginX1, beginX2, beginX3, beginY1, beginY2, beginY3, consenX, consenY
    global x1, x2, x3, y1, y2, y3, z1, z2, z3, varB

    x2 = msg.x
    y2 = msg.y
    z2 = msg.theta
    # print('x2=', x2, 'y2=', y2)

    if(varB == 0):
        beginX2 = x2
        beginY2 = y2
        varB = 1


def getOdomR3(msg):
    global targetX1, targetY1, targetX2, targetY2, targetX3, targetY3
    global beginX1, beginX2, beginX3, beginY1, beginY2, beginY3, consenX, consenY
    global x1, x2, x3, y1, y2, y3, z1, z2, z3, varC

    x3 = msg.x
    y3 = msg.y
    z3 = msg.theta
    # print('x3=', x3, 'y3=', y3)

    if(varC == 0):
        beginX3 = x3
        beginY3 = y3
        varC = 1


def caseFormation():
    global targetX1, targetY1, targetX2, targetY2, targetX3, targetY3
    global beginX1, beginX2, beginX3, beginY1, beginY2, beginY3, consenX, consenY
    global x1, x2, x3, y1, y2, y3, z1, z2, z3

    consenX = (beginX1 + beginX2 + beginX3)/3
    consenY = (beginY1 + beginY2 + beginY3)/3
    # consenX = 2.0
    # consenY = 1.0

    # if (consenY) >= 0.00000001 :
    if (beginY1) >= 0.00000001:
        targetX1 = consenX
        targetY1 = consenY + 1.0

        targetX2 = consenX - 1.0
        targetY2 = consenY

        targetX3 = consenX + 1.0
        targetY3 = consenY

        print("+++")
        print('tx1=', targetX1, 'ty1=', targetY1)
        print('x1=', beginX1, 'y1=', beginY1)
        print('cY=', consenY)
    else:
        targetX1 = consenX
        targetY1 = consenY - 1.0

        targetX2 = consenX + 1.0
        targetY2 = consenY

        targetX3 = consenX - 1.0
        targetY3 = consenY

        print("---")
        print('tx1=', targetX1, 'ty1=', targetY1)
        print('bx1=', beginX1, 'by1=', beginY1)
        print('cY=', consenY)

    # print('x1=', x1, 'y1=', y1, 'x2=', x2, 'y2=', y2,'x3=', x3, 'y3=', y3)



def open_base1():
    global targetX1, targetY1
    global x1, y1

    movePub1 = rospy.Publisher('/open_base1/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    mov = Movement()
    mov.movement = 1
    mov.generic.type = 0
    mov.generic.frame = 3

    desired_angle_goal = math.atan2(targetY1-y1, targetX1-x1)         # tetha

    mov.generic.target.x = targetX1
    mov.generic.target.y = targetY1
    # mov.generic.target.theta = desired_angle_goal

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

    desired_angle_goal = math.atan2(targetY2-y2, targetX2-x2)         # tetha

    mov.generic.target.x = targetX2
    mov.generic.target.y = targetY2
    # mov.generic.target.theta = desired_angle_goal

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

    desired_angle_goal = math.atan2(targetY3-y3, targetX3-x3)         # tetha

    mov.generic.target.x = targetX3
    mov.generic.target.y = targetY3
    # mov.generic.target.theta = desired_angle_goal

    movePub1.publish(mov)
    # print ('openbase3')


if __name__ == '__main__':
    try:
        while (True):
            while not rospy.is_shutdown():
                rospy.init_node('OPENBASE_TAAA')

                rospy.Subscriber('/open_base1/pose/world', Pose2D, getOdomR1)
                rospy.Subscriber('/open_base2/pose/world', Pose2D, getOdomR2)
                rospy.Subscriber('/open_base3/pose/world', Pose2D, getOdomR3)

                # consensus()
                # printOdom()
                caseFormation()

                open_base1()
                open_base2()
                open_base3()

                # rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
