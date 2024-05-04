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

    def get_continuous_sensor_data(self, serial_port='/dev/ttyUSB0', baud_rate=9600):
        """
        Continuously retrieves sensor data from the serial port and yields the latest SensorData object.

        Args:
            serial_port (str): The serial port to read data from. Default is '/dev/ttyUSB0'.
            baud_rate (int): The baud rate for the serial communication. Default is 9600.

        Yields:
            SensorData: An instance of the SensorData class containing the latest sensor data.
        """
        with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
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

    def get_latest_sensor_data(self, serial_port='/dev/ttyUSB0', baud_rate=9600):
        """
        Retrieves the latest sensor data from the serial port and returns a dictionary.

        Args:
            serial_port (str): The serial port to read data from. Default is '/dev/ttyUSB0'.
            baud_rate (int): The baud rate for the serial communication. Default is 9600.

        Returns:
            dict: A dictionary containing the latest sensor data with keys 'pH', 'salinity', 'temperature', and 'dOxygen'.
        """
        with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
            incoming_data = ser.read(ser.inWaiting())
            sensor_data = sensor_data_pb2.SensorData()
            sensor_data.ParseFromString(incoming_data)

            self.temperature = round(sensor_data.temperature, 2)
            self.pH = round(sensor_data.pH, 2)
            self.dOxygen = round(sensor_data.dOxygen, 2)
            self.salinity = round(sensor_data.salinity, 2)



            return {
                'pH': self.pH,
                'salinity': self.salinity,
                'temperature': self.temperature,
                'dOxygen': self.dOxygen
            }