import random
import threading
import time
from tkinter import Tk
from interface.gui import GUI
from data.realtime_data import SensorData

def update_sensor_data(gui, sensor_data):
    while True:
        data = next(sensor_data.get_continuous_sensor_data())
        gui.update_sensor_data(
            temperature=data.temperature,
            pH=data.pH,
            dOxygen=data.dOxygen,
            salinity=data.salinity,
            sim_signal=random.choice(["Strong", "Weak"]),
            sensors=random.choice(["Running", "Stopped"]),
            internet=random.choice(["Connected", "Disconnected"])
        )

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

    # start a separate thread to update sensor data
    threading.Thread(target=update_sensor_data, args=(gui, sensor_data), daemon=True).start()

    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    main()