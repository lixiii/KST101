# Library to control the stretching jig
# The module needs to be initialised with an init function
import serial
from bcolours import BC
ser = serial.Serial()

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
    # the following variables are obtained from the communication protocol and applies to the KST101
    des = 0x50  # generic USB
    source = 0x01  # host
    cmdIdentify = bytearray([ 0x23, 0x02, 0, 0, des, source ])
    print(BC.OKGREEN + "Sending command 'MGMSG_MOD_IDENTIFY' to controller. " + BC.ENDC)
    ser.write(cmdIdentify)



def closePort():
    ser.close()