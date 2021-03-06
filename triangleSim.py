import numpy as np
import math
import argparse
import os

from utils import *
from mathUtils import *

def arg_parse():
    """
    :return: Arguments for triangle simulation
    """
    parser = argparse.ArgumentParser(description='Isosceles Triangle Simulation')
    parser.add_argument("--angle", dest="angle", help="Primary angle of the isosceles triangle",
                        default=75, type=int)
    parser.add_argument("--number", dest="N", help="Number of triangles to simulate",
                        default=30, type=int)
    return parser.parse_args()


def main():
    """
    The main operation to see a random packing
    """
    args = arg_parse()
    angle = args.angle
    N = args.N
    triangleCoordinates = generateTriangles(angle, N, 'uniform')
    drawTriangles(triangleCoordinates).show()

if __name__ == '__main__':
    main()
