import time
import numpy as np
from tkinter import Tk, Canvas, Button, PhotoImage
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from monitor.monitor import THRESHOLDS
from .utils import relative_to_assets

class SensorGraph:
    def __init__(self, master, width=5, height=4, dpi=100, duration=60):
        self.master = master
        self.width = width
        self.height = height
        self.dpi = dpi
        self.duration = duration  # Duration in seconds

        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor='none', edgecolor='none')
        self.ax = self.fig.add_subplot(111, facecolor='none')
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Value")
        self.ax.set_title("Sensor Data")

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().place(x=25, y=150, width=497, height=215)

        self.lines = {}
        self.init_plot()

    def init_plot(self):
        self.lines["temperature"], = self.ax.plot([], [], label="Temperature")
        self.lines["pH"], = self.ax.plot([], [], label="pH")
        self.lines["dOxygen"], = self.ax.plot([], [], label="Dissolved Oxygen")
        self.lines["salinity"], = self.ax.plot([], [], label="Salinity")
        self.ax.legend(facecolor='none', edgecolor='none')

        self.data = {
            "temperature": np.array([], dtype=float),
            "pH": np.array([], dtype=float),
            "dOxygen": np.array([], dtype=float),
            "salinity": np.array([], dtype=float)
        }

    def update_plot(self, time, temperature, pH, dOxygen, salinity):
        # Update data arrays
        if temperature >= 0:
            self.data["temperature"] = np.append(self.data["temperature"], temperature)

        if pH >= 0:
            self.data["pH"] = np.append(self.data["pH"], pH)

        if dOxygen >= 0:
            self.data["dOxygen"] = np.append(self.data["dOxygen"], dOxygen)

        self.data["salinity"] = np.append(self.data["salinity"], salinity)

        # Update plot only if needed
        if len(self.data["temperature"]) > 0:
            x = np.arange(len(self.data["temperature"]))
            self.lines["temperature"].set_xdata(x)
            self.lines["temperature"].set_ydata(self.data["temperature"])

        if len(self.data["pH"]) > 0:
            x = np.arange(len(self.data["pH"]))
            self.lines["pH"].set_xdata(x)
            self.lines["pH"].set_ydata(self.data["pH"])

        if len(self.data["dOxygen"]) > 0:
            x = np.arange(len(self.data["dOxygen"]))
            self.lines["dOxygen"].set_xdata(x)
            self.lines["dOxygen"].set_ydata(self.data["dOxygen"])

        if len(self.data["salinity"]) > 0:
            x = np.arange(len(self.data["salinity"]))
            self.lines["salinity"].set_xdata(x)
            self.lines["salinity"].set_ydata(self.data["salinity"])

        # Update limits and autoscale
        self.ax.relim()
        self.ax.autoscale_view(True, True, True)

        # Redraw canvas
        self.canvas.draw()

        # Trim data arrays if needed
        for key in self.data.keys():
            if len(self.data[key]) > self.duration:
                self.data[key] = self.data[key][-self.duration:]

