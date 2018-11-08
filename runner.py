import math

from agent import Agent
from utils import distance_btw_points


class Runner(Agent):
    def step(self, env):
        print('Runner - {0} stepping...'.format(self.get_id()))

    def get_icon(self):
        return 'icons/red.png'

    def evade(self, chaser):
        target_coords = chaser.get_self_coords()
        theta = self.get_angle_to_target(target_coords[0], target_coords[1])
        print('Runner Angle', theta)
        # print('distance to kill : {}'.format(distance_btw_points(target_coords, self.get_self_coords())))
        self.move(-2 * math.cos(theta), -2 * math.sin(theta))
        return distance_btw_points(target_coords, self.get_self_coords())

    def unit_distance(self):
        return 4
