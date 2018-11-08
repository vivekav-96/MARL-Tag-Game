import tkinter as tk

import gym
import pyscreenshot as ImageGrab
from utils import distance_btw_points

from agent import Type

CAPTURE_REWARD = 10


class TagEnv(gym.Env):

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("%dx%d+0+0" % (750, 750))
        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.box = None
        self.update_ui()
        self.runners = []
        self.chasers = []

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        self.update_ui()

    def observe(self):
        """
        :return: Current frame as Pillow image
        """
        im = ImageGrab.grab(bbox=self.box)
        return im

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
                    reward -= CAPTURE_REWARD
                else:
                    temp_reward = distance_btw_points(agent.get_self_coords(), c.get_self_coords()) / 1060
                    reward += temp_reward
        else:
            # Calculate Chaser Reward
            for r in self.runners:
                if agent.is_collided(r):
                    # Runner has bee captured
                    reward += CAPTURE_REWARD
                else:
                    temp_reward = distance_btw_points(agent.get_self_coords(), r.get_self_coords()) / 1060
                    reward -= temp_reward
        return reward

    def update_ui(self):
        self.root.update_idletasks()
        self.root.update()
        self.box = (self.canvas.winfo_rootx(), self.canvas.winfo_rooty(),
                    self.canvas.winfo_width(), self.canvas.winfo_height())

    def get_canvas(self):
        return self.canvas

    def spawn_agents(self, runners, chasers):
        self.runners = runners
        self.chasers = chasers

    # def callback(self):
    #     print('root.geometry:', self.root.winfo_geometry())
    #     print('canvas.geometry:', self.canvas.winfo_geometry())
    #     print('canvas.width :', self.canvas.winfo_width())
    #     print('canvas.height:', self.canvas.winfo_height())
    #     print('canvas.x:', self.canvas.winfo_x())
    #     print('canvas.y:', self.canvas.winfo_y())
    #     print('canvas.rootx:', self.canvas.winfo_rootx())
    #     print('canvas.rooty:', self.canvas.winfo_rooty())
