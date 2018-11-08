import gym

from agent import Actions
from chaser import Chaser
from runner import Runner

if __name__ == '__main__':
    env = gym.make('tag-v0')

    a1 = Chaser(env.get_canvas(), 350, 100)
    b1 = Runner(env.get_canvas(), 500, 500)
    i = 0
    j = 0
    actions = [Actions.NORTH,
               Actions.NORTH_EAST,
               Actions.EAST,
               Actions.SOUTH_EAST,
               Actions.SOUTH,
               Actions.SOUTH_WEST,
               Actions.WEST,
               Actions.NORTH_WEST]

    # env.render()
    # env.observe().save("{0}_{1}.png".format(i, j))

    while True:
        i += 1
        if i % 20 == 0:
            j += 1
            j %= 8
        a1.take_action(actions[j])
        env.render()
