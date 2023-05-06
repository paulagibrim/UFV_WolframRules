# ######################################################################## #
#   Trabalho de Conclusão de Curso - Departamento de Ciência da Computação #
#               Paula Teresa Mota Gibrim - Matrícula: ES90366              #
#                                                                          #
#   File: rules.py                                                         #
# ######################################################################## #

import math

"""
    Classification:
    I   | null               | Evolution leads to a homogeneous state.
    II  | periodic or stable | Evolution leads to a set of separated simple stable or periodic structures.
    III | chaotic            | Evolution leads to a chaotic pattern.
    IV  | complex            | Evolution leads to complex localized structures, sometimes long-lived.
"""


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


# Rule 2 (stable) - < http://atlas.wolfram.com/01/01/2/01_01_1_2.html#01_01_9_2 >
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


# Rule 4 (stable) - < http://atlas.wolfram.com/01/01/4/01_01_1_4.html#01_01_164_4 >
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
    return math.fmod((1 + block[0]) * (block[1] + block[2]), 2)


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


# Rule 10 (stable) - < http://atlas.wolfram.com/01/01/10/01_01_1_10.html#01_01_164_10 >
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


# Rule 12 (stable) - < http://atlas.wolfram.com/01/01/12/01_01_1_12.html#01_01_164_12 >
def rule12(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0]) * block[1], 2)


# Rule 13 (stable) - < http://atlas.wolfram.com/01/01/13/01_01_1_13.html#01_01_164_13 >
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
    return math.fmod((1 + block[0]) * (block[1] + block[2] + block[1] * block[2]), 2)


# Rule 15 (periodic) - < http://atlas.wolfram.com/01/01/15/01_01_1_15.html#01_01_164_15 >
def rule15(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0])


# Rule 16 (stable) - < http://atlas.wolfram.com/01/01/15/01_01_1_15.html#01_01_164_15 >
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


# Rule 20 (periodic) - < http://atlas.wolfram.com/01/01/20/01_01_1_20.html#01_01_164_20 >
def rule20(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((block[0] + block[1]) * (1 + block[2]), 2)


# Rule 21 (periodic) - < http://atlas.wolfram.com/01/01/21/01_01_1_21.html#01_01_164_21 >
def rule21(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] and block[1] or block[2])


# Rule 22 (chaotic) - < http://atlas.wolfram.com/01/01/22/01_01_1_22.html#01_01_164_22 >
def rule22(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((block[0] + block[1] + block[2] + block[0] * block[1] * block[2]), 2)


# Rule 23 (periodic) - < http://atlas.wolfram.com/01/01/23/01_01_1_23.html#01_01_164_23 >
def rule23(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 24 (stable) - < http://atlas.wolfram.com/01/01/24/01_01_1_24.html#01_01_164_24 >
def rule24(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 25 (periodic) - < http://atlas.wolfram.com/01/01/25/01_01_1_25.html#01_01_164_25 >
def rule25(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 26 (periodic) - < http://atlas.wolfram.com/01/01/26/01_01_1_26.html#01_01_164_26 >
def rule26(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 27 (periodic) - < http://atlas.wolfram.com/01/01/27/01_01_1_27.html#01_01_164_27 >
def rule27(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 28 (periodic) - < http://atlas.wolfram.com/01/01/28/01_01_1_28.html#01_01_164_28 >
def rule28(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 29 (periodic) - < http://atlas.wolfram.com/01/01/29/01_01_1_29.html#01_01_164_29 >
def rule29(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[2] + block[1] * block[2], 2)


# Rule 30 (chaotic) - < http://atlas.wolfram.com/01/01/30/01_01_1_30.html#01_01_164_30 >
def rule30(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[2] + block[1] * block[2], 2)


# Rule 31 (periodic) - < http://atlas.wolfram.com/01/01/31/01_01_1_31.html#01_01_164_31 >
def rule31(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] and (block[1] or block[2]))


# Rule 32 (null) - < http://atlas.wolfram.com/01/01/32/01_01_1_32.html#01_01_164_32 >
def rule32(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and not(block[1]) and block[2]


# Rule 33 (periodic) - < http://atlas.wolfram.com/01/01/33/01_01_1_33.html#01_01_164_33 >
def rule33(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[1]) * (1 + block[0] + block[2]), 2)


# Rule 34 (static) - < http://atlas.wolfram.com/01/01/34/01_01_1_34.html#01_01_164_34 >
def rule34(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[1]) and block[2]


# Rule 35 (periodic) - < http://atlas.wolfram.com/01/01/35/01_01_1_35.html#01_01_164_35 >
def rule35(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[1]) * (1 + block[0] + block[0] * block[2]), 2)


# Rule 36 (static) - < http://atlas.wolfram.com/01/01/36/01_01_1_36.html#01_01_164_36 >
def rule36(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 37 (periodic) - < http://atlas.wolfram.com/01/01/37/01_01_1_37.html#01_01_164_37 >
def rule37(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 38 (periodic) - < http://atlas.wolfram.com/01/01/38/01_01_1_38.html#01_01_164_38 >
def rule38(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 39 (periodic) - < http://atlas.wolfram.com/01/01/39/01_01_1_39.html#01_01_164_39 >
def rule39(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 40 (null) - < http://atlas.wolfram.com/01/01/40/01_01_1_40.html#01_01_164_40 >
def rule40(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((block[0] + block[1]) * block[2], 2)


# Rule 41 (periodic) - < http://atlas.wolfram.com/01/01/41/01_01_1_41.html#01_01_164_41 >
def rule41(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 42 (static) - < http://atlas.wolfram.com/01/01/42/01_01_1_42.html#01_01_164_42 >
def rule42(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0] * block[1]) * block[2], 2)


# Rule 43 (periodic) - < http://atlas.wolfram.com/01/01/43/01_01_1_43.html#01_01_164_43 >
def rule43(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 44 (static) - < http://atlas.wolfram.com/01/01/44/01_01_1_44.html#01_01_164_44 >
def rule44(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 45 (chaotic) - < http://atlas.wolfram.com/01/01/45/01_01_1_45.html#01_01_164_45 >
def rule45(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[2] + block[1] * block[2], 2)


# Rule 46 (static) - < http://atlas.wolfram.com/01/01/46/01_01_1_46.html#01_01_164_46 >
def rule46(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[2] + block[1] * block[2], 2)


# Rule 47 (periodic) - < http://atlas.wolfram.com/01/01/47/01_01_1_47.html#01_01_164_47 >
def rule47(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0]) or not(block[1]) and block[2]


# Rule 48 (static) - < http://atlas.wolfram.com/01/01/48/01_01_1_48.html#01_01_164_48 >
def rule48(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and not(block[1])


# Rule 49 (periodic) - < http://atlas.wolfram.com/01/01/49/01_01_1_49.html#01_01_164_49 >
def rule49(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[1]) * (1 + block[2] + block[0] * block[2]), 2)
