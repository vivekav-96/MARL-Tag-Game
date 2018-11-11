from rl_agent import AbstractRLAgent
from runner import Runner
import numpy as np
from utils import preprocess_image


class RLRunner(AbstractRLAgent, Runner):
    def act(self, observed_frame):
        stimulus = preprocess_image(observed_frame)
        prediction = self.network.predict(stimulus)
        action = np.argmax(prediction)
        return stimulus, action
