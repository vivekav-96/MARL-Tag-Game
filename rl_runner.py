from rl_agent import AbstractRLAgent
from runner import Runner
import numpy as np
from utils import preprocess_image


class RLRunner(AbstractRLAgent, Runner):
    def act(self, observed_frame):
        stimulus = preprocess_image(observed_frame)
        q_values = self.network.predict(stimulus)
        action = np.argmax(q_values)
        return stimulus, q_values, action
