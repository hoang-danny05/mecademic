import mecademicpy.robot
from Components.VacuumSwitch import VacuumSwitch

#Class based off of SOP16
class BigResistor:
    def __init__(self, robot : mecademicpy.robot, switch : VacuumSwitch):
        ##########################################################################################
        # LOCAL NAMES OF THE ROBOT AND VACCUM SENSOR/SWITCH
        ##########################################################################################
        self.rbt = robot
        self.switch = switch
    
    def pressButton(self):
        ##########################################################################################
        # FIRST BLOCK EXECTUED BY main.py
        ##########################################################################################
        #RESET ROBOT
        ### pressbutton ### 12mm
        SetJointVel(75)
        SetCartLinVel(100)
        MoveJoints(90, 0, 0, 0, 0, 0)
        #buttono above
        self.rbt.MoveJoints(118.44233,70.25043,-48.89198,-136.70483,31.49069,137.04052)
        self.rbt.MoveLinRelWrf(0, 0, -13, 0, 0, 0)
        self.rbt.Delay(.5)
        self.rbt.MoveLinRelWrf(0, 0, 13, 0, 0, 0)
        #//button is done 
    
    def grabComp(self):
        #//new pick up
        self.rbt.MoveLinRelWrf(-9,  -28,  0,  0,  0,  0)
        self.rbt.MoveLinRelWrf(0, 0, -11.5, 0, 0, 0)
        self.rbt.SetValveState(1)
        self.rbt.Delay(.2)
        self.rbt.MoveLinRelWrf(0, 0, 11.5, 0, 0, 0)
        self.switch.assert_on()
        print("component grabbed")

    def flux(self):
        self.rbt.MoveJoints(34.26388,27.11716,-19.84707,-43.92569,-5.55259,43.57155)
        self.switch.assert_on()
        self.rbt.MoveJoints(34.26388,27.15233,0.90517,-9.11483,-25.07121,8.04914)
        self.rbt.Delay(.3)
        self.rbt.MoveJoints(34.26388,27.11716,-19.84707,-43.92569,-5.55259,43.57155)
        print("component fluxxed")

    def solder(self):
        print("solder process started")
        self.rbt.MoveJoints(14.02759,15.52448,-7.64043,61.23259,-16.05259,-60.26121)
        self.switch.assert_on()
        self.rbt.SetCartLinVel(75)
        self.rbt.MoveLinRelWrf(5, 0, -56.5, 0, 0, 0)
        self.rbt.MoveLinRelWrf(0,-35, 0, 0, 0, 0)
        self.rbt.SetCartLinVel(30)
        self.rbt.MoveLinRelWrf(0, -35, 0, 0, 0, 0)
        self.rbt.SetCartLinVel(75)
        # self.rbt.MoveLinRelWrf(0, 0, 20, -30, 0, 0) #jared movement
        print("solder process done")

    def drop(self):
        self.rbt.MoveJoints(-46.29698,48.49603,-47.96922,-89.49672,-46.29931,89.27155)
        self.rbt.SetValveState(0)
        self.rbt.Delay(1)
        self.switch.assert_off()
