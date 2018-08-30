import tkinter as tk
import time
import random


class gui(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.canvas = tk.Canvas(parent, bg="blue", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.img = tk.PhotoImage(file="red.png")
        self.card = self.canvas.create_image(200, 200, image=self.img)
        self.canvas.tag_bind(self.card, '<Button-1>', self.onObjectClick1)

    def onObjectClick1(self, event):
        period = 500
        for i in range(period):
            self.canvas.move(self.card, 3 * random.randint(-10, 10), 3 * random.randint(-10, 10))  # chosen_card
            root.after(10)
            # root.after(total_time/period) #Pause for time, creating animation effect
            root.update()  # Update position of card on canvas


if __name__ == "__main__":
    root = tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    gui(root)
    root.mainloop()
