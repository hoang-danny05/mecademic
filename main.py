import mecademicpy.robot as MecademicRobot
import mecademicpy.robot_classes  
from SOP16 import SOP16
import sys
from time import sleep
from VacuumSwitch import VacuumSwitch
#debugging
import traceback
#use python -m main

############################################
#TODO: MAKE ROBOT ASYNC FOR BETTER STOPPAGE
############################################
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
    sys.exit()

switch = VacuumSwitch()

component = SOP16(robot)
robot.ActivateAndHome()

try:
    loops = int(sys.argv[1]) if len(sys.argv) > 1 else 1 #default amount of loops is 1, else it is the first argument
except ValueError:
    print("Wrong type entered, only an integer is accepted. Using default value of 1.")
    loops = 1
except Exception as e:
    traceback.print_exc()
    loops = 1

try:
    print("Starting Try loop")
    print(robot.GetJoints())
    for i in range(loops): #You know what to do >:] (try 500 at a time) doing 100 + 108+53
        print(f"Starting Loop {i+1}")
        component.pressButton()
        component.grabComp()
        if switch.read_state() == False:
            raise Exception('No part is connected to the robot') 
        component.flux()
        if switch.read_state() == False:
            raise Exception('No part is connected to the robot') 
        # #component.preheat()
        component.solder()
        component.drop()
except KeyboardInterrupt:
    robot.PauseMotion() #experimental, said to completely interrupt the robot.
    robot.ClearMotion()
    print("\nManually Exited With CTRL+C")
except Exception as e:
    print(f"Unknown Exception \"{e}\" happened, exiting.")
    print("######## START TRACEBACK")
    traceback.print_exc()
    print("######## END TRACEBACK")
else: 
    print("Successfully Exited.")

print("Program finished.")
try:
    robot.ResumeMotion()
    #################################################
    # ROBOT RESET
    #################################################
    robot.MoveJoints(90,0,0,0,0,0)
    robot.SetValveState(0, 0)
except Exception:
    traceback.print_exc()
    print("robot interrupted during deactivation.") 
# robot.DeactivateRobot()
robot.Disconnect()