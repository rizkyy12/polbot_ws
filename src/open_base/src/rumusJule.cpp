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

const float R = 0.227756813566454;
float yj = 0, yi = 0, yk = 1;
float xj = 1, xi = 0, xk = 1.5;
float thetas = 0, thetaf = 0, deltatheta = 0;
float L2 = 0;
float L = 0.3; //belum tahu rumusnya gimana
float tantheta = 0;
float Xrs = 0, Yrs = 0, Xrf = 0, Yrf = 0;
float a = 0, b = 0, c = 0, d = 0;
float xf = 0, yf = 0, xs = 0, ys = 0;

float ab, angle, op;

open_base::Movement Movement;
std::vector<geometry_msgs::Pose2D> poseWorld;
ros::Publisher publisherPose;

double ConvertDegtoRad(double degree)
{
    double pi = 3.14159265359;
    return (degree * (pi / 180));
}

double ConvertRadtoDeg(double radian)
{
    double pi = 3.141592653589793238463;
    return (radian * (180 / pi));
}

void rumus()
{
    a = yj - yi;
    b = xj - xi;
    c = yj - yk;
    d = xj - xk;

    angle = 30; // hasil bentuk awal keluarannya radian (pas dicoba tan45 bukan 1)
    ab = ConvertRadtoDeg(angle);
    op = sin(ab);

    // thetas = math.degrees(atan(a / b)); //HASIL DALAM BENTUK RADIAN
    // thetaf = math.degrees(atan(c / d)); //HASIL DALAM BENTUK RADIAN

    // deltatheta = thetaf - thetas;
    // tantheta = deltatheta / 2;
    // L2 = R * (tan(radians(tantheta)));
    // Xrs = xj - (L2 * cos(radians(thetas)));
    // Yrs = yj - (L2 * sin(radians(thetas)));
    // Xrf = xj + (L2 * cos(radians(thetaf)));
    // Yrf = yj + (L2 * sin(radians(thetaf)));
    // xs = xj - (L * cos(radians(thetas)));
    // ys = yj - (L * sin(radians(thetas)));
    // xf = xj + (L * cos(radians(thetaf)));
    // yf = yj + (L * sin(radians(thetaf)));
}

int main(int argc, char **argv)
{
    try
    {
        while (true)
        {
            //awal
            ros::init(argc, argv, "OpenbaseToPoint");
            ros::NodeHandle node;

            // ros::Subscriber sub = node.subscribe("/open_base1/pose/world", 1, getOdomR1);
            publisherPose = node.advertise<open_base::Movement>("/open_base1/command", 1);
            // open_base1();

            rumus();

            cout << op << endl;
        }
        throw;
    }
    catch (int x)
    {
        cout << "masuk except";
    }
    return 0;
}