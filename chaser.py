import math
import threading

from agent import Agent
from utils import distance_btw_points


class Chaser(Agent):

    def chase(self, runner):
        t = threading.Thread(target=self.go,
                             args=(runner,))
        t.start()

    def go(self, runner):
        tcoords = runner.get_self_coords()
        theta = self.get_angle_to_target(tcoords[0], tcoords[1])
        print('distance to kill : {}'.format(distance_btw_points(tcoords, self.get_self_coords())))
        self.move(math.cos(theta), math.sin(theta))
        self.parent.after(10, self.go, runner)

    def get_icon(self):
        return 'blue.png'
