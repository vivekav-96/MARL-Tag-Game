import time
import tkinter as tk
from threading import Thread

from chaser import Chaser
from runner import Runner


class Environment:

    def __init__(self):
        root = tk.Tk()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        print(w, h)
        root.geometry("%dx%d+0+0" % (1000, 1000))

        canvas = tk.Canvas(root, bg="black", highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        self.a1 = Chaser(canvas, 650, 100)
        self.b1 = Runner(canvas, 500, 500)

        Thread(target=play, name='Play', args=(self,)).start()

        root.bind('a', self.test)

        root.mainloop()

    def get_runner(self):
        return self.b1

    def get_chaser(self):
        return self.a1

    def test(self, event):
        self.get_chaser().step(self)
        self.get_runner().step(self)


def play(env):
    while True:
        # env.get_chaser().step(env)
        env.get_runner().step(env)
        time.sleep(0.1)


env = Environment()
