import mecademicpy.robot as MecademicRobot
import mecademicpy.robot_classes  
from Components.SOIC8 import Component
import sys
from time import sleep
from lib.OutputStyle import Foreground, Style
from Components.VacuumSwitch import VacuumSwitch
#debugging
import traceback
#use python -m main

#################################
# NOTE: INITIALIZATION FOR NEEDED OJBECTS
#################################

switch = VacuumSwitch()
robot = MecademicRobot.Robot()

def test_callback(self):
    for i in range(5): 
        sleep(1)
        print(f"test check #{i}")

callbacks: mecademicpy.robot.RobotCallbacks = mecademicpy.robot.RobotCallbacks()
callbacks.on_checkpoint_reached = test_callback
robot.RegisterCallbacks(callbacks=callbacks, run_callbacks_in_separate_thread=True)

try:
    # print(robot.IsConnected())
    robot.Connect(address="192.168.0.100", enable_synchronous_mode=True, disconnect_on_exception=False)
except mecademicpy.robot_classes.CommunicationError:
    print(Foreground.red, Style.bold, "Error Communicating with the robot. Exiting Now.")
    sys.exit()
except TimeoutError:
    print(Foreground.red, Style.bold, "Error Communicating with the robot. Exiting Now.")
    sys.exit()
except Exception:
    print(Foreground.red, Style.bold, "Unknown Error: ", Style.reset)
    traceback.print_exc()
    switch.cleanup()
    sys.exit()


component = Component(robot, switch)
robot.ActivateAndHome()

###################################
# INPUT HANDLING
##################################
try:
    loops = int(sys.argv[1]) if len(sys.argv) > 1 else 1 #default amount of loops is 1, else it is the first argument
except ValueError:
    print(Foreground.orange, Style.bold, "Wrong type entered, only an integer is accepted. Using default value of 1.", Style.reset)
    loops = 1
except Exception as e:
    traceback.print_exc()
    loops = 1

##################################
# MAIN ACTIONS
##################################
try:
    print("Starting process..")
    print(robot.GetJoints(), end="\r")
    for i in range(loops): #You know what to do >:] (try 500 at a time) doing 100 + 108+53
        print(f"Starting Loop {i+1}")
        ##########################################################################################
        # Start of all blocks of code that will execute [loop] times.
        ##########################################################################################
        component.pressButton()
        component.grabComp()
        component.flux()
        # #component.preheat() #one day
        component.solder()
        component.drop()
        ##########################################################################################
        # End of block
        ##########################################################################################
except KeyboardInterrupt:
    robot.PauseMotion() #experimental, said to completely interrupt the robot.
    robot.ClearMotion()
    print(Style.bold, "\nManually Exited With CTRL+C", Style.reset)
except AssertionError:
    # stop right there buster!!
    robot.PauseMotion() #works btw
    robot.ClearMotion()
    # beep and wait for hooman
    switch.start_alarm()
    try:
        input(Style.bold, "Robot missing part, Press any key to exit:", Style.reset)
    except KeyboardInterrupt:
        print("Exited with CTRL + C")
    switch.stop_alarm()
    print("exited, returning to normal position. ")
except Exception as e:
    print(Foreground.red, Style.bold, f"Unknown Exception \"{e}\" happened, exiting.")
    print(Style.reset, Foreground.red, "######## START TRACEBACK ########", Style.reset)
    traceback.print_exc()
    print(Foreground.red, "######## END TRACEBACK ########", Style.reset)
    robot.PauseMotion() #works btw
    robot.ClearMotion()
    try:
        input("Error. Input to raise arm, cancel to simply home.")
        robot.MoveLinRelWrf(0, 0, 100, 0, 0, 0)
    except KeyboardInterrupt:
        print("Exited with CTRL + C")
    except Exception:
        print("danny was dumb. EXITING NOW")
else: 
    print(Foreground.green, "Successfully Exited.", Style.reset)

####################################
# PROGRAM END
####################################
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

#should ALWAYS execute on exit
robot.Disconnect()
switch.cleanup()
