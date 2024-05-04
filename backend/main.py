import random
import threading
import time
from tkinter import Tk
from interface.gui import GUI
from data.realtime_data import SensorData
from log.logger import SensorDataLogger
import subprocess

def check_internet_connection():
   try:
      subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
      return True
   except subprocess.CalledProcessError:
      return False

def log_sensor_data(data, logger):
    query = logger.log(data.temperature, data.pH, data.dOxygen, data.salinity)
    logger.execute_query(query)

def update_sensor_data(gui, sensor_data, logger):
    while True:
        data = next(sensor_data.get_continuous_sensor_data())
        gui.update_sensor_data(
            temperature=data.temperature,
            pH=data.pH,
            dOxygen=data.dOxygen,
            salinity=data.salinity,
            sim_signal=random.choice(["Strong", "Strong"]),
            sensors="Running" if sensor_data.check_sensors() else "Stopped",
            internet="Connected" if check_internet_connection() else "Disconnected"
        )
        
        # update graph
        gui.update_graph(data.temperature, data.pH, data.dOxygen, data.salinity)

        # call the log_sensor_data function
        log_sensor_data(data, logger)

def main():
    window = Tk()
    window.geometry("800x480")
    window.attributes('-fullscreen', True)
    window.configure(bg="#FFFFFF")

    def toggle_fullscreen(event=None):
        window.attributes('-fullscreen', not window.attributes('-fullscreen'))

    window.bind('<F11>', toggle_fullscreen)
    window.bind('<Escape>', toggle_fullscreen)

    sensor_data = SensorData()

    # initialize with latest sensor data
    latest_data = sensor_data.get_latest_sensor_data()
    gui = GUI(window, latest_data['temperature'], latest_data['pH'], latest_data['dOxygen'], latest_data['salinity'])

    # create a logger instance
    db_url = "sqlite:///swims_log.db"
    logger = SensorDataLogger(db_url)

    # start a separate thread to update sensor data and log it
    threading.Thread(target=update_sensor_data, args=(gui, sensor_data, logger), daemon=True).start()

    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    main()