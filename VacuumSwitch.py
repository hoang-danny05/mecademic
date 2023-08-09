import serial

class VacuumSwitch:
    def __init__(self):
        #pin is the BOARD number of the pi
        try:
            self.ser = serial.Serial('/dev/ttyACM0', 9600)
        except:
            print("error setting up the connection")

    def read_state(self):
        self.ser.write(b'1')
        state = self.ser.read()
        print(f'state: {state.decode()}')
        if int(state.decode()) == 1:
            return True
        else:
            return False