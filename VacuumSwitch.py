from RPi import GPIO

#############################
# INTEDNDED TO READ THE PSK100 VACUUM SWITCH
# CONNECTIONS:
# GPIO 4 (PIN 7) <-> OPTOCOUPLER COLLECTOR
# GND <-> OPTOCOUPLER EMITTER
############################

class VacuumSwitch:
    def __init__(self):
        #pin is the BOARD number of the pi
        try:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(11, GPIO.OUT)
        except Exception:
           print("error setting up the connection")

    def read_state(self): #TRUE for if there's a part ON, FALSE for if there's NO PART
        return (not GPIO.input(7))
    
    def assert_state(self, condition: bool): #TRUE if there should be a part ON
        if not (self.read_state() == condition):
            GPIO.output(11, True)
            input("ERROR: NO PART ON ROBOT, FIX NOW.")
            GPIO.output(11, False)
            raise AssertionError("The robot's part state was not expected")
    
    def cleanup():
        GPIO.cleanup()
        GPIO.output(11, False)