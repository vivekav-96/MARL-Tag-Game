import math

# import numpy
from keras_preprocessing.image import img_to_array


def distance_btw_points(a, b):
    """
    :param a: point 1
    :param b:  point 2
    :return: Euclidean distance between points a and b.
    """
    distance = math.sqrt(((a[1] - b[1]) ** 2) + ((a[0] - b[0]) ** 2))
    # distance = numpy.linalg.norm(numpy.asarray(a) - numpy.asarray(b))
    return distance


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
