import mecademicpy.robot as MecademicRobot
import mecademicpy.robot_classes  
from BGAsm import BGAsm
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

component = BGAsm(robot)
robot.ActivateAndHome()

loops = sys.argv[1] if len(sys.argv) > 1 else 1 #default amount of loops is 1, else it is the first argument

try:
    print("Starting Try loop")
    print(robot.GetJoints())
    for i in range(loops): #You know what to do >:] (try 500 at a time) doing 100 + 108+53
        print(f"Starting Loop {i+1}")
        component.pressButton()
        component.grabComp()
        component.flux()
        #component.preheat()
        component.solder()
        component.drop()
except KeyboardInterrupt:
    print("Manually Exited")

print("successfully exited")
robot.Delay(2)
robot.SetValveState(0, 0)  
# robot.DeactivateRobot()
robot.Disconnect()