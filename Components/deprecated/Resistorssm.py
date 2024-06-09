import mecademicpy.robot
# from VacuumSwitch import VacuumSwitch

#Class based off of SOP16
class Component:
    """
    Deprecated
    Wrong Nozzle
    Wrong fluxer
    No Switch
    """
    def __init__(self, robot : mecademicpy.robot):
        self.rbt = robot
        # self.switch = switch
    
    def pressButton(self):
        #RESET ROBOT
        self.rbt.SetCartLinVel(175) # this also applies to te flux btw
        self.rbt.SetJointVel(50)
        self.rbt.MoveJoints(87.96362,62.90664,-11.82931,-2.61672,-51.10655,-88.35603)
        #right above, change position to boop
        self.rbt.MoveLinRelWrf(0,0,-22,0,0,0)
        self.rbt.Delay(.1)
        self.rbt.MoveLinRelWrf(0,0,50,0,0,0)
        print("button pressed")
    
    def grabComp(self):
        #test
        #is right above, going to grab.
        self.rbt.MoveJoints()
        #picked up, go straight up
        self.rbt.SetJointVel()
        self.rbt.MoveJoints()
        self.rbt.SetValveState()
        self.rbt.Delay()
        self.rbt.MoveLinRelWrf()
        self.rbt.SetJointVel()
        print("component grabbed")

    def flux(self):
        self.rbt.MoveJoints()#upflux - right above the flux
        # self.switch.assert_state(True)
        self.rbt.MoveLinRelWrf()
        self.rbt.Delay()
        self.rbt.MoveLinRelWrf()
        # self.rbt.MoveJoints()
        print("component fluxxed")

    def solder(self):
        print("solder process started")
        self.rbt.SetJointVel(55)
        self.rbt.MoveJoints(16.38724,26.13543,22.60319,21.36569,-50.75017,-13.90172) #right before soldering
        # self.switch.assert_state(True)
        self.rbt.MoveLinRelWrf(0,0,-2.3,0,0,0) # set correct elevation
        self.rbt.SetCartLinVel(60)
        self.rbt.MoveLinRelWrf(0, -55, 0, 0, 0, 0) #75 goes all the way through
        self.rbt.SetJointVel(10)
        self.rbt.MoveJointsRel(0,0,0,0,0,-40)
        self.rbt.SetJointVel(55)
        # self.rbt.MoveLinRelWrf(0, 0, 20, -30, 0, 0) #jared movement
        print("solder process done")

    def drop(self):
        self.rbt.SetJointVel(100)
        self.rbt.MoveJoints(-48.97319,46.6275,-18.48647,-67.68828,-54.63259,54.66379)
        #random pos time
        self.rbt.SetValveState(0,0)
        self.rbt.MoveJoints(90,10.33345,9.92922,0,-20.26293,0)
        print("component done, dropped in cleaner.")
        