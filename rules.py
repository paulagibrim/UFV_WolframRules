# ######################################################################## #
#   Trabalho de Conclusão de Curso - Departamento de Ciência da Computação #
#               Paula Teresa Mota Gibrim - Matrícula: ES90366              #
#                                                                          #
#   File: rules.py                                                         #
# ######################################################################## #

import math


# Rule 0 (null) - < http://atlas.wolfram.com/01/01/0/01_01_1_0.html#01_01_164_0 >
def rule0(block):
    """
    :param block: 3-size block
    :return: int (0 or 1)
    """
    return 0


# Rule 1 (periodic) - < http://atlas.wolfram.com/01/01/1/01_01_1_1.html#01_01_164_1 >
def rule1(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0] or block[1] or block[2])


# Rule 2 (fixed point) - < http://atlas.wolfram.com/01/01/2/01_01_1_2.html#01_01_9_2 >
def rule2(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0]) and not(block[1]) and block[2]


# Rule 3 (periodic) - < http://atlas.wolfram.com/01/01/3/01_01_1_3.html#01_01_164_3 >
def rule3(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] or block[1])


# Rule 4 (fixed point) - < http://atlas.wolfram.com/01/01/4/01_01_1_4.html#01_01_164_4 >
def rule4(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] or block[2]) and block[1]


# Rule 5 (periodic) - < http://atlas.wolfram.com/01/01/5/01_01_1_5.html#01_01_164_5 >
def rule5(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] or block[2])


# Rule 6 (periodic) - < http://atlas.wolfram.com/01/01/6/01_01_1_6.html#01_01_164_6 >
def rule6(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1+block[0])*(block[1]+block[2]),2)


# Rule 7 (periodic) - < http://atlas.wolfram.com/01/01/7/01_01_1_7.html#01_01_164_7 >
def rule7(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] or block[1] and block[2])


# Rule 8 (null) - < http://atlas.wolfram.com/01/01/8/01_01_1_8.html#01_01_164_8 >
def rule8(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0]) and block[1] and block[2]


# Rule 9 (periodic) - < http://atlas.wolfram.com/01/01/9/01_01_1_9.html#01_01_164_9 >
def rule9(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0]) * (1 + block[1] + block[2]), 2)


# Rule 10 (fixed point) - < http://atlas.wolfram.com/01/01/10/01_01_1_10.html#01_01_164_10 >
def rule10(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0]) and block[2]


# Rule 11 (periodic) - < http://atlas.wolfram.com/01/01/11/01_01_1_11.html#01_01_164_11 >
def rule11(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0]) * (1 + block[1] + block[1] * block[2]), 2)


# Rule 12 (fixed point) - < http://atlas.wolfram.com/01/01/12/01_01_1_12.html#01_01_164_12 >
def rule12(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0]) * block[1], 2)


# Rule 13 (fixed point) - < http://atlas.wolfram.com/01/01/13/01_01_1_13.html#01_01_164_13 >
def rule13(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1+block[0])*(1+block[2]+block[1]*block[2]), 2)


# Rule 14 (periodic) - < http://atlas.wolfram.com/01/01/14/01_01_1_14.html#01_01_164_14 >
def rule14(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1+block[0])*(block[1]+block[2]+block[1]*block[2]),2)


# Rule 15 (periodic) - < http://atlas.wolfram.com/01/01/15/01_01_1_15.html#01_01_164_15 >
def rule15(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0])


# Rule 16 (fixed point) - < http://atlas.wolfram.com/01/01/15/01_01_1_15.html#01_01_164_15 >
def rule16(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and not(block[1]) and not(block[2])


# Rule 17 (periodic) - < http://atlas.wolfram.com/01/01/17/01_01_1_17.html#01_01_164_17 >
def rule17(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[1] or block[2])


# Rule 18 (chaotic) - < http://atlas.wolfram.com/01/01/18/01_01_1_18.html#01_01_164_18 >
def rule18(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1+block[1])*(block[0]+block[2]), 2)


# Rule 19 (periodic) - < http://atlas.wolfram.com/01/01/19/01_01_1_19.html#01_01_164_19 >
def rule19(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] and block[2] or block[1])


