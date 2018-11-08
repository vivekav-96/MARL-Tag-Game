import gym

from agent import Actions
from chaser import Chaser
from runner import Runner

NUMBER_OF_RUNNERS = 1
NUMBER_OF_CHASERS = 1

actions = [Actions.NORTH,
           Actions.NORTH_EAST,
           Actions.EAST,
           Actions.SOUTH_EAST,
           Actions.SOUTH,
           Actions.SOUTH_WEST,
           Actions.WEST,
           Actions.NORTH_WEST]


def step_agents(agents):
    for a in agents:
        a.step()


if __name__ == '__main__':
    env = gym.make('tag-v0')
    agents = []
    chasers = []
    runners = []

    for i in range(NUMBER_OF_CHASERS):
        c = Chaser(i, env, env.get_canvas(), 350, 100)
        chasers.append(c)

    for i in range(NUMBER_OF_RUNNERS):
        r = Runner(i, env, env.get_canvas(), 500, 500)
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
        for a in agents:
            a.step(observed_frame)
        print('Done episode #{0}'.format(i))
