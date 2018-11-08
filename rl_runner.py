from rl_agent import AbstractRLAgent
from runner import Runner
import numpy as np


class RLRunner(AbstractRLAgent, Runner):
    def step(self, observed_frame):
        stimulus = self.preprocess_image(observed_frame)
        prediction = self.network.predict(stimulus)
        action = np.argmax(prediction)
        return action
