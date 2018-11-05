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
        """
        Starts Random Movement.
        """
        t = threading.Thread(target=self.__start_random)
        t.start()

    def __start_random(self):
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        i = 0
        while True:
            if i % 10 == 0:
                x = random.randint(-10, 10)
                y = random.randint(-10, 10)
            self.move(x, y)
            time.sleep(0.05)
            i += 1

    def move(self, x, y):
        """
        :param x: Distance to move in X direction
        :param y: Distance to move in Y direction
        :return: None

        The actual_x and actual_y are calculated so as that the agent won't move outside the screen
        actual_x and actual_y are the distances actually in X and Y directions respectively.
        """
        coords = self.get_self_coords()
        actual_x = x if 15 < coords[0] + x < self.parent.winfo_width() - 15 else 0
        actual_y = y if 15 < coords[1] + y < self.parent.winfo_height() - 15 else 0
        self.parent.move(self.card, actual_x, actual_y)

    def get_self_coords(self):
        """
        :return: X, Y coordinates of the agent
        """
        return self.parent.coords(self.card)

    def get_angle_to_target(self, target_x, target_y):
        """
        :param target_x: Target X co-ordinate
        :param target_y: Target Y co-ordinate
        :return: Euclidean angle to th target.

        Divide by Zero error cases are avoided.
        """
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

    @abstractmethod
    def step(self, env):
        pass
