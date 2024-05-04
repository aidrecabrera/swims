from tkinter import Tk
from interface.gui import GUI

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
    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    main()