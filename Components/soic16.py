import mecademicpy.robot as mecarbt
import sys
sys.path.append("../")
from lib.Logger import Logger

from Components.VacuumSwitch import VacuumSwitch

#Class based off of SOP16
class Component(Logger):
    """
    FEEDER: 8-pitch wide tape with horizontal parts

    FLUX: temporary position against the hakko for the fluxer

    END EFFECTOR: Brass vacuum nozzle without the flex thing
        
    NOTE: Do NOT let it suck up flux!
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
// //setup
// SetJointVel(50)
// MoveJoints(90, 0, 0, 0, 0, 0)
        self.rbt.SetCartLinVel(50)
    
    def grabComp(self):
        #//new pick up
// //above the part
// MoveJoints(91.70922,38.45224,11.54845,2.23241,-50.02397,-1.43534)
// MoveLinRelWrf(0, 0, -15, 0, 0, 0)
// SetValveState(1)
// Delay(.5)
// MoveLinRelWrf(0, 0, 15, 0, 0, 0)
// MoveJoints(90, 0, 0, 0, 0, 0)
        self.log("component grabbed")

    def flux(self):
// //be flux
// MoveJoints(68.50862,48.29483,-54.1694,7.16276,-0.95121,-31.51552) //before
// MoveJoints(58.52845,54.92741,-57.43448,7.16276,-0.95121,-7.16897) //above
// MoveLinRelWrf(0, 0, -15, 0, 0, 0)
// Delay(1)
// MoveLinRelWrf(0, 0,5, 0, 0, 0)
// MoveJoints(57.33724,49.15474,-56.80034,7.16276,-0.95121,-7.1680)
        self.rbt.SetCartLinVel(1000)
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

    def preheat(self):
        self.rbt.MoveJoints(45.92638,28.83078,1.85586,30.81052,-34.33086,-26.18103)
        self.rbt.Delay(1)

    def solder(self):
        self.log("solder process started")
        #// //above solder
        self.rbt.MoveJoints(5.09198,16.83362,7.24164,12.32276,-24.57621,-11.23621)
        self.rbt.MoveJoints(5.18509,18.26509,17.85207,8.75328,-36.43655,-7.06121)
        self.rbt.MoveLinRelWrf(0, 0, -1, 0, 0, 0)
        self.rbt.SetCartLinVel(15)
        self.rbt.MoveLinRelWrf(0, -15, 0, 0, 0, 0)
        self.rbt.SetCartAngVel(10)
        self.rbt.MoveLinRelWrf(0, 4, 15, -20, 0, 0)

    def drop(self):
        #// //above cleaner
        self.rbt.MoveJoints(-37.86828,23.55569,8.08034,-55.9981,-47.76828,14.89655)
        self.rbt.SetValveState(0)
        self.rbt.Delay(1)
        self.rbt.SetJointVel(50)
        self.rbt.MoveJoints(90, 0, 0, 0, 0, 0)
        #// optional shaky shaky
        # self.rbt.SetCartLinVel(5000)
        # self.rbt.MoveLinRelWrf(0, 0, 10, 0, 0, 0)
        # self.rbt.Delay(.01)
        # self.rbt.MoveLinRelWrf(0, 0, -10, 0, 0, 0)
        # self.rbt.Delay(.01)
        # self.rbt.MoveLinRelWrf(0, 0, 10, 0, 0, 0)
        # self.rbt.Delay(.01)
        # self.rbt.MoveLinRelWrf(0, 0, -10, 0, 0, 0)
        self.log("part dropped")
        #//assert off here
        self.rbt.SetValveState(1)
        self.rbt.Delay(.1)
        self.switch.assert_off()
        self.rbt.SetValveState(0)
        self.rbt.SetCartLinVel(1000)
