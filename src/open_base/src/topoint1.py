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


def move():
    rospy.init_node('cekPub', anonymous=False)
    velocity_publisher = rospy.Publisher('/open_base1/command', Movement, queue_size=1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 2
    vel.generic.frame = 3
    print ('openbase1')

    speed = input("Input your speed:")
    speed = float(speed)

    distance = input("Type your distance:")
    distance = float(distance)

    isForward = input("Foward?: ")  # True or False
    isForward = float(isForward)


    # Checking if the movement is forward or backwards
    if(isForward == 1):
        vel.generic.target.y = abs(speed)
    else:
        vel.generic.target.y = -abs(speed)

    vel.generic.target.x = 0
    vel.generic.target.theta = 0

    while not rospy.is_shutdown():

        # Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while(current_distance < distance):
            velocity_publisher.publish(vel)
            # Takes actual time to velocity calculus
            t1 = rospy.Time.now().to_sec()
            # Calculates distancePoseStamped
            current_distance = speed*(t1-t0)
        # After the loop, stops the robot
        vel.generic.target.y = 0
        # Force the robot to stop
        velocity_publisher.publish(vel)


if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass