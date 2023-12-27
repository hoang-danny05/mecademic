import mecademicpy.robot as MecademicRobot
robot = MecademicRobot.Robot()
robot.Connect(address="192.168.0.100", enable_synchronous_mode=True, disconnect_on_exception=False)
robot.ResetError()
robot.ResumeMotion()
