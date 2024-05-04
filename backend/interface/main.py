from datetime import datetime, timedelta
from pathlib import Path

from tkinter import Tk, Canvas, Button, PhotoImage

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from pathlib import Path

CURRENT_PATH = Path(__file__).parent
ASSETS_PATH = CURRENT_PATH / 'assets' / 'frame0'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("800x480")
window.attributes('-fullscreen')
window.configure(bg="#FFFFFF")

def toggle_fullscreen(event=None):
    window.attributes('-fullscreen', not window.attributes('-fullscreen'))

window.bind('<F11>', toggle_fullscreen)
window.bind('<Escape>', toggle_fullscreen)

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=480,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x=0, y=0)

# Creating rectangles
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
    canvas.create_rectangle(*rect, fill="#FFFFFF", outline="#e2e8f0")

# Adding images and text
metadata_sensor = [
    {
        "image": "image_4.png",
        "text": ("Dissolved Oxygen", "8.2 mg/L", "Normal range: 6.5 - 8.5"),
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
        "text": ("Temperature", "22°C", "Normal range: 6.5 - 8.5"),
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
        "text": ("Salinity", "10.5 ppt", "Normal range: 6.5 - 8.5"),
        "coords": (
            301.0,
            47.0006103515625,
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
        "text": ("pH", "12.0 (Normal)", "Normal range: 6.5 - 8.5"),
        "coords": (43.0, 47.5, 55.75, 38, 37.0, 62.0, 37.0, 102.0),
    },
]

for element in metadata_sensor:
    text = element["text"]
    coords = element["coords"]

    # type label
    canvas.create_text(
        coords[2],
        coords[3],
        anchor="nw",
        text=text[0],
        fill="#000000",
        font=("Inter", 16 * -1),
    )

    # data label
    canvas.create_text(
        coords[4],
        coords[5],
        anchor="nw",
        text=text[1],
        fill="#000000",
        font=("Inter Bold", 27 * -1),
    )

    # normal range label
    if len(text) > 2:  # check if there's a third line of text
        canvas.create_text(
            coords[6],
            coords[7],  # adjust vertical position for the third line
            anchor="nw",
            text=text[2],  # range
            fill="#000000",
            font=("Inter", 13 * -1),
        )


image_icons = [
    {"image": "image_1.png", "coords": (599.0, 422.0)},
    {"image": "image_2.png", "coords": (101.0, 421.0)},
    {"image": "image_3.png", "coords": (320.0, 424.0)},
    {"image": "image_4.png", "coords": (556.0, 167.98077392578125)},
    {"image": "image_5.png", "coords": (555.0, 48.0)},
    {"image": "image_6.png", "coords": (301.0, 47.0006103515625)},
    {"image": "image_7.png", "coords": (43.0, 47.50018310546875)},
]

sensor_labels = [
    {"text": "SIM Signal", "coords": (626.0, 403.0)},
    {"text": "Sensors", "coords": (127.0, 400.0)},
    {"text": "Internet Access", "coords": (346.0, 403.0)},
]

for elem in sensor_labels:
    canvas.create_text(
        elem["coords"][0],
        elem["coords"][1],
        anchor="nw",
        text=elem["text"],
        fill="#000000",
        font=("Inter", 20 * -1),
    )

sensor_status = [
    {"text": "Strong", "coords": (626.0, 427.0)},
    {"text": "Running", "coords": (127.0, 424.0)},
    {"text": "Connected", "coords": (346.0, 427.0)},
]

for elem in sensor_status:
    canvas.create_text(
        elem["coords"][0],
        elem["coords"][1],
        anchor="nw",
        text=elem["text"],
        fill="#000000",
        font=("Inter", 15 * -1),
    )

# render icons
images = []
for elem in image_icons:
    image = PhotoImage(file=relative_to_assets(elem["image"]))
    # Store the image in the list
    images.append(image)
    canvas.create_image(elem["coords"][0], elem["coords"][1], image=image)

# button
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
)
button_1.place(x=532.0, y=264.0, width=246.0, height=110.0)

window.resizable(False, False)
window.mainloop()