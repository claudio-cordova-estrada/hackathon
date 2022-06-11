import serial.tools.list_ports

ports = serial.tools.list_ports
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: Com ==> ")

for x in range(0, len(portList)):
    if portList[x].startswith('COM: ' + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])
        
serialInst.bandrate = 9600
serialInst.port = portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.realine()
        print(packet.decode('utf'))
    