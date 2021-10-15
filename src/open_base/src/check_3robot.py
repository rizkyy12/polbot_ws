#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64, UInt8
from open_base.msg import Movement, MovementGeneric
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist, Quaternion, Pose2D
from math import atan2, cos, sin
import math
import numpy as np
import time


def callback(msg):
    print('open_base1:','x', msg.x , 'y', msg.y , 'z', msg.theta)

def callback1(msg):
    print('open_base2:','x', msg.x , 'y', msg.y , 'z', msg.theta)

def callback2(msg):
    print('open_base3:','x', msg.x , 'y', msg.y , 'z', msg.theta)


def run():
    rospy.init_node('check_pose')
    pose = rospy.Subscriber('/open_base1/pose/world', Pose2D, callback)
    pose = rospy.Subscriber('/open_base2/pose/world', Pose2D, callback1)
    pose = rospy.Subscriber('/open_base3/pose/world', Pose2D, callback2)
    rospy.spin()

if __name__ == '__main__':
    run()
