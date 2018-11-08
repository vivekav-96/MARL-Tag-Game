import numpy as np

from chaser import Chaser
from rl_agent import AbstractRLAgent


class RLChaser(AbstractRLAgent, Chaser):

    def step(self, observed_frame):
        stimulus = self.preprocess_image(observed_frame)
        prediction = self.network.predict(stimulus)
        action = np.argmax(prediction)
        return action
