from tkinter import Tk, Canvas, Button, PhotoImage
from pathlib import Path
from .utils import relative_to_assets 
from PIL import Image, ImageTk

class GUI:
    def __init__(self, window, temperature, pH, dOxygen, salinity):
        self.window = window
        self.canvas = self.create_canvas()
        self.create_rectangles()
        self.create_image_icons()
        self.create_sensor_labels()
        
        self.temperature = temperature
        self.pH = pH
        self.dOxygen = dOxygen
        self.salinity = salinity
        
        self.sensor_data = {
            "pH": {"value": self.pH, "normal_range": "6.5 - 8.5"},
            "Salinity": {"value": self.salinity, "normal_range": "6.5 - 8.5"},
            "Temperature": {"value": self.temperature, "normal_range": "6.5 - 8.5"},
            "Dissolved Oxygen": {"value": f"{self.dOxygen}/L", "normal_range": "6.5 - 8.5"},
            "SIM Signal": "Strong",
            "Sensors": "Running",
            "Internet Access": "Connected"
        }
        
        self.create_metadata_sensor()
        self.create_sensor_status()
        self.create_button()

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
        if temperature is not None:
            self.temperature = temperature
            self.sensor_data["Temperature"]["value"] = temperature
            self.canvas.itemconfig(self.metadata_sensor_elements["Temperature"]["value"], text=temperature)
        if pH is not None:
            self.pH = pH
            self.sensor_data["pH"]["value"] = pH
            self.canvas.itemconfig(self.metadata_sensor_elements["pH"]["value"], text=pH)
        if dOxygen is not None:
            self.dOxygen = dOxygen
            self.sensor_data["Dissolved Oxygen"]["value"] = f"{dOxygen}/L"
            self.canvas.itemconfig(self.metadata_sensor_elements["Dissolved Oxygen"]["value"], text=f"{dOxygen}/L")
        if salinity is not None:
            self.salinity = salinity
            self.sensor_data["Salinity"]["value"] = salinity
            self.canvas.itemconfig(self.metadata_sensor_elements["Salinity"]["value"], text=salinity)
        if sim_signal is not None:
            self.sensor_data["SIM Signal"] = sim_signal
            self.canvas.itemconfig(self.sensor_status_elements["Strong"], text=sim_signal)
        if sensors is not None:
            self.sensor_data["Sensors"] = sensors
            self.canvas.itemconfig(self.sensor_status_elements["Running"], text=sensors)
        if internet is not None:
            self.sensor_data["Internet Access"] = internet
            self.canvas.itemconfig(self.sensor_status_elements["Connected"], text=internet)