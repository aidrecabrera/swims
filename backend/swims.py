import os
from venv import logger
import serial
import proto.sensor_data_pb2 as sensor_data_pb2
from tkinter import Tk, StringVar, Label, Frame
from tkinter.font import Font
from log.logger import SensorDataLogger
import time

def clear_screen():
    # Windows   
    if os.name == 'nt':
        os.system('cls')
    # Linux and macOS
    else:
        os.system('clear')

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)

class SensorData:
    def __init__(self, temperature, pH, dOxygen, salinity):
        self.temperature = temperature
        self.pH = pH
        self.dOxygen = dOxygen
        self.salinity = salinity

data = SensorData(0, 0, 0, 0)

# Create a Tkinter window
root = Tk()
root.title("Sensor Data")

# Set the window to fullscreen mode
root.attributes("-fullscreen", True)

# Create a frame to hold the labels
frame = Frame(root, bg="white")
frame.pack(expand=True, fill="both")

# Create a custom font for labels
label_font = Font(family="Arial", size=24, weight="bold")

# Create StringVar for each sensor data
temp_var = StringVar()
pH_var = StringVar()
dOxygen_var = StringVar()
salinity_var = StringVar()

# Create labels for each sensor data
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
        
        current_time = time.time()
        if current_time - last_logged_time >= 1:  # Only log if a second has passed
            # log data
            logger.execute_query(logger.log(data.temperature, data.pH, data.dOxygen, data.salinity))
            last_logged_time = current_time

            # Get all logs
            logs = logger.execute_query(logger.get_logs())
            for log in logs:
                print(log)

        # Update the StringVar with the new data
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

    # Update the data every 1000ms
    root.after(1000, update_data)

# Start updating data
update_data()

# Start the Tkinter event loop
root.mainloop()