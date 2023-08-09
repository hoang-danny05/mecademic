import mecademicpy.robot

#class for the SOP16 component (2 sets of 8 terminals)
class BGAsm:
    def __init__(self, robot):
        self.rbt = robot

    
    def pressButton(self):
        #RESET ROBOT
        self.rbt.SetJointVel(100)
        self.rbt.MoveJoints(89.60276,58.61276,-9.38405,2.50345,-47.11293,-90)
        #right above, change position to boop
        self.rbt.MoveJoints(89.60534,67.08336,-11.71448,2.29293,-53.24948,-90.81724)
        print("button pressed")
    
    def grabComp(self):
        # facepalm... the robot doesnt move straight unless movelin command
        self.rbt.MoveJoints(91.26595,44.15069,7.275,1.61897,-51.44379,-1.00862)#prepick
        self.rbt.SetJointVel(25)
        self.rbt.MoveJoints(91.26595,54.73086,8.26371,1.42034,-63.0119,-0.64483) # downpick
        self.rbt.SetValveState(1,0)
        self.rbt.Delay(.5)
        self.rbt.SetCartLinVel(175) # this also applies to te flux btw
        self.rbt.MoveLinRelWrf(0,0,100,0,0,0)
        self.rbt.SetJointVel(100)

    def flux(self):
        self.rbt.MoveJoints(63.82759,47.56629,-37.65569,85.16172,-64.25638,-78.9819)#upflux
        # self.rbt.MoveLinRelWrf(0,0,-47.5,0,0,0)
        # self.rbt.Delay(.5)
        # self.rbt.MoveLinRelWrf(0,0,50,0,0,0)
        
    def solder(self):
        self.rbt.SetJointVel(55)
        self.rbt.MoveJoints(17.72922,22.98543,18.34293,25.83259,-44.33431,-37.17328)
        self.rbt.MoveJoints(17.72922,27.64034,23.15664,22.41931,-52.9831,-32.02241)
        self.rbt.MoveLinRelWrf(0,0,-.5,0,0,0)
        self.rbt.SetCartLinVel(45)
        self.rbt.MoveLinRelWrf(0, -75, 0, 0, 0, 0)
        

    def drop(self):
        self.rbt.SetJointVel(100)
        self.rbt.MoveJoints(-58.7281,62.32707,-58.39759,-87.61655,-58.80983,85.40517)
        self.rbt.SetValveState(0,0)
        # self.rbt.MoveJoints(-58.7281,61.38181,-55.24914,-86.28879,-58.92672,82.83534)
        # self.rbt.MoveJoints(-58.7281,62.32707,-58.39759,-87.61655,-58.80983,85.40517)
        self.rbt.MoveJoints(90,10.33345,9.92922,0,-20.26293,0)

        