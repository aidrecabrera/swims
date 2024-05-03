import os
import time
import tkinter as tk
from tkinter import ttk
from typing import NamedTuple
import serial
import proto.sensor_data_pb2 as sensor_data_pb2
from log.logger import SensorDataLogger
from monitor.monitor import SensorDataMonitor

class SensorData(NamedTuple):
    temperature: float
    pH: float
    dissolved_oxygen: float
    salinity: float

def clear_screen():
    os.system('clear')

class SerialCommunicator:
    """
    Handling serial communication.
    """
    def __init__(self, port: str, baud_rate: int, timeout: float):
        """
        Initialize the SerialCommunicator instance.

        :param port: Serial port to connect to
        :param baud_rate: Baud rate for serial communication
        :param timeout: Timeout for serial communication
        """
        self.serial = serial.Serial(port, baud_rate, timeout=timeout)

    def read_sensor_data(self) -> SensorData:
        """
        Read sensor data from the serial port.

        :return: SensorData instance containing the sensor data
        """
        incoming_data = self.serial.read(self.serial.inWaiting()) # type: ignore
        if incoming_data:
            sensor_data = sensor_data_pb2.SensorData() # type: ignore
            sensor_data.ParseFromString(incoming_data)
            return SensorData(
                temperature=round(sensor_data.temperature, 2),
                pH=round(sensor_data.pH, 2),
                dissolved_oxygen=round(sensor_data.dOxygen, 2),
                salinity=round(sensor_data.salinity, 2)
            )
        return SensorData(0.0, 0.0, 0.0, 0.0)

class SensorDataGUI(tk.Tk):
    """
    GUI for displaying sensor data.
    """
    def __init__(self, serial_communicator: SerialCommunicator):
        """
        Initialize the SensorDataGUI instance.

        :param serial_communicator: SerialCommunicator instance for reading sensor data
        """
        super().__init__()
        self.title("Sensor Data")
        self.attributes("-fullscreen", True)
        self.configure(bg="white")

        self.serial_communicator = serial_communicator
        self.monitor = SensorDataMonitor()
        self.logger = SensorDataLogger('sqlite:///swims_log.db')
        self.last_logged_time = time.time()

        self.data_frame = ttk.Frame(self)
        self.data_frame.pack(pady=20)

        self.temp_label = ttk.Label(self.data_frame, font=("Arial", 24, "bold"), background="white")
        self.temp_label.pack(pady=10)

        self.pH_label = ttk.Label(self.data_frame, font=("Arial", 24, "bold"), background="white")
        self.pH_label.pack(pady=10)

        self.dOxygen_label = ttk.Label(self.data_frame, font=("Arial", 24, "bold"), background="white")
        self.dOxygen_label.pack(pady=10)

        self.salinity_label = ttk.Label(self.data_frame, font=("Arial", 24, "bold"), background="white")
        self.salinity_label.pack(pady=10)

        self.update_data()

    def update_data(self):
        """
        Update the sensor data labels and log the data.
        """
        sensor_data = self.serial_communicator.read_sensor_data()

        current_time = time.time()
        if current_time - self.last_logged_time >= 1:
            self.logger.execute_query(self.logger.log(sensor_data.temperature, sensor_data.pH,
                                                      sensor_data.dissolved_oxygen, sensor_data.salinity))
            self.last_logged_time = current_time

        self.temp_label.config(text=f"Temperature: {sensor_data.temperature}°C")
        self.pH_label.config(text=f"pH: {sensor_data.pH}")

        dOxygen_status = "N/A"
        if sensor_data.dissolved_oxygen >= 0:
            if sensor_data.dissolved_oxygen < 2:
                dOxygen_status = "Critically Low"
            elif sensor_data.dissolved_oxygen < 4:
                dOxygen_status = "Low"
            elif sensor_data.dissolved_oxygen < 7:
                dOxygen_status = "Moderate"
            elif sensor_data.dissolved_oxygen < 11:
                dOxygen_status = "High"
            else:
                dOxygen_status = "Very High"
        self.dOxygen_label.config(text=f"Dissolved Oxygen: {sensor_data.dissolved_oxygen} mg/L ({dOxygen_status})")
        self.salinity_label.config(text=f"Salinity: {sensor_data.salinity} ppt")

        self.after(1000, self.update_data)

if __name__ == "__main__":
    serial_communicator = SerialCommunicator('/dev/ttyUSB0', 9600, timeout=2)
    app = SensorDataGUI(serial_communicator)
    app.mainloop()