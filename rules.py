# ######################################################################## #
#   Trabalho de Conclusão de Curso - Departamento de Ciência da Computação #
#               Paula Teresa Mota Gibrim - Matrícula: ES90366              #
#                                                                          #
#   File: rules.py                                                         #
# ######################################################################## #

import math

"""
    Classification:
    I   | Evolution leads to a homogeneous state.
    II  | Evolution leads to a set of separated simple stable or periodic structures.
    III | Evolution leads to a chaotic pattern.
    IV  | Evolution leads to complex localized structures, sometimes long-lived.
"""


# Rule 0 (I) - < http://atlas.wolfram.com/01/01/0/01_01_1_0.html#01_01_164_0 >
# Equivalent rules: 255
def rule0(block):
    """
    :param block: 3-size block
    :return: int (0 or 1)
    """

    return 0


# Rule 1 (II) - < http://atlas.wolfram.com/01/01/1/01_01_1_1.html#01_01_164_1 >
# Equivalent rules: 127
def rule1(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0] or block[1] or block[2])


# Rule 2 (II) - < http://atlas.wolfram.com/01/01/2/01_01_1_2.html#01_01_9_2 >
# Equivalent rules: 16, 191, 247
def rule2(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0]) and not(block[1]) and block[2]


# Rule 3 (II) - < http://atlas.wolfram.com/01/01/3/01_01_1_3.html#01_01_164_3 >
# Equivalent rules: 17, 63, 119
def rule3(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] or block[1])


# Rule 4 (II) - < http://atlas.wolfram.com/01/01/4/01_01_1_4.html#01_01_164_4 >
# Equivalent rules: 223
def rule4(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] or block[2]) and block[1]


# Rule 5 (II) - < http://atlas.wolfram.com/01/01/5/01_01_1_5.html#01_01_164_5 >
# Equivalent rules: 95
def rule5(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] or block[2])


# Rule 6 (II) - < http://atlas.wolfram.com/01/01/6/01_01_1_6.html#01_01_164_6 >
# Equivalent rules: 20, 159, 215
def rule6(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0]) * (block[1] + block[2]), 2)


# Rule 7 (II) - < http://atlas.wolfram.com/01/01/7/01_01_1_7.html#01_01_164_7 >
# Equivalent rules: 21, 31, 87
def rule7(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] or block[1] and block[2])


# Rule 8 (I) - < http://atlas.wolfram.com/01/01/8/01_01_1_8.html#01_01_164_8 >
# Equivalent rules: 64, 239, 253
def rule8(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0]) and block[1] and block[2]


# Rule 9 (II) - < http://atlas.wolfram.com/01/01/9/01_01_1_9.html#01_01_164_9 >
# Equivalent rules: 65, 111, 125
def rule9(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0]) * (1 + block[1] + block[2]), 2)


# Rule 10 (II) - < http://atlas.wolfram.com/01/01/10/01_01_1_10.html#01_01_164_10 >
# Equivalent rules: 80, 175, 245
def rule10(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0]) and block[2]


# Rule 11 (II) - < http://atlas.wolfram.com/01/01/11/01_01_1_11.html#01_01_164_11 >
# Equivalent rules: 47, 81, 117
def rule11(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0]) * (1 + block[1] + block[1] * block[2]), 2)


# Rule 12 (II) - < http://atlas.wolfram.com/01/01/12/01_01_1_12.html#01_01_164_12 >
# Equivalent rules: 68, 207, 221
def rule12(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0]) * block[1], 2)


# Rule 13 (II) - < http://atlas.wolfram.com/01/01/13/01_01_1_13.html#01_01_164_13 >
# Equivalent rules: 69, 79, 93
def rule13(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1+block[0])*(1+block[2]+block[1]*block[2]), 2)


# Rule 14 (II) - < http://atlas.wolfram.com/01/01/14/01_01_1_14.html#01_01_164_14 >
# Equivalent rules: 84, 143, 213
def rule14(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0]) * (block[1] + block[2] + block[1] * block[2]), 2)


