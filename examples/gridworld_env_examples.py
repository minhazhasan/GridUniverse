import time

from core.envs.gridworld_env import GridWorldEnv

def run_default_gridworld():
    """
    Run a random agent on the default gridworld.
    This piece of code shows the main interface to the environment. This runs in ascii format
    """

    print('\n' + '*' * 20 + 'Starting to run random agent on default GridWorld' + '*' * 20 + '\n')
    env = GridWorldEnv()
    for i_episode in range(1):
        observation = env.reset()
        for t in range(100):
            env.render()  # set mode='graphic for pyglet render
            action = env.action_space.sample()
            print('go ' + env.action_descriptors[action])
            observation, reward, done, info = env.step(action)

            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                break

def run_gridworld_from_text_file():
    """
    Run a random agent on an environment tat was save via ascii text file.
    Check core/envs/maze_text_files for examples or the _create_custom_world_from_text() function within the environment.
    """

    print('\n' + '*' * 20 + 'Creating a pre-made GridWorld from text file and running random agent on it' + '*' * 20 + '\n')
    env = GridWorldEnv(custom_world_fp='../core/envs/maze_text_files/test_env.txt')
    # env = GridWorldEnv(custom_world_fp='../core/envs/maze_text_files/maze_21x21.txt')
    # env = GridWorldEnv(custom_world_fp='../core/envs/maze_text_files/maze_101x101.txt')
    for i_episode in range(1):
        observation = env.reset()
        for t in range(1000):
            env.render(mode='graphic')
            action = env.action_space.sample()
            # print('go ' + env.action_descriptors[action])
            # time.sleep(0.1) # uncomment to watch slower
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                break

def run_random_maze():
    """
    Run a random agent on a randomly generated maze. If random_maze parameter is set to True,
    a maze generation algorithm will place walls to form the maze in the requested shape.
    """

    print('\n' + '*' * 20 + 'Creating a random GridWorld and running random agent on it' + '*' * 20 + '\n')
    env = GridWorldEnv(grid_shape=(11, 11), random_maze=True)
    # env = GridWorldEnv(grid_shape=(101, 101), random_maze=True)
    # env = GridWorldEnv(grid_shape=(49, 51), random_maze=True)
    # env = GridWorldEnv(grid_shape=(51, 49), random_maze=True)
    # todo print to user how long is left, so they can get comfortable with how constrained random search works. Step number out of step number?
    # todo exiting shouldn't crash everything
    for i_episode in range(1):
        observation = env.reset()
        for t in range(1000):
            env.render(mode='graphic')
            env.step_num = t
            action = env.action_space.sample()
            # print('go ' + env.action_descriptors[action])
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                break

def run_lever_gridworld():
    """
    Run a random agent on a GridWorld with a lever and a doors
    """

    print('\n' + '*' * 20 + 'Starting to run specific agent on GridWorld with levers' + '*' * 20 + '\n')
    env = GridWorldEnv((7, 7), walls=[7, 8, 9], levers={3: 8})

    actions_to_take = [env.action_descriptor_to_int['RIGHT'] for i in range(4)]
    for i_episode in range(1):
        observation = env.reset()
        # for t in range(10):
        for t, action in enumerate(actions_to_take):
            # env.render(mode='graphic')  # set mode='graphic for pyglet render
            env.render()  # set mode='graphic for pyglet render
            #action = env.action_space.sample()
            print('go ' + env.action_descriptors[action])
            observation, reward, done, info = env.step(action)

            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                break

    env.close()
    # test if random agent ever opens door to terminal and then goes to terminal
    # Both very difficult for random agent to pass

    print('\n' + '*' * 20 + 'Starting to run random agent on GridWorld with levers' + '*' * 20 + '\n')
    # env = GridWorldEnv((7, 7), walls=[47, 47 - 7, 48 - 7], levers={42: 48 - 7}) # harder
    env = GridWorldEnv((7, 7), walls=[47, 47 - 7, 48 - 7], levers={42: 47}) # easier
    for i_episode in range(1):
        observation = env.reset()
        for t in range(1000000):
            #env.render()  # set mode='graphic' for pyglet render
            env.render(mode='graphic')  # set mode='graphic' for pyglet render
            action = env.action_space.sample()
            # print('go ' + env.action_descriptors[action])
            observation, reward, done, info = env.step(action)

            if done:
                env.render(mode='graphic')
                time.sleep(5)
                print("Episode finished after {} timesteps".format(t + 1))
                break

def run_lever_gridworld_from_text_file():
    # env = GridWorldEnv(custom_world_fp='../core/envs/maze_text_files/lever_level_1.txt')
    env = GridWorldEnv(custom_world_fp='../core/envs/maze_text_files/lever_level_2.txt')
    env.render()

    for i_episode in range(1):
        observation = env.reset()
        for t in range(1000000):
            #env.render()  # set mode='graphic' for pyglet render
            env.render(mode='graphic')  # set mode='graphic' for pyglet render
            action = env.action_space.sample()
            # print('go ' + env.action_descriptors[action])
            observation, reward, done, info = env.step(action)

            if done:
                env.render(mode='graphic')
                time.sleep(5)
                print("Episode finished after {} timesteps".format(t + 1))
                break

if __name__ == '__main__':
    # Run random agent on environment variations
    run_default_gridworld()
    run_gridworld_from_text_file()
    run_random_maze()
    run_lever_gridworld()
    run_lever_gridworld_from_text_file()
