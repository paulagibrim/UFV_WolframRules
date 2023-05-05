# ######################################################################## #
#   Trabalho de Conclusão de Curso - Departamento de Ciência da Computação #
#               Paula Teresa Mota Gibrim - Matrícula: ES90366              #
#                                                                          #
#   File: utils.py                                                       #
# ######################################################################## #
import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image, ImageDraw


def compose_rules(rule1, rule2, size, steps):
    """
        This function composes two 1D cellular automata rules by applying rule1 followed by rule2 for the specified
        number of steps

        @args:
        rule1   (function)  : The first rule to apply
        rule2   (function)  : The second rule to apply
        size    (int)       : The size of the cellular automaton
        steps   (int)       : The number of steps to apply the rules

        @return:
        numpy.ndarray       : The final state of the cellular automaton

    """
    # Initialize the state of the cellular automaton
    state = np.zeros((steps, size), dtype=int)
    state[0, size//2] = 1  # Set the center cell to 1

    # Apply rule 1 followed by rule2 for the specified number of steps
    for i in range(0, steps):
        for j in range(size):

            left = state[i, (j-1) % size]
            center = state[i, j]
            right = state[i, (j+1) % size]

            block = [left, center, right]

            # Apply rule1
            state[i, j] = rule1(block)

            # Apply rule2
            state[i, j] = rule2(block)

    return state


def apply_rule(rule, size: int, steps: int, need_more=False):
    """
        This function apply a 1D cellular automata rule for the specified number of steps

        Parameters
        ----------
            rule : function, The rule to apply
            size : int, the size of the cellular automaton
            steps : int, the number of steps to apply the rules

        Returns
        -------
            numpy.ndarray : the final state of the cellular automaton

    """
    # Initialize the state of the cellular automaton
    state = np.zeros((steps, size), dtype=int)
    state[0, size//2+1] = 1  # Set the center cell to 1

    if need_more:
        state[0, size // 2 + 2] = 1  # Set the right cell to 1

    # Apply rule for the specified number of steps
    for i in range(0, steps-1):
        for j in range(size):

            left = state[i, (j-1) % size]
            center = state[i, j]
            right = state[i, (j+1) % size]

            block = [left, center, right]

            # Apply rule
            state[i+1, j] = rule(block)
    #
    # for i in range(steps):
    #     print(''.join('X' if x == 1 else '.' for x in state[i]))
    return state


def get_image(arr_orig, size, steps):
    arr = arr_orig.copy()

    for i in range(steps):
        for j in range(size):
            if arr[i][j] == 0:
                arr[i][j] = 255
            else:
                arr[i][j] = 1

    return Image.fromarray(arr)
