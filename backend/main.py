from tkinter import Tk
from interface.gui import GUI
import random

def main():
    window = Tk()
    window.geometry("800x480")
    window.attributes('-fullscreen')
    window.configure(bg="#FFFFFF")

    def toggle_fullscreen(event=None):
        window.attributes('-fullscreen', not window.attributes('-fullscreen'))

    window.bind('<F11>', toggle_fullscreen)
    window.bind('<Escape>', toggle_fullscreen)

    gui = GUI(window)

    def update_data():
        # TODO: reaplce with real-time data source from sensor
        data = {
            "pH": {"value": f"{random.uniform(6.5, 8.5):.1f} (Normal)", "normal_range": "6.5 - 8.5"},
            "Salinity": {"value": f"{random.uniform(6.5, 8.5):.1f} ppt", "normal_range": "6.5 - 8.5"},
            "Temperature": {"value": f"{random.uniform(6.5, 8.5):.1f}°C", "normal_range": "6.5 - 8.5"},
            "Dissolved Oxygen": {"value": f"{random.uniform(6.5, 8.5):.1f} mg/L", "normal_range": "6.5 - 8.5"},
            "SIM Signal": random.choice(["Strong", "Weak"]),
            "Sensors": random.choice(["Running", "Not Running"]),
            "Internet Access": random.choice(["Connected", "Disconnected"])
        }
        gui.update_sensor_data(data)
        window.after(300, update_data)

    update_data()  # data update loop

    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    main()