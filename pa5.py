#!/usr/bin/env python3

import math

def gcd(a, b):
    '''The gcd of two integers using Euclid's algorithm.'''
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


def remove_pairs(path):
    '''Remove turnaround pairs from a string.'''
    if len(path) < 2:
        return path
    
    if path[0] == opposite_direction(path[1]):
        return remove_pairs(path[2:])
    else:
        return path[0] + remove_pairs(path[1:])


def opposite_direction(direction):
    '''Get the opposite direction for a given direction.'''
    if direction == 'N':
        return 'S'
    elif direction == 'E':
        return 'W'
    elif direction == 'S':
        return 'N'
    elif direction == 'W':
        return 'E'


def bisection_root(func, x1, x2):
    '''Root of a function using the bisection method.'''

    y1 = func(x1)
    y2 = func(x2)

    if y1 * y2 > 0:
        raise ValueError("Initial guesses do not bracket the root")

    while abs(x1 - x2) > 0.001:
        x_mid = (x1 + x2) / 2
        y_mid = func(x_mid)

        if abs(y_mid) < 0.001:
            return x_mid

        if y1 * y_mid < 0:
            x2 = x_mid
            y2 = y_mid
        else:
            x1 = x_mid
            y1 = y_mid

    raise ValueError("Failed to find a root within the tolerance")

root = bisection_root(math.sin, 2, 4)
print(root)  

