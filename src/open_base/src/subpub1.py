#!/usr/bin/env python3

# sub dr gazebo
# pub ke arduino

import rospy
from std_msgs.msg import Float64



def gazeRead1(msg):
    global pubGazebo1
    pubGazebo1 = msg.data
def gazeRead2(msg):
    global pubGazebo2
    pubGazebo2 = msg.data
def gazeRead3(msg):
    global pubGazebo3
    pubGazebo3 = msg.data  

def fromArdu():
    rospy.Subscriber("/open_base1/left_joint_velocity_controller/command", Float64, rpmRead1)
    rospy.Subscriber("/open_base1/right_joint_velocity_controller/command", Float64, rpmRead2)
    rospy.Subscriber("/open_base1/back_joint_velocity_controller/command", Float64, rpmRead3)

def moveMotor1():
    global pubGazebo1
    velocity_publisher = rospy.Publisher(
        '/set_point_rpm_roda1', Float64, queue_size=1)
        
    velMsg = Float64()
    speed = float(pubGazebo1)
    print("ke motor1", pubGazebo1)

    velMsg.data = abs(speed)
    velocity_publisher.publish(velMsg)

def moveMotor2():
    global pubGazebo2
    velocity_publisher = rospy.Publisher(
        '/set_point_rpm_roda2', Float64, queue_size=1)
        
    velMsg = Float64()
    speed = float(pubGazebo2)
    print(" ke motor2", pubGazebo2)

    velMsg.data = abs(speed)
    velocity_publisher.publish(velMsg)

def moveMotor3():
    global pubGazebo3
    velocity_publisher = rospy.Publisher(
        '/set_point_rpm_roda3', Float64, queue_size=1)
    
    velMsg = Float64()
    speed = float(pubGazebo3)
    print("  ke motor3", pubGazebo3)

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


    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
                
