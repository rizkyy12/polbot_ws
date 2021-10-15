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

def open_base4():
    global targetX3, targetY3
    global x3, y3

    movePub1 = rospy.Publisher('/open_base4/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    mov = Movement()
    mov.movement = 1
    mov.generic.type = 0
    mov.generic.frame = 3


    # --- program formasi ---

    mov.generic.target.x = targetX3
    mov.generic.target.y = targetY3

    movePub1.publish(mov)
    # print ('openbase3')


if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            rospy.init_node('Formation_Node')

            open_base4()


    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