# Rule 15 (II) - < http://atlas.wolfram.com/01/01/15/01_01_1_15.html#01_01_164_15 >
# Equivalent rules: 85
def rule15(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0])


# Rule 16 (II) - < http://atlas.wolfram.com/01/01/15/01_01_1_15.html#01_01_164_15 >
# EQUIVALENT TO RULE2
def rule16(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and not(block[1]) and not(block[2])


# Rule 17 (II) - < http://atlas.wolfram.com/01/01/17/01_01_1_17.html#01_01_164_17 >
# EQUIVALENT TO RULE3
def rule17(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[1] or block[2])


# Rule 18 (III) - < http://atlas.wolfram.com/01/01/18/01_01_1_18.html#01_01_164_18 >
# Equivalent rules: 183
def rule18(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1+block[1])*(block[0]+block[2]), 2)


# Rule 19 (II) - < http://atlas.wolfram.com/01/01/19/01_01_1_19.html#01_01_164_19 >
# Equivalent rules: 55
def rule19(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] and block[2] or block[1])


# Rule 20 (II) - < http://atlas.wolfram.com/01/01/20/01_01_1_20.html#01_01_164_20 >
# EQUIVALENT TO RULE6
def rule20(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((block[0] + block[1]) * (1 + block[2]), 2)


# Rule 21 (II) - < http://atlas.wolfram.com/01/01/21/01_01_1_21.html#01_01_164_21 >
# EQUIVALENT TO RULE7
def rule21(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] and block[1] or block[2])


