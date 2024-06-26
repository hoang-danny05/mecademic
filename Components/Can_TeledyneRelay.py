import mecademicpy.robot as mecarbt
import sys
sys.path.append("../")
from lib.Logger import Logger

from Components.VacuumSwitch import VacuumSwitch

#Class based off of SOP16
class Component(Logger):
    """
    FEEDER: Fixture on the steel plate denoted by the red lines if they're still there
    FLUX: Flux bowl somewhat centered within the hakko
    Notes: 
        hakko's solder level is very fussy
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
        self.rbt.SetJointVel(100)
        self.rbt.MoveLinRelWrf(0, 100, -150, 0, 0, 0)
        #//button is done 
    
    def grabComp(self):
        #//new pick up
        self.rbt.SetCartLinVel(70)
        self.rbt.MoveLinRelWrf(0, 1, -26, 0, 0, 0)
        if (not self.debug):
            self.rbt.SetValveState(1)
            self.rbt.Delay(1)
        self.rbt.MoveLinRelWrf(0, 0, 50, 0, 0, 0)
        self.rbt.SetJointVel(30)
        self.rbt.MoveJoints(90,0,0,0,0,0)
        if (not self.debug):
            self.switch.assert_on()
        self.log("component grabbed")

    def flux(self):
        self.rbt.SetJointVel(30)
        self.rbt.MoveJoints(50.13491, 52.4834, -67.20228, 101.97951, -51.68729, -108.89322)
        #self.rbt.MoveLinRelWrf(0,0,10,0,0,0)
        # has moved right above
        self.rbt.SetJointVel(50)
        self.rbt.SetCartLinVel(50)
        if (not self.debug):
            self.switch.assert_on()
        self.rbt.MoveLinRelWrf(0,0,-29,0,0,0)
        self.rbt.Delay(.3)
        self.rbt.MoveLinRelWrf(0,-25,40,15,0,0)
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
        self.rbt.MoveLinRelWrf(7,-38.5, 0, 0, 0, 0)
        self.rbt.SetCartLinVel(150)
        #dip height below, reduced for sanity
        self.rbt.SetCartLinVel(30)
        #45.6 first success
        #46.15 hits
        #46.3
        self.rbt.MoveLinRelWrf(0, 0, -48.8, 0, 0, 0)
        self.rbt.Delay(2.5)
        self.rbt.SetCartLinVel(15)
        self.rbt.MoveLinRelWrf(0, 0, 45, 0, 0, 0)
        ##check 2: outside  wave
        self.rbt.SetCheckpoint(2)
        if (not self.debug):
            self.switch.assert_on()
        self.rbt.SetCartLinVel(75)
        self.log("solder process done")

    def drop(self):
        #self.rbt.MoveJoints(0,0,0,0,0,-90)
        self.rbt.MoveLinRelWrf(10, 0, -30, -90, 0, 0)
        self.rbt.MoveLinRelWrf(0, -65, -60, 0, 0, 0)
        #self.rbt.MoveJoints(-46.29698,48.49603,-47.96922,-89.49672,-46.29931,0)
        self.rbt.SetValveState(0)
        # self.rbt.Delay(1)
        # self.rbt.SetCartLinVel(5000)
        #self.rbt.MoveLinRelWrf(0, 0, 10, 0, 0, 0)
        #self.rbt.Delay(.01)
        #self.rbt.MoveLinRelWrf(0, 0, -10, 0, 0, 0)
        #self.rbt.Delay(.01)
        #self.rbt.MoveLinRelWrf(0, 0, 10, 0, 0, 0)
        #self.rbt.Delay(.01)
        #self.rbt.MoveLinRelWrf(0, 0, -10, 0, 0, 0)
        #if (not self.debug):
        #    self.rbt.SetValveState(1)
        #    self.switch.assert_off()
        #    self.rbt.SetValveState(0)
        self.rbt.MoveLinRelWrf(0, 0, 90, 0, 0, 0)
        self.finished()
