import tkinter as tk

from chaser import Chaser
from runner import Runner

root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w/2, h/2))

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

a1 = Runner(canvas, 200, 200)
a1.gogogo()
a2 = Runner(canvas, 200, 200)
a2.gogogo()

b1 = Chaser(canvas, 500, 300)
b1.gogogo()
b2 = Chaser(canvas, 500, 300)
b2.gogogo()

root.mainloop()

