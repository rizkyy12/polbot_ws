#include <cmath>
#include <math.h>
#include <string>
#include <iostream>
// #include <conio.h>
using namespace std;

#include <ros/ros.h>
#include <geometry_msgs/Pose2D.h>
#include <std_msgs/Float64.h>

#include <open_base/Movement.h>
#include <open_base/MovementGeneric.h>
#include <open_base/Velocity.h>

float X1 = 0, Y1 = 0, Z1 = 0;
float X2 = 0, Y2 = 0, Z2 = 0;
float X3 = 0, Y3 = 0, Z3 = 0;

float targetX1 = 0, targetY1 = 0, targetZ1 = 0;
float targetX2 = 0, targetY2 = 0, targetZ2 = 0;
float targetX3 = 0, targetY3 = 0, targetZ3 = 0;

float beginX1 = 0, beginY1 = 0, beginZ1 = 0;
float beginX2 = 0, beginY2 = 0, beginZ2 = 0;
float beginX3 = 0, beginY3 = 0, beginZ3 = 0;

int varA = 0, varB = 0, varC = 0;

ros::Publisher publisherPose1;
ros::Publisher publisherPose2;
ros::Publisher publisherPose3;

void pose1Callback(const geometry_msgs::Pose2D::ConstPtr &pose_msg)
{
    X1 = pose_msg->x;
    Y1 = pose_msg->y;
    Z1 = pose_msg->theta;

    if (varA == 0)
    {
        beginX1 = X1;
        beginY1 = Y1;
        varA = 1;
    }

    cout << "X1= " << X1;
    cout << "\n Y1= " << Y1;
}

void pose2Callback(const geometry_msgs::Pose2D::ConstPtr &pose_msg)
{
    X2 = pose_msg->x;
    Y2 = pose_msg->y;
    Z2 = pose_msg->theta;

    if (varB == 0)
    {
        beginX2 = X2;
        beginY2 = Y2;
        varB = 1;
    }

    // cout << "\ny2 " << Y2;
}

void pose3Callback(const geometry_msgs::Pose2D::ConstPtr &pose_msg)
{
    X3 = pose_msg->x;
    Y3 = pose_msg->y;
    Z3 = pose_msg->theta;

    if (varC == 0)
    {
        beginX3 = X3;
        beginY3 = Y3;
        varC = 1;
    }

    // cout << "\ny3 " << Y3;
}

void open_base1()
{
    open_base::Movement Movement;
    // ros::Rate loop_rate(1);
    Movement.movement = 1;
    Movement.generic.type = 0;
    Movement.generic.frame = 3;
    Movement.generic.target.x = targetX1;
    Movement.generic.target.y = targetY1;
    Movement.generic.target.theta = 0;
    publisherPose1.publish(Movement);
    ros::spinOnce();
}

void open_base2()
{
    open_base::Movement Movement;
    // ros::Rate loop_rate(1);
    Movement.movement = 1;
    Movement.generic.type = 0;
    Movement.generic.frame = 3;
    Movement.generic.target.x = targetX2;
    Movement.generic.target.y = targetY2;
    Movement.generic.target.theta = 0;
    publisherPose2.publish(Movement);
    ros::spinOnce();
}

void open_base3()
{
    open_base::Movement Movement;
    // ros::Rate loop_rate(1);
    Movement.movement = 1;
    Movement.generic.type = 0;
    Movement.generic.frame = 3;
    Movement.generic.target.x = targetX3;
    Movement.generic.target.y = targetY3;
    Movement.generic.target.theta = 0;
    publisherPose3.publish(Movement);
    ros::spinOnce();
}

void formation()
{
    float consenX;
    float consenY;

    consenX = (beginX1 + beginX2 + beginX3) / 3;
    consenY = (beginY1 + beginY2 + beginY3) / 3;

    if (beginY1 >= consenY)
    {
        targetX1 = consenX;
        targetY1 = consenY + 1.0;

        targetX2 = consenX - 1.0;
        targetY2 = consenY;

        targetX3 = consenX + 1.0;
        targetY3 = consenY;

        // cout << "consenX= " << consenX;
        // cout << "\n consenY= " << consenY;
    }
    else
    {
        targetX1 = consenX;
        targetY1 = consenY - 1.0;

        targetX2 = consenX + 1.0;
        targetY2 = consenY;

        targetX3 = consenX - 1.0;
        targetY3 = consenY;

        // cout << "consenx= " << consenX;
        // cout << "\n consenY= " << consenY;
    }
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "OpenbaseToPoint");
    ros::NodeHandle node;

    publisherPose1 = node.advertise<open_base::Movement>("/open_base1/command", 1);
    publisherPose2 = node.advertise<open_base::Movement>("/open_base2/command", 1);
    publisherPose3 = node.advertise<open_base::Movement>("/open_base3/command", 1);

    ros::Subscriber sub1 = node.subscribe("/open_base1/pose/world", 1, &pose1Callback);
    ros::Subscriber sub2 = node.subscribe("/open_base2/pose/world", 1, &pose2Callback);
    ros::Subscriber sub3 = node.subscribe("/open_base3/pose/world", 1, &pose3Callback);

    while (ros::ok())
    {
        formation();

        open_base1();
        open_base2();
        open_base3();
        ros::spinOnce();

        // ros::spin();
    }
    return 0;
}
