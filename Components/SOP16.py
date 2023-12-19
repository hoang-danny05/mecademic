import mecademicpy.robot
from Components.VacuumSwitch import VacuumSwitch

#class for the SOP16 component (2 sets of 8 terminals)
class Component:
    """
    Deprecated
    Wrong Nozzle 
    Wrong Fluxer
    """
    def __init__(self, robot : mecademicpy.robot, switch : VacuumSwitch):
        self.rbt = robot
        self.switch = switch
    
    def pressButton(self):
        #RESET ROBOT
        self.rbt.SetCartLinVel(175) # this also applies to te flux btw
        self.rbt.SetJointVel(100)
        self.rbt.MoveJoints(89.60276,58.61276,-9.38405,2.50345,-47.11293,-90)
        #right above, change position to boop
        self.rbt.MoveJoints(89.60534,67.08336,-11.71448,2.29293,-53.24948,-90.81724)
        print("button pressed")
    
    def grabComp(self):
        #test
        #is right above, going to grab.
        self.rbt.MoveJoints(90.88241,33.42078,-5.06483,1.8569,-28.36862,-1.63362)
        #picked up, go straight up
        self.rbt.SetJointVel(25)
        self.rbt.MoveJoints(90.88241,54.30621,8.67569,0.99,-62.98552,-0.45)
        self.rbt.SetValveState(1, 0)
        self.rbt.Delay(.5)
        self.rbt.MoveLinRelWrf(0,0,100,0,0,0)
        self.rbt.SetJointVel(100)
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        print("component grabbed")

    def flux(self):
        self.rbt.MoveJoints(63.82759,47.56629,-37.65569,85.16172,-64.25638,-78.9819)#upflux - right above the flux
        self.switch.assert_state(True)
        self.rbt.MoveLinRelWrf(0,0,-44,0,0,0)
        self.rbt.Delay(.5)
        self.rbt.MoveLinRelWrf(0,0,50,0,0,0)
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        print("component fluxxed")

    def solder(self):
        print("solder process started")
        self.rbt.SetJointVel(55)
        self.rbt.MoveJoints(16.38724,26.13543,22.60319,21.36569,-50.75017,-13.90172) #right before soldering
        self.switch.assert_state(True)
        self.rbt.MoveLinRelWrf(0,0,-2.3,0,0,0) # set correct elevation
        self.rbt.SetCartLinVel(60)
        self.rbt.MoveLinRelWrf(0, -55, 0, 0, 0, 0) #75 goes all the way through
        self.rbt.SetJointVel(10)
        self.rbt.MoveJointsRel(0,0,0,0,0,-40)
        self.rbt.SetJointVel(55)
        # self.rbt.MoveLinRelWrf(0, 0, 20, -30, 0, 0) #jared movement
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        print("solder process done")

    def drop(self):
        self.rbt.SetJointVel(100)
        self.rbt.MoveJoints(-48.97319,46.6275,-18.48647,-67.68828,-54.63259,54.66379)
        #random pos time
        self.rbt.SetValveState(0,0)
        self.rbt.MoveJoints(90,10.33345,9.92922,0,-20.26293,0)
        print("component done, dropped in cleaner.")
        