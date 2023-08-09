from RPi import GPIO

class VacuumSwitch:
    def __init__(self):
        #pin is the BOARD number of the pi
        try:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        except Exception:
           print("error setting up the connection")
           
    def read_state(self):
        return GPIO.input(7)
    
    def cleanup():
        GPIO.cleanup()