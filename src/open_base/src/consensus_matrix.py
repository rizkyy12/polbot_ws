#!/usr/bin/env python3

# ____ Tambah Coba Konsensus  BWLOM BERES

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

MX_delta = [[2, 0, 0],
            [0, 2, 0],
            [0, 0, 2]]

MX_A = [[0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]]

# print (MX_delta)
       
MX_L = [[MX_delta[i][j] - MX_A[i][j]  for j in range(len(MX_delta[0]))] for i in range(len(MX_delta))]
MX_L = np.negative(MX_L)

print (MX_L)