# Rule 22 (III) - < http://atlas.wolfram.com/01/01/22/01_01_1_22.html#01_01_164_22 >
# Equivalent rules: 151
def rule22(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((block[0] + block[1] + block[2] + block[0] * block[1] * block[2]), 2)


# Rule 23 (II) - < http://atlas.wolfram.com/01/01/23/01_01_1_23.html#01_01_164_23 >
# Equivalent rules: NONE
def rule23(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 24 (II) - < http://atlas.wolfram.com/01/01/24/01_01_1_24.html#01_01_164_24 >
# Equivalent rules: 66, 189, 231
def rule24(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 25 (II) - < http://atlas.wolfram.com/01/01/25/01_01_1_25.html#01_01_164_25 >
# Equivalent rules: 61, 67, 103
def rule25(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 26 (II) - < http://atlas.wolfram.com/01/01/26/01_01_1_26.html#01_01_164_26 >
# Equivalent rules: 82, 167, 181
def rule26(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 27 (II) - < http://atlas.wolfram.com/01/01/27/01_01_1_27.html#01_01_164_27 >
# Equivalent rules: 39, 53, 83
def rule27(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 28 (II) - < http://atlas.wolfram.com/01/01/28/01_01_1_28.html#01_01_164_28 >
# Equivalent rules: 70, 157, 199
def rule28(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 29 (II) - < http://atlas.wolfram.com/01/01/29/01_01_1_29.html#01_01_164_29 >
# Equivalent rules: 71
def rule29(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[2] + block[1] * block[2], 2)


# Rule 30 (III) - < http://atlas.wolfram.com/01/01/30/01_01_1_30.html#01_01_164_30 >
# Equivalent rules: 86, 135, 149
def rule30(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[2] + block[1] * block[2], 2)


# Rule 31 (II) - < http://atlas.wolfram.com/01/01/31/01_01_1_31.html#01_01_164_31 >
# EQUIVALENT TO RULE7
def rule31(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] and (block[1] or block[2]))


# Rule 32 (I) - < http://atlas.wolfram.com/01/01/32/01_01_1_32.html#01_01_164_32 >
# Equivalent rules: 251
def rule32(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and not(block[1]) and block[2]


# Rule 33 (II) - < http://atlas.wolfram.com/01/01/33/01_01_1_33.html#01_01_164_33 >
# Equivalent rules: 123
def rule33(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[1]) * (1 + block[0] + block[2]), 2)


# Rule 34 (II) - < http://atlas.wolfram.com/01/01/34/01_01_1_34.html#01_01_164_34 >
# Equivalent rules: 48, 187, 243
def rule34(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[1]) and block[2]


# Rule 35 (II) - < http://atlas.wolfram.com/01/01/35/01_01_1_35.html#01_01_164_35 >
# Equivalent rules: 49, 59, 115
def rule35(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[1]) * (1 + block[0] + block[0] * block[2]), 2)


# Rule 36 (II) - < http://atlas.wolfram.com/01/01/36/01_01_1_36.html#01_01_164_36 >
# Equivalent rules: 219
def rule36(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 37 (II) - < http://atlas.wolfram.com/01/01/37/01_01_1_37.html#01_01_164_37 >
# Equivalent rules: 91
def rule37(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 38 (II) - < http://atlas.wolfram.com/01/01/38/01_01_1_38.html#01_01_164_38 >
# Equivalent rules: 52, 155, 211
def rule38(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 39 (II) - < http://atlas.wolfram.com/01/01/39/01_01_1_39.html#01_01_164_39 >
# EQUIVALENT TO RULE27
def rule39(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 40 (I) - < http://atlas.wolfram.com/01/01/40/01_01_1_40.html#01_01_164_40 >
# Equivalent rules: 96, 235, 249
def rule40(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((block[0] + block[1]) * block[2], 2)


# Rule 41 (IV) - < http://atlas.wolfram.com/01/01/41/01_01_1_41.html#01_01_164_41 >
# Equivalent rules: 97, 107, 121
def rule41(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 42 (II) - < http://atlas.wolfram.com/01/01/42/01_01_1_42.html#01_01_164_42 >
# Equivalent rules: 112, 171, 241
def rule42(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0] * block[1]) * block[2], 2)


# Rule 43 (II) - < http://atlas.wolfram.com/01/01/43/01_01_1_43.html#01_01_164_43 >
# Equivalent rules: 113
def rule43(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 44 (II) - < http://atlas.wolfram.com/01/01/44/01_01_1_44.html#01_01_164_44 >
# Equivalent rules: 100, 203, 217
def rule44(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 45 (III) - < http://atlas.wolfram.com/01/01/45/01_01_1_45.html#01_01_164_45 >
# Equivalent rules: 75, 89, 101
def rule45(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[2] + block[1] * block[2], 2)


# Rule 46 (II) - < http://atlas.wolfram.com/01/01/46/01_01_1_46.html#01_01_164_46 >
# Equivalent rules: 116, 139, 209
def rule46(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[2] + block[1] * block[2], 2)


# Rule 47 (II) - < http://atlas.wolfram.com/01/01/47/01_01_1_47.html#01_01_164_47 >
# EQUIVALENT TO RULE11
def rule47(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0]) or not(block[1]) and block[2]


# Rule 48 (II) - < http://atlas.wolfram.com/01/01/48/01_01_1_48.html#01_01_164_48 >
# EQUIVALENT TO RULE34
def rule48(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and not(block[1])


# Rule 49 (II) - < http://atlas.wolfram.com/01/01/49/01_01_1_49.html#01_01_164_49 >
# EQUIVALENT TO RULE35
def rule49(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[1]) * (1 + block[2] + block[0] * block[2]), 2)


# Rule 50 (II) - < http://atlas.wolfram.com/01/01/50/01_01_1_50.html#01_01_164_50 >
# Equivalent rules: 179
def rule50(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[1]) * (block[0] + block[2] + block[0] * block[2]), 2)


# Rule 51 (II) - < http://atlas.wolfram.com/01/01/51/01_01_1_51.html#01_01_164_51 >
# Equivalent rules: NONE
def rule51(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[1])


# Rule 52 (II) - < http://atlas.wolfram.com/01/01/52/01_01_1_52.html#01_01_164_52 >
# EQUIVALENT TO RULE38
def rule52(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 53 (II) - < http://atlas.wolfram.com/01/01/53/01_01_1_53.html#01_01_164_53 >
# EQUIVALENT TO RULE27
def rule53(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[2] + block[0] * block[2], 2)


# Rule 54 (IV) - < http://atlas.wolfram.com/01/01/54/01_01_1_54.html#01_01_164_54 >
# Equivalent rules: 147
def rule54(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[2] + block[0] * block[2], 2)


# Rule 55 (II) - < http://atlas.wolfram.com/01/01/55/01_01_1_55.html#01_01_164_55 >
# EQUIVALENT TO RULE19
def rule55(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not((block[0] or block[2]) and block[1])


# Rule 56 (II) - < http://atlas.wolfram.com/01/01/56/01_01_1_56.html#01_01_164_56 >
# Equivalent rules: 98, 185, 227
def rule56(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 57 (II) - < http://atlas.wolfram.com/01/01/57/01_01_1_57.html#01_01_164_57 >
# Equivalent rules: 99
def rule57(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[2] + block[0] * block[2], 2)


# Rule 58 (II) - < http://atlas.wolfram.com/01/01/58/01_01_1_58.html#01_01_164_58 >
# Equivalent rules: 114, 163, 177
def rule58(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[2] + block[0] * block[2], 2)


# Rule 59 (II) - < http://atlas.wolfram.com/01/01/59/01_01_1_59.html#01_01_164_59 >
# EQUIVALENT TO RULE35
def rule59(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 60 (III) - < http://atlas.wolfram.com/01/01/60/01_01_1_60.html#01_01_164_60 >
# Equivalent rules: 102, 153, 195
def rule60(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0], 2)


# Rule 61 (II) - < http://atlas.wolfram.com/01/01/61/01_01_1_61.html#01_01_164_61 >
# EQUIVALENT TO RULE25
def rule61(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[2] + block[0] * block[2] + block[1] * block[2] + block[0] *
                     block[1] * block[2], 2)


# Rule 62 (II) - < http://atlas.wolfram.com/01/01/62/01_01_1_62.html#01_01_164_62 >
# Equivalent rules: 118, 131, 145
def rule62(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[2] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 63 (II) - < http://atlas.wolfram.com/01/01/63/01_01_1_63.html#01_01_164_63 >
# EQUIVALENT TO RULE3
def rule63(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] and block[1])


# Rule 64 (I) - < http://atlas.wolfram.com/01/01/64/01_01_1_64.html#01_01_164_64 >
# EQUIVALENT TO RULE8
def rule64(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and block[1] and not(block[2])


# Rule 65 (II) - < http://atlas.wolfram.com/01/01/65/01_01_1_65.html#01_01_164_65 >
# EQUIVALENT TO RULE9
def rule65(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0] + block[1]) * (1 + block[2]), 2)


# Rule 66 (II) - < http://atlas.wolfram.com/01/01/66/01_01_1_66.html#01_01_164_66 >
# EQUIVALENT TO RULE24
def rule66(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * block[1] + block[2] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 67 (II) - < http://atlas.wolfram.com/01/01/67/01_01_1_67.html#01_01_164_67 >
# EQUIVALENT TO RULE25
def rule67(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] * block[2], 2)


# Rule 68 (II) - < http://atlas.wolfram.com/01/01/68/01_01_1_68.html#01_01_164_68 >
# EQUIVALENT TO RULE12
def rule68(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[1] and not(block[2])


# Rule 69 (II) - < http://atlas.wolfram.com/01/01/69/01_01_1_69.html#01_01_164_69 >
# EQUIVALENT TO RULE13
def rule69(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0] + block[0] * block[1]) * (1 + block[2]), 2)


# Rule 70 (II) - < http://atlas.wolfram.com/01/01/70/01_01_1_70.html#01_01_164_70 >
# EQUIVALENT TO RULE28
def rule70(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[2] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 71 (II) - < http://atlas.wolfram.com/01/01/71/01_01_1_71.html#01_01_164_71 >
# EQUIVALENT TO RULE29
def rule71(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[1] + block[1] * block[2], 2)


# Rule 72 (II) - < http://atlas.wolfram.com/01/01/72/01_01_1_72.html#01_01_164_72 >
# Equivalent rules: 237
def rule72(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] * (block[0] + block[2]), 2)


# Rule 73 (II) - < http://atlas.wolfram.com/01/01/73/01_01_1_73.html#01_01_164_73 >
# Equivalent rules: 109
def rule73(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[2] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 74 (II) - < http://atlas.wolfram.com/01/01/74/01_01_1_74.html#01_01_164_74 >
# Equivalent rules: 88, 173, 229
def rule74(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * block[1] + block[2] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 75 (III) - < http://atlas.wolfram.com/01/01/75/01_01_1_75.html#01_01_164_75 >
# EQUIVALENT TO RULE45
def rule75(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[1] * block[2], 2)


# Rule 76 (II) - < http://atlas.wolfram.com/01/01/76/01_01_1_76.html#01_01_164_76 >
# Equivalent rules: 205
def rule76(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] * (1 + block[0] * block[2]), 2)


# Rule 77 (II) - < http://atlas.wolfram.com/01/01/77/01_01_1_77.html#01_01_164_77 >
# Equivalent rules: NONE
def rule77(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[1] + block[2] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 78 (II) - < http://atlas.wolfram.com/01/01/78/01_01_1_78.html#01_01_164_78 >
# Equivalent rules: 92, 141, 197
def rule78(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[2] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 79 (II) - < http://atlas.wolfram.com/01/01/79/01_01_1_79.html#01_01_164_79 >
# EQUIVALENT TO RULE13
def rule79(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0]) or block[1] and not(block[2])


# Rule 80 (II) - < http://atlas.wolfram.com/01/01/80/01_01_1_80.html#01_01_164_80 >
# EQUIVALENT TO RULE10
def rule80(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and not(block[2])


# Rule 81 (II) - < http://atlas.wolfram.com/01/01/81/01_01_1_81.html#01_01_164_81 >
# EQUIVALENT TO RULE11
def rule81(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[1] + block[0] * block[1]) * (1 + block[2]), 2)


# Rule 82 (II) - < http://atlas.wolfram.com/01/01/82/01_01_1_82.html#01_01_164_82 >
# EQUIVALENT TO RULE26
def rule82(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 83 (II) - < http://atlas.wolfram.com/01/01/83/01_01_1_83.html#01_01_164_83 >
# EQUIVALENT TO RULE27
def rule83(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[1] + block[0] * block[2], 2)


# Rule 84 (II) - < http://atlas.wolfram.com/01/01/84/01_01_1_84.html#01_01_164_84 >
# EQUIVALENT TO RULE14
def rule84(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((block[0] + block[1] + block[0] * block[1]) * (1 + block[2]), 2)


# Rule 85 (II) - < http://atlas.wolfram.com/01/01/85/01_01_1_85.html#01_01_164_85 >
# EQUIVALENT TO RULE15
def rule85(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[2])


# Rule 86 (III) - < http://atlas.wolfram.com/01/01/86/01_01_1_86.html#01_01_164_86 >
# EQUIVALENT TO RULE30
def rule86(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[1] + block[2], 2)


# Rule 87 (II) - < http://atlas.wolfram.com/01/01/87/01_01_1_87.html#01_01_164_87 >
# EQUIVALENT TO RULE7
def rule87(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not((block[0] or block[1]) and block[2])


# Rule 88 (II) - < http://atlas.wolfram.com/01/01/88/01_01_1_88.html#01_01_164_88 >
# EQUIVALENT TO RULE74
def rule88(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 89 (III) - < http://atlas.wolfram.com/01/01/89/01_01_1_89.html#01_01_164_89 >
# EQUIVALENT TO RULE45
def rule89(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[1] + block[2], 2)


# Rule 90 (III) - < http://atlas.wolfram.com/01/01/90/01_01_1_90.html#01_01_164_90 >
# Equivalent rules: 165
def rule90(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[2], 2)


# Rule 91 (II) - < http://atlas.wolfram.com/01/01/91/01_01_1_91.html#01_01_164_91 >
# EQUIVALENT TO RULE37
def rule91(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2] + block[0] *
                     block[1] * block[2], 2)


# Rule 92 (II) - < http://atlas.wolfram.com/01/01/92/01_01_1_92.html#01_01_164_92 >
# EQUIVALENT TO RULE78
def rule92(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[1] + block[0] * block[2], 2)


# Rule 93 (II) - < http://atlas.wolfram.com/01/01/93/01_01_1_93.html#01_01_164_93 >
# EQUIVALENT TO RULE13
def rule93(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not((block[0] or not(block[1])) and block[2])


# Rule 94 (II) - < http://atlas.wolfram.com/01/01/94/01_01_1_94.html#01_01_164_94 >
# Equivalent rules: 133
def rule94(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[1] + block[2] + block[1] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 95 (II) - < http://atlas.wolfram.com/01/01/95/01_01_1_95.html#01_01_164_95 >
# EQUIVALENT TO RULE5
def rule95(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] and block[2])


# Rule 96 (I) - < http://atlas.wolfram.com/01/01/96/01_01_1_96.html#01_01_164_96 >
# EQUIVALENT TO RULE40
def rule96(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * (block[1] + block[2]), 2)


# Rule 97 (IV) - < http://atlas.wolfram.com/01/01/97/01_01_1_97.html#01_01_164_97 >
# EQUIVALENT TO RULE41
def rule97(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 98 (II) - < http://atlas.wolfram.com/01/01/98/01_01_1_98.html#01_01_164_98 >
# EQUIVALENT TO RULE56
def rule98(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * block[1] + block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 99 (II) - < http://atlas.wolfram.com/01/01/99/01_01_1_99.html#01_01_164_99 >
# EQUIVALENT TO RULE57
def rule99(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[2], 2)


# Rule 100 (II) - < http://atlas.wolfram.com/01/01/100/01_01_1_100.html#01_01_164_100 >
# EQUIVALENT TO RULE44
def rule100(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 101 (III) - < http://atlas.wolfram.com/01/01/101/01_01_1_101.html#01_01_164_101 >
# EQUIVALENT TO RULE45
def rule101(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[1] + block[2], 2)


# Rule 102 (III) - < http://atlas.wolfram.com/01/01/102/01_01_1_102.html#01_01_164_102 >
# EQUIVALENT TO RULE60
def rule102(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[2], 2)


# Rule 103 (II) - < http://atlas.wolfram.com/01/01/103/01_01_1_103.html#01_01_164_103 >
# EQUIVALENT TO RULE25
def rule103(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2] + block[0] *
                     block[1] * block[2], 2)


# Rule 104 (II) - < http://atlas.wolfram.com/01/01/104/01_01_1_104.html#01_01_164_104 >
# Equivalent rules: 233
def rule104(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * block[1] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 105 (III) - < http://atlas.wolfram.com/01/01/105/01_01_1_105.html#01_01_164_105 >
# Equivalent rules: none
def rule105(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[2], 2)


# Rule 106 (IV) - < http://atlas.wolfram.com/01/01/106/01_01_1_106.html#01_01_164_106 >
# Equivalent rules: 120, 169, 225
def rule106(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * block[1] + block[2], 2)


# Rule 107 (IV) - < http://atlas.wolfram.com/01/01/107/01_01_1_107.html#01_01_164_107 >
# EQUIVALENT TO RULE41
def rule107(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] *
                     block[2], 2)
