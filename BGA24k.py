import mecademicpy.robot

#class for the SOP16 component (2 sets of 8 terminals)
class BGA:
    def __init__(self, robot):
        self.rbt = robot
    
    def pressButton(self):
        #must be calibrated for parts
        self.rbt.MoveJoints(89.60276,58.61276,-9.38405,2.50345,-47.11293,1.98966)
        
        #right above, change velocity to boop
        self.rbt.MoveJoints(89.60276,61.97767,-9.49086,2.3819,-50.36845,2.17414)
        print("button pressed")
    
    def grabComp(self):
        #test
        self.rbt.MoveJoints(90.93181,43.23,9.86819,2.6519,-50.89707,2.07069)
        #is right above, going to grab.
        self.rbt.MoveJoints(91.17698,55.9231,9.54026,1.29414,-65.46931,-0.5370)
        self.rbt.SetValveState(1, 0)
        #picked up, go straight up
        self.rbt.MoveJoints(91.17724,35.84328,3.16138,1.86983,-39.02017,-1.45259)
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
        #150mm tall flux bowl
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        print("component fluxxed")

    def preheat(self):
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        print("preheat done")

    def solder(self):
        print("solder process started")
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        print("solder process done")

    def drop(self):
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        print("component done, dropped in cleaner.")
        