from tkinter import Tk
from interface.gui import GUI

def main():
    window = Tk()
    gui = GUI(window)
    gui.render_application()
    
    # Example usage: Update dynamic data
    dynamic_data = {
        "pH": "7.8 (Normal)",
        "Salinity": "9.2 ppt",
        "Temperature": "25°C",
        "Dissolved Oxygen": "7.6 mg/L",
        "SIM Signal": "Weak",
        "Sensors": "Idle",
        "Internet Access": "Disconnected"
    }
    gui.update_dynamic_data(dynamic_data)

if __name__ == "__main__":
    main()