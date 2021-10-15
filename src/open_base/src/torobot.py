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

def callback(x):
    poseWorld = Pose2D()
    poseWorld.x = x
    print (x)

rospy.init_node('check_pose')
pose = rospy.Subscriber('/open_base2/pose/world', Pose2D, callback)
rospy.spin()