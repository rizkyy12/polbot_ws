#include <cmath>
#include <math.h>
#include <string>
#include <iostream>
using namespace std;

#include <ros/ros.h>
#include <geometry_msgs/Pose2D.h>
#include <std_msgs/Float64.h>

#include <open_base/Movement.h>
#include <open_base/MovementGeneric.h>
#include <open_base/Velocity.h>

float x1 = 0, b = 0, z1 = 0;
open_base::Movement Movement;
std::vector<geometry_msgs::Pose2D> poseWorld;
// geometry_msgs::Pose2D poseWorld ;
ros::Publisher publisherPose;

void printOdom(){
    cout << "x ="+to_string(x1)+"y"+to_string(b);
}

void getOdomR1(const geometry_msgs::Pose2D::ConstPtr& msg){
    x1 = msg->x    ;
    b  = msg->y    ;
    z1 = msg->theta;
}

// void getOdomR1(const geometry_msgs::Pose2D::ConstPtr& msg ){
//     x1 = msg->poseWorld.x;
//     b = msg->poseWorld.y;
//     z1 = msg->poseWorld.theta;
// }


void open_base1(){
    ros::Rate loop_rate(1);
    Movement.movement = 1;
    Movement.generic.type = 0;
    Movement.generic.frame = 3;
    Movement.generic.target.x = 1;
    Movement.generic.target.y = 1;
    publisherPose.publish(Movement);
}


int main(int argc, char **argv){
        try {
        while(true){
            //awal
            ros::init(argc, argv, "OpenbaseToPoint");
            ros::NodeHandle node;
            ros::Subscriber sub = node.subscribe("/open_base1/pose/world", 1, getOdomR1);
            publisherPose = node.advertise<open_base::Movement>("/open_base1/command", 1);


            open_base1();
        }
    throw ; 
    }
    catch (int x) {
        cout << "masuk except";
    }
    return 0;
}
