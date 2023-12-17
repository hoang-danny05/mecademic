import mecademicpy.robot as mecarbt

from Components.VacuumSwitch import VacuumSwitch

#Class based off of SOP16
class BigResistor:
    def __init__(self, robot : mecarbt.Robot, switch : VacuumSwitch):
        ##########################################################################################
        # LOCAL NAMES OF THE ROBOT AND VACCUM SENSOR/SWITCH
        ##########################################################################################
        self.rbt: mecarbt.Robot = robot
        self.switch: VacuumSwitch = switch
        callbacks: mecarbt.RobotCallbacks = mecarbt.RobotCallbacks()
        callbacks.on_checkpoint_reached = self.test_callback
        self.rbt.RegisterCallbacks(callbacks=callbacks, run_callbacks_in_separate_thread=True)

    def test_callback(self):
        for i in range(5): 
            print(f"test check #{i}")
    
    def pressButton(self):
        ##########################################################################################
        # FIRST BLOCK EXECTUED BY main.py
        ##########################################################################################
        #RESET ROBOT
        ### pressbutton ### 12mm
        #buttono above
        self.rbt.SetJointVel(100)
        self.rbt.SetCartLinVel(200)
        self.rbt.MoveJoints(90,0,0,0,0,0)
        self.rbt.SetJointVel(60)
        self.rbt.MoveJoints(118.44233,70.25043,-48.89198,-136.70483,31.49069,137.04052)
        self.rbt.MoveLinRelWrf(0, 0, -13, 0, 0, 0)
        self.rbt.Delay(.3)
        self.rbt.MoveLinRelWrf(0, 0, 13, 0, 0, 0)
        #//button is done 
    
    def grabComp(self):
        #//new pick up
        self.rbt.MoveLinRelWrf(-11.5,  -27.5,  0,  0,  0,  0)
        self.rbt.SetCartLinVel(70)
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
        ##check 1: hold on! wave is going!!
        self.rbt.setCheckpoint(1)
        self.switch.assert_on()
        self.rbt.SetCartLinVel(150)
        self.rbt.MoveLinRelWrf(5, 0, -57.25, 0, 0, 0)
        self.rbt.SetCartLinVel(30)
        self.rbt.MoveLinRelWrf(0,-38.5, 0, 0, 0, 0)
        self.rbt.Delay(.8)
        self.rby.SetCartLinVel(10)
        self.rbt.MoveLinRelWrf(0, 0, 12, 0, 0, 0)
        ##check 2: outside  wave
        self.rbt.setCheckpoint(2)
        self.rbt.SetCartLinVel(75)
        # self.rbt.MoveLinRelWrf(0, 0, 20, -30, 0, 0) #jared movement
        print("solder process done")

    def drop(self):
        self.rbt.MoveJoints(-46.29698,48.49603,-47.96922,-89.49672,-46.29931,89.27155)
        self.rbt.SetValveState(0)
        self.rbt.Delay(1)
        self.switch.assert_off()
