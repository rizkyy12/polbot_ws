#!/usr/bin/env python3

# -------- Gerakin dr R1 ke R3

import yaml
import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64, UInt8
from open_base.msg import Movement, MovementGeneric
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist, Quaternion, Pose2D
from math import atan2, cos, radians, sin, atan, tan
from rosgraph_msgs.msg import Clock
import math
import numpy as np
import time

x1 = 0
y1 = 0
z1 = 0

x2 = 0
y2 = 0
z2 = 0

x3 = 0
y3 = 0
z3 = 0

x4 = 0
y4 = 0
z4 = 0

# variabel1
mulai = 1
varC = 0
varD = 0
varE = 0
varF = 0
# varG = 0
# varH = 0
# varI = 0
# varJ = 0
a = 0
b = 0
c = 0
d = 0
# koordinat1
xi = 0.75
yi = 0.25
xj = 1.09
yj = 0.25
xk = 1.10
yk = 1
xl = 1.5
yl = 1
# persamaan1
Xrs = 0
Yrs = 0
Xrf = 0
Yrf = 0
xf = 0
yf = 0
xs = 0
ys = 0
thetas = 0
thetas1rad = 0
thetaf = 0
deltatheta = 0
L2 = 0
tantheta = 0
R = 0.09
L = 0.2  # belum tahu rumusnya gimana
Xrs1 = 0
Yrs1 = 0
Xrf1 = 0
Yrf1 = 0
thetas1 = 0
thetaf1 = 0
xf1 = 0
yf1 = 0
xs1 = 0
ys1 = 0


def rumus():
    # global xf,yf,xs,ys,xf1,yf1,xs1,ys1,Xrf,Yrf,Yrs,Xrs,Xrf1,Yrf1,Yrs1,Xrs1,L2,tantheta,R,thetas,thetas1,thetas1rad,yj,yi,xj,xi,thetaf,thetaf1,yk,xk,deltatheta,a,b,c,d,L
    global Xrs, Yrs, Xrf, Yrf, Xrs1, Yrs1, Xrf1, Yrf1, xl, yl
    a = yj - yi
    b = xj - xi
    c = yj - yk
    d = xj - xk
    thetas = math.degrees(atan(a/b))  # HASIL DALAM BENTUK RADIAN
    thetaf = math.degrees(atan(c/d))  # HASIL DALAM BENTUK RADIAN
    # HASIL DALAM BENTUK RADIAN
    thetas1 = math.degrees(atan(((yk-yj)/(xk-xj))))
    thetas1rad = atan(((yk-yj)/(xk-xj)))  # HASIL DALAM BENTUK RADIAN
    # HASIL DALAM BENTUK RADIAN
    thetaf1 = math.degrees(atan(((yk-yl)/(xk-xl))))
    deltatheta = thetaf - thetas
    tantheta = deltatheta/2
    L2 = R * (tan(radians(tantheta)))
    Xrs = xj - (L2*cos(radians(thetas)))
    Yrs = yj - (L2*sin(radians(thetas)))
    Xrf = xj + (L2*cos(radians(thetaf)))
    Yrf = yj + (L2*sin(radians(thetaf)))
    Xrs1 = xk - (L2*cos(radians(thetas1)))
    Yrs1 = yk - (L2*sin(radians(thetas1)))
    Xrf1 = xk + (L2*cos(radians(thetaf1)))
    Yrf1 = yk + (L2*sin(radians(thetaf1)))
    xs = xj - (L*cos(radians(thetas)))
    ys = yj - (L*sin(radians(thetas)))
    xf = xj + (L*cos(radians(thetaf)))
    yf = yj + (L*sin(radians(thetaf)))
    xs1 = xk - (L*cos(radians(thetas1)))
    ys1 = yk - (L*sin(radians(thetas1)))
    xf1 = xk + (L*cos(radians(thetaf1)))
    yf1 = yk + (L*sin(radians(thetaf1)))
    # print(Xrs1,Yrs1,Xrf1,Yrf1)

