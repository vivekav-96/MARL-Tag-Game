from abc import ABC

from agent import Agent, Type


class Chaser(Agent, ABC):

    def unit_distance(self):
        return 5

    def get_icon(self):
        return 'icons/blue.png'

    def get_agent_type(self):
        return Type.CHASER

    # def chase(self, runner):
    #     """
    #     Moves a step towards an agent.
    #     :param runner: The target agent
    #     :return: Distance to kill
    #     """
    #     target_coords = runner.get_self_coords()
    #     theta = self.get_angle_to_target(target_coords[0], target_coords[1])
    #     self.move(2 * math.cos(theta), 2 * math.sin(theta))
    #     return distance_btw_points(target_coords, self.get_self_coords())
