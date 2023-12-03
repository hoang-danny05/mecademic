from RPi import GPIO

#############################
# INTEDNDED TO READ THE PSK100 VACUUM SWITCH
# CONNECTIONS:
# GPIO 4 (PIN 7) <-> OPTOCOUPLER COLLECTOR
# GND <-> OPTOCOUPLER EMITTER
# GPIO 17 (PIN 11) <-> Speaker +
# GND (14) <-> Speaker -
############################

class VacuumSwitch:
    def __init__(self):
        self.setup()
        GPIO.output(11, False)

    def setup(self):
        #pin is the BOARD number of the pi
        try:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(11, GPIO.OUT)
        except Exception:
            print("error setting up the connection")

    def read_state(self): #TRUE for if there's a part ON, FALSE for if there's NO PART
        self.setup()
        return (not GPIO.input(7))
    
    def assert_on(self): #TRUE if there should be a part ON
        if not (self.read_state()):
            raise AssertionError("The robot's part state was not expected")

    def assert_off(self): #TRUE if there should be a part ON
        if (self.read_state()):
            raise AssertionError("The robot's part state was not expected")

    def assert_state(self, partOn: bool): #TRUE if there should be a part ON
        if not (self.read_state() == partOn):
            raise AssertionError("The robot's part state was not expected")
    
    def start_alarm(self):
        self.setup()
        GPIO.output(11, True)

    def stop_alarm(self):
        self.setup()
        GPIO.output(11, False)

    def cleanup(self):
        GPIO.cleanup()
