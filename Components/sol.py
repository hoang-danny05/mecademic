import mecademicpy.robot as mecarbt
import sys
sys.path.append("../")
from lib.Logger import Logger

from Components.VacuumSwitch import VacuumSwitch

#Class based off of SOP16
class Component(Logger):
    """
    FEEDER: SOL tube feeder
        tube feeder on the right steel slot
        tube on slot 5 & 6 from the left most slot being 1

    VACCUM: brass one with the rubber thing

    FLUX: chad's fluxer, hopefully!

    Notes: 
        fluxer position is in my camera roll! lying directly on the hakko
        preheats!

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
        # it setups the robot :)
        self.rbt.SetJointVel(50)
        self.rbt.SetCartLinVel(200)
        self.rbt.MoveJoints(90,0,0,0,0,0)
        self.rbt.SetJointVel(100)
        self.rbt.MoveLinRelWrf(0, 100, -150, 0, 0, 0)
    
    def grabComp(self):
        #//new pick up
        self.rbt.MoveJoints(90, 0, 0, 0, 0, 0)
        self.rbt.MoveJoints(100.31224,63.22681,-36.39957,-80.37931,-72.06207,61.33621)
        self.rbt.MoveLinRelWrf(0, 0, -10, 0, 0, 0)
        self.rbt.Delay(.5)
        if (not self.debug):
            self.rbt.SetValveState(1)
            self.rbt.Delay(.5)
        self.rbt.MoveLinRelWrf(0, 0, 10, 0, 0, 0)
        self.rbt.MoveJoints(90,0,0,0,0,0)
        if (not self.debug):
            self.switch.assert_on()
        self.log("component grabbed")

    def flux(self):
        #be flux
        self.rbt.MoveJoints(54.62664,68.86629,-80.15793,0,1.92,0) # above

        # # linear dip
        # self.rbt.MoveLinRelWrf(0, 0, -5, 0, 0, 0)
        # self.rbt.Delay(.5)
        # self.rbt.MoveLinRelWrf(0, 0, 5, 0, 0, 0)

        # angular dip
        # self.rbt.MoveJointsRel(0, 0 , 3, 0, 0, 0)
        # self.rbt.Delay(.5)
        # self.rbt.MoveJointsRel(0, 0 , -3, 0, 0, 0)

        self.rbt.MoveJoints(56,49.15474,-56.80034,7.16276,-0.95121,-7.1680) #out

        self.log("component fluxxed")

    def preheat(self):
        self.rbt.MoveJoints(38.97543,24.66,6.1606,5.16983,-34.98672,-4.44828)
        self.rbt.Delay(1)

    def solder(self):
        self.log("solder process started")

        self.rbt.MoveJoints(5.49724,17.10466,14.71216,10.34586,-32.23966,-8.77759)
        if (not self.debug):
            self.switch.assert_on()
        self.rbt.MoveLinRelWrf(0,0, 0, 0, 0, 0)
        self.rbt.MoveLinRelWrf(0, 0, -1, 0, 0, 0)
        self.rbt.Delay(2.5)
        self.rbt.SetCartLinVel(15)
        self.rbt.MoveLinRelWrf(0, 0, 10, 0, 0, 0)

        ##check 2: outside  wave
        if (not self.debug):
            self.switch.assert_on()
        self.rbt.SetCartLinVel(75)
        self.log("solder process done")

    def drop(self):

        self.rbt.MoveJoints(-32.58388,15.56043,6.46009,14.39638,-22.66397,-13.32586)
        self.rbt.SetValveState(0)

        self.rbt.Delay(1)

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
        self.finished()
        self.rbt.MoveJoints(90, 0, 0, 0, 0, 0)
