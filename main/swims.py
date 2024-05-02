import os
import serial
import sensor_data_pb2

def clear_screen():
    # Windows   
    if os.name == 'nt':
        os.system('cls')
    # Linux and macOS
    else:
        os.system('clear')

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)

while True:
    # read the incoming data
    data = ser.read(ser.inWaiting())
    if data:
        # decode the sensor data
        sensor_data = sensor_data_pb2.SensorData()
        sensor_data.ParseFromString(data)

        clear_screen()

        print(f"Temperature: {round(sensor_data.temperature, 1)} °C")
        print(f"pH: {round(sensor_data.pH, 1)}")
        print(f"Dissolved Oxygen: {sensor_data.dOxygen} mg/L")
        print(f"Salinity: {sensor_data.salinity} ppt")
        print()
