import serial
import cx_Oracle
# import config as cfg
from datetime import datetime
import geocoder as geo


geoIp = geo.ip("me")
geoIp = geoIp.latlng
tiempo = datetime.now()
print(f"Ubicación:\t{geoIp}\nHora:\t{tiempo}")
    
# usar loc para las cordenadas, hora para la fecha y hora(SON LOS PARAMETROS DEL INSERT)
arduino = serial.Serial("COM4", 9600)

while True:
    switch = arduino.readline().decode("ascii")
    if switch == "1":
        print("XD")

