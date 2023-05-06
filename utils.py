# ######################################################################## #
#   Trabalho de Conclusão de Curso - Departamento de Ciência da Computação #
#               Paula Teresa Mota Gibrim - Matrícula: ES90366              #
#                                                                          #
#   File: utils.py                                                       #
# ######################################################################## #
import numpy as np
from random import randint
from PIL import Image


def compose_rules(rule1, rule2, size, steps, begin=0):
    """
    This function composes two 1D cellular automata rules by applying rule1 followed by rule2 for the specified number
    of steps

    :param rule1: The first rule to apply
    :param rule2: The second rule to apply
    :param size: The size of the cellular automaton
    :param steps: The number of steps to apply the rules
    :param begin: default: 0 - 0 for random, 1 for one cell
    :return: numpy.ndarray - The final state of the cellular automaton
    """

    # Initialize the state of the cellular automaton
    state = np.zeros((steps, size), dtype=int)

    if begin == 0:
        # Define random values to the first line
        for i in range(0, size):
            state[0][i] = randint(0, 1)

    elif begin == 1:
        state[0, size//2] = 1  # Set the center cell to 1

    # Apply rule 1 followed by rule2 for the specified number of steps
    for i in range(0, steps-1):
        for j in range(size):

            left = state[i, (j - 1) % size]
            center = state[i, j]
            right = state[i, (j + 1) % size]

            block = [left, center, right]

            if i % 2 == 0:
                # Apply rule1
                state[i + 1, j] = rule1(block)
            else:
                # Apply rule2
                state[i + 1, j] = rule2(block)

    return state


def apply_rule(rule, size: int, steps: int, begin=0):
    """
    This function apply a 1D cellular automata rule for the specified number of steps

    :param rule: function, The rule to apply
    :param size: int, the size of the cellular automaton
    :param steps: int, the number of steps to apply the rules
    :param begin: default: 0 - 0 for random, 1 for one cell
    :return: numpy.ndarray, the final state of the cellular automaton
    """

    # Initialize the state of the cellular automaton
    state = np.zeros((steps, size), dtype=int)

    if begin == 0:
        # Define random values to the first line
        for i in range(0, size):
            state[0][i] = randint(0, 1)

    elif begin == 1:
        state[0, size // 2] = 1  # Set the center cell to 1

    # Apply rule for the specified number of steps
    for i in range(0, steps-1):
        for j in range(size):

            left = state[i, (j-1) % size]
            center = state[i, j]
            right = state[i, (j+1) % size]

            block = [left, center, right]

            # Apply rule
            state[i+1, j] = rule(block)

    return state


def get_image(state, size, steps):
    """
    Convert the state (array) to image
    :param state: final state of the cellular automaton
    :param size: int, the size of the cellular automaton
    :param steps: int, the number of steps to apply the rules
    :return: PIL.Image, image of the cellular automaton
    """
    arr = state.copy()

    for i in range(steps):
        for j in range(size):
            if arr[i][j] == 0:
                arr[i][j] = 255
            else:
                arr[i][j] = 1

    return Image.fromarray(arr)
