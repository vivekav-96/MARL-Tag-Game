import math
import random
import threading
import time
import tkinter as tk
from abc import ABC, abstractmethod
from enum import Enum
from utils import distance_btw_points


class Type(Enum):
    RUNNER = 0
    CHASER = 1


class Actions(Enum):
    NORTH = 0
    NORTH_EAST = 1
    EAST = 2
    SOUTH_EAST = 3
    SOUTH = 4
    SOUTH_WEST = 5
    WEST = 6
    NORTH_WEST = 7


actions = [Actions.NORTH,
           Actions.NORTH_EAST,
           Actions.EAST,
           Actions.SOUTH_EAST,
           Actions.SOUTH,
           Actions.SOUTH_WEST,
           Actions.WEST,
           Actions.NORTH_WEST]


class Agent(ABC):
    def __init__(self, id, environment, parent, init_x, init_y):
        """
        :param id: ID of the agent. An integer
        :param environment: environment the agent is acting in
        :param parent: parent canvas of the agent.
        :param init_x: Initial X co-ordinate of the agent
        :param init_y: Initial Y co-ordinate of the agent

        Pass these arguments to initialise an agent.
        """
        self.id = id
        self.img = tk.PhotoImage(file=self.get_icon())
        self.card = parent.create_image(init_x, init_y, image=self.img)
        self.parent = parent

    def act(self, observed_frame):
        action = self.step(observed_frame)
        self.move_to_direction(actions[action])
        return action

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

    def move_to_direction(self, direction):
        """
        :param direction: direction

        Moves agent unit distance to the passed direction
        """
        if direction == Actions.NORTH:
            self.move(0, -self.unit_distance())
        elif direction == Actions.EAST:
            self.move(self.unit_distance(), 0)
        elif direction == Actions.SOUTH:
            self.move(0, self.unit_distance())
        elif direction == Actions.WEST:
            self.move(-self.unit_distance(), 0)
        elif direction == Actions.NORTH_EAST:
            self.move(self.unit_distance(), -self.unit_distance())
        elif direction == Actions.NORTH_WEST:
            self.move(-self.unit_distance(), -self.unit_distance())
        elif direction == Actions.SOUTH_EAST:
            self.move(self.unit_distance(), self.unit_distance())
        elif direction == Actions.SOUTH_WEST:
            self.move(-self.unit_distance(), self.unit_distance())

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

    def is_collided(self, agent):
        """
        :param agent: Target agent
        :return: boolean

        Returns true if the agent has been collided  with the target agent.
        """
        return distance_btw_points(self.get_self_coords(), agent.get_self_coords()) <= 15

    def get_id(self):
        return self.id

    @abstractmethod
    def get_icon(self):
        pass

    @abstractmethod
    def step(self, observed_frame):
        """
        :param observed_frame: passes the observed_frame
        :return: the action to take, an integer between 0 to 7
        """
        pass

    @abstractmethod
    def unit_distance(self):
        """
        :return: Unit distance

        That is distance travelled by agent in one step. It'll be slightly higher for runner than chasers.
        """
        pass

    @abstractmethod
    def get_agent_type(self):
        """
        :return: Type of the agent. Either RUNNER or CHASER
        """
        pass

    @abstractmethod
    def learn(self, observed_frame, action, reward):
        """
        :param observed_frame: Frame observed
        :param action: Action taken
        :param reward: Reward got for the step.
        :return: Error rate.

        Update the Agent's knowledge based on the reward got.
        """
        pass

    # def get_angle_to_target(self, target_x, target_y):
    #     """
    #     :param target_x: Target X co-ordinate
    #     :param target_y: Target Y co-ordinate
    #     :return: Euclidean angle to th target.
    #
    #     Divide by Zero error cases are avoided.
    #     """
    #     coords = self.get_self_coords()
    #     if target_x == coords[0] and target_y > coords[1]:
    #         print('case 1 : {}'.format(-90))
    #         return -90
    #     elif target_x == coords[0] and target_y <= coords[1]:
    #         print('case 2 : {}'.format(90))
    #         return 90
    #     else:
    #         theta = math.degrees(math.atan((coords[1] - target_y) / (coords[0] - target_x)))
    #         return theta
