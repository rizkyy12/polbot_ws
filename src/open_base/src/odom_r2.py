#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Header
from gazebo_msgs.srv import GetModelState, GetModelStateRequest  # import class


rospy.init_node('odom_pub_r2')

odom_pub = rospy.Publisher('/my_odom_r2', Odometry, queue_size=1)

rospy.wait_for_service('/gazebo/get_model_state')
# cek apakah service sudah available

get_model_srv = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)

odom = Odometry()
header = Header()  # timestamp & sequence
header.frame_id = '/odom_r2'

model = GetModelStateRequest()
model.model_name = 'open_base2'  # model robot

r = rospy.Rate(10)

while not rospy.is_shutdown():

    result = get_model_srv(model)

    odom.pose.pose = result.pose
    odom.twist.twist = result.twist

    header.stamp = rospy.Time.now()
    odom.header = header

    odom_pub.publish(odom)

    r.sleep()
