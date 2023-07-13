import mecademicpy.robot as MecademicRobot
import mecademicpy.robot_classes  
from BGA24k import BGA
import sys
from time import sleep
#use python -m main

############################################
#TODO: MAKE ROBOT ASYNC FOR BETTER STOPPAGE
############################################
try:
    robot = MecademicRobot.Robot()
    # print(robot.IsConnected())
    robot.Connect(address="192.168.0.100", enable_synchronous_mode=True)
except mecademicpy.robot_classes.CommunicationError:
    print("Error Communicating with the robot. Exiting Now.")
    sys.exit()

component = BGA(robot)


robot.ActivateAndHome()

try:
    print("Starting Try loop")
    print(robot.GetJoints())
    for i in range(1): #You know what to do >:] (try 500 at a time)
        print(f"Starting Loop {i+1}")
        component.pressButton()
        component.grabComp()
        component.flux()
        component.preheat()
        component.solder()
        component.drop()
except KeyboardInterrupt:
    print("Manually Exited")

print("successfully exited")
robot.Delay(2)
robot.SetValveState(0, 0)  
# robot.DeactivateRobot()
robot.Disconnect()