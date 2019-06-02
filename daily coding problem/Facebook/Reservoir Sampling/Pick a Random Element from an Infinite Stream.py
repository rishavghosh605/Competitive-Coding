'''
This problem was asked by Facebook.

Given a stream of elements too large to store in memory,
pick a random element from the stream with uniform probability.
'''
import random

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if i == 0:
            random_element = e
        elif random.randint(1, i + 1) == 1:
            random_element = e
    return random_element
# Note:Return random integer in range [a, b], including both end points.
# Since we are only storing a single variable, this only takes up constant space!
# Turns out this algorithm is called Reservoir Sampling.
