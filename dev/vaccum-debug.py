import sys
sys.path.append("../")
from Components.VacuumSwitch import VacuumSwitch
import mecademicpy.robot as MecademicRobot
from time import sleep
import traceback
robot = MecademicRobot.Robot()
try:
    robot.Connect(address="192.168.0.100", enable_synchronous_mode=True, disconnect_on_exception=False)
    robot.ActivateAndHome()
    robot.SetValveState(1)
    robot.MoveJoints(90, 0, 0, 0, 0, 0)
except Exception:
    print("oh noes")

try:
    print("connected to robit, doing other stuff")
    sensor = VacuumSwitch()

    print("entering loop")
    while True:
        sleep(.5)
        print("ON" if (sensor.read_state()) else "OFF")
except Exception:
    print("error happened")
    traceback.print_exc()
except KeyboardInterrupt:
    print("exited")

robot.SetValveState(0)
sensor.cleanup()
# robot.SetValveState(0,0)
# robot.Disconnect()
