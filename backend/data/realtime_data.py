import os
import sys
import serial

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from proto import sensor_data_pb2

class SensorData:
    def __init__(self):
        self.temperature = 0
        self.pH = 0
        self.dOxygen = 0
        self.salinity = 0

    def get_sensor_data(self, serial_port='/dev/ttyUSB0', baud_rate=9600):
        """
        Retrieves sensor data from the serial port and yields a SensorData object.

        Args:
            serial_port (str): The serial port to read data from. Default is '/dev/ttyUSB0'.
            baud_rate (int): The baud rate for the serial communication. Default is 9600.

        Yields:
            SensorData: An instance of the SensorData class containing the sensor data.
            
            Example:
                def test_get_sensor_data():
                sensor_data = SensorData()
                for data in sensor_data.get_sensor_data():
                    print(data.__dict__)
            
            {'temperature': 25.67, 'pH': 7.2, 'dOxygen': 8.1, 'salinity': 35.0}
            {'temperature': 26.1, 'pH': 7.15, 'dOxygen': 8.0, 'salinity': 35.2}
            {'temperature': 25.9, 'pH': 7.25, 'dOxygen': 8.2, 'salinity': 34.9}
            ...
        """
        with serial.Serial(serial_port, baud_rate, timeout=2) as ser:
            while True:
                incoming_data = ser.read(ser.inWaiting())

                if incoming_data:
                    sensor_data = sensor_data_pb2.SensorData()
                    sensor_data.ParseFromString(incoming_data)

                    self.temperature = round(sensor_data.temperature, 2)
                    self.pH = round(sensor_data.pH, 2)
                    self.dOxygen = round(sensor_data.dOxygen, 2)
                    self.salinity = round(sensor_data.salinity, 2)

                    yield self