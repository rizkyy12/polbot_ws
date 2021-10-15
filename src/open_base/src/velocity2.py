#!/usr/bin/env python3

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

# vx1 = 0.0
# vy1 = 0.0


# def toPoint(msg):
#     global vx1, vy1

#     obMsg = Movement()

#     obMsg.movement = 1
#     obMsg.generic.type = 2
#     obMsg..generic.frame = 3

#     obMsg.generic.target.x = 0.8
#     obMsg.generic.target.y = 0.0

#     movePub.publish(obMsg)
#     print ('done published')

# rospy.init_node('moveCoba1')
# movePub = rospy.Publisher('/open_base/command', Movement, queue_size=10)
def open_base4():
    movePub1 = rospy.Publisher('/open_base1/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 2
    vel.generic.frame = 3
    vel.generic.target.x = 0.5
    vel.generic.target.y = 0.0
    movePub1.publish(vel)
    print ('openbase1')

def open_base2():
    movePub1 = rospy.Publisher('/open_base2/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 2
    vel.generic.frame = 3
    vel.generic.target.x = 0.5
    vel.generic.target.y = 0.0
    movePub1.publish(vel)
    print ('openbase2')

def open_base3():
    movePub1 = rospy.Publisher('/open_base3/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 2
    vel.generic.frame = 3
    vel.generic.target.x = 0.5
    vel.generic.target.y = 0.0
    movePub1.publish(vel)
    print ('openbase3')

if __name__ == '__main__':
    try:
        while (True):
            while not rospy.is_shutdown():
                rospy.init_node('Openbase')
                open_base4()
                open_base2()
                open_base3()
                # rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
        print('masuk except')
