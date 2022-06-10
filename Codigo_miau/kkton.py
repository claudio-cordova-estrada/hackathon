import serial 
import cx_Oracle
# import config as cfg
from datetime import datetime
from geopy import Nominatim

geo = Nominatim(user_agent="Myapp")
localidad = geo.geocode("Concepcion, Chile")
loc = localidad.latitude, localidad.longitude
hora = datetime.now()
print(hora)
print(loc)
# usar loc para las cordenadas, hora para la fecha y hora(SON LOS PARAMETROS DEL INSERT)
arduino = serial.Serial("COM4", 9600)

"""def insert_sos(p_cod, p_ubicacion, p_rut, p_fecha):
    sql = ('insert into SOS(p_cod, p_ubicacion, p_rut, p_fecha)'
            'values(:cod, :ubicacion, :rut, :fecha)')"""
    
    

"""while True:
    switch = arduino.readline().decode("ascii")
    if switch == "1":
        print("XD")"""