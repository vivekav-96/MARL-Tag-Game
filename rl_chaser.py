import numpy as np

from chaser import Chaser
from rl_agent import AbstractRLAgent
from utils import preprocess_image


class RLChaser(AbstractRLAgent, Chaser):

    def act(self, observed_frame):
        stimulus = preprocess_image(observed_frame)
        prediction = self.network.predict(stimulus)
        action = np.argmax(prediction)
        return stimulus, action
