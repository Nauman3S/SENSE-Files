#Plug to Raspberry PI with USB cable and check the connection between Arduino and Raspberry pi by
#type "ls /dev/tty*"
#in Raspberry Pi terminal, the result should be content
#"/dev/ttyACM0" and you are good to go.

import serial
def get_num(x):
    return float(''.join(ele for ele in x if ele.isdigit() or ele == '.'))

ser = serial.Serial('/dev/ttyACM0',9600)
data=[]
while True:
	read_serial=ser.readline()
	data=read_serial.split(',')
	
	#logic for float conversion
	print(data)
