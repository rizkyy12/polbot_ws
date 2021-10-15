#!/usr/bin/env python3
import yaml
import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64, UInt8
from open_base.msg import Movement, MovementGeneric
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist, Quaternion, Pose2D
from math import atan2, cos, radians, sin,atan,tan
import math
import numpy as np
import time

R = 0.227756813566454
yj = 0
yi = 0
yk = 1
xj = 1
xi = 0
xk = 1.5
thetas = 0
thetaf = 0
deltatheta = 0
L2 = 0
L = 0.3 #belum tahu rumusnya gimana
tantheta = 0
Xrs = 0
Yrs = 0
Xrf = 0
Yrf = 0
a = 0
b = 0
c = 0
d = 0
xf = 0
yf = 0
xs = 0
ys = 0

def rumus():
    global xf,yf,xs,ys,Xrf,Yrf,Yrs,Xrs,L2,tantheta,R,thetas,yj,yi,xj,xi,thetaf,yk,xk,deltatheta,a,b,c,d
    a = yj - yi
    b = xj - xi
    c = yj - yk
    d = xj - xk
    thetas = math.degrees(atan(a/b)) #HASIL DALAM BENTUK RADIAN
    thetaf = math.degrees(atan(c/d)) #HASIL DALAM BENTUK RADIAN
    deltatheta = thetaf - thetas
    tantheta = deltatheta/2
    L2 = R * (tan(radians(tantheta)))
    Xrs = xj- (L2*cos(radians(thetas)))
    Yrs = yj- (L2*sin(radians(thetas)))
    Xrf = xj+ (L2*cos(radians(thetaf)))
    Yrf = yj+ (L2*sin(radians(thetaf)))
    xs = xj- (L*cos(radians(thetas)))
    ys = yj- (L*sin(radians(thetas)))
    xf = xj+ (L*cos(radians(thetaf)))
    yf = yj+ (L*sin(radians(thetaf)))
    print(xf,yf,xs,ys)
        


# def callback(msg):
#     global x
#     global y

#     x = msg.x
#     y = msg.y
#     print('open_base1:','x', x, 'y', y )



if __name__ == '__main__':
    rumus()
    # try:
    #     while (True):
    #         while not rospy.is_shutdown():

                # rumus()


                # printOdom()
                # rospy.spin()

    # except rospy.ROSInterruptException:
    #     rospy.loginfo("terminated")
    #     print('masuk except')

