#!/usr/bin/env python3

# sub dr arduino
# pub rpm ke cmd_vel

import rospy
# from rospy_tutorials.msg import Floats
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64


pubRpmMotor = 0
inSpRpm = 0



def toArdu():
    global inSpRpm
    setPointPublisher = rospy.Publisher(
        '/set_point_rpm_roda1', Float64, queue_size=1)
    spMsg = Float64()

    # sp = input("input SP = ")
    inSpRpm = 0.0
    
    sp = float(inSpRpm)
    spMsg.data = sp

    setPointPublisher.publish(spMsg)
    #print("input rpm = ", inSpRpm)


def rpmRead(msg):
    global pubRpmMotor
    pubRpmMotor = msg.data


def fromArdu():
    rospy.Subscriber("/data_pid_roda1_from_arduino", Float64, rpmRead)
    # rospy.spin()


def moveMotor():
    global pubRpmMotor
    velocity_publisher = rospy.Publisher(
        '/vel_roda1', Float64, queue_size=1)
    velMsg = Float64()

    # speed = input("speed = ")
    speed = float(pubRpmMotor)
    print("rpm ke motor",pubRpmMotor)
    #print(" ")

    velMsg.data = abs(speed)
    #velMsg.angular.z = abs(speed)

    # while not rospy.is_shutdown():
    velocity_publisher.publish(velMsg)


if __name__ == '__main__':
    try:
        while (True):
            while not rospy.is_shutdown():
                rospy.init_node('node_comm')
                fromArdu()
                moveMotor()

#                toArdu()

        # rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
        print('masuk except')
