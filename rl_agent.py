import os
from abc import ABC

from keras import Sequential
from keras.layers import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Dense, Flatten, Activation
from keras.models import model_from_json
from keras.optimizers import Adam
from utils import preprocess_image

import random

from agent import Agent


class AbstractRLAgent(Agent, ABC):
    network: Sequential
    EPSILON = 25

    def __init__(self, id, environment, parent, init_x, init_y):
        super().__init__(id, environment, parent, init_x, init_y)
        self.network = None
        self.load_network()

    def learn(self, stimulus, q_values, action, reward):
        q_values[0][action] += reward
        error = self.network.train_on_batch(stimulus, q_values)
        print('{} {} got reward {} for taking action {}. Trained agent with error {}'.format(self.get_agent_type().name,
                                                                                             self.get_id(), reward,
                                                                                             action, error))

    def load_network(self, force_rebuild_network=False):
        """
        :param force_rebuild_network: Force the rebuilding of the RLAgent's network

        Loads the network into variable self.network
        """
        if force_rebuild_network:
            self.network = self.__build_network()
        else:
            if self.network is None:
                # load network from file if present else build and load network
                model_json = self.get_model_dir() + 'model.json'
                model_weights = self.get_model_dir() + 'model.h5'

                if os.path.exists(model_json) and os.path.exists(model_weights):
                    # load json and create model
                    with open(model_json, 'r') as json_file:
                        loaded_model_json = json_file.read()
                    self.network = model_from_json(loaded_model_json)
                    # load weights into new model
                    self.network.load_weights(model_weights)
                    print('Loaded {0}-{1} network from file'.format(self.get_agent_type().name, self.get_id()))
                else:
                    self.network = self.__build_network()
        optimizer = Adam(epsilon=0.3)
        self.network.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])

    def save_network(self):
        model_dir = self.get_model_dir()
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)
        nw_json = self.network.to_json()
        with open(model_dir + 'model.json', 'w') as json_file:
            json_file.write(nw_json)
        self.network.save_weights(model_dir + 'model.h5')

    def get_model_dir(self):
        return 'models/{0}/{1}/'.format(self.get_agent_type().name, self.get_id())

    def act(self, observed_frame):
        """
        Produces a random number between 0 and 100, and
        if the random number is less than EPSILON value, takes a random action
        else predict an action and take it
        """
        stimulus = preprocess_image(observed_frame)
        q_values = self.network.predict(stimulus)
        r = random.randint(0, 100)
        if r < AbstractRLAgent.EPSILON:
            print(self.get_agent_type().name, " taking random action")
            action = random.randint(0, 7)
        else:
            action = np.argmax(q_values)
        return stimulus, q_values, action

    @staticmethod
    def __build_network():
        """
        :return: RLAgent's network

        Build the network and return it. The model is able to process RGB image of size 96 x 96
        Output is 8 class directions.
        """
        model = Sequential()
        model.add(Conv2D(32, (3, 3), padding="same", input_shape=(96, 96, 3)))
        model.add(MaxPooling2D(pool_size=(3, 3)))
        model.add(Flatten())
        model.add(Dense(8))
        model.add(Activation('tanh'))
        return model