# def printOdom():
#     global x1, y1, z1
#     global x2, y2, z2
#     global x3, y3, z3
#     global x4, y4, z4

#     # print('openbase1 :', 'x1', x1, 'y1', y1 )
#     # print('openbase2:' , 'x2', x2, 'y2', y2 )
#     # print('openbase3 :', 'x3 ', x3, 'y3', y3)
#     print('openbase1 ke 3: ', 'x', (x3-x1), 'y', (y3-y1) )
#     print('')
#     print('openbase2 ke 3: ', 'x', (x3-x2), 'y', (y3-y2) )
#     print('')
#     print('openbase1 ke 2: ', 'x', (x1-x2), 'y', (y1-y2) )
#     print('')


def getOdomR1(msg):
    # global x1, y1, z1

    x1 = msg.x
    y1 = msg.y
    z1 = msg.theta


def getOdomR2(msg):
    # global x2, y2, z2

    x2 = msg.x
    y2 = msg.y
    z2 = msg.theta


def getOdomR3(msg):
    global x3, y3, z3

    x3 = msg.x
    y3 = msg.y
    z3 = msg.theta


def getOdomR4(msg):
    # global x4, y4, z4

    x4 = msg.x
    y4 = msg.y
    z4 = msg.theta


def open_base1():
    global x3, y3

    movePub1 = rospy.Publisher('/open_base1/command', Movement, queue_size=0.1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 0
    vel.generic.frame = 3
    vel.generic.target.x = x3 - 0.75
    vel.generic.target.y = y3 - 0.25
    vel.generic.target.theta = z3
    movePub1.publish(vel)


def open_base2():
    global x3, y3

    movePub1 = rospy.Publisher('/open_base2/command', Movement, queue_size=0.1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 0
    vel.generic.frame = 3
    vel.generic.target.x = x3 - 0.75
    vel.generic.target.y = y3 + 0.25
    vel.generic.target.theta = z3
    movePub1.publish(vel)


def open_base4():
    global x3, y3

    movePub1 = rospy.Publisher('/open_base4/command', Movement, queue_size=0.1)
    rate = rospy.Rate(1)
    vel = Movement()
    vel.movement = 1
    vel.generic.type = 0
    vel.generic.frame = 3
    vel.generic.target.x = x3 - 0.25
    vel.generic.target.y = y3 - 0
    vel.generic.target.theta = z3
    movePub1.publish(vel)


def open_base3():
    # global x3,y3, varC, mulai,xf,yf,xs,ys,Xrf,Yrf,Yrs,Xrs,thetas,thetaf
    global x3, y3, mulai, varC, Xrs, Yrs
    if (mulai == 1 and x3 <= Xrs):
        #        print('menuju xrs dan yrs')
        movePub1 = rospy.Publisher(
            '/open_base3/command', Movement, queue_size=0.1)
        rate = rospy.Rate(1)
        vel = Movement()
        vel.movement = 1
        vel.generic.type = 0
        vel.generic.frame = 3
        vel.generic.target.x = Xrs
        vel.generic.target.y = Yrs
        vel.generic.target.theta = 0
        movePub1.publish(vel)
        if (x3 >= (Xrs-0.02) and y3 >= (Yrs-0.02)):
            mulai = 0
            varC = 1


def open_base31():
    # global x3,y3, varC, varD, mulai,xf,yf,xs,ys,Xrf,Yrf,Yrs,Xrs,thetas,thetaf
    global x3, y3, varC, varD, Xrf, Yrf
    if(varC == 1):
        #        print('menuju xrf dan yrf')
        movePub1 = rospy.Publisher(
            '/open_base3/command', Movement, queue_size=0.1)
        rate = rospy.Rate(1)
        vel = Movement()
        vel.movement = 1
        vel.generic.type = 0
        vel.generic.frame = 3
        vel.generic.target.x = Xrf
        vel.generic.target.y = Yrf
        vel.generic.target.theta = 0
        movePub1.publish(vel)
        if (x3 >= (Xrf-0.02) and y3 >= (Yrf-0.02)):
            varD = 1
            varC = 0
            print('masuk')


def open_base32():
    # global x3,y3, varC, varD, mulai, varE,xf,yf,xs,ys,Xrf,Yrf,Yrs,Xrs,thetas,thetaf
    global x3, y3, varD, varE, Xrs1, Yrs1
    if(varD == 1):
        #        print('menuju xrs1 dan yrs1')
        movePub1 = rospy.Publisher(
            '/open_base3/command', Movement, queue_size=0.1)
        rate = rospy.Rate(1)
        vel = Movement()
        vel.movement = 1
        vel.generic.type = 0
        vel.generic.frame = 3
        vel.generic.target.x = Xrs1
        vel.generic.target.y = Yrs1
        vel.generic.target.theta = 0
        movePub1.publish(vel)
        if (x3 >= (Xrs1-0.02) and y3 >= (Yrs1-0.02)):
            varE = 1
            varD = 0


def open_base33():
    # global x3,y3, varC, varD, mulai, varE,varG, varF,xf,yf,xs,ys,Xrf,Yrf,Yrs,Xrs,thetas,thetaf
    global x3, y3, varE, varF, Xrf1, Yrf1
    if(varE == 1):
        #        print('menuju xrf1 dan yrf1')
        movePub1 = rospy.Publisher(
            '/open_base3/command', Movement, queue_size=0.1)
        rate = rospy.Rate(1)
        vel = Movement()
        vel.movement = 1
        vel.generic.type = 0
        vel.generic.frame = 3
        vel.generic.target.x = Xrf1
        vel.generic.target.y = Yrf1
        vel.generic.target.theta = 0
        movePub1.publish(vel)
        if (x3 >= (Xrf1-0.02) and y3 >= (Yrf1-0.02)):
            varF = 1
            varE = 0


def open_base34():
    # global x3,y3, varC, varD, mulai, xf1,yf1,xs1,ys1,varE, varF,xf,yf,xs,ys,Xrf,Yrf,Yrs,Xrs,thetas,thetaf,varG
    global x3, y3, varF, mulai, xl, yl
    if(varF == 1):
        #        print('menuju xl dan yl')
        movePub1 = rospy.Publisher(
            '/open_base3/command', Movement, queue_size=0.1)
        rate = rospy.Rate(1)
        vel = Movement()
        vel.movement = 1
        vel.generic.type = 0
        vel.generic.frame = 3
        vel.generic.target.x = xl
        vel.generic.target.y = yl
        vel.generic.target.theta = 0
        movePub1.publish(vel)
        if (x3 >= (xl-0.02) and y3 >= (yl-0.02)):
            varF = 0
            mulai = 0


if __name__ == '__main__':
    try:
        lim = 1000
        arr = [0.0003]*lim
        c = 0
        awal = time.time()
        while not rospy.is_shutdown():
            skrng = time.time()
            
            waktu = skrng - awal

            start_time = time.time()
            rospy.init_node('OpenbaseGo')
#            print(x3, y3, z3)

            movePub1 = rospy.Publisher(
                '/jedarrrr', Float64, queue_size=0.1)
            
            pub2 = rospy.Publisher('/jam', Float64, queue_size=0.1)

            rospy.Subscriber('/open_base1/pose/world', Pose2D, getOdomR1)
            rospy.Subscriber('/open_base2/pose/world', Pose2D, getOdomR2)
            rospy.Subscriber('/open_base3/pose/world', Pose2D, getOdomR3)
            rospy.Subscriber('/open_base4/pose/world', Pose2D, getOdomR4)

            # awal()
            rumus()
            open_base1()
            open_base2()
            open_base4()
            open_base3()
            open_base31()
            open_base32()
            open_base33()
            open_base34()
            # printOdom()
            end_time = time.time()
            jeda = end_time - start_time
            print(jeda)
            if c < lim-1:
                c += 1
            else:
                c = 0
            arr[c] = jeda
            avejeda = sum(arr)/len(arr)
            movePub1.publish(avejeda)
            

            pub2.publish(waktu)

            # printOdom()
            # rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("terminated")
        print('masuk except')
