import mecademicpy.robot as MecademicRobot
import mecademicpy.robot_classes  
from Components.BigResistor import BigResistor
import sys
from time import sleep
from Components.VacuumSwitch import VacuumSwitch
#debugging
import traceback
#use python -m main

#################################
# NOTE: INITIALIZATION FOR NEEDED OJBECTS
#################################

switch = VacuumSwitch()

try:
    robot = MecademicRobot.Robot()
    # print(robot.IsConnected())
    robot.Connect(address="192.168.0.100", enable_synchronous_mode=True, disconnect_on_exception=False)
except mecademicpy.robot_classes.CommunicationError:
    print("Error Communicating with the robot. Exiting Now.")
    sys.exit()
except TimeoutError:
    print("Error Communicating with the robot. Exiting Now.")
    sys.exit()
except Exception:
    traceback.print_exc()
    switch.cleanup()
    sys.exit()

robot.SetValveState(0)
