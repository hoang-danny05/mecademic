import mecademicpy.robot as mecarbt
import sys
sys.path.append("../")
from lib.Logger import Logger

from Components.VacuumSwitch import VacuumSwitch

#Class based off of SOP16
class Component(Logger):
    """
    TAPE: 12mm button dispenser in the 3rd slot to the left. 
        part was at the red line (probably gone now)
    FLUX: small ceramic bowl on top of the large black flux holder
        2.5 inches from the inner edge from both sides of the hakko sides
        flux level really low
    IMPLEMENTS: LOGGER, DEBUG, INDEX
    PROGRAMMING: SHOULD START AT INDEX 0 UNLESS OTHERWISE SPECIFIED.
    """
    def __init__(self, robot : mecarbt.Robot, switch : VacuumSwitch, **kwargs):
        ##########################################################################################
        # LOCAL NAMES OF THE ROBOT AND VACCUM SENSOR/SWITCH
        ##########################################################################################
        self.rbt: mecarbt.Robot = robot
        self.switch: VacuumSwitch = switch
        self.debug = False

        ##########################################################################################
        # handling tray attributes        
        ##########################################################################################
        self.X_DISTANCE = -15.2
        self.Y_DISTANCE = 15.5
        #amount of rows/colums minus 1
        self.X_COLUMNS = 20
        self.Y_ROWS = 8
        self.X_COLUMNS_M1 = 20-1
        self.Y_ROWS_M1 = 8-1
        MAX_INDEX = self.X_COLUMNS * self.Y_ROWS

        #TODO: make this inherited, not in the code. 
        #### HANDLING KWARGS
        if "debug" in kwargs.keys():
            val = kwargs["debug"]
            assert isinstance(val, bool), "Invalid value for debug"
            self.debug = val
        if ("index" in kwargs.keys()):
            ind = kwargs["index"]
            print(f"recieved index: {ind}")
            assert isinstance(ind, int), "Invalid index type passed"
            assert ind >= 0, "Invalid index value"
            assert ind < MAX_INDEX, "Invalid index value"
            self.index = ind
        else:
            self.index = 0
        

    def _moveToIndex(self, index: int):
        """
        moves the robot to the cell corresponding to the current position
        """
        self.rbt.MoveLinRelWrf(self.X_DISTANCE * (index // self.Y_ROWS), self.Y_DISTANCE * (index % self.Y_ROWS),0 ,0 ,0, 0)
    
    def _indexPositions(self): 
        """
        development function that tests the robot's ability to go to each spot
        """
        self.rbt.Delay(.5)
        print(self.rbt.GetJoints())
        self.rbt.Delay(.5)
        # THE SPOT
        X_DISTANCE = -15.2
        Y_DISTANCE = 15.5
        #amount of rows/colums minus 1
        X_COLUMNS = 20
        Y_ROWS_M1 = 8-1
        for i in range(X_COLUMNS // 2):
            for i in range(Y_ROWS_M1):
                self.rbt.MoveLinRelWrf(0, Y_DISTANCE, 0, 0, 0, 0)
            else: 
                self.rbt.MoveLinRelWrf(0, -1 * Y_DISTANCE * Y_ROWS_M1, 0, 0, 0, 0)
            self.rbt.MoveLinRelWrf(X_DISTANCE, 0, 0, 0, 0, 0)

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
        self.rbt.SetJointVel(50)
        self.rbt.MoveJoints(90,0,0,0,90,0)
        self.rbt.MoveLinRelWrf(0, 90, -65, 0, 0, 0)
        self.rbt.MoveLinRelWrf(81.5, 0, 0, 0, 0, 0)
        self.rbt.Delay(1)
        self._indexPositions()

        raise KeyboardInterrupt
        #self.rbt.MoveJoints(56.4198, 28.02392, 39.36864, -35.7222, -71.32128, 12.97013)
        self._moveToIndex(self.index)
        self.index += 1
        #//button is done 
    
    def grabComp(self):
        #//new pick up
        self.rbt.MoveJoints(70,0,0,0,0,0)
        #self.rbt.MoveLinRelWrf(80, 25.5, 0, 0, 0, 0)
        #//button is done 
        self.log("component grabbed")

    def flux(self):
        self.rbt.MoveJoints(35,30,-30,0,0,0)
        self.rbt.SetCartLinVel(30)
        self.rbt.MoveLinRelWrf(0, 0, -40, 0, 0, 0)
        self.rbt.Delay(.3)
        self.rbt.MoveLinRelWrf(0, 0, 40, 0, 0, 0)
        self.rbt.SetCartLinVel(200)
        #self.rbt.SetJointVel(30)
        #self.rbt.MoveJoints(50.13491, 52.4834, -67.20228, 101.97951, -51.68729, -108.89322)
        #self.rbt.MoveLinRelWrf(0,0,10,0,0,0)
        # has moved right above
        #self.rbt.SetJointVel(50)
        #self.rbt.SetCartLinVel(50)
        #if (not self.debug):
            #self.switch.assert_on()
        #self.rbt.MoveLinRelWrf(0,0,-29,0,0,0)
        #self.rbt.Delay(.3)
        #self.rbt.MoveLinRelWrf(0,-25,40,15,0,0)
        #if (not self.debug):
            #self.switch.assert_on()
        self.log("component fluxxed")

    def solder(self):
        self.rbt.MoveJoints(0,0,0,0,0,0)
        self.rbt.MoveLinRelWrf(22, 0, -77, 0, 0, 0)
        self.rbt.SetCartLinVel(30)
        self.rbt.MoveLinRelWrf(0, 0, 0, 0, 0, -80)
        self.rbt.MoveLinRelWrf(0, 0, 0, 0, 0, -80)
        self.rbt.MoveLinRelWrf(0, 0, 0, 0, 0, -80)
        self.rbt.Delay(.3)
        self.rbt.MoveJoints(0,0,0,0,0,0)
        #self.log("solder process started")
        #self.rbt.MoveJoints(14.02759,15.52448,-7.64043,61.23259,-16.05259,-60.26121)
        ##check 1: hold on! wave is going!!
        #self.rbt.SetCheckpoint(1)
        #if (not self.debug):
            #self.switch.assert_on()
        #self.rbt.MoveLinRelWrf(7,-38.5, 0, 0, 0, 0)
        #self.rbt.SetCartLinVel(150)
        #dip height below, reduced for sanity
        #self.rbt.SetCartLinVel(30)
        #45.6 first success
        #46.15 hits
        #self.rbt.MoveLinRelWrf(0, 0, -46.3, 0, 0, 0)
        #self.rbt.Delay(2.5)
        #self.rbt.SetCartLinVel(15)
        #self.rbt.MoveLinRelWrf(0, 0, 45, 0, 0, 0)
        ##check 2: outside  wave
        #self.rbt.SetCheckpoint(2)
        #if (not self.debug):
            #self.switch.assert_on()
        #self.rbt.SetCartLinVel(75)
        self.log("solder process done")

    def drop(self):
        #self.rbt.MoveJoints(0,0,0,0,0,-90)
        #self.rbt.MoveLinRelWrf(10, 0, -30, -90, 0, 0)
        #self.rbt.MoveLinRelWrf(0, -65, -60, 0, 0, 0)
        #self.rbt.MoveJoints(-46.29698,48.49603,-47.96922,-89.49672,-46.29931,0)
        #self.rbt.SetValveState(0)
        #self.rbt.Delay(1)
        #self.rbt.SetCartLinVel(5000)
        #self.rbt.MoveLinRelWrf(0, 0, 10, 0, 0, 0)
        #self.rbt.Delay(.01)
        #self.rbt.MoveLinRelWrf(0, 0, -10, 0, 0, 0)
        #self.rbt.Delay(.01)
        #self.rbt.MoveLinRelWrf(0, 0, 10, 0, 0, 0)
        #self.rbt.Delay(.01)
        #self.rbt.MoveLinRelWrf(0, 0, -10, 0, 0, 0)
        #if (not self.debug):
            #self.rbt.SetValveState(1)
            #self.switch.assert_off()
            #self.rbt.SetValveState(0)
        #self.rbt.MoveLinRelWrf(0, 0, 90, 0, 0, 0)
        self.finished()
