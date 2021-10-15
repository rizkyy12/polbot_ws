#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist, Quaternion
from math import atan2, cos, sin
import math
import numpy as np
import time

x, x1, x2 = 0, 0, 0
y, y1, y2 = 0, 0, 0
z, z1, z2 = 0, 0, 0
yaw, yaw1, yaw2 = 0, 0, 0

ex, ex1, ex2 = 0, 0, 0
ey, ey1, ey2 = 0, 0, 0

varA = 0
x1a = 0
y1a = 0


def posisiawal(pasan):
    global x
    global y, z, yaw
    global x1a, y1a
    global varA

    x = pasan.pose.pose.position.x
    y = pasan.pose.pose.position.y

    rot_q = pasan.pose.pose.orientation
    (roll, pitch, yaw) = euler_from_quaternion(
        [rot_q.x, rot_q.y, rot_q.z, rot_q.w])

    # simpan posisi robot1
    if (varA == 0):
        x1a = x
        y1a = y
        varA += 1


def posisi1(pasan):
    global x_goal
    global y_goal

    x_goal = pasan.pose.pose.position.x
    y_goal = pasan.pose.pose.position.y


def posisi2(pasan):
    global x1, y1, z1
    global roll1, pitch1, yaw1

    x1 = pasan.pose.pose.position.x
    y1 = pasan.pose.pose.position.y

    rot_q1 = pasan.pose.pose.orientation
    (roll1, pitch1, yaw1) = euler_from_quaternion(
        [rot_q1.x, rot_q1.y, rot_q1.z, rot_q1.w])


def posisi3(pasan):
    global x_goal1
    global y_goal1

    x_goal1 = pasan.pose.pose.position.x
    y_goal1 = pasan.pose.pose.position.y


def posisi4(pasan):
    global x2, y2, z2
    global roll2, pitch2, yaw2

    x2 = pasan.pose.pose.position.x
    y2 = pasan.pose.pose.position.y

    rot_q2 = pasan.pose.pose.orientation
    (roll2, pitch2, yaw2) = euler_from_quaternion(
        [rot_q2.x, rot_q2.y, rot_q2.z, rot_q2.w])


def posisiakhir(pasan):
    global x_goal2
    global y_goal2

    x_goal2 = pasan.pose.pose.position.x
    y_goal2 = pasan.pose.pose.position.y


def dari1ke2(x_goal, y_goal):
    global x
    global y, z, yaw
    global ex, ey

    velocity_message = Twist()
    cmd_vel_topic = '/tb3_0/cmd_vel'

    while(True):
        K_linear = 0.1
        distance = abs(math.sqrt(((x_goal-x)**2) + ((y_goal-y)**2)))

        ex = x_goal-x
        ey = y_goal-y

        K_angular = 4.0
        desired_angle_goal = math.atan2(y_goal-y, x_goal-x)
        angular_speed = (desired_angle_goal - yaw)*K_angular

        #linear_speed = distance * K_linear

        velocity_message.linear.x = abs(
            K_linear*ex*math.cos(desired_angle_goal)) - (K_linear*ey*math.sin(desired_angle_goal))
        velocity_message.linear.y = (
            K_linear*ex*math.sin(desired_angle_goal)) + (K_linear*ey*math.cos(desired_angle_goal))
        velocity_message.angular.z = angular_speed

        velocity_publisher.publish(velocity_message)
        print('x', x, 'y=', y)

        if(distance < 0.5):

            velocity_message.linear.x = 0.0
            velocity_message.angular.z = 0.0

            velocity_publisher.publish(velocity_message)

            break


