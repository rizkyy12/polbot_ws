#!/usr/bin/env python3

# sub dr arduino
# pub rpm ke cmd_vel

import rospy
# from rospy_tutorials.msg import Floats
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64


pubRpmMotor1 = 0
pubRpmMotor2 = 0
pubRpmMotor3 = 0

inSpRpm = 0



#def toArdu():
#    global inSpRpm
#    setPointPublisher = rospy.Publisher(
#        '/set_point_rpm_roda1', Float64, queue_size=1)
#        
#    spMsg = Float64()

#    inSpRpm = 0.0
#    sp = float(inSpRpm)
#    spMsg.data = sp
#    setPointPublisher.publish(spMsg)


def rpmRead1(msg):
    global pubRpmMotor1
    pubRpmMotor1 = msg.data
def rpmRead2(msg):
    global pubRpmMotor2
    pubRpmMotor2 = msg.data
def rpmRead3(msg):
    global pubRpmMotor3
    pubRpmMotor3 = msg.data        


def fromArdu():
    rospy.Subscriber("/data_pid_roda1_from_arduino", Float64, rpmRead1)
    rospy.Subscriber("/data_pid_roda2_from_arduino", Float64, rpmRead2)
    rospy.Subscriber("/data_pid_roda3_from_arduino", Float64, rpmRead3)
    # rospy.spin()


def moveMotor1():
    global pubRpmMotor1
    velocity_publisher = rospy.Publisher(
        '/vel_roda1', Float64, queue_size=1)
    velMsg = Float64()

    speed = float(pubRpmMotor1)
    print("rpm ke motor1",pubRpmMotor1)

    velMsg.data = abs(speed)
    velocity_publisher.publish(velMsg)

def moveMotor2():
    global pubRpmMotor2
    velocity_publisher = rospy.Publisher(
        '/vel_roda2', Float64, queue_size=1)
    velMsg = Float64()

    speed = float(pubRpmMotor2)
    print("rpm ke motor2",pubRpmMotor2)

    velMsg.data = abs(speed)
    velocity_publisher.publish(velMsg)

def moveMotor3():
    global pubRpmMotor3
    velocity_publisher = rospy.Publisher(
        '/vel_roda3', Float64, queue_size=1)
    velMsg = Float64()

    speed = float(pubRpmMotor3)
    print("rpm ke motor3",pubRpmMotor3)

    velMsg.data = abs(speed)
    velocity_publisher.publish(velMsg)        


if __name__ == '__main__':
    try:
        while (True):
            while not rospy.is_shutdown():
                rospy.init_node('node_comm')
                
                fromArdu()
                moveMotor1()
                moveMotor2()
                moveMotor3()

#                toArdu()

        # rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
        print('masuk except')
