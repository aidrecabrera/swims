import os
from venv import logger
import serial
import proto.sensor_data_pb2 as sensor_data_pb2
from tkinter import Tk, StringVar, Label, Frame, messagebox
from tkinter.font import Font
from log.logger import SensorDataLogger
import time
from monitor.monitor import SensorDataMonitor

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
monitor = SensorDataMonitor()

# tkinter window
root = Tk()
root.title("Sensor Data")

# fullscreen mode
root.attributes("-fullscreen", True)

# frame to hold the labels
frame = Frame(root, bg="white")
frame.pack(expand=True, fill="both")

label_font = Font(family="Arial", size=24, weight="bold")

# StringVar for each sensor data
temp_var = StringVar()
pH_var = StringVar()
dOxygen_var = StringVar()
salinity_var = StringVar()

# labels for each sensor data
Label(frame, textvariable=temp_var, font=label_font, bg="white").pack(pady=20)
Label(frame, textvariable=pH_var, font=label_font, bg="white").pack(pady=20)
Label(frame, textvariable=dOxygen_var, font=label_font, bg="white").pack(pady=20)
Label(frame, textvariable=salinity_var, font=label_font, bg="white").pack(pady=20)

last_logged_time = time.time()

def update_data():
    global last_logged_time
    # read the incoming data
    incoming_data = ser.read(ser.inWaiting())
    # logger instance
    logger = SensorDataLogger('sqlite:///swims_log.db')
    
    if incoming_data:
        # decode the sensor data
        sensor_data = sensor_data_pb2.SensorData()
        sensor_data.ParseFromString(incoming_data)

        data.temperature = round(sensor_data.temperature, 2)
        data.pH = round(sensor_data.pH, 2)
        data.dOxygen = round(sensor_data.dOxygen, 2)
        data.salinity = round(sensor_data.salinity, 2)
        
        # monitor data
        statusPh: bool = monitor.check_parameter_level("ph", data.pH)
        statusSalinity: bool = monitor.check_parameter_level("salinity", data.salinity)
        statusDoxygen: bool = monitor.check_parameter_level("dissolved_oxygen", data.dOxygen)
        statusTemperature: bool = monitor.check_parameter_level("temperature", data.temperature)
        
        current_time = time.time()
        if current_time - last_logged_time >= 1:  # Only log if a second has passed
            # log data
            logger.execute_query(logger.log(data.temperature, data.pH, data.dOxygen, data.salinity))
            last_logged_time = current_time

            # Get all logs
            logs = logger.execute_query(logger.get_logs())
            for log in logs:
                print(log)

        # update StringVar with new data
        temp_var.set(f'Temperature: {data.temperature}°C')
        pH_var.set(f'pH: {data.pH}')
        dOxygen_status = "N/A"
        if data.dOxygen >= 0:
            if data.dOxygen < 2:
                dOxygen_status = "Critically Low"
            elif data.dOxygen < 4:
                dOxygen_status = "Low"
            elif data.dOxygen < 7:
                dOxygen_status = "Moderate"
            elif data.dOxygen < 11:
                dOxygen_status = "High"
            else:
                dOxygen_status = "Very High"
        dOxygen_var.set(f'Dissolved Oxygen: {data.dOxygen} mg/L ({dOxygen_status})')
        salinity_var.set(f'Salinity: {data.salinity} ppt')

    root.after(1000, update_data)

# update data
update_data()
# tkinter event loopa
root.mainloop()