from abc import ABC

from keras import Sequential
from keras.layers import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Dense, Flatten
from keras.preprocessing.image import img_to_array

from agent import Agent


class AbstractRLAgent(Agent, ABC):

    def __init__(self, id, environment, parent, init_x, init_y):
        super().__init__(id, environment, parent, init_x, init_y)
        self.network = None
        self.load_network(force_rebuild_network=True)

    def learn(self, observed_frame, action, reward):
        print('Agent {0} got reward {1} for performing action {2}'.format(self.get_id(), reward, action))

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
                self.network = self.__build_network()

    def train_network(self):
        pass

    def save_network(self):
        pass

    def __build_network(self):
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
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        self.save_network()

        return model

    @staticmethod
    def preprocess_image(observed_frame):
        """
        :param observed_frame: pass the observed_frame, a Pillow image as argument
        :return: return the image as array of shape (1, 96, 96, 3)

        Resize the image into dimensions 96 x 96
        Convert the image into array with keras image processing
        Reshape the array to shape (1, 96, 96, 3)
        """
        img = observed_frame.resize((96, 96))
        arr = img_to_array(img)
        arr = arr.reshape((1,) + arr.shape)
        return arr
