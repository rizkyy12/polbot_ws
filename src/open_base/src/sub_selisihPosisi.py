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


def getOdomR2(msg):
    global targetX1, targetY1, targetX2, targetY2, targetX3, targetY3
    global beginX1, beginX2, beginX3, beginY1, beginY2, beginY3, consenX, consenY
    global x1, x2, x3, y1, y2, y3, z1, z2, z3, varB

    x2 = msg.x
    y2 = msg.y
    z2 = msg.theta

def getOdomR3(msg):
    global targetX1, targetY1, targetX2, targetY2, targetX3, targetY3
    global beginX1, beginX2, beginX3, beginY1, beginY2, beginY3, consenX, consenY
    global x1, x2, x3, y1, y2, y3, z1, z2, z3, varC

    x3 = msg.x
    y3 = msg.y
    z3 = msg.theta


def selisihX1(msg):
    global targetX1, targetY1, targetX2, targetY2, targetX3, targetY3
    global x1, x2, x3, y1, y2, y3, z1, z2, z3

    


def caseFormation():
    global targetX1, targetY1, targetX2, targetY2, targetX3, targetY3
    global beginX1, beginX2, beginX3, beginY1, beginY2, beginY3, consenX, consenY
    global x1, x2, x3, y1, y2, y3, z1, z2, z3

    targetX1_pub = rospy.Publisher('/target/robot1/X', Float64, queue_size=1)
    targetY1_pub = rospy.Publisher('/target/robot1/Y', Float64, queue_size=1)
    targetX2_pub = rospy.Publisher('/target/robot2/X', Float64, queue_size=1)
    targetY2_pub = rospy.Publisher('/target/robot2/Y', Float64, queue_size=1)
    targetX3_pub = rospy.Publisher('/target/robot3/X', Float64, queue_size=1)
    targetY3_pub = rospy.Publisher('/target/robot3/Y', Float64, queue_size=1)

    consenX = (beginX1 + beginX2 + beginX3)/3
    consenY = (beginY1 + beginY2 + beginY3)/3

    targetX1 = 0.0
    targetY1 = 2.0

    targetX2 = 1.0
    targetY2 = 2.0

    targetX3 = 2.0
    targetY3 = 2.0

    # print('x1=', x1, 'y1=', y1)

    targetX1_pub.publish(targetX1)
    targetY1_pub.publish(targetY1)
    targetX2_pub.publish(targetX2)
    targetY2_pub.publish(targetY2)
    targetX3_pub.publish(targetX3)
    targetY3_pub.publish(targetY3)



if __name__ == '__main__':
    try:
        # while (True):
        while not rospy.is_shutdown():
            rospy.init_node('OPENBASE_TAAA')

            rospy.Subscriber('/open_base1/pose/world', Pose2D, getOdomR1)
            rospy.Subscriber('/open_base2/pose/world', Pose2D, getOdomR2)
            rospy.Subscriber('/open_base3/pose/world', Pose2D, getOdomR3)

            # printOdom()
            # caseFormation()


            # rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
