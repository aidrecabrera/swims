import os
import threading
import time
from data.realtime_data import SensorData

def print_sensor_data(sensor_data):
    """Print sensor data."""
    while True:
        try:
            data = next(sensor_data.get_continuous_sensor_data())
            print(f"Temperature: {data.temperature}")
            print(f"pH: {data.pH}")
            print(f"Dissolved Oxygen: {data.dOxygen}")
            print(f"Salinity: {data.salinity}")
            print()
        except Exception as e:
            print(f"Error printing sensor data: {e}")

def main():
    while True:
        try:
            sensor_data = SensorData()
            threading.Thread(target=print_sensor_data, args=(sensor_data,), daemon=True).start()
            while True:
                time.sleep(1)  # Keep the main thread alive
        except Exception as e:
            print(f"Waiting for sensor data to become available: {e}")
            time.sleep(0.2)

if __name__ == "__main__":
    main()