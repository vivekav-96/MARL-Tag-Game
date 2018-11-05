from gym.envs.registration import register

register(
    id='tag-v0',
    entry_point='tag_environment.envs:TagEnv',
)
