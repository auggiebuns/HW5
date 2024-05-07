#!/usr/bin/env python3
'''pa5 functions for homework 5'''

import math


def gcd(integer1, integer2):
    '''The gcd of two integers using Euclid's algorithm.'''
    if integer2 > integer1:
        integer1, integer2 = integer2, integer1
    if integer2 == 0:
        return integer1
    return gcd(integer2, integer1 % integer2)


def remove_pairs(path):
    '''Remove turnaround pairs from a string.'''
    if len(path) < 2:
        return path
    if path[0] == opposite_direction(path[1]):
        return remove_pairs(path[2:])
    return path[0] + remove_pairs(path[1:])


def opposite_direction(direction):
    '''Get the opposite direction for a given direction.'''
    if direction == 'N':
        return 'S'
    if direction == 'E':
        return 'W'
    if direction == 'S':
        return 'N'
    if direction == 'W':
        return 'E'


def bisection_root(func, variable1, variable2):
    '''Root of a function using the bisection method.'''
    try:
        y_pred1 = func(variable1)
        y_pred2 = func(variable2)

        if y_pred1 * y_pred2 > 0:
            raise ValueError("Initial guesses do not bracket the root")
        while abs(variable1 - variable2) > 0.001:
            x_mid = (variable1 + variable2) / 2
            y_mid = func(x_mid)

            if abs(y_mid) < 0.001:
                return x_mid

            if y_pred1 * y_mid < 0:
                variable2 = x_mid
                y_pred2 = y_mid
            else:
                variable1 = x_mid
                y_pred1 = y_mid
        raise ValueError("Failed to find a root within the tolerance")
    except ValueError as e:
        print("Warning:", e)
        raise


ROOT = bisection_root(math.sin, 2, 4)
print(ROOT)
