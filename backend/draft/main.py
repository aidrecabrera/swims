import os
import serial
import main.backend.proto.sensor_data_pb2 as sensor_data_pb2
from tkinter import Tk, StringVar, Label, Frame, Button
from tkinter.font import Font
from log.logger import SensorDataLogger
import time
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

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

# Create a custom font for labels
label_font = Font(family="Arial", size=14, weight="bold")

# Create StringVar for each sensor data
temp_var = StringVar()
pH_var = StringVar()
dOxygen_var = StringVar()
salinity_var = StringVar()

# Create a frame to hold the labels and graph
main_frame = Frame(root, bg="black")
main_frame.pack(expand=True, fill="both")

# Create a frame to hold the labels
label_frame = Frame(main_frame, bg="black")
label_frame.pack(side="top", pady=10)

# Create labels for each sensor data
temp_label = Label(label_frame, textvariable=temp_var, font=label_font, fg="white", bg="black")
temp_label.pack(side="left", padx=10)

pH_label = Label(label_frame, textvariable=pH_var, font=label_font, fg="white", bg="black")
pH_label.pack(side="left", padx=10)

dOxygen_label = Label(label_frame, textvariable=dOxygen_var, font=label_font, fg="white", bg="black")
dOxygen_label.pack(side="left", padx=10)

salinity_label = Label(label_frame, textvariable=salinity_var, font=label_font, fg="white", bg="black")
salinity_label.pack(side="left", padx=10)

# Create a frame to hold the graph
graph_frame = Frame(main_frame, bg="black")
graph_frame.pack(expand=True, fill="both", pady=10)

# Create a figure and axis for the graph
fig, ax = plt.subplots(figsize=(4, 2))
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack()

# Lists to store sensor data for plotting
temperature_data = []
pH_data = []
dOxygen_data = []
salinity_data = []
timestamps = []

# Variable to track the display mode (real-time or historical)
display_mode = "real-time"

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

            # Append data to lists for plotting
            temperature_data.append(data.temperature)
            pH_data.append(data.pH)
            dOxygen_data.append(data.dOxygen)
            salinity_data.append(data.salinity)
            timestamps.append(time.time())

            # Update the graph based on the display mode
            update_graph()

        # Update the StringVar with the new data
        temp_var.set(f'Temp: {data.temperature}°C')
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
        dOxygen_var.set(f'DO: {data.dOxygen} ({dOxygen_status})')
        salinity_var.set(f'Salinity: {data.salinity} ppt')

    # Update the data every 1000ms
    root.after(1000, update_data)

def update_graph():
    ax.clear()
    if display_mode == "real-time":
        ax.plot(timestamps[-100:], temperature_data[-100:], label='Temperature')
        ax.plot(timestamps[-100:], pH_data[-100:], label='pH')
        ax.plot(timestamps[-100:], dOxygen_data[-100:], label='Dissolved Oxygen')
        ax.plot(timestamps[-100:], salinity_data[-100:], label='Salinity')
    else:
        ax.plot(timestamps, temperature_data, label='Temperature')
        ax.plot(timestamps, pH_data, label='pH')
        ax.plot(timestamps, dOxygen_data, label='Dissolved Oxygen')
        ax.plot(timestamps, salinity_data, label='Salinity')
    ax.legend(fontsize=8)
    ax.set_xlabel('Time', fontsize=8)
    ax.set_ylabel('Value', fontsize=8)
    ax.tick_params(axis='both', which='major', labelsize=8)
    canvas.draw()

def toggle_display_mode():
    global display_mode
    if display_mode == "real-time":
        display_mode = "historical"
    else:
        display_mode = "real-time"
    update_graph()

# Create a button to toggle the display mode
toggle_button = Button(root, text="Toggle Display Mode", command=toggle_display_mode, font=label_font, bg="black", fg="white")
toggle_button.pack(side="bottom", pady=5)

# Start updating data
update_data()

# Start the Tkinter event loop
root.mainloop()