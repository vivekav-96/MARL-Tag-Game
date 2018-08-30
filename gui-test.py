import time
from tkinter import Tk, Frame, Button, Canvas, PhotoImage


class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = Tk(baseName='Tag')
back = Frame(master=root, width=1000, height=1000, bg='black')
canvas = Canvas(back, width=400, height=400)
b = Button(master=canvas)
canva = Canvas(back, width=400, height=400)
img = PhotoImage(file='red.png')
image = canva.create_image(140, 140, image=img)


def move():
    canva.move(image, 1, -1)


b.pack({'side': 'left'})
b['text'] = "Yes"
b['command'] = move
canvas.pack()
coord = [20, 20, 100, 100]

canva.pack()
back.pack()
root.mainloop()
