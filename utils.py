import numpy


def distance_btw_points(a, b):
    dist = numpy.linalg.norm(numpy.asarray(a) - numpy.asarray(b))
    return dist
