# import serial
# from bcolours import BC

# ser = serial.Serial('/dev/serial/by-id/usb-Thorlabs_Stepper_Controller_26001411-if00-port0', 115200)
# des = 0x50  # generic USB
# source = 0x01  # host
# cmdHome = bytearray([ 0x43, 0x04, 0, 0, des, source ])
# print(BC.HEADER + "Sending command 'MGMSG_MOT_MOVE_HOME' to controller. " + BC.ENDC)
# ser.write(cmdHome)
# res = ser.read(6)

# ser.close()

import jig

jig.init()
jig.home()
jig.closePort()