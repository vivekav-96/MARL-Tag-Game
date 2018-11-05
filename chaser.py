import math

from agent import Agent
from utils import distance_btw_points


class Chaser(Agent):

    def step(self, env):
        self.chase(env.get_runner())

    def chase(self, runner):
        """
        Moves a step towards an agent.
        :param runner: The target agent
        :return: Distance to kill
        """
        target_coords = runner.get_self_coords()
        theta = self.get_angle_to_target(target_coords[0], target_coords[1])
        self.move(2 * math.cos(theta), 2 * math.sin(theta))
        return distance_btw_points(target_coords, self.get_self_coords())

    def get_icon(self):
        return 'blue.png'
