import mecademicpy.robot as mecarbt
import sys
sys.path.append("../")
from lib.Logger import Logger

from Components.VacuumSwitch import VacuumSwitch

#Class based off of SOP16
class Component(Logger):
    """
    FEEDER: SOP 8 tube dispenser in the second-most right position
    FLUX: small ceramic bowl on top of the large black flux holder
        2.5 inches from the inner edge from both sides of the hakko sides
        flux level really low
    DROP: fluxer that hangs off of the DI container
    END EFFECTOR: new nozzle that may or may not be on correctly 
    note: can be a lot more optimal with some position changes, but i'm too lazy to do them
    """
    def __init__(self, robot : mecarbt.Robot, switch : VacuumSwitch):
        ##########################################################################################
        # LOCAL NAMES OF THE ROBOT AND VACCUM SENSOR/SWITCH
        ##########################################################################################
        self.rbt: mecarbt.Robot = robot
        self.switch: VacuumSwitch = switch
    
    def pressButton(self):
        ##########################################################################################
        # FIRST BLOCK EXECTUED BY main.py
        ##########################################################################################
        #RESET ROBOT
        ### pressbutton ### 12mm
        #buttono above
        self.rbt.SetJointVel(75)
        self.rbt.SetCartLinVel(50)
        self.rbt.MoveJoints(90, 0, 0, 0, 0, 0)
        #//button is done 
    
    def grabComp(self):
        #//new pick up
        self.rbt.MoveJoints(70.46095,31.76819,18.8144,-24.67345,-53.24431,15.37069)
        self.rbt.MoveLinRelWrf(0, 0, -11.25, 0, 0, 0)
        self.rbt.SetValveState(1)
        self.rbt.Delay(.3)
        self.log("component grabbed")

    def flux(self):
        self.rbt.SetCartLinVel(5000)
        self.rbt.MoveLinRelWrf(0, 0, 100, 0, 0, 0)
        #// robot at 47.08707,18.72905,-4.39034,-75.08431,-44.80034,69.42328
        self.rbt.MoveJoints(50.13491,45.08948,-48.0494,92.46931,-50.19828,-93.85345)
        self.rbt.SetCartLinVel(50)
        self.switch.assert_on()
        #//FLUXdip starts here
        #//assert on
        self.rbt.MoveLinRelWrf(0,0,-47.5,0,0,0)
        self.rbt.Delay(.3)
        self.rbt.MoveLinRelWrf(0,0,47.5,0,0,0)
        self.switch.assert_on()
        self.log("component fluxxed")

    def solder(self):
        self.log("solder process started")
        #//offset: y=-30, alpha=20
        #//solder time
        #//travel
        self.switch.assert_on()
        self.rbt.SetCartLinVel(150)
        self.rbt.MoveLinRelWrf(26, -140, 0, 0, 0, 0)
        self.rbt.MoveLinRelWrf(0, 0, 0, -20, 0, 0)
        self.rbt.SetCartLinVel(50)
        #//solder dunk
        #//assert on 
        self.switch.assert_on()
        self.rbt.MoveLinRelWrf(0, 0, -47, 0, 0, 0)
        self.rbt.Delay(.8)
        self.rbt.MoveLinRelWrf(0, 0, 47, 0, 0, 0)
        self.rbt.MoveLinRelWrf( 0,  -50,  0,  40,  0, 0 )
        #//assert on
        self.switch.assert_on()
        self.rbt.MoveLinRelWrf(0, 0, -47, 0, 0, 0)
        self.rbt.Delay(.8)
        self.rbt.MoveLinRelWrf(0, 0, 47, 0, 0, 0)
        self.log("solder process done")

    def drop(self):
        self.rbt.MoveJoints(-47.61233,46.67767,-38.22543,-82.35828,-48.18155,78.62414)
        self.rbt.SetValveState(0)
        #//shaky shaky
        self.rbt.SetCartLinVel(5000)
        self.rbt.MoveLinRelWrf(0, 0, 10, 0, 0, 0)
        self.rbt.Delay(.01)
        self.rbt.MoveLinRelWrf(0, 0, -10, 0, 0, 0)
        self.rbt.Delay(.01)
        self.rbt.MoveLinRelWrf(0, 0, 10, 0, 0, 0)
        self.rbt.Delay(.01)
        self.rbt.MoveLinRelWrf(0, 0, -10, 0, 0, 0)
        #//assert off here
        self.rbt.SetValveState(1)
        self.rbt.Delay(.1)
        self.switch.assert_off()
        self.rbt.SetValveState(0)
        self.rbt.SetCartLinVel(1000)