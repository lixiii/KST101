import serial
ser = serial.Serial('/dev/serial/by-id/usb-Thorlabs_Stepper_Controller_26001411-if00-port0', 115200)
des = 0x50  # generic USB
source = 0x01  # host
cmdIdentify = bytearray([ 0x23, 0x02, 0, 0, des, source ])
ser.write(cmdIdentify)
ser.close()