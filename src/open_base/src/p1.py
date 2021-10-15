#!/usr/bin/env python3
#baca odom R1

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


x1 = 0
y1 = 0
z1 = 0


def getOdom(msg):
    global x1, y1, z1

    x1 = msg.pose.pose.position.x
    y1 = msg.pose.pose.position.y
    z1 = msg.pose.pose.orientation.w
    
    # rospy.Subscriber('/my_odom', Odometry, getOdom)

    print('x1= ', x1, 'y1= ', y1,'z1= ', z1)


def open_base1():
    movePub1 = rospy.Publisher('/open_base3/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 0
    vel.generic.frame = 3
    vel.generic.target.x = 5
    vel.generic.target.y = 0.0
    movePub1.publish(vel)
    # print('openbase1')


if __name__ == '__main__':
    try:
        while (True):
            while not rospy.is_shutdown():
                rospy.init_node('OpenbaseASIK')
                rospy.Subscriber('/my_odom', Odometry, getOdom)

                open_base1()

                # rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
        print('masuk except')
