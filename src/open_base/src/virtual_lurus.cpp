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

float x1 = 0, b = 0, z1 = 0;
float x2 = 0, b2 = 0, z2 = 0;
float x3 = 0, b3 = 0, z3 = 0;
float x4 = 0, b4 = 0, z4 = 0;
float c;

open_base::Movement Movement;
// std::vector<geometry_msgs::Pose2D> poseWorld;
// geometry_msgs::Pose2D poseWorld ;
geometry_msgs::Pose2D msg;
ros::Publisher publisherPose;
ros::Publisher publisherPose2;
ros::Publisher publisherPose3;
ros::Publisher publisherPose4;

void getOdomR1(const geometry_msgs::Pose2D::ConstPtr& msg){
    x1 = msg->x    ;
    b  = msg->y    ;
    z1 = msg->theta;
}

void getOdomR2(const geometry_msgs::Pose2D::ConstPtr& msg){
    x2 = msg->x    ;
    b2  = msg->y    ;
    z2 = msg->theta;
}

void getOdomR3(const geometry_msgs::Pose2D::ConstPtr& msg){
    x3 = msg->x    ;
    b3  = msg->y    ;
    z3 = msg->theta;
    // cout<<"\nNilai x3 = "<<x3;
}

void getOdomR4(const geometry_msgs::Pose2D::ConstPtr& msg){
    x4 = msg->x    ;
    b4  = msg->y    ;
    z4 = msg->theta;
}

void printOdom(){
    // cout << "x1 ="+to_string(x1)+"y1"+to_string(b) << endl;
    // cout << "x2 ="+to_string(x2)+"y2"+to_string(b2) << endl;
    // cout << "x3 ="+to_string(x3)+"y3"+to_string(b3) << endl;
    // cout << "x4 ="+to_string(x4)+"y4"+to_string(b4) << endl;
    cout<<"\nNilai x3 = "<<x3;
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
    Movement.generic.target.y = 4;
    Movement.generic.target.theta = 0;
    // c = x3 - 0.5;
    publisherPose.publish(Movement);    
    // cout<<"\nNilai a = "<<c;
}

void open_base2(){
    ros::Rate loop_rate(1);
    Movement.movement = 1;
    Movement.generic.type = 0;
    Movement.generic.frame = 3;
    Movement.generic.target.x = -1;
    Movement.generic.target.y = 4;
    Movement.generic.target.theta = 0;
    publisherPose2.publish(Movement);
}

void open_base3(){
    ros::Rate loop_rate(1);
    Movement.movement = 1;
    Movement.generic.type = 0;
    Movement.generic.frame = 3;
    Movement.generic.target.x = 0.0;
    Movement.generic.target.y = 4;
    Movement.generic.target.theta = 0;
    publisherPose3.publish(Movement);
}

// void open_base4(){
//     ros::Rate loop_rate(1);
//     Movement.movement = 1;
//     Movement.generic.type = 0;
//     Movement.generic.frame = 3;
//     Movement.generic.target.x = 0.25;
//     Movement.generic.target.y = 1;
//     Movement.generic.target.theta = 0;
//     publisherPose4.publish(Movement);
// }


int main(int argc, char **argv){
        try {
        while(true){
            //awal
            ros::init(argc, argv, "OpenbaseToPoint");
            ros::NodeHandle node;
            ros::Subscriber sub = node.subscribe("/open_base1/pose/world", 1, getOdomR1);
            ros::Subscriber sub2 = node.subscribe("/open_base2/pose/world", 1, getOdomR2);
            ros::Subscriber sub3 = node.subscribe("/open_base3/pose/world", 1, getOdomR3);
            ros::Subscriber sub4 = node.subscribe("/open_base4/pose/world", 1, getOdomR4);
            publisherPose = node.advertise<open_base::Movement>("/open_base1/command", 1);
            publisherPose2 = node.advertise<open_base::Movement>("/open_base2/command", 1);
            publisherPose3 = node.advertise<open_base::Movement>("/open_base3/command", 1);
            // publisherPose4 = node.advertise<open_base::Movement>("/open_base4/command", 1);



            open_base1();
            open_base2();
            open_base3();
            // open_base4();
            printOdom();
        }
    throw ; 
    }
    catch (int x) {
        cout << "masuk except";
    }
    return 0;
}
