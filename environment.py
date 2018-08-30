from agent import Agent
import tkinter as tk
import random

root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

canvas = tk.Canvas(root, bg="blue", highlightthickness=0)
canvas.pack(fill="both", expand=True)


# a = Agent(canvas, 100, 100)
# a.gogogo()

b = Agent(canvas, 800, 800)
b.gogogo()

root.mainloop()

