import os
import threading
import subprocess
import time
from tkinter import Tk, Canvas, Button, PhotoImage
from dotenv import load_dotenv
from supabase import Client, create_client
from interface.gui import GUI
from data.realtime_data import SensorData
from log.logger import SensorDataLogger

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
DB_URL = "sqlite:///swims_log.db"
DURATION = 30  # Duration in seconds for sensor graph

def check_internet_connection():
    """Check if there is an internet connection."""
    try:
        subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
        return True
    except subprocess.CalledProcessError:
        return False

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
        query = logger.log(data.temperature, data.pH, data.dOxygen, data.salinity)
        query_anomaly = logger.log_anomaly(data.temperature, data.pH, data.dOxygen, data.salinity)
        logger.execute_query(query_anomaly)
        logger.execute_query(query)
        threading.Thread(target=logger.sync_to_supabase).start()
    except Exception as e:
        print(f"Error logging sensor data: {e}")

def main():
    """Main function."""
    window = Tk()
    window.geometry("800x480")
    window.configure(bg="#FFFFFF")
    window.attributes('-fullscreen', True)

    def toggle_fullscreen(_=None):
        """Toggle fullscreen mode."""
        window.attributes('-fullscreen', not window.attributes('-fullscreen'))

    window.bind('<F11>', toggle_fullscreen)
    window.bind('<Escape>', toggle_fullscreen)

    sensor_data = SensorData()
    latest_data = sensor_data.get_latest_sensor_data()
    gui = GUI(window, latest_data['temperature'], latest_data['pH'], latest_data['dOxygen'], latest_data['salinity'])

    logger = SensorDataLogger(DB_URL)

    threading.Thread(target=update_sensor_data, args=(gui, sensor_data, logger), daemon=True).start()

    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    main()