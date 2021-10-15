import math

class Robot :
    def __init__(self, startpos, robotimg, width, follow =None):
        self.m2p=3779.52 #from meters to pixels
        
        self.leader= False # is this robot a leader ?
        self.follow=follow  # who to follow ?

        self.x,self.y=startpos
        self.theta=0
        self.w = width
        self.u = 30 #pix/sec
        self.w=0 #rad/sec

        pass
    def move(self):
        pass
    def following(self):
        pass
    def dist(self,point1,point2):
        pass
    def draw(self):
        pass
    def trail(self):
        pass

class Envir :
    def __init__(self):
        pass
    def write_info(self):
        pass
    def robot_frame(self):
        pass
    
# inizialization area
# animation loop
while True :
