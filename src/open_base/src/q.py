#!/usr/bin/env python3
import keyboard
import rospy
from ros_basics.msg import Keyboard


# -------- Gerakin dr R1 ke R3

import rospy
from std_msgs.msg import Float64, UInt8
from open_base.msg import Movement, MovementGeneric
from geometry_msgs.msg import Pose2D

from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2, sin
import math
import numpy as np


def main():
    rospy.init_node('KeyboardData', anonymous=True)

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        data = Movement()
        publisher = rospy.Publisher('data', Keyboard, queue_size=25)

        up = keyboard.is_pressed('up')
        down = keyboard.is_pressed('down')
        right = keyboard.is_pressed('right')
        left = keyboard.is_pressed('left')
        if(up):
            print("Up key pressed")
            data.up = True
            publisher.publish(data)

        rate.sleep()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
