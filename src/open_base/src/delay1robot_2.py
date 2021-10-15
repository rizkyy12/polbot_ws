#!/usr/bin/env python3

# -------- Gerakin dr R1 ke R3

import rospy
import keyboard
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

varA = 0
varB = 0
varC = 0
varM = 0

targetX1 = 0.0
beginX1 = 0.0
targetY1 = 0.0
beginY1 = 0.0
beginZ1 = 0.0

mulaiSimulasi= 0
mulai = 0


def printOdom():
    global x1, y1, z1

    # print('openbase1 :', 'x1', x1, 'y1', y1 )
    # print('openbase2:' , 'x2', x2, 'y2', y2 )
    # print('openbase3 :', 'x3 ', x3, 'y3', y3)
    print('x:', x1, 'y:', y1)


def getOdomR1(msg):
    global x1, y1, z1, varA
    global beginX1, beginY1, beginZ1

    x1 = msg.x
    y1 = msg.y
    z1 = msg.theta

    if(varA == 0):
        rospy.sleep(0.1)
        beginX1 = x1
        beginY1 = y1
        beginZ1 = z1
        varA = 1


def ob1Awal():
    movePub1 = rospy.Publisher('/open_base1/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 0
    vel.generic.frame = 3
    vel.generic.target.x = 0
    vel.generic.target.y = 0
    vel.generic.target.theta = 0
    movePub1.publish(vel)
    print("awal")


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
    print("jalan")


if __name__ == '__main__':
    # global mulai
    try:
        while not rospy.is_shutdown():
            rospy.init_node('OpenbaseDelay')

            rospy.Subscriber('/open_base1/pose/world', Pose2D, getOdomR1)

            # print("varM = ", varM)
            if (mulai == 1):
                open_base1()
                # varM = 1 
            else:
                ob1Awal()

            if keyboard.is_pressed('a'):
                # mulai = 0
                mulai = input("mulai? : ")
                mulai = float(mulai)
                varM = 1    

            # if(varM == 0):
            #     # mulai = 0
            #     mulai = input("mulai? : ")
            #     mulai = float(mulai)
            #     varM = 1


            # if (mulai == True):
            #     mulaiSimulasi = True
            #     # varM = 1 
            # elif (mulai == False):
            #     mulaiSimulasi = False

            # if(mulaiSimulasi == False):
            #     ob1Awal()
            # elif (mulaiSimulasi == True):
            #     open_base1()

            # open_base1()
            # printOdom()

            # printOdom()
            # rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
        print('masuk except')