class GUI:
    def __init__(self, window, temperature, pH, dOxygen, salinity):
        self.window = window
        self.canvas = self.create_canvas()
        self.create_rectangles()
        self.create_image_icons()
        self.create_sensor_labels()
        
        self.sensor_graph = SensorGraph(window, duration=30)
        self.temperature = temperature
        self.pH = pH
        self.dOxygen = dOxygen
        self.salinity = salinity
        
        self.sensor_data = {
            "pH": {"value": self.pH, "normal_range": "6.5 - 9.0"},
            "Salinity": {"value": self.salinity, "normal_range": "4.5 - 5.5"},
            "Temperature": {"value": self.temperature, "normal_range": "25.0 - 32.0"},
            "Dissolved Oxygen": {"value": f"{self.dOxygen}/L", "normal_range": "4.8 - 5.2"},
            "SIM Signal": "Disconnected",
            "Sensors": "Running",
            "Internet Access": "Connected"
        }
        
        self.create_metadata_sensor()
        self.create_sensor_status()
        self.create_button()
        
        self.update_gui(temperature, pH, dOxygen, salinity)

    def create_canvas(self):
        canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=480,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        canvas.place(x=0, y=0)
        return canvas

    def create_rectangles(self):
        rectangles = [
            # sensor data
            (21.0, 23.0, 267.0, 133.0),
            (277.0, 23.0, 522.0, 133.0),
            (532.0, 23.0, 778.0, 133.0), 
            (532.0, 144.0, 778.0, 254.0),
            # sensor status
            (21.0, 385.0, 267.0, 457.0),
            (277.0, 385.0, 522.0, 457.0),
            (532.0, 385.0, 778.0, 457.0),
            # sensor graph
            (21.0, 144.0, 522.0, 374.0), 
        ]
        for rect in rectangles:
            self.canvas.create_rectangle(*rect, fill="#FFFFFF", outline="#e2e8f0")

    def create_metadata_sensor(self):
        metadata_sensor = [
            {
                "image": "image_4.png",
                "text": ("Dissolved Oxygen", self.sensor_data["Dissolved Oxygen"]["value"], f"Normal range: {self.sensor_data['Dissolved Oxygen']['normal_range']}"),
                "coords": (
                    556.0,
                    167.98077392578125,
                    570.0,
                    159.0,
                    548.0,
                    183.0,
                    548.0,  # x1
                    223.0,  # y1
                ),
            },
            {
                "image": "image_5.png",
                "text": ("Temperature", self.sensor_data["Temperature"]["value"], f"Normal range: {self.sensor_data['Temperature']['normal_range']}"),
                "coords": (
                    555.0,
                    48.0,
                    568.0,
                    39.280975341796875,
                    548.0,
                    63.56195068359375,
                    548.0,  # x1
                    103.0,  # y1
                ),
            },
            {
                "image": "image_6.png",
                "text": ("Salinity", self.sensor_data["Salinity"]["value"], f"Normal range: {self.sensor_data['Salinity']['normal_range']}"),
                "coords": (
                    301.0,47.0006103515625,
                    315.0,
                    38.0,
                    293.0,
                    62.0,
                    293.0,  # x1
                    102.0,  # y1
                ),
            },
            {
                "image": "image_7.png",
                "text": ("pH", self.sensor_data["pH"]["value"], f"Normal range: {self.sensor_data['pH']['normal_range']}"),
                "coords": (43.0, 47.5, 55.75, 38, 37.0, 62.0, 37.0, 102.0),
            },
        ]
        self.metadata_sensor_elements = {}
        for element in metadata_sensor:
            text = element["text"]
            coords = element["coords"]
            
            title_text = self.canvas.create_text(
                coords[2],
                coords[3],
                anchor="nw",
                text=text[0],
                fill="#000000",
                font=("Inter", 16 * -1),
            )
            value_text = self.canvas.create_text(
                coords[4],
                coords[5],
                anchor="nw",
                text=text[1],
                fill="#000000",
                font=("Inter Bold", 27 * -1),
            )
            range_text = None
            if len(text) > 2:  
                range_text = self.canvas.create_text(
                    coords[6],
                    coords[7],
                    anchor="nw",
                    text=text[2],
                    fill="#000000",
                    font=("Inter", 13 * -1),
                )
            self.metadata_sensor_elements[text[0]] = {
                "title": title_text,
                "value": value_text,
                "range": range_text
            }

    def create_image_icons(self):
        image_icons = [
            {"image": "image_1.png", "coords": (599.0, 422.0)},
            {"image": "image_2.png", "coords": (101.0, 421.0)},
            {"image": "image_3.png", "coords": (320.0, 424.0)},
            {"image": "image_4.png", "coords": (556.0, 167.98077392578125)},
            {"image": "image_5.png", "coords": (555.0, 48.0)},
            {"image": "image_6.png", "coords": (301.0, 47.0006103515625)},
            {"image": "image_7.png", "coords": (43.0, 47.50018310546875)},
        ]
        self.images = []
        for elem in image_icons:
            image = PhotoImage(file=relative_to_assets(elem["image"]))
            self.images.append(image)
            self.canvas.create_image(elem["coords"][0], elem["coords"][1], image=image)

    def create_sensor_labels(self):
        sensor_labels = [
            {"text": "SIM Signal", "coords": (626.0, 403.0)},
            {"text": "Sensors", "coords": (127.0, 400.0)},
            {"text": "Internet Access", "coords": (346.0, 403.0)},
        ]
        self.sensor_label_elements = {}
        for elem in sensor_labels:
            text = self.canvas.create_text(
                elem["coords"][0],
                elem["coords"][1],
                anchor="nw",
                text=elem["text"],
                fill="#000000",
                font=("Inter", 20 * -1),
            )
        self.sensor_label_elements[elem["text"]] = text

    def create_sensor_status(self):
        sensor_status = [
            {"text": self.sensor_data["SIM Signal"], "coords": (626.0, 427.0)},
            {"text": self.sensor_data["Sensors"], "coords": (127.0, 424.0)},
            {"text": self.sensor_data["Internet Access"], "coords": (346.0, 427.0)},
        ]
        self.sensor_status_elements = {}
        for elem in sensor_status:
            text = self.canvas.create_text(
                elem["coords"][0],
                elem["coords"][1],
                anchor="nw",
                text=elem["text"],
                fill="#000000",
                font=("Inter", 15 * -1),
            )
            self.sensor_status_elements[elem["text"]] = text
            
    def create_button(self):
        button_image_path = relative_to_assets("button_1.png")
        button_img = Image.open(button_image_path)
        button_img = button_img.resize((246, 110))
        button_img = ImageTk.PhotoImage(button_img)
        
        self.button_1 = Button(
            image=button_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat",
            padx=0,
            pady=0
        )
        self.button_1.image = button_img  # reference to avoid garbage collection
        self.button_1.place(x=532, y=264)

    def update_sensor_data(self, temperature=None, pH=None, dOxygen=None, salinity=None, sim_signal=None, sensors=None, internet=None):
        if temperature is not None and temperature >= 0:
            self.temperature = temperature
            self.sensor_data["Temperature"]["value"] = temperature
            self.canvas.itemconfig(self.metadata_sensor_elements["Temperature"]["value"], text=temperature)
            if not THRESHOLDS['temperature'][0] <= temperature <= THRESHOLDS['temperature'][1]:
                self.canvas.itemconfig(self.metadata_sensor_elements["Temperature"]["value"], fill="red")
            else:
                self.canvas.itemconfig(self.metadata_sensor_elements["Temperature"]["value"], fill="black")

        if pH is not None and pH >= 0:
            self.pH = pH
            self.sensor_data["pH"]["value"] = pH
            self.canvas.itemconfig(self.metadata_sensor_elements["pH"]["value"], text=pH)
            if not THRESHOLDS['ph'][0] <= pH <= THRESHOLDS['ph'][1]:
                self.canvas.itemconfig(self.metadata_sensor_elements["pH"]["value"], fill="red")
            else:
                self.canvas.itemconfig(self.metadata_sensor_elements["pH"]["value"], fill="black")

        if dOxygen is not None and dOxygen >= 0:
            self.dOxygen = dOxygen
            self.sensor_data["Dissolved Oxygen"]["value"] = f"{dOxygen}/L"
            self.canvas.itemconfig(self.metadata_sensor_elements["Dissolved Oxygen"]["value"], text=f"{dOxygen}/L")
            if not THRESHOLDS['dissolved_oxygen'][0] <= dOxygen <= THRESHOLDS['dissolved_oxygen'][1]:
                self.canvas.itemconfig(self.metadata_sensor_elements["Dissolved Oxygen"]["value"], fill="red")
            else:
                self.canvas.itemconfig(self.metadata_sensor_elements["Dissolved Oxygen"]["value"], fill="black")

        if salinity is not None and salinity >= 0:
            self.salinity = salinity
            self.sensor_data["Salinity"]["value"] = salinity
            self.canvas.itemconfig(self.metadata_sensor_elements["Salinity"]["value"], text=salinity)
            if not THRESHOLDS['salinity'][0] <= salinity <= THRESHOLDS['salinity'][1]:
                self.canvas.itemconfig(self.metadata_sensor_elements["Salinity"]["value"], fill="red")
            else:
                self.canvas.itemconfig(self.metadata_sensor_elements["Salinity"]["value"], fill="black")

        if sim_signal is not None:
            self.sensor_data["SIM Signal"] = sim_signal
            self.canvas.itemconfig(self.sensor_status_elements["SIM Signal"], text=sim_signal)

        if sensors is not None:
            self.sensor_data["Sensors"] = sensors
            self.canvas.itemconfig(self.sensor_status_elements["Sensors"], text=sensors)

        if internet is not None:
            self.sensor_data["Internet Access"] = internet
            self.canvas.itemconfig(self.sensor_status_elements["Internet Access"], text=internet)

    def update_gui(self, temperature, pH, dOxygen, salinity):
        self.update_sensor_data(temperature, pH, dOxygen, salinity)
        self.sensor_graph.update_plot(time.time(), temperature, pH, dOxygen, salinity)