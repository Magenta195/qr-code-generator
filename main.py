from gui import GUI
from generator import Generator

if __name__ == "__main__":
    generator = Generator()
    gui = GUI(generator)

    gui.render()
    gui.pack()
    gui.mainloop()
