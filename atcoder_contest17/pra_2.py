import numpy
import itertools

def main(x1, y1, x2, y2, x3, y3):
    u = numpy.array([x2 - x1, y2 - y1])
    v = numpy.array([x3 - x1, y3 - y1])
    L = abs(numpy.cross(u, v) / numpy.linalg.norm(u))
    return L

print(main(0,0,100,100,100,100))