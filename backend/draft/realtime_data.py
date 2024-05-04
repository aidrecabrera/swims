import os
import sys
import serial
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from proto import sensor_data_pb2

def clear_screen():
    os.system('clear')

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)

class SensorData:
    def __init__(self, temperature, pH, dOxygen, salinity):
        self.temperature = temperature
        self.pH = pH
        self.dOxygen = dOxygen
        self.salinity = salinity

data = SensorData(0, 0, 0, 0)

def get_sensor_data():
    # read the incoming data
    incoming_data = ser.read(ser.inWaiting())

    if incoming_data:
        # decode the sensor data
        sensor_data = sensor_data_pb2.SensorData()
        sensor_data.ParseFromString(incoming_data)

        data.temperature = round(sensor_data.temperature, 2)
        data.pH = round(sensor_data.pH, 2)
        data.dOxygen = round(sensor_data.dOxygen, 2)
        data.salinity = round(sensor_data.salinity, 2)
    
    return data