import mecademicpy.robot as MecademicRobot
import mecademicpy.robot_classes  
from BGA24k import BGA
import sys
from time import sleep
#use python -m main

try:
    robot = MecademicRobot.Robot()
    robot.Connect(address="192.168.0.100", enable_synchronous_mode=True)
except mecademicpy.robot_classes.CommunicationError:
    print("Error Communicating with the robot. Exiting Now.")
    sys.exit()

component = BGA(robot)


robot.ActivateAndHome()

try:
    print("Starting Try loop")
    print(robot.GetJoints())
    robot.SetJointVel(25)
    component.pressButton()
    component.grabComp()
    component.flux()
    component.preheat()
    component.solder()
    component.drop()
except KeyboardInterrupt:
    print("Manually Exited")

robot.DeactivateRobot()
robot.Disconnect()