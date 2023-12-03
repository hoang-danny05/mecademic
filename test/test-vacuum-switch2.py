from Components.VacuumSwitch import VacuumSwitch
import mecademicpy.robot as MecademicRobot
from time import sleep
import traceback
# robot = MecademicRobot.Robot()
# try:
#   robot.Connect(address="192.168.0.100", enable_synchronous_mode=True, disconnect_on_exception=False)
#   robot.ActivateAndHome()
 # except Exception:
 #   print("oh noes")
try:
    print("connected to robit, doing other stuff")
    sensor = VacuumSwitch()

    print("entering loop")
    while True:
        action = input("Type r to read and 1/0 to assert. \n>")
        sleep(.5)
        print("ON" if (sensor.read_state()) else "OFF")
except Exception:
    print("error happened")
    traceback.print_exc()
except KeyboardInterrupt:
    print("exited")

# robot.SetValveState(0,0)
# robot.Disconnect()
