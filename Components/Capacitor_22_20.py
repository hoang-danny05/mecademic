import mecademicpy.robot as mecarbt
import sys
sys.path.append("../")
from lib.Logger import Logger

from Components.VacuumSwitch import VacuumSwitch

#Class based off of SOP16
class Component(Logger):
    """
    in memory of big resistor
    TAPE: 12mm button dispenser in the 3rd slot to the left. 
        part was at the red line (probably gone now)
    FLUX: small ceramic bowl on top of the large black flux holder
        2.5 inches from the inner edge from both sides of the hakko sides
        flux level really low
    IMPLEMENTS: LOGGER, DEBUG 
    """
    def __init__(self, robot : mecarbt.Robot, switch : VacuumSwitch, **kwargs):
        ##########################################################################################
        # LOCAL NAMES OF THE ROBOT AND VACCUM SENSOR/SWITCH
        ##########################################################################################
        self.rbt: mecarbt.Robot = robot
        self.switch: VacuumSwitch = switch
        self.debug = False
        #TODO: make this inherited, not in the code. 
        if "debug" in kwargs.keys():
            val = kwargs["debug"]
            assert isinstance(val, bool), "Invalid value for debug"
            self.debug = val
    
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
        if(not self.debug):
            self.rbt.MoveLinRelWrf(0, 0, -13, 0, 0, 0)
            self.rbt.Delay(.3)
            self.rbt.MoveLinRelWrf(0, 0, 13, 0, 0, 0)
        #//button is done 
    
    def grabComp(self):
        #//new pick up
        self.rbt.MoveLinRelWrf(-11.5,  -26.5,  0,  0,  0,  0)
        self.rbt.SetCartLinVel(70)
        self.rbt.MoveLinRelWrf(0, 0, -11.5, 0, 0, 0)
        if (not self.debug):
            self.rbt.SetValveState(1)
            self.rbt.Delay(.2)
        self.rbt.MoveLinRelWrf(0, 0, 11.5, 0, 0, 0)
        self.rbt.MoveJoints(90,0,0,0,0,0)
        if (not self.debug):
            self.switch.assert_on()
        self.log("component grabbed")

    def flux(self):
        self.rbt.SetJointVel(50)
        self.rbt.MoveJoints(50.13491,45.08948,-48.0494,92.46931,-50.19828,-93.85345)
        # has moved right above
        self.rbt.SetJointVel(60)
        self.rbt.SetCartLinVel(50)
        if (not self.debug):
            self.switch.assert_on()
        self.rbt.MoveLinRelWrf(0,0,-47.5,0,0,0)
        self.rbt.Delay(.3)
        self.rbt.MoveLinRelWrf(0,0,47.5,0,0,0)
        if (not self.debug):
            self.switch.assert_on()
        self.log("component fluxxed")

    def solder(self):
        self.log("solder process started")
        self.rbt.MoveJoints(14.02759,15.52448,-7.64043,61.23259,-16.05259,-60.26121)
        ##check 1: hold on! wave is going!!
        self.rbt.SetCheckpoint(1)
        if (not self.debug):
            self.switch.assert_on()
        self.rbt.SetCartLinVel(150)
        #dip height below, reduced for sanity
        self.rbt.MoveLinRelWrf(5, 0, -56, 0, 0, 0)
        self.rbt.SetCartLinVel(30)
        self.rbt.MoveLinRelWrf(0,-38.5, 0, 0, 0, 0)
        #delay for longer because flux must crawl
        self.rbt.Delay(2.2)
        self.rbt.SetCartLinVel(10)
        self.rbt.MoveLinRelWrf(0, 0, 12, 0, 0, 0)
        ##check 2: outside  wave
        self.rbt.SetCheckpoint(2)
        self.rbt.SetCartLinVel(75)
        # self.rbt.MoveLinRelWrf(0, 0, 20, -30, 0, 0) #jared movement
        self.log("solder process done")

    def drop(self):
        self.rbt.MoveJoints(-46.29698,48.49603,-47.96922,-89.49672,-46.29931,89.27155)
        self.rbt.SetValveState(0)
        self.rbt.Delay(1)
        if (not self.debug):
            self.rbt.SetValveState(1)
            self.switch.assert_off()
            self.rbt.SetValveState(0)
            self.finished()
