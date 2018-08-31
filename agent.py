import random
import threading
import time
import tkinter as tk
from abc import ABC, abstractmethod


class Agent(ABC):
    def __init__(self, parent, init_x, init_y):
        print(parent.winfo_width())
        print(parent.winfo_height())
        self.img = tk.PhotoImage(file=self.get_icon())
        self.card = parent.create_image(init_x, init_y, image=self.img)
        self.parent = parent

    def gogogo(self):
        t = threading.Thread(target=self.start)
        t.start()

    def start(self):
        period = 500
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        for i in range(period):
            coords = self.parent.coords(self.card)
            print(coords)
            if i % 10 == 0:
                x = random.randint(-10, 10)
                y = random.randint(-10, 10)
            x = x if coords[0] + x > 15 else 0
            y = y if coords[1] + y > 15 else 0
            self.move(x, y)
            time.sleep(0.05)

    def move(self, x, y):
        self.parent.move(self.card, x, y)
        pass

    @abstractmethod
    def get_icon(self):
        pass
