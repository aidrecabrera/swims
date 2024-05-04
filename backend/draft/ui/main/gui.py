from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\.dev\projects\python\ui_swims\final\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x480")
window.configure(bg = "#FFFFFF")

entry = Entry(window)  # Access the Entry class
text = Text(window)  # Access the Text class


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 480,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    21.0,
    23.0,
    267.0,
    133.0,
    fill="#FFFFFF",
    outline="#e2e8f0")

canvas.create_rectangle(
    277.0,
    23.0,
    522.0,
    133.0,
    fill="#FFFFFF",
    outline="#e2e8f0")

canvas.create_rectangle(
    532.0,
    23.0,
    778.0,
    133.0,
    fill="#FFFFFF",
    outline="#e2e8f0")

canvas.create_rectangle(
    21.0,
    144.0,
    522.0,
    374.0,
    fill="#FFFFFF",
    outline="#e2e8f0")

canvas.create_rectangle(
    532.0,
    144.0,
    778.0,
    254.0,
    fill="#FFFFFF",
    outline="#e2e8f0")

canvas.create_rectangle(
    21.0,
    385.0,
    267.0,
    457.0,
    fill="#FFFFFF",
    outline="#e2e8f0")

canvas.create_rectangle(
    277.0,
    385.0,
    522.0,
    457.0,
    fill="#FFFFFF",
    outline="#e2e8f0")

canvas.create_rectangle(
    532.0,
    385.0,
    778.0,
    457.0,
    fill="#FFFFFF",
    outline="#e2e8f0")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    599.0,
    422.0,
    image=image_image_1
)

canvas.create_text(
    626.0,
    403.0,
    anchor="nw",
    text="SIM Signal",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    626.0,
    427.0,
    anchor="nw",
    text="Strong",
    fill="#000000",
    font=("Inter", 15 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    101.0,
    421.0,
    image=image_image_2
)

canvas.create_text(
    127.0,
    400.0,
    anchor="nw",
    text="Sensors",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    127.0,
    424.0,
    anchor="nw",
    text="Running",
    fill="#000000",
    font=("Inter", 15 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    320.0,
    424.0,
    image=image_image_3
)

canvas.create_text(
    346.0,
    403.0,
    anchor="nw",
    text="Internet Access",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    346.0,
    427.0,
    anchor="nw",
    text="Connected",
    fill="#000000",
    font=("Inter", 15 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    556.0,
    167.98077392578125,
    image=image_image_4
)

canvas.create_text(
    570.0,
    159.0,
    anchor="nw",
    text="Dissolved Oxygen",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    548.0,
    183.0,
    anchor="nw",
    text="8.2 mg/L",
    fill="#000000",
    font=("Inter Bold", 27 * -1)
)

canvas.create_text(
    548.0,
    223.0,
    anchor="nw",
    text="Normal range: 6.5 - 8.5",
    fill="#000000",
    font=("Inter", 13 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    555.0,
    48.0,
    image=image_image_5
)

canvas.create_text(
    568.0,
    39.280975341796875,
    anchor="nw",
    text="Temperature",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    548.0,
    63.56195068359375,
    anchor="nw",
    text="22°C",
    fill="#000000",
    font=("Inter Bold", 27 * -1)
)

canvas.create_text(
    548.0,
    103.0,
    anchor="nw",
    text="Normal range: 6.5 - 8.5",
    fill="#000000",
    font=("Inter", 13 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    301.0,
    47.0006103515625,
    image=image_image_6
)

canvas.create_text(
    315.0,
    38.0,
    anchor="nw",
    text="Salinity",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    293.0,
    62.0,
    anchor="nw",
    text="10.5 ppt",
    fill="#000000",
    font=("Inter Bold", 27 * -1)
)

canvas.create_text(
    293.0,
    102.0,
    anchor="nw",
    text="Normal range: 6.5 - 8.5",
    fill="#000000",
    font=("Inter", 13 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    43.0,
    47.50018310546875,
    image=image_image_7
)

canvas.create_text(
    55.75,
    38.0,
    anchor="nw",
    text="pH",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    37.0,
    62.0,
    anchor="nw",
    text="12.0 (Normal)",
    fill="#000000",
    font=("Inter Bold", 27 * -1)
)

canvas.create_text(
    37.0,
    102.0,
    anchor="nw",
    text="Normal range: 6.5 - 8.5",
    fill="#000000",
    font=("Inter", 13 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=532.0,
    y=264.0,
    width=246.0,
    height=110.0
)
window.resizable(False, False)
window.mainloop()
