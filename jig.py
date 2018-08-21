# Library to control the stretching jig
# The module needs to be initialised with an init function
import serial
from bcolours import BC
ser = serial.Serial()

# the following variables are obtained from the communication protocol and applies to the KST101
des = 0x50  # generic USB
source = 0x01  # host


# Initialisation
################
# WARNING
# The serial port is opened by this function. If the port is successfully opened, ensure that the port is closed before termination. 

def init( port = '/dev/serial/by-id/usb-Thorlabs_Stepper_Controller_26001411-if00-port0'):
    ser.baudrate = 115200
    ser.port = port
    ser.open()
    if ser.is_open:
        print(BC.WARNING + "Serial port is open. Please ensure that port is closed before terminating the program." + BC.ENDC)


# Identify the controller by asking it to flash its screen
def identify():
    cmdIdentify = bytearray([ 0x23, 0x02, 0, 0, des, source ])
    print(BC.OKGREEN + "Sending command 'MGMSG_MOD_IDENTIFY' to controller. " + BC.ENDC)
    ser.write(cmdIdentify)


# Move to home
def home():
    cmdHome = bytearray([ 0x43, 0x04, 0, 0, des, source ])
    print(BC.HEADER + "Sending command 'MGMSG_MOT_MOVE_HOME' to controller. Waiting for completion response" + BC.ENDC)
    ser.write(cmdHome)
    resp = ser.read(6) # message consists of 6 bytes
    if resp[0] == 0x44 and resp[1] == 0x04:
        print(BC.OKGREEN + "Homing completed successfully." + BC.ENDC)
    else:
        print(BC.FAIL + "Command failed. Controller responds with error. Response received:" + resp.hex() + BC.ENDC)
        raise Exception("Controller Error")


def closePort():
    ser.close()