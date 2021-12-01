# generate random integer values
from random import seed
from random import randint
import sys


def gen_random_array(input_size_r,seed_val):
    """
    The function helps generate an array of randomly generated integers.
    :param input_size_r: The size of input array.
    :return: An array of integers of given input size.
    """
    # generate some integers
    seed(seed_val)
    values = [randint(1, sys.maxsize) for _ in range(input_size_r)]
    #values = [randint(1, 500) for _ in range(input_size_r)]
    #values = [randint(1, input_size_r) for _ in range(input_size_r)]
    return values
