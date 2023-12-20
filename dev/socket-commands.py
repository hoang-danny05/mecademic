#test socket packet from Mecademic

import sys
import socket
import time 

try: 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create socket")
    sys.exit()
else:
    print("Socket Created")
    ROBOT_IP = "192.168.0.100"
    ROBOT_PORT = 10000
    client.connect((ROBOT_IP, ROBOT_PORT))
    print(f"Socket connected to {ROBOT_IP}")
    msg = client.recv(1024).decode("ascii")
    print(msg) #should print out success message

def sendCommand(cmd):
    try:
        client.send(bytes(f"{cmd}\0", 'ascii'))
        time.sleep(1)
        msg = client.recv(1024).decode('ascii')
        print(msg)
        return msg
    except socket.error:
        print("Failed to send data")
        return None

sendCommand("ActivateRobot")
sendCommand("Home")
sendCommand("MoveJoints(90,0,0,0,0,0)")
time.sleep(1)
sendCommand("DeactivateRobot")
client.close()
sys.exit()
