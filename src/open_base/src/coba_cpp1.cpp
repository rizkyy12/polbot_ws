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

float x1 = 0, b1 = 0, z1 = 0;
float x2 = 0, b2 = 0, z2 = 0;
float x3 = 0, b3 = 0, z3 = 0;
float x4 = 0, b4 = 0, z4 = 0;
float c;

open_base::Movement Movement;

// std::vector<geometry_msgs::Pose2D> poseWorld;
// geometry_msgs::Pose2D poseWorld;
// geometry_msgs::Pose2D msg;

// geometry_msgs::Pose2D ob_pose;

ros::Publisher publisherPose;

void poseCallback(const geometry_msgs::Pose2D::ConstPtr &pose_msg)
{
    x1 = pose_msg->x;
    b1 = pose_msg->y;
    z1 = pose_msg->theta;
    // cout<< "\ncalbak";

    cout<<"\ny1 "<< b1;
    // ros::spin(); // gakebaca klo rospin disini
}

void open_base1()
{

    ros::Rate loop_rate(1);
    Movement.movement = 1;
    Movement.generic.type = 0;
    Movement.generic.frame = 3;
    Movement.generic.target.x = 0;
    Movement.generic.target.y = 0.75;
    Movement.generic.target.theta = 0;
    // c = x3 - 0.5;
    publisherPose.publish(Movement);
    ros::spinOnce();
    // cout<<"\nNilai a = "<<c;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "OpenbaseToPoint");
    ros::NodeHandle node;

    // ros::Subscriber sub = node.subscribe("/open_base1/pose/world", 1, getOdomR1);
    publisherPose = node.advertise<open_base::Movement>("/open_base1/command", 1);

    ros::Subscriber sub = node.subscribe("/open_base1/pose/world",1, &poseCallback);

    while (ros::ok())
    {
        open_base1();
        ros::spinOnce();

        // ros::spin();
    }
    return 0 ;
}
