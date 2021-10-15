#!/usr/bin/env python3

# ____ Coba control speed agar sampai ke tujuan (titik pke sudut)

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

    print('x1= ', x1, 'y1= ', y1, 'x3= ', x3, 'y3= ', y3)


def getOdomR1(msg):
    # simpen posisi realtime & posisi awal
    global targetX1, targetY1, targetX2, targetY2, targetX3, targetY3
    global beginX1, beginX2, beginX3, beginY1, beginY2, beginY3, consenX, consenY
    global x1, x2, x3, y1, y2, y3, z1, z2, z3, varA

    x1 = msg.x
    y1 = msg.y
    z1 = msg.theta

    if(varA == 0):
        beginX1 = x1
        beginY1 = y1
        varA = 1


def goal1Callback():
    # goal nanti diganti ke = (titik cons)
    global xgoal1, ygoal1
    xgoal1 = 0.0
    ygoal1 = 2.0


def togoal1(xgoal1, ygoal1):
    # cuma ngasih control speed (yg bikin ke tujuannya itu angle)
    global x1, y1

    movePub1 = rospy.Publisher('/open_base1/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    mov = Movement()

    ex1 = abs(xgoal1-x1)
    ey1 = abs(ygoal1-y1)
    # print ('ex1', ex1, 'ey1', ey1)

    distance = abs(math.sqrt(((xgoal1-x1) ** 2) + ((ygoal1-y1) ** 2)))
    desired_angle_goal = math.atan2(ygoal1-y1, xgoal1-x1)         # tetha

    mov.movement = 1
    mov.generic.type = 2
    mov.generic.frame = 3

    kLinear = 37.0 # cari yang pas 0.73 ?

    if (distance > 0.2):
        vx1 = abs(kLinear*ex1*math.cos(desired_angle_goal)) - \
            (kLinear*ey1*math.sin(desired_angle_goal))
        vy1 = (kLinear*ex1*math.cos(desired_angle_goal)) + \
            (kLinear*ey1*math.sin(desired_angle_goal))

        # vx1 = abs(kLinear*math.cos(desired_angle_goal)) - \
        #     (kLinear*math.sin(desired_angle_goal))
        # vy1 = (kLinear*math.cos(desired_angle_goal)) + \
        #     (kLinear*math.sin(desired_angle_goal))

        mov.generic.target.x = vx1
        mov.generic.target.y = vy1
        movePub1.publish(mov)
        print( x1, y1)

    elif (distance <= 0.2):
        vx1 = 0.0
        vy1 = 0.0
        mov.generic.target.x = vx1
        mov.generic.target.y = vy1
        movePub1.publish(mov)
        print("stop = ", vx1, vy1)


if __name__ == '__main__':
    try:
        while (True):
            while not rospy.is_shutdown():
                rospy.init_node('OPENBASE_TAAA')

                rospy.Subscriber('/open_base1/pose/world', Pose2D, getOdomR1)

                goal1Callback()
                togoal1(xgoal1, ygoal1)

                # rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
