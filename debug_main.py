import mecademicpy.robot as MecademicRobot
import mecademicpy.robot_classes  
from Components.QuadTray import Component
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

# def test_callback(self):
#     for i in range(5): 
#         sleep(1)
#         print(f"test check #{i}")
#
# callbacks: mecademicpy.robot.RobotCallbacks = mecademicpy.robot.RobotCallbacks()
# callbacks.on_checkpoint_reached = test_callback
# robot.RegisterCallbacks(callbacks=callbacks, run_callbacks_in_separate_thread=True)
 
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

###################################
# ARGS HANDLING
##################################
# USAGE: python main.py [LOOPS] [INDEX]
try:
    loops = int(sys.argv[1]) if len(sys.argv) > 1 else 1 #default amount of loops is 1, else it is the first argument
except ValueError:
    print(Foreground.orange, Style.bold, "Wrong type entered, only an integer is accepted. Using default value of 1.", Style.reset)
    loops = 1
except Exception as e:
    traceback.print_exc()
    loops = 1

try:
    index = int(sys.argv[2]) if len(sys.argv) > 2 else None #default amount of loops is 1, else it is the first argument
except ValueError:
    print(Foreground.orange, Style.bold, "Wrong type entered, only an integer is accepted. Using default value of 1.", Style.reset)
    index = 1
except Exception as e:
    traceback.print_exc()
    index = 1

##################################
# COMPONENT INITIALIZATION
##################################

if index != None:
    component = Component(robot, switch, debug=True, index=index - 1)
else:
    component = Component(robot, switch, debug=True)
robot.ActivateAndHome()






##################################
# MAIN ACTIONS
##################################
try:
    print("Starting process..")
    # print(robot.GetJoints(), end="\r")
    for i in range(loops): #You know what to do >:] (try 500 at a time) doing 100 + 108+53
        print(f"\rStarting Loop {i+1}")
        ##########################################################################################
        # Start of all blocks of code that will execute [loop] times.
        ##########################################################################################
        component.pressButton()
        component.grabComp()
        # #component.preheat() #one day
        component.flux()
        component.solder()
        #component.flux()
        #component.solder()
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
        print(Style.bold, Foreground.orange, "Robot missing part.", Foreground.red, Style.underline, "CTRL+C to return", Foreground.orange, "or ENTER to lift", end="")
        input(f":{Style.reset}")
        robot.MoveLinRelWrf(0, 0, 100, 0, 0, 0)
    except KeyboardInterrupt:
        print(Style.bold, "Exited", Style.reset)
    except mecademicpy.robot_classes.InterruptException:
        robot.ResetError()
        robot.ResumeMotion()
        try: 
            robot.MoveLinRelWrf(0, 0, 10, 0, 0, 0)
        except Exception:
            pass
    switch.stop_alarm()
    print("exited, returning to normal position. ")
except mecademicpy.robot_classes.InterruptException as e:
        robot.ResetError()
        robot.ClearMotion()
        robot.ResumeMotion()
        print(Foreground.red, Style.bold, f"Robot Exception \"{e}\" happened, exiting.")
except Exception as e:
    print(Foreground.red, Style.bold, f"Unknown Exception \"{e}\" happened, exiting.")
    print(Style.reset, Foreground.red, "######## START TRACEBACK ########", Style.reset)
    traceback.print_exc()
    print(Foreground.red, "######## END TRACEBACK ########", Style.reset)
    robot.PauseMotion() #works btw
    robot.ClearMotion()
    try:
        print(Style.bold, Style.underline, Foreground.red, "CTRL+C for return", Foreground.orange, " or ENTER to lift")
        input(f":{Style.reset}")
        robot.MoveLinRelWrf(0, 0, 100, 0, 0, 0)
    except KeyboardInterrupt:
        print(Style.bold, "Exited", Style.reset)
    except Exception:
        print(Foreground.pink, "danny was dumb. EXITING NOW", Style.reset)
else: 
    print(Foreground.green, "Successfully Exited.", Style.reset)

####################################
# PROGRAM END
####################################
print(Style.bold, "Program finished.")
try:
    robot.ResumeMotion()
    #################################################
    # ROBOT RESET
    #################################################
    robot.MoveJoints(90,0,0,0,0,0)
    robot.SetValveState(0, 0)
    robot.SetValveState(0)
except Exception:
    traceback.print_exc()
    print(Foreground.red, "robot interrupted during deactivation.") 
# robot.DeactivateRobot()

#should ALWAYS execute on exit
robot.Disconnect()
switch.cleanup()
