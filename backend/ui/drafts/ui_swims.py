import tkinter as tk

class GUIApplication:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Swims")
        self.root.geometry("800x480")  # Adjusted size for 5-inch display
        self.root.attributes("-fullscreen", True)  # Start in fullscreen mode
        self.initialize()
        self.root.mainloop()
        
    def initialize(self):
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=0)  # Adjusted weight for the row containing signal, internet, and sensors
        self.root.config(width=800, height=480)  # Adjusted size for 5-inch display

        def create_card(root, card_style, grid_position, texts, colspan=1, rowspan=1):
            card = tk.Canvas(root, **card_style)
            if texts == ["Sensors"] or texts == ["Signal"] or texts == ["Internet"]:
                card = tk.Canvas(root, **card_style)
                
            card.grid(row=grid_position[0], column=grid_position[1], sticky="nsew", padx=5, pady=5, columnspan=colspan, rowspan=rowspan)
            
            if texts[0] not in ["Sensors", "Signal", "Internet"]:
                for i, text in enumerate(texts[:-1]):  # Exclude the last text (normal range)
                    font_size = 14 if i == 0 else 24  # Adjusted font sizes
                    font_weight = "bold" if i == 1 else "normal"
                    y_position = 10 if i == 0 else 35  # Adjusted y-positions
                    card.create_text(10, y_position, anchor="nw", text=text, font=("Inter", font_size, font_weight), justify="left")
                
            if texts[0] == "Settings":
                button = tk.Button(card, text="Settings", font=("Inter", 10, "normal"), command=lambda: print("Settings clicked"), bg="#f3f4f6", border=0, activebackground="#f3f4f6")
                button.place(relx=0.5, rely=0.5, anchor="center")
            elif texts[0] == "Sensor Data":
                card.create_text(10, 10, anchor="nw", text=texts[0], font=("Inter", 14, "normal"), justify="left")
            elif texts[0] == "Sensors" or texts[0] == "Signal" or texts[0] == "Internet":
                card.create_text(10, 10, anchor="nw", text=texts[0], font=("Inter", 18, "normal"), justify="left")
                card.create_text(10, 40, anchor="nw", text=texts[1], font=("Inter", 14, "normal"), justify="left")
            else:
                normal_range_text = texts[-1]
                normal_range_font_size = 10  # Adjusted font size
                padding = 10  # Adjusted padding
                normal_range_y_position = card_style.get("height") - normal_range_font_size - padding
                card.create_text(10, normal_range_y_position, anchor="sw", text=normal_range_text, font=("Inter", normal_range_font_size, "normal"), justify="left")
            
            return card
    
        card_style = {
            "bg": "#f3f4f6",
            "border": 1,
            "borderwidth": 0.5,
            "highlightbackground": "black",
            "width": 250,
            "height": 120  # Adjusted height
        }
        
        widget_style = {
            "bg": "#f3f4f6",
            "border": 1,
            "borderwidth": 0.5,
            "highlightbackground": "black",
            "width": 250,
            "height": 40  # Adjusted height for signal, internet, and sensors
        }
        
        for i in range(3):
            self.canvas = tk.Canvas(self.root, **card_style)
            self.canvas.grid(row=0, column=i, sticky="nsew", padx=5, pady=5)

        metadata_ph = ["pH", "7.4", "Normal range: 7.2 - 7.6"]
        metadata_temperature = ["Temperature", "25°C", "Normal range: 24 - 26°C"]
        metadata_salinity = ["Salinity", "35 ppt", "Normal range: 34 - 36 ppt"]        
        metadata_doxygen = ["Dissolved Oxygen", "8.2 mg/L", "Normal range: 6.5 - 8.5"]
        metadata_settings = ["Settings"]
        metadata_sensor_data = ["Sensor Data"]
        metadata_signal = ["Signal", "Strong"]
        metadata_internet = ["Internet", "Connected"]
        metadata_sensors = ["Sensors", "Running"]

        self.pHCard = create_card(self.root, card_style, (0, 0), metadata_ph)
        self.salinityCard = create_card(self.root, card_style, (0, 1), metadata_salinity)
        self.temperatureCard = create_card(self.root, card_style, (0, 2), metadata_temperature)
        
        self.doxygenCard = create_card(self.root, card_style, (1, 0), metadata_doxygen, colspan=1, rowspan=1)
        self.sensorData = create_card(self.root, card_style, (1, 1), metadata_sensor_data, colspan=2, rowspan=2)
        
        self.settingsCard = create_card(self.root, card_style, (2, 0), metadata_settings, colspan=1, rowspan=1)
        
        self.signal = create_card(self.root, widget_style, (3, 0), metadata_signal)
        self.internet = create_card(self.root, widget_style, (3, 1), metadata_internet)
        self.sensors = create_card(self.root, widget_style, (3, 2), metadata_sensors)
            
    
    def destroy(self):
        self.root.destroy()

def main():
    app = GUIApplication()

if __name__ == "__main__":
    main()