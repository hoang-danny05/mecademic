import mecademicpy.robot

#class for the SOP16 component (2 sets of 8 terminals)
class component:
    def __init__(self, robot):
        self.rbt = robot
    
    def pressButton(self):
        #must be calibrated for parts
        self.rbt.MoveJoints()
        
        #right above, change velocity to boop
        self.rbt.MoveJoints()
        print()
    
    def grabComp(self):
        #test
        self.rbt.MoveJoints()
        #is right above, going to grab.
        self.rbt.MoveJoints()
        self.rbt.SetValveState(1, 0)
        #picked up, go straight up
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        print("component grabbed")

    def flux(self):
        #150mm tall flux bowl
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        print("component fluxxed")

    def preheat(self):
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        print("preheat done")

    def solder(self):
        print("solder process started")
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        print("solder process done")

    def drop(self):
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        self.rbt.MoveJoints()
        print("component done, dropped in cleaner.")
        