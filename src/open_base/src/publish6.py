#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist


def move():
    rospy.init_node('cekPub', anonymous=False)
    velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    speed = input("Input your speed:")
    speed = float(speed)

    distance = input("Type your distance:")
    distance = float(distance)

    isForward = input("Foward?: ")  # True or False
    isForward = float(isForward)


    # Checking if the movement is forward or backwards
    if(isForward == 1):
        vel_msg.linear.y = abs(speed)
    else:
        vel_msg.linear.y = -abs(speed)

    vel_msg.linear.x = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        # Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while(current_distance < distance):
            velocity_publisher.publish(vel_msg)
            # Takes actual time to velocity calculus
            t1 = rospy.Time.now().to_sec()
            # Calculates distancePoseStamped
            current_distance = speed*(t1-t0)
        # After the loop, stops the robot
        vel_msg.linear.y = 0
        # Force the robot to stop
        velocity_publisher.publish(vel_msg)


if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
