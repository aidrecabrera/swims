from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\.dev\projects\python\ui_swims\final\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x480")
window.configure(bg="#FFFFFF")

entry = Entry(window)  
text = Text(window)  

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=480,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

canvas.create_rectangle(
    21.0, 23.0, 267.0, 133.0, fill="#FFFFFF", outline="#e2e8f0")
canvas.create_rectangle(
    277.0, 23.0, 522.0, 133.0, fill="#FFFFFF", outline="#e2e8f0")
canvas.create_rectangle(
    532.0, 23.0, 778.0, 133.0, fill="#FFFFFF", outline="#e2e8f0")
canvas.create_rectangle(
    21.0, 144.0, 522.0, 374.0, fill="#FFFFFF", outline="#e2e8f0")
canvas.create_rectangle(
    532.0, 144.0, 778.0, 254.0, fill="#FFFFFF", outline="#e2e8f0")
canvas.create_rectangle(
    21.0, 385.0, 267.0, 457.0, fill="#FFFFFF", outline="#e2e8f0")
canvas.create_rectangle(
    277.0, 385.0, 522.0, 457.0, fill="#FFFFFF", outline="#e2e8f0")
canvas.create_rectangle(
    532.0, 385.0, 778.0, 457.0, fill="#FFFFFF", outline="#e2e8f0")

image_icons = [
    {"image": "image_1.png", "coords": (599.0, 422.0)},
    {"image": "image_2.png", "coords": (101.0, 421.0)},
    {"image": "image_3.png", "coords": (320.0, 424.0)},
    {"image": "image_4.png", "coords": (556.0, 167.98077392578125)},
    {"image": "image_5.png", "coords": (555.0, 48.0)},
    {"image": "image_6.png", "coords": (301.0, 47.0006103515625)},
    {"image": "image_7.png", "coords": (43.0, 47.50018310546875)}
]

for icon in image_icons:
    image = PhotoImage(file=relative_to_assets(icon["image"]))
    canvas.create_image(icon["coords"][0], icon["coords"][1], image=image)

window.resizable(False, False)
window.mainloop()
