import os
import threading
import time
import tkinter as tk
from dotenv import load_dotenv
from supabase import Client, create_client
from interface.gui import GUI
from data.realtime_data import SensorData
from log.logger import SensorDataLogger

load_dotenv()

SUPABASE_URL = "https://kpypbiqtjzcctqrcrnwt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtweXBiaXF0anpjY3RxcmNybnd0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTQ4MjQ5NDcsImV4cCI6MjAzMDQwMDk0N30.NqOmREZ7PNWhXOAOarrcvGOyzC7Xhch_ThwOOt4z1rA"
DB_URL = "sqlite:////home/swims/swims/backend/swims_log.db"
DURATION = 30  # Duration in seconds for sensor graph

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg="#FFFFFF")
        self.overrideredirect(True)
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.resizable(False, False)

        self.after(1000, self.hide_cursor)  # Hide cursor after 1 second of inactivity
        self.bind('<Motion>', self.show_cursor)  # Show cursor on mouse movement

    def hide_cursor(self):
        self.config(cursor='none')

    def show_cursor(self, event):
        self.config(cursor='')
        self.after(1000, self.hide_cursor)  # Reset the timer on mouse movement

def update_sensor_data(gui, sensor_data, logger):
    """Update sensor data and log it."""
    while True:
        try:
            data = next(sensor_data.get_continuous_sensor_data())
            gui.update_gui(
                temperature=data.temperature,
                pH=data.pH,
                dOxygen=data.dOxygen,
                salinity=data.salinity
            )
            log_sensor_data(data, logger)
        except Exception as e:
            print(f"Error updating sensor data: {e}")

def log_sensor_data(data, logger):
    """Log sensor data."""
    try:
        queries = []
        query = logger.log(data.temperature, data.pH, data.dOxygen, data.salinity)
        query_anomaly = logger.log_anomaly(data.temperature, data.pH, data.dOxygen, data.salinity)
        if query_anomaly is not None:
            queries.append(query_anomaly)
        queries.append(query)
        logger.execute_queries(queries)
        threading.Thread(target=logger.sync_to_supabase).start()
    except Exception as e:
        print(f"Error logging sensor data: {e}")

def main():
    while True:
        try:
            """Main function."""
            window = App()

            sensor_data = SensorData()
            latest_data = sensor_data.get_latest_sensor_data()
            gui = GUI(window, latest_data['temperature'], latest_data['pH'], latest_data['dOxygen'], latest_data['salinity'])

            logger = SensorDataLogger(DB_URL)

            threading.Thread(target=update_sensor_data, args=(gui, sensor_data, logger), daemon=True).start()

            window.mainloop()
        except Exception as e:
            print(f"Waiting for GUI to become available: {e}")
            time.sleep(0.2)

if __name__ == "__main__":
    main()