#!/usr/bin/env python

import rospy
import cv2
import cv_bridge
import numpy as np
from sensor_msgs.msg import Image, CameraInfo
from geometry_msgs.msg import Twist

from sensor_msgs.msg import LaserScan

goal_1 = 0.0
goal_2 = 0.0
goal_3 = 0.0
urutan = 0

def empty(a):
    pass


class Follower:

    def __init__(self):

        self.bridge = cv_bridge.CvBridge()
        #cv2.namedWindow("window", 1)
        self.image_sub = rospy.Subscriber('/tb3_0/camera/rgb/image_raw',
                                          Image, self.image_callback)
        self.cmd_vel_pub = rospy.Publisher('/tb3_0/cmd_vel',
                                           Twist, queue_size=1)
        self.twist = Twist()

        self.laser_sub = rospy.Subscriber('/tb3_0/scan', LaserScan, self.laser)

    def image_callback(self, msg):
        #image = cv2.VideoCapture(0)
	global urutan
	print ('urutan:', urutan)
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        lower_yellow = np.array([22, 93, 0])
        upper_yellow = np.array([45, 255, 255])

        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        h, w, d = image.shape
        sv_x = w/2
        sv_y = h/2
        M = cv2.moments(mask)

        if M['m00'] > 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            ex = sv_x - cx
            ey = sv_y - cy
            kp_linier = 3
	    print ('ey:', ey)

            #print ('ex:', ex)
            #print ('ey:', ey)

            cv2.circle(image, (cx, cy), 5, (130, 0, 0), -1)
            cv2.circle(image, (sv_x, sv_y), 5, (255, 0, 255), -1)

            if ex > w:
                ex = w
            
            if ey < 38 and urutan == 0:
                self.twist.linear.x = 0.2 * kp_linier
                self.twist.angular.z = float(ex) / 100
            
        else:
            self.twist.angular.z = 0.5

        self.cmd_vel_pub.publish(self.twist)

        # CONTROL ends
        # cv2.imshow("mask",mask)
        #cv2.imshow("output", image)
        # cv2.imshow("hsv",hsv)
        # cv2.waitKey(3)

    def laser(self, msg):
        global goal_1
        global urutan
        #print ('jarak', msg.ranges[0])

        if msg.ranges[0] < 0.7:
            
            self.twist.linear.x = 0
            self.twist.angular.z = 0
            goal_1 = msg.ranges[0]
            if urutan == 0:
              urutan = 1
        self.cmd_vel_pub.publish(self.twist)
        #print ('goal_1', goal_1)


class Follower2:

    # while goal_1 <= 0.70:
    def __init__(self):

        self.bridge = cv_bridge.CvBridge()
    #cv2.namedWindow("window", 1)
        self.image_sub = rospy.Subscriber('/tb3_1/camera/rgb/image_raw',
                                          Image, self.image_callback)
        self.cmd_vel_pub = rospy.Publisher('/tb3_1/cmd_vel',
                                           Twist, queue_size=1)
        self.twist = Twist()

        self.laser_sub = rospy.Subscriber('/tb3_1/scan', LaserScan, self.laser)


    def image_callback(self, msg):
        #image = cv2.VideoCapture(0)
       # global goal_1

        # if goal_1 < 0.70:
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        lower_green = np.array([36, 25, 25])
        upper_green = np.array([70, 255, 255])

        mask = cv2.inRange(hsv, lower_green, upper_green)

        h, w, d = image.shape
        sv_x = w/2
        sv_y = h/2
        M = cv2.moments(mask)

        if M['m00'] > 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            ex = sv_x - cx
            ey = sv_y - cy
            kp_linier = 3

            #print ('ex:', ex)
            #print ('ey:', ey)

            cv2.circle(image, (cx, cy), 5, (130, 0, 0), -1)
            cv2.circle(image, (sv_x, sv_y), 5, (255, 0, 255), -1)

            if ex > w:
                ex = w

            if ey < 38 and urutan == 2:
                self.twist.linear.x = 0.2 * kp_linier
                self.twist.angular.z = float(ex) / 100

        else:
            self.twist.angular.z = 0.5

        self.cmd_vel_pub.publish(self.twist)

        # CONTROL ends
    # cv2.imshow("mask",mask)
        cv2.imshow("output2", image)
    # cv2.imshow("hsv",hsv)
    # cv2.waitKey(3)

    def laser(self, msg):
        global goal_2
        global urutan
        if msg.ranges[0] < 0.7:

            self.twist.linear.x = 0
            self.twist.angular.z = 0
            goal_2 = msg.ranges[0]
            if urutan == 2:
              urutan = 3
                
        self.cmd_vel_pub.publish(self.twist)

        #print ('goal_2', goal_2)


class Follower3:

    def __init__(self):

        self.bridge = cv_bridge.CvBridge()
        #cv2.namedWindow("window", 1)
        self.image_sub = rospy.Subscriber('/tb3_2/camera/rgb/image_raw',
                                          Image, self.image_callback)
        self.cmd_vel_pub = rospy.Publisher('/tb3_2/cmd_vel',
                                           Twist, queue_size=1)
        self.twist = Twist()

        self.laser_sub = rospy.Subscriber('/tb3_2/scan', LaserScan, self.laser)

    
    def image_callback(self, msg):
        #image = cv2.VideoCapture(0)

        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, lower_red, upper_red)

        h, w, d = image.shape
        sv_x = w/2
        sv_y = h/2
        M = cv2.moments(mask)

        if M['m00'] > 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            ex = sv_x - cx
            ey = sv_y - cy
            kp_linier = 3

            #print ('ex:', ex)
            #print ('ey:', ey)

            cv2.circle(image, (cx, cy), 5, (130, 0, 0), -1)
            cv2.circle(image, (sv_x, sv_y), 5, (255, 0, 255), -1)

            if ex > w:
                ex = w

            if ey < 38 and urutan == 1:
                self.twist.linear.x = 0.2 * kp_linier
                self.twist.angular.z = float(ex) / 100
            
        else:
            self.twist.angular.z = 0.5

        self.cmd_vel_pub.publish(self.twist)

        # CONTROL ends
        # cv2.imshow("mask",mask)
        #cv2.imshow("output", image)
        # cv2.imshow("hsv",hsv)
        # cv2.waitKey(3)

    def laser(self, msg):
        global goal_3
        global urutan
        #print ('jarak3', msg.ranges[0])

        if msg.ranges[0] < 0.7:
            self.twist.linear.x = 0
            self.twist.angular.z = 0
            goal_3 = msg.ranges[0]
            if urutan == 1:
              urutan = 2
        self.cmd_vel_pub.publish(self.twist)

        #print ('goal_3', goal_3)


rospy.init_node('follower')
Follower()
Follower2()
Follower3()

#print ("goal_1", goal_1)
#print ("goal_2", goal_2)
#print ("goal_3", goal_3)
rospy.spin()
# END ALL