def dari2ke3(x_goal1, y_goal1):
    global x1
    global y1, z1, yaw1
    global ex1, ey1

    velocity_message = Twist()
    cmd_vel_topic = '/tb3_1/cmd_vel'

    while(True):
        K_linear = 0.1
        distance = abs(math.sqrt(((x_goal1-x1)**2) + ((y_goal1-y1)**2)))

        ex1 = x_goal1-x1
        ey1 = y_goal1-y1

        K_angular = 4.0
        desired_angle_goal = math.atan2(y_goal1-y1, x_goal1-x1)
        angular_speed = (desired_angle_goal - yaw1)*K_angular

        #linear_speed = distance * K_linear

        velocity_message.linear.x = abs(
            K_linear*ex1*math.cos(desired_angle_goal)) - (K_linear*ey1*math.sin(desired_angle_goal))
        velocity_message.linear.y = (
            K_linear*ex1*math.sin(desired_angle_goal)) + (K_linear*ey1*math.cos(desired_angle_goal))
        velocity_message.angular.z = angular_speed
        velocity_publisher1.publish(velocity_message)

        print('x', x1, 'y=', y1)

        if(distance < 0.5):

            velocity_message.linear.x = 0.0
            velocity_message.angular.z = 0.0

            velocity_publisher1.publish(velocity_message)
            break


def dari3ke1(x1a, y1a):
    global x2
    global y2, z2, yaw2

    velocity_message = Twist()
    cmd_vel_topic = '/tb3_2/cmd_vel'

    while(True):
        K_linear = 0.1
        distance = abs(math.sqrt(((x1a-x2)**2) + ((y1a-y2)**2)))

        ex2 = x1a-x2
        ey2 = y1a-y2

        K_angular = 1.0
        desired_angle_goal = math.atan2(y1a-y2, x1a-x2)

        angular_speed = (desired_angle_goal - yaw2)*K_angular

        #linear_speed = distance * K_linear

        velocity_message.linear.x = abs(
            K_linear*ex2*math.cos(desired_angle_goal)) - (K_linear*ey2*math.sin(desired_angle_goal))
        velocity_message.linear.y = (
            K_linear*ey2*math.sin(desired_angle_goal)) + (K_linear*ey2*math.cos(desired_angle_goal))
        velocity_message.angular.z = angular_speed
        velocity_publisher2.publish(velocity_message)

        print('x', x2, 'y=', y2)

        if(distance < 0.5):
            velocity_message.linear.x = 0.0
            velocity_message.angular.z = 0.0

            velocity_publisher2.publish(velocity_message)
            break


if __name__ == '__main__':
    try:

        rospy.init_node('turlesim_motion_pose', anonymous=True)

        # Robot 1 ke Robot2
        velocity_publisher = rospy.Publisher(
            '/tb3_0/cmd_vel', Twist, queue_size=10)
        odom_subscriber = rospy.Subscriber("/tb3_0/odom", Odometry, posisiawal)
        time.sleep(1)
        odim_subscriber = rospy.Subscriber('/tb3_1/odom', Odometry, posisi1)
        time.sleep(1)
        dari1ke2(x_goal, y_goal)
        time.sleep(1)

        # Robot 2 ke Robot 3
        velocity_publisher1 = rospy.Publisher(
            '/tb3_1/cmd_vel', Twist, queue_size=10)
        odom1_subscriber = rospy.Subscriber("/tb3_1/odom", Odometry, posisi2)
        time.sleep(1)
        odim1_subscriber = rospy.Subscriber('/tb3_2/odom', Odometry, posisi3)
        time.sleep(1)
        dari2ke3(x_goal1, y_goal1)
        time.sleep(1)

        # Robot 3 ke Robot 1
        velocity_publisher2 = rospy.Publisher(
            '/tb3_2/cmd_vel', Twist, queue_size=10)
        odom2_subscriber = rospy.Subscriber("/tb3_2/odom", Odometry, posisi4)
        time.sleep(1)
        odim2_subscriber = rospy.Subscriber(
            '/tb3_0/odom', Odometry, posisiawal)
        time.sleep(1)
        dari3ke1(x1a, y1a)
        time.sleep(1)

    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
