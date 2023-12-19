import mecademicpy.robot as MecademicRobot
import mecademicpy.robot_classes  
from Components.Resistorssm import Component
import sys
from time import sleep
#debugging
import traceback
#use python -m main

#################################
# NOTE: INITIALIZATION FOR NEEDED OJBECTS
#################################

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
    print("Error Communicating with the robot. Exiting Now.")
    sys.exit()
except TimeoutError:
    print("Error Communicating with the robot. Exiting Now.")
    sys.exit()
except Exception:
    traceback.print_exc()
    sys.exit()


component = Component(robot)
robot.ActivateAndHome()

###################################
# INPUT HANDLING
##################################
try:
    loops = int(sys.argv[1]) if len(sys.argv) > 1 else 1 #default amount of loops is 1, else it is the first argument
except ValueError:
    print("Wrong type entered, only an integer is accepted. Using default value of 1.")
    loops = 1
except Exception as e:
    traceback.print_exc()
    loops = 1

##################################
# MAIN ACTIONS
##################################
try:
    print("Starting Try loop")
    print(robot.GetJoints())
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
    print("\nManually Exited With CTRL+C")
except AssertionError:
    # stop right there buster!!
    robot.PauseMotion() #works btw
    robot.ClearMotion()
    # beep and wait for hooman
    try:
        input("Robot missing part, Press any key to exit:")
    except KeyboardInterrupt:
        print("Exited with CTRL + C")
    print("exited, returning to normal position. ")
except Exception as e:
    print(f"Unknown Exception \"{e}\" happened, exiting.")
    print("######## START TRACEBACK ########")
    traceback.print_exc()
    print("######## END TRACEBACK ########")
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
    print("Successfully Exited.")

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
