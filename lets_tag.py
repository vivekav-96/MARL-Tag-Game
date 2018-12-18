import os
import random
import time

import gym

from rl_chaser import RLChaser
from rl_runner import RLRunner
from tag_environment.envs import TagEnv
from tkinter.messagebox import showinfo

NUMBER_OF_RUNNERS = 1
NUMBER_OF_CHASERS = 1

debug_mode = False

if __name__ == '__main__':
    env: TagEnv = gym.make('tag-v0')
    agents = []
    chasers = []
    runners = []

    for i in range(NUMBER_OF_CHASERS):
        c = RLChaser(i, env, env.get_canvas(), random.randint(400, 500), random.randint(400, 500))
        chasers.append(c)

    for i in range(NUMBER_OF_RUNNERS):
        r = RLRunner(i + NUMBER_OF_CHASERS, env, env.get_canvas(), random.randint(400, 500), random.randint(400, 500))
        runners.append(r)

    agents = runners + chasers
    env.spawn_agents(runners, chasers)
    i = 0
    if not os.path.exists('frames'):
        os.mkdir('frames')
    while not env.is_game_end():
        i += 1
        env.render()
        observed_frame = env.observe()
        observed_frame.save('frames/observed_frame_{0}.png'.format(i))
        for agent in agents:
            stimulus, q_values, action, reward = agent.step(observed_frame)
            agent.learn(stimulus, q_values, action, reward)

        print('Done episode #{0}\n--------------------------------------------------------------------------'.format(i))
        if debug_mode:
            time.sleep(0.5)
    showinfo("ok", "Runner has been captured")
    for a in agents:
        a.save_network()
