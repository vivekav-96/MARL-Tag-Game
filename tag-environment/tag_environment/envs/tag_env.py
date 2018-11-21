import tkinter as tk

import Xlib
import gym
import platform
import pyscreenshot as ImageGrab
from PIL import Image
from Xlib.display import Display, X

from agent import Type
from utils import distance_btw_points

ENV_NAME = 'MARL Tag'
ENV_WIDTH = 750
ENV_HEIGHT = 750

CAPTURE_REWARD = 10


class TagEnv(gym.Env):

    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_title(ENV_NAME)
        self.root.geometry("%dx%d+0+0" % (ENV_WIDTH, ENV_HEIGHT))
        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.box = None
        self.window = None
        self.update_ui()
        self.runners = []
        self.chasers = []
        display = Display()
        root = display.screen().root

        # If current platform is linux, initialize Xlib to find game window hierarchy to observe frames.
        if 'Linux' in platform.system():
            self.find_window_hierarchy(root, ENV_NAME)

        self.box = (self.canvas.winfo_rootx(), self.canvas.winfo_rooty(),
                    self.canvas.winfo_width(), self.canvas.winfo_height())

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        self.update_ui()

    def observe(self):
        """
        :return: Current frame as Pillow image

        If the working platform is linux, we'll use Xlib to capture the window frame (which is almost 10 times faster)
        else we'll use the basic screenshoting method.
        """
        if 'Linux' in platform.system():
            return self.xlib_observe()
        else:
            return self.pyscreenshot_observe()

    def pyscreenshot_observe(self):
        """
        :return: Current frame as Pillow image
        """
        im = ImageGrab.grab(bbox=self.box)
        return im

    def xlib_observe(self):
        """
        :return: Current frame as Pillow Image

        NOTE : find_window_hierarchy must be called before calling this method or will raise an error
        """
        raw = self.window.get_image(0, 0, ENV_WIDTH, ENV_HEIGHT, X.ZPixmap, 0xffffffff)
        image = Image.frombytes("RGB", (ENV_WIDTH, ENV_HEIGHT), raw.data, "raw", "BGRX")
        return image

    def get_reward_for_agent(self, agent):
        """
        :param agent: Agent whose reward has to be calculated
        :return:  Reward of the agent
        """
        reward = 0
        if agent.get_agent_type() == Type.RUNNER:
            # Calculate Runner Reward
            for c in self.chasers:
                if agent.is_collided(c):
                    # Runner has bee captured
                    print('{0} {1} got captured'.format(agent.get_agent_type(), agent.get_id()))
                    reward -= CAPTURE_REWARD
                else:
                    temp_reward = distance_btw_points(agent.get_self_coords(), c.get_self_coords()) / 1060
                    reward += temp_reward
        else:
            # Calculate Chaser Reward
            for r in self.runners:
                if agent.is_collided(r):
                    # Runner has bee captured
                    print('{0} {1} captured the runner'.format(agent.get_agent_type(), agent.get_id()))
                    reward += CAPTURE_REWARD
                else:
                    temp_reward = distance_btw_points(agent.get_self_coords(), r.get_self_coords()) / 1060
                    reward -= temp_reward
        return reward

    def update_ui(self):
        self.root.update_idletasks()
        self.root.update()

    def get_canvas(self):
        return self.canvas

    def spawn_agents(self, runners, chasers):
        self.runners = runners
        self.chasers = chasers

    def find_window_hierarchy(self, window, window_name):
        # window: Xlib.display.drawable.Window
        children = window.query_tree().children
        w: Xlib.display.drawable.Window
        for w in children:
            cl = window.get_wm_name()
            if cl == 'MARL Tag':
                try:
                    raw = w.get_image(0, 0, ENV_WIDTH, ENV_HEIGHT, X.ZPixmap, 0xffffffff)
                    self.window = w
                    return
                except:
                    pass
            self.find_window_hierarchy(w, window_name)

    # def callback(self):
    #     print('root.geometry:', self.root.winfo_geometry())
    #     print('canvas.geometry:', self.canvas.winfo_geometry())
    #     print('canvas.width :', self.canvas.winfo_width())
    #     print('canvas.height:', self.canvas.winfo_height())
    #     print('canvas.x:', self.canvas.winfo_x())
    #     print('canvas.y:', self.canvas.winfo_y())
    #     print('canvas.rootx:', self.canvas.winfo_rootx())
    #     print('canvas.rooty:', self.canvas.winfo_rooty())
