import math
import random
import threading
import time
import tkinter as tk
from abc import ABC, abstractmethod


class Agent(ABC):
    def __init__(self, parent, init_x, init_y):
        self.img = tk.PhotoImage(file=self.get_icon())
        self.card = parent.create_image(init_x, init_y, image=self.img)
        self.parent = parent

    def gogogo(self):
        t = threading.Thread(target=self.__start)
        t.start()

    """
    Starts Random Movement.
    """

    def __start(self):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        i = 0
        while True:
            coords = self.parent.coords(self.card)
            if i % 10 == 0:
                x = random.randint(-10, 10)
                y = random.randint(-10, 10)
            x = x if 15 < coords[0] + x < self.parent.winfo_width() - 15 else 0
            y = y if 15 < coords[1] + y < self.parent.winfo_height() - 15 else 0
            self.move(x, y)
            time.sleep(0.1)
            i += 1

    def move(self, x, y):
        self.parent.move(self.card, x, y)
        pass

    def get_self_coords(self):
        return self.parent.coords(self.card)

    def get_angle_to_target(self, target_x, target_y):
        coords = self.get_self_coords()
        if target_x == coords[0] and target_y > coords[1]:
            print('case 1 : {}'.format(-90))
            return -90
        elif target_x == coords[0] and target_y <= coords[1]:
            print('case 2 : {}'.format(90))
            return 90
        else:
            theta = math.degrees(math.atan((coords[1] - target_y) / (coords[0] - target_x)))
            return theta

    @abstractmethod
    def get_icon(self):
        pass
