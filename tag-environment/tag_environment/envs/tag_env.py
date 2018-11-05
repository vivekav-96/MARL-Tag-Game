import tkinter as tk

import gym

from chaser import Chaser
from runner import Runner


class TagEnv(gym.Env):

    def __init__(self):
        def callback():
            print('  root.geometry:', self.root.winfo_geometry())
            print('canvas.geometry:', canvas.winfo_geometry())
            print('canvas.width :', canvas.winfo_width())
            print('canvas.height:', canvas.winfo_height())
            print('canvas.x:', canvas.winfo_x())
            print('canvas.y:', canvas.winfo_y())
            print('canvas.rootx:', canvas.winfo_rootx())
            print('canvas.rooty:', canvas.winfo_rooty())

        self.root = tk.Tk()
        self.root.geometry("%dx%d+0+0" % (750, 750))

        canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        self.a1 = Chaser(canvas, 350, 100)
        self.b1 = Runner(canvas, 500, 500)
        self.update_ui()

        callback()

    def step(self, action):
        self.get_chaser().step(self)
        # self.get_runner().step(self)

    def reset(self):
        pass

    def render(self, mode='human'):
        self.update_ui()

    def update_ui(self):
        self.root.update_idletasks()
        self.root.update()

    def get_runner(self):
        return self.b1

    def get_chaser(self):
        return self.a1
