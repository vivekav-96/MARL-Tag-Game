from rl_agent import AbstractRLAgent
from runner import Runner


class RLRunner(AbstractRLAgent, Runner):
    def step(self, observed_frame):
        pass

    def learn(self, reward):
        pass
