import gym

from rl_chaser import RLChaser
from rl_runner import RLRunner

NUMBER_OF_RUNNERS = 1
NUMBER_OF_CHASERS = 1

if __name__ == '__main__':
    env = gym.make('tag-v0')
    agents = []
    chasers = []
    runners = []

    for i in range(NUMBER_OF_CHASERS):
        c = RLChaser(i, env, env.get_canvas(), 350, 100)
        chasers.append(c)

    for i in range(NUMBER_OF_RUNNERS):
        r = RLRunner(i, env, env.get_canvas(), 500, 500)
        runners.append(r)

    agents = runners + chasers

    i = 0
    j = 0

    while True:
        i += 1
        if i % 20 == 0:
            j += 1
            j %= 8

        env.render()
        observed_frame = env.observe()
        for agent in agents:
            agent.act(observed_frame)
            reward = env.get_reward_for_agent(agent)
            agent.learn(reward)

        print('Done episode #{0}'.format(i))
