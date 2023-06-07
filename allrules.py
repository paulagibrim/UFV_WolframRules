# ######################################################################## #
#   Trabalho de Conclusão de Curso - Departamento de Ciência da Computação #
#               Paula Teresa Mota Gibrim - Matrícula: ES90366              #
#                                                                          #
#   File: allrules.py                                                         #
# ######################################################################## #

import math

"""
    Classification:
    I   | Evolution leads to a homogeneous state.
    II  | Evolution leads to a set of separated simple stable or periodic structures.
    III | Evolution leads to a chaotic pattern.
    IV  | Evolution leads to complex localized structures, sometimes long-lived.
"""


# Rule 0 - < http://atlas.wolfram.com/01/01/0/01_01_1_0.html#01_01_164_0 >
# Equivalent rules: 255
def rule0(block):
    """
    :param block: 3-size block
    :return: int (0 or 1)
    """

    return 0


# Rule 1 - < http://atlas.wolfram.com/01/01/1/01_01_1_1.html#01_01_164_1 >
# Equivalent rules: 127
def rule1(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0] or block[1] or block[2])


# Rule 2 - < http://atlas.wolfram.com/01/01/2/01_01_1_2.html#01_01_9_2 >
# Equivalent rules: 16, 191, 247
def rule2(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0]) and not (block[1]) and block[2]


# Rule 3 - < http://atlas.wolfram.com/01/01/3/01_01_1_3.html#01_01_164_3 >
# Equivalent rules: 17, 63, 119
def rule3(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0] or block[1])


# Rule 4 - < http://atlas.wolfram.com/01/01/4/01_01_1_4.html#01_01_164_4 >
# Equivalent rules: 223
def rule4(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0] or block[2]) and block[1]


# Rule 5 - < http://atlas.wolfram.com/01/01/5/01_01_1_5.html#01_01_164_5 >
# Equivalent rules: 95
def rule5(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0] or block[2])


# Rule 6 - < http://atlas.wolfram.com/01/01/6/01_01_1_6.html#01_01_164_6 >
# Equivalent rules: 20, 159, 215
def rule6(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0]) * (block[1] + block[2]), 2)


# Rule 7 - < http://atlas.wolfram.com/01/01/7/01_01_1_7.html#01_01_164_7 >
# Equivalent rules: 21, 31, 87
def rule7(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0] or block[1] and block[2])


# Rule 8 - < http://atlas.wolfram.com/01/01/8/01_01_1_8.html#01_01_164_8 >
# Equivalent rules: 64, 239, 253
def rule8(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0]) and block[1] and block[2]


# Rule 9 - < http://atlas.wolfram.com/01/01/9/01_01_1_9.html#01_01_164_9 >
# Equivalent rules: 65, 111, 125
def rule9(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0]) * (1 + block[1] + block[2]), 2)


# Rule 10 - < http://atlas.wolfram.com/01/01/10/01_01_1_10.html#01_01_164_10 >
# Equivalent rules: 80, 175, 245
def rule10(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0]) and block[2]


# Rule 11 - < http://atlas.wolfram.com/01/01/11/01_01_1_11.html#01_01_164_11 >
# Equivalent rules: 47, 81, 117
def rule11(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0]) * (1 + block[1] + block[1] * block[2]), 2)


# Rule 12 - < http://atlas.wolfram.com/01/01/12/01_01_1_12.html#01_01_164_12 >
# Equivalent rules: 68, 207, 221
def rule12(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0]) * block[1], 2)


# Rule 13 - < http://atlas.wolfram.com/01/01/13/01_01_1_13.html#01_01_164_13 >
# Equivalent rules: 69, 79, 93
def rule13(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0]) * (1 + block[2] + block[1] * block[2]), 2)


# Rule 14 - < http://atlas.wolfram.com/01/01/14/01_01_1_14.html#01_01_164_14 >
# Equivalent rules: 84, 143, 213
def rule14(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0]) * (block[1] + block[2] + block[1] * block[2]), 2)


# Rule 15 - < http://atlas.wolfram.com/01/01/15/01_01_1_15.html#01_01_164_15 >
# Equivalent rules: 85
def rule15(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0])


# Rule 16 - < http://atlas.wolfram.com/01/01/15/01_01_1_15.html#01_01_164_15 >
# EQUIVALENT TO RULE2
def rule16(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and not (block[1]) and not (block[2])


# Rule 17 - < http://atlas.wolfram.com/01/01/17/01_01_1_17.html#01_01_164_17 >
# EQUIVALENT TO RULE3
def rule17(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[1] or block[2])


# Rule 18) - < http://atlas.wolfram.com/01/01/18/01_01_1_18.html#01_01_164_18 >
# Equivalent rules: 183
def rule18(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[1]) * (block[0] + block[2]), 2)


# Rule 19 - < http://atlas.wolfram.com/01/01/19/01_01_1_19.html#01_01_164_19 >
# Equivalent rules: 55
def rule19(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0] and block[2] or block[1])


# Rule 20 - < http://atlas.wolfram.com/01/01/20/01_01_1_20.html#01_01_164_20 >
# EQUIVALENT TO RULE6
def rule20(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((block[0] + block[1]) * (1 + block[2]), 2)


# Rule 21 - < http://atlas.wolfram.com/01/01/21/01_01_1_21.html#01_01_164_21 >
# EQUIVALENT TO RULE7
def rule21(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0] and block[1] or block[2])


# Rule 22) - < http://atlas.wolfram.com/01/01/22/01_01_1_22.html#01_01_164_22 >
# Equivalent rules: 151
def rule22(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((block[0] + block[1] + block[2] + block[0] * block[1] * block[2]), 2)


# Rule 23 - < http://atlas.wolfram.com/01/01/23/01_01_1_23.html#01_01_164_23 >
# Equivalent rules: NONE
def rule23(block):
    """
        Remember to set need_more=True
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 24 - < http://atlas.wolfram.com/01/01/24/01_01_1_24.html#01_01_164_24 >
# Equivalent rules: 66, 189, 231
def rule24(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 25 - < http://atlas.wolfram.com/01/01/25/01_01_1_25.html#01_01_164_25 >
# Equivalent rules: 61, 67, 103
def rule25(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 26 - < http://atlas.wolfram.com/01/01/26/01_01_1_26.html#01_01_164_26 >
# Equivalent rules: 82, 167, 181
def rule26(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 27 - < http://atlas.wolfram.com/01/01/27/01_01_1_27.html#01_01_164_27 >
# Equivalent rules: 39, 53, 83
def rule27(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 28 - < http://atlas.wolfram.com/01/01/28/01_01_1_28.html#01_01_164_28 >
# Equivalent rules: 70, 157, 199
def rule28(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 29 - < http://atlas.wolfram.com/01/01/29/01_01_1_29.html#01_01_164_29 >
# Equivalent rules: 71
def rule29(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[2] + block[1] * block[2], 2)


# Rule 30 - < http://atlas.wolfram.com/01/01/30/01_01_1_30.html#01_01_164_30 >
# Equivalent rules: 86, 135, 149
def rule30(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[2] + block[1] * block[2], 2)


# Rule 31 - < http://atlas.wolfram.com/01/01/31/01_01_1_31.html#01_01_164_31 >
# EQUIVALENT TO RULE7
def rule31(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0] and (block[1] or block[2]))


# Rule 32 - < http://atlas.wolfram.com/01/01/32/01_01_1_32.html#01_01_164_32 >
# Equivalent rules: 251
def rule32(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and not (block[1]) and block[2]


# Rule 33 - < http://atlas.wolfram.com/01/01/33/01_01_1_33.html#01_01_164_33 >
# Equivalent rules: 123
def rule33(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[1]) * (1 + block[0] + block[2]), 2)


# Rule 34 - < http://atlas.wolfram.com/01/01/34/01_01_1_34.html#01_01_164_34 >
# Equivalent rules: 48, 187, 243
def rule34(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[1]) and block[2]


# Rule 35 - < http://atlas.wolfram.com/01/01/35/01_01_1_35.html#01_01_164_35 >
# Equivalent rules: 49, 59, 115
def rule35(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[1]) * (1 + block[0] + block[0] * block[2]), 2)


# Rule 36 - < http://atlas.wolfram.com/01/01/36/01_01_1_36.html#01_01_164_36 >
# Equivalent rules: 219
def rule36(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 37 - < http://atlas.wolfram.com/01/01/37/01_01_1_37.html#01_01_164_37 >
# Equivalent rules: 91
def rule37(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 38 - < http://atlas.wolfram.com/01/01/38/01_01_1_38.html#01_01_164_38 >
# Equivalent rules: 52, 155, 211
def rule38(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 39 - < http://atlas.wolfram.com/01/01/39/01_01_1_39.html#01_01_164_39 >
# EQUIVALENT TO RULE27
def rule39(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 40 - < http://atlas.wolfram.com/01/01/40/01_01_1_40.html#01_01_164_40 >
# Equivalent rules: 96, 235, 249
def rule40(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((block[0] + block[1]) * block[2], 2)


# Rule 41 - < http://atlas.wolfram.com/01/01/41/01_01_1_41.html#01_01_164_41 >
# Equivalent rules: 97, 107, 121
def rule41(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 42 - < http://atlas.wolfram.com/01/01/42/01_01_1_42.html#01_01_164_42 >
# Equivalent rules: 112, 171, 241
def rule42(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0] * block[1]) * block[2], 2)


# Rule 43 - < http://atlas.wolfram.com/01/01/43/01_01_1_43.html#01_01_164_43 >
# Equivalent rules: 113
def rule43(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 44 - < http://atlas.wolfram.com/01/01/44/01_01_1_44.html#01_01_164_44 >
# Equivalent rules: 100, 203, 217
def rule44(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 45 - < http://atlas.wolfram.com/01/01/45/01_01_1_45.html#01_01_164_45 >
# Equivalent rules: 75, 89, 101
def rule45(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[2] + block[1] * block[2], 2)


# Rule 46 - < http://atlas.wolfram.com/01/01/46/01_01_1_46.html#01_01_164_46 >
# Equivalent rules: 116, 139, 209
def rule46(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[2] + block[1] * block[2], 2)


# Rule 47 - < http://atlas.wolfram.com/01/01/47/01_01_1_47.html#01_01_164_47 >
# EQUIVALENT TO RULE11
def rule47(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0]) or not (block[1]) and block[2]


# Rule 48 - < http://atlas.wolfram.com/01/01/48/01_01_1_48.html#01_01_164_48 >
# EQUIVALENT TO RULE34
def rule48(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and not (block[1])


# Rule 49 - < http://atlas.wolfram.com/01/01/49/01_01_1_49.html#01_01_164_49 >
# EQUIVALENT TO RULE35
def rule49(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[1]) * (1 + block[2] + block[0] * block[2]), 2)


# Rule 50 - < http://atlas.wolfram.com/01/01/50/01_01_1_50.html#01_01_164_50 >
# Equivalent rules: 179
def rule50(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[1]) * (block[0] + block[2] + block[0] * block[2]), 2)


# Rule 51 - < http://atlas.wolfram.com/01/01/51/01_01_1_51.html#01_01_164_51 >
# Equivalent rules: NONE
def rule51(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[1])


# Rule 52 - < http://atlas.wolfram.com/01/01/52/01_01_1_52.html#01_01_164_52 >
# EQUIVALENT TO RULE38
def rule52(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 53 - < http://atlas.wolfram.com/01/01/53/01_01_1_53.html#01_01_164_53 >
# EQUIVALENT TO RULE27
def rule53(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[2] + block[0] * block[2], 2)


# Rule 54 - < http://atlas.wolfram.com/01/01/54/01_01_1_54.html#01_01_164_54 >
# Equivalent rules: 147
def rule54(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[2] + block[0] * block[2], 2)


# Rule 55 - < http://atlas.wolfram.com/01/01/55/01_01_1_55.html#01_01_164_55 >
# EQUIVALENT TO RULE19
def rule55(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not ((block[0] or block[2]) and block[1])


# Rule 56 - < http://atlas.wolfram.com/01/01/56/01_01_1_56.html#01_01_164_56 >
# Equivalent rules: 98, 185, 227
def rule56(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 57 - < http://atlas.wolfram.com/01/01/57/01_01_1_57.html#01_01_164_57 >
# Equivalent rules: 99
def rule57(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[2] + block[0] * block[2], 2)


# Rule 58 - < http://atlas.wolfram.com/01/01/58/01_01_1_58.html#01_01_164_58 >
# Equivalent rules: 114, 163, 177
def rule58(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[2] + block[0] * block[2], 2)


# Rule 59 - < http://atlas.wolfram.com/01/01/59/01_01_1_59.html#01_01_164_59 >
# EQUIVALENT TO RULE35
def rule59(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 60 - < http://atlas.wolfram.com/01/01/60/01_01_1_60.html#01_01_164_60 >
# Equivalent rules: 102, 153, 195
def rule60(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0], 2)


# Rule 61 - < http://atlas.wolfram.com/01/01/61/01_01_1_61.html#01_01_164_61 >
# EQUIVALENT TO RULE25
def rule61(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[2] + block[0] * block[2] + block[1] * block[2] + block[0] *
                     block[1] * block[2], 2)


# Rule 62 - < http://atlas.wolfram.com/01/01/62/01_01_1_62.html#01_01_164_62 >
# Equivalent rules: 118, 131, 145
def rule62(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[2] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 63 - < http://atlas.wolfram.com/01/01/63/01_01_1_63.html#01_01_164_63 >
# EQUIVALENT TO RULE3
def rule63(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0] and block[1])


# Rule 64 - < http://atlas.wolfram.com/01/01/64/01_01_1_64.html#01_01_164_64 >
# EQUIVALENT TO RULE8
def rule64(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and block[1] and not (block[2])


# Rule 65 - < http://atlas.wolfram.com/01/01/65/01_01_1_65.html#01_01_164_65 >
# EQUIVALENT TO RULE9
def rule65(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0] + block[1]) * (1 + block[2]), 2)


# Rule 66 - < http://atlas.wolfram.com/01/01/66/01_01_1_66.html#01_01_164_66 >
# EQUIVALENT TO RULE24
def rule66(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * block[1] + block[2] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 67 - < http://atlas.wolfram.com/01/01/67/01_01_1_67.html#01_01_164_67 >
# EQUIVALENT TO RULE25
def rule67(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] * block[2], 2)


# Rule 68 - < http://atlas.wolfram.com/01/01/68/01_01_1_68.html#01_01_164_68 >
# EQUIVALENT TO RULE12
def rule68(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[1] and not (block[2])


# Rule 69 - < http://atlas.wolfram.com/01/01/69/01_01_1_69.html#01_01_164_69 >
# EQUIVALENT TO RULE13
def rule69(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0] + block[0] * block[1]) * (1 + block[2]), 2)


# Rule 70 - < http://atlas.wolfram.com/01/01/70/01_01_1_70.html#01_01_164_70 >
# EQUIVALENT TO RULE28
def rule70(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[2] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 71 - < http://atlas.wolfram.com/01/01/71/01_01_1_71.html#01_01_164_71 >
# EQUIVALENT TO RULE29
def rule71(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[1] + block[1] * block[2], 2)


# Rule 72 - < http://atlas.wolfram.com/01/01/72/01_01_1_72.html#01_01_164_72 >
# Equivalent rules: 237
def rule72(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] * (block[0] + block[2]), 2)


# Rule 73 - < http://atlas.wolfram.com/01/01/73/01_01_1_73.html#01_01_164_73 >
# Equivalent rules: 109
def rule73(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[2] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 74 - < http://atlas.wolfram.com/01/01/74/01_01_1_74.html#01_01_164_74 >
# Equivalent rules: 88, 173, 229
def rule74(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * block[1] + block[2] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 75 - < http://atlas.wolfram.com/01/01/75/01_01_1_75.html#01_01_164_75 >
# EQUIVALENT TO RULE45
def rule75(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[1] * block[2], 2)


# Rule 76 - < http://atlas.wolfram.com/01/01/76/01_01_1_76.html#01_01_164_76 >
# Equivalent rules: 205
def rule76(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] * (1 + block[0] * block[2]), 2)


# Rule 77 - < http://atlas.wolfram.com/01/01/77/01_01_1_77.html#01_01_164_77 >
# Equivalent rules: NONE
def rule77(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[1] + block[2] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 78 - < http://atlas.wolfram.com/01/01/78/01_01_1_78.html#01_01_164_78 >
# Equivalent rules: 92, 141, 197
def rule78(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[2] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 79 - < http://atlas.wolfram.com/01/01/79/01_01_1_79.html#01_01_164_79 >
# EQUIVALENT TO RULE13
def rule79(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0]) or block[1] and not (block[2])


# Rule 80 - < http://atlas.wolfram.com/01/01/80/01_01_1_80.html#01_01_164_80 >
# EQUIVALENT TO RULE10
def rule80(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and not (block[2])


# Rule 81 - < http://atlas.wolfram.com/01/01/81/01_01_1_81.html#01_01_164_81 >
# EQUIVALENT TO RULE11
def rule81(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[1] + block[0] * block[1]) * (1 + block[2]), 2)


# Rule 82 - < http://atlas.wolfram.com/01/01/82/01_01_1_82.html#01_01_164_82 >
# EQUIVALENT TO RULE26
def rule82(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 83 - < http://atlas.wolfram.com/01/01/83/01_01_1_83.html#01_01_164_83 >
# EQUIVALENT TO RULE27
def rule83(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[1] + block[0] * block[2], 2)


# Rule 84 - < http://atlas.wolfram.com/01/01/84/01_01_1_84.html#01_01_164_84 >
# EQUIVALENT TO RULE14
def rule84(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((block[0] + block[1] + block[0] * block[1]) * (1 + block[2]), 2)


# Rule 85 - < http://atlas.wolfram.com/01/01/85/01_01_1_85.html#01_01_164_85 >
# EQUIVALENT TO RULE15
def rule85(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[2])


# Rule 86 - < http://atlas.wolfram.com/01/01/86/01_01_1_86.html#01_01_164_86 >
# EQUIVALENT TO RULE30
def rule86(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[1] + block[2], 2)


# Rule 87 - < http://atlas.wolfram.com/01/01/87/01_01_1_87.html#01_01_164_87 >
# EQUIVALENT TO RULE7
def rule87(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not ((block[0] or block[1]) and block[2])


# Rule 88 - < http://atlas.wolfram.com/01/01/88/01_01_1_88.html#01_01_164_88 >
# EQUIVALENT TO RULE74
def rule88(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 89 - < http://atlas.wolfram.com/01/01/89/01_01_1_89.html#01_01_164_89 >
# EQUIVALENT TO RULE45
def rule89(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[1] + block[2], 2)


# Rule 90 - < http://atlas.wolfram.com/01/01/90/01_01_1_90.html#01_01_164_90 >
# Equivalent rules: 165
def rule90(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[2], 2)


# Rule 91 - < http://atlas.wolfram.com/01/01/91/01_01_1_91.html#01_01_164_91 >
# EQUIVALENT TO RULE37
def rule91(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2] + block[0] *
                     block[1] * block[2], 2)


# Rule 92 - < http://atlas.wolfram.com/01/01/92/01_01_1_92.html#01_01_164_92 >
# EQUIVALENT TO RULE78
def rule92(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[1] + block[0] * block[2], 2)


# Rule 93 - < http://atlas.wolfram.com/01/01/93/01_01_1_93.html#01_01_164_93 >
# EQUIVALENT TO RULE13
def rule93(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not ((block[0] or not (block[1])) and block[2])


# Rule 94 - < http://atlas.wolfram.com/01/01/94/01_01_1_94.html#01_01_164_94 >
# Equivalent rules: 133
def rule94(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[1] + block[2] + block[1] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 95 - < http://atlas.wolfram.com/01/01/95/01_01_1_95.html#01_01_164_95 >
# EQUIVALENT TO RULE5
def rule95(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not (block[0] and block[2])


# Rule 96 - < http://atlas.wolfram.com/01/01/96/01_01_1_96.html#01_01_164_96 >
# EQUIVALENT TO RULE40
def rule96(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * (block[1] + block[2]), 2)


# Rule 97 - < http://atlas.wolfram.com/01/01/97/01_01_1_97.html#01_01_164_97 >
# EQUIVALENT TO RULE41
def rule97(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 98 - < http://atlas.wolfram.com/01/01/98/01_01_1_98.html#01_01_164_98 >
# EQUIVALENT TO RULE56
def rule98(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * block[1] + block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 99 - < http://atlas.wolfram.com/01/01/99/01_01_1_99.html#01_01_164_99 >
# EQUIVALENT TO RULE57
def rule99(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[2], 2)


# Rule 100 - < http://atlas.wolfram.com/01/01/100/01_01_1_100.html#01_01_164_100 >
# EQUIVALENT TO RULE44
def rule100(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 101 - < http://atlas.wolfram.com/01/01/101/01_01_1_101.html#01_01_164_101 >
# EQUIVALENT TO RULE45
def rule101(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[1] + block[2], 2)


# Rule 102 - < http://atlas.wolfram.com/01/01/102/01_01_1_102.html#01_01_164_102 >
# EQUIVALENT TO RULE60
def rule102(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[2], 2)


# Rule 103 - < http://atlas.wolfram.com/01/01/103/01_01_1_103.html#01_01_164_103 >
# EQUIVALENT TO RULE25
def rule103(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2] + block[0] *
                     block[1] * block[2], 2)


# Rule 104 - < http://atlas.wolfram.com/01/01/104/01_01_1_104.html#01_01_164_104 >
# Equivalent rules: 233
def rule104(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * block[1] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 105 - < http://atlas.wolfram.com/01/01/105/01_01_1_105.html#01_01_164_105 >
# Equivalent rules: none
def rule105(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[2], 2)


# Rule 106 - < http://atlas.wolfram.com/01/01/106/01_01_1_106.html#01_01_164_106 >
# Equivalent rules: 120, 169, 225
def rule106(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * block[1] + block[2], 2)


# Rule 107 - < http://atlas.wolfram.com/01/01/107/01_01_1_107.html#01_01_164_107 >
# EQUIVALENT TO RULE41
def rule107(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 108 - < http://atlas.wolfram.com/01/01/108/01_01_1_108.html#01_01_164_108 >
# Equivalent rules: 201
def rule108(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[2], 2)


# Rule 109 - < http://atlas.wolfram.com/01/01/109/01_01_1_109.html#01_01_164_109 >
# EQUIVALENT TO RULE73
def rule109(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[1] + block[2] + block[1] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 110 - < http://atlas.wolfram.com/01/01/110/01_01_1_110.html#01_01_164_110 >
# Equivalent rules: 124, 137, 193
def rule110(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 111 - < http://atlas.wolfram.com/01/01/111/01_01_1_111.html#01_01_164_111 >
# EQUIVALENT TO RULE9
def rule111(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[1] + block[0] * block[2], 2)


# Rule 112 - < http://atlas.wolfram.com/01/01/112/01_01_1_112.html#01_01_164_112 >
# EQUIVALENT TO RULE42
def rule112(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * (1 + block[1] * block[2]), 2)


# Rule 113 - < http://atlas.wolfram.com/01/01/113/01_01_1_113.html#01_01_164_113 >
# EQUIVALENT TO RULE43
def rule113(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[1] + block[2] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 114 - < http://atlas.wolfram.com/01/01/114/01_01_1_114.html#01_01_164_114 >
# EQUIVALENT TO RULE58
def rule114(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[2] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 115 - < http://atlas.wolfram.com/01/01/115/01_01_1_115.html#01_01_164_115 >
# EQUIVALENT TO RULE35
def rule115(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[1] + block[0] * block[1] * block[2], 2)


# Rule 116 - < http://atlas.wolfram.com/01/01/116/01_01_1_116.html#01_01_164_116 >
# EQUIVALENT TO RULE46
def rule116(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[1] + block[1] * block[2], 2)


# Rule 117 - < http://atlas.wolfram.com/01/01/117/01_01_1_117.html#01_01_164_117 >
# EQUIVALENT TO RULE11
def rule117(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[2] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 118 - < http://atlas.wolfram.com/01/01/118/01_01_1_118.html#01_01_164_118 >
# EQUIVALENT TO RULE62
def rule118(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[1] + block[2] + block[0] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 119 - < http://atlas.wolfram.com/01/01/119/01_01_1_119.html#01_01_164_119 >
# EQUIVALENT TO RULE3
def rule119(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] * block[2], 2)


# Rule 120 - < http://atlas.wolfram.com/01/01/120/01_01_1_120.html#01_01_164_120 >
# EQUIVALENT TO RULE106
def rule120(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] * block[2], 2)


# Rule 121 - < http://atlas.wolfram.com/01/01/121/01_01_1_121.html#01_01_164_121 >
# EQUIVALENT TO RULE41
def rule121(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[1] + block[2] + block[0] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 122 - < http://atlas.wolfram.com/01/01/122/01_01_1_122.html#01_01_164_122 >
def rule122(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[2] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 123 - < http://atlas.wolfram.com/01/01/123/01_01_1_123.html#01_01_164_123 >
def rule123(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[1] + block[1] * block[2], 2)


# Rule 124 - < http://atlas.wolfram.com/01/01/124/01_01_1_124.html#01_01_164_124 >
def rule124(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[1] + block[0] * block[1] * block[2], 2)


# Rule 125 - < http://atlas.wolfram.com/01/01/125/01_01_1_125.html#01_01_164_125 >
def rule125(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[2] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 126 - < http://atlas.wolfram.com/01/01/126/01_01_1_126.html#01_01_164_126 >
def rule126(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[1] + block[2] + block[0] * block[2] + block[1] *
                     block[2], 2)


# Rule 127 - < http://atlas.wolfram.com/01/01/127/01_01_1_127.html#01_01_164_127 >
def rule127(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] * block[2], 2)


# Rule 128 - < http://atlas.wolfram.com/01/01/128/01_01_1_128.html#01_01_164_128 >
def rule128(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * block[1] * block[2], 2)


# Rule 129 - < http://atlas.wolfram.com/01/01/129/01_01_1_129.html#01_01_164_129 >
def rule129(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] + block[2] + block[0] * block[2] + block[1] *
                     block[2], 2)


# Rule 130 - < http://atlas.wolfram.com/01/01/130/01_01_1_130.html#01_01_164_130 >
def rule130(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0] + block[1]) * block[2], 2)


# Rule 131 - < http://atlas.wolfram.com/01/01/131/01_01_1_131.html#01_01_164_131 >
def rule131(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] + block[0] * block[1] * block[2], 2)


# Rule 132 - < http://atlas.wolfram.com/01/01/132/01_01_1_132.html#01_01_164_132 >
def rule132(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] * (1 + block[0] + block[2]), 2)


# Rule 133 - < http://atlas.wolfram.com/01/01/133/01_01_1_133.html#01_01_164_133 >
def rule133(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[2] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 134 - < http://atlas.wolfram.com/01/01/134/01_01_1_134.html#01_01_164_134 >
def rule134(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[2] + block[0] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 135 - < http://atlas.wolfram.com/01/01/135/01_01_1_135.html#01_01_164_135 >
def rule135(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] * block[2], 2)


# Rule 136 - < http://atlas.wolfram.com/01/01/136/01_01_1_136.html#01_01_164_136 >
def rule136(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[1] * block[2]


# Rule 137 - < http://atlas.wolfram.com/01/01/137/01_01_1_137.html#01_01_164_137 >
def rule137(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] + block[2] + block[0] * block[2] + block[0] *
                     block[1] * block[2], 2)


# Rule 138 - < http://atlas.wolfram.com/01/01/138/01_01_1_138.html#01_01_164_138 >
def rule138(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[0] + block[0] * block[1]) * block[2], 2)


# Rule 139 - < http://atlas.wolfram.com/01/01/139/01_01_1_139.html#01_01_164_139 >
def rule139(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] + block[1] * block[2], 2)


# Rule 140 - < http://atlas.wolfram.com/01/01/140/01_01_1_140.html#01_01_164_140 >
def rule140(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] * (1 + block[0] + block[1] * block[2]), 2)


# Rule 141 - < http://atlas.wolfram.com/01/01/141/01_01_1_141.html#01_01_164_141 >
def rule141(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[2] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 142 - < http://atlas.wolfram.com/01/01/142/01_01_1_142.html#01_01_164_142 >
def rule142(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[2] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 143 - < http://atlas.wolfram.com/01/01/143/01_01_1_143.html#01_01_164_143 >
def rule143(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[1] * block[2], 2)


# Rule 144 - < http://atlas.wolfram.com/01/01/144/01_01_1_144.html#01_01_164_144 >
def rule144(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * (1 + block[1] + block[2]), 2)


# Rule 145 - < http://atlas.wolfram.com/01/01/145/01_01_1_145.html#01_01_164_145 >
def rule145(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 146 - < http://atlas.wolfram.com/01/01/146/01_01_1_146.html#01_01_164_146 >
def rule146(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[2] + block[1] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 147 - < http://atlas.wolfram.com/01/01/147/01_01_1_147.html#01_01_164_147 >
def rule147(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[2], 2)


# Rule 148 - < http://atlas.wolfram.com/01/01/148/01_01_1_148.html#01_01_164_148 >
def rule148(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 149 - < http://atlas.wolfram.com/01/01/149/01_01_1_149.html#01_01_164_149 >
def rule149(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[2], 2)


# Rule 150 - < http://atlas.wolfram.com/01/01/150/01_01_1_150.html#01_01_164_150 >
def rule150(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[2], 2)


# Rule 151 - < http://atlas.wolfram.com/01/01/151/01_01_1_151.html#01_01_164_151 >
def rule151(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 152 - < http://atlas.wolfram.com/01/01/152/01_01_1_152.html#01_01_164_152 >
def rule152(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 153 - < http://atlas.wolfram.com/01/01/153/01_01_1_153.html#01_01_164_153 >
def rule153(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[2], 2)


# Rule 154 - < http://atlas.wolfram.com/01/01/154/01_01_1_154.html#01_01_164_154 >
def rule154(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[2], 2)


# Rule 155 - < http://atlas.wolfram.com/01/01/155/01_01_1_155.html#01_01_164_155 >
def rule155(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 156 - < http://atlas.wolfram.com/01/01/156/01_01_1_156.html#01_01_164_156 >
def rule156(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[2], 2)


# Rule 157 - < http://atlas.wolfram.com/01/01/157/01_01_1_157.html#01_01_164_157 >
def rule157(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] * block[0] + block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 158 - < http://atlas.wolfram.com/01/01/158/01_01_1_158.html#01_01_164_158 >
def rule158(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 159 - < http://atlas.wolfram.com/01/01/159/01_01_1_159.html#01_01_164_159 >
def rule159(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[0] * block[2], 2)


# Rule 160 - < http://atlas.wolfram.com/01/01/160/01_01_1_160.html#01_01_164_160 >
def rule160(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] * block[2]


# Rule 161 - < http://atlas.wolfram.com/01/01/161/01_01_1_161.html#01_01_164_161 >
def rule161(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] + block[2] + block[1] * block[2] + block[0] *
                     block[1] * block[2], 2)


# Rule 162 - < http://atlas.wolfram.com/01/01/162/01_01_1_162.html#01_01_164_162 >
def rule162(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod((1 + block[1] + block[0] * block[1]) * block[2], 2)


# Rule 163 - < http://atlas.wolfram.com/01/01/163/01_01_1_163.html#01_01_164_163 >
def rule163(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] + block[0] * block[2], 2)


# Rule 164 - < http://atlas.wolfram.com/01/01/164/01_01_1_164.html#01_01_164_164 >
def rule164(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] *
                     block[2], 2)


# Rule 165 - < http://atlas.wolfram.com/01/01/165/01_01_1_165.html#01_01_165_165 >
def rule165(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[2], 2)


# Rule 166 - < http://atlas.wolfram.com/01/01/166/01_01_1_166.html#01_01_166_166 >
def rule166(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[2], 2)


# Rule 167 - < http://atlas.wolfram.com/01/01/167/01_01_1_167.html#01_01_167_167 >
def rule167(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 168 - < http://atlas.wolfram.com/01/01/168/01_01_1_168.html#01_01_168_168 >
def rule168(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[2] * (block[0] + block[1] + block[0] * block[1]), 2)


# Rule 169 - < http://atlas.wolfram.com/01/01/169/01_01_1_169.html#01_01_169_169 >
def rule169(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] + block[2], 2)


# Rule 170 - < http://atlas.wolfram.com/01/01/170/01_01_1_170.html#01_01_170_170 >

def rule170(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[2]


# Rule 171 - < http://atlas.wolfram.com/01/01/171/01_01_1_171.html#01_01_171_171 >
def rule171(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] or block[1]) or block[2]


# Rule 172 - < http://atlas.wolfram.com/01/01/172/01_01_1_172.html#01_01_172_172 >
def rule172(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[0] * block[2], 2)


# Rule 173 - < http://atlas.wolfram.com/01/01/173/01_01_1_173.html#01_01_173_173 >
def rule173(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[1] + block[2], 2)


# Rule 174 - < http://atlas.wolfram.com/01/01/174/01_01_1_174.html#01_01_174_174 >
def rule174(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[1] + block[2] + block[1] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 175 - < http://atlas.wolfram.com/01/01/175/01_01_1_175.html#01_01_175_175 >
def rule175(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[2], 2)


# Rule 176 - < http://atlas.wolfram.com/01/01/176/01_01_1_176.html#01_01_176_176 >
def rule176(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * (1 + block[1] + block[1] * block[2]), 2)


# Rule 177 - < http://atlas.wolfram.com/01/01/177/01_01_1_177.html#01_01_177_177 >
def rule177(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[2] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 178 - < http://atlas.wolfram.com/01/01/178/01_01_1_178.html#01_01_178_178 >
def rule178(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[2] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 179 - < http://atlas.wolfram.com/01/01/179/01_01_1_179.html#01_01_179_179 >
def rule179(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[1] * block[2], 2)


# Rule 180 - < http://atlas.wolfram.com/01/01/180/01_01_1_180.html#01_01_180_180 >
def rule180(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[1] * block[2], 2)


# Rule 181 - < http://atlas.wolfram.com/01/01/181/01_01_1_181.html#01_01_181_181 >
def rule181(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[2] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 182 - < http://atlas.wolfram.com/01/01/182/01_01_1_182.html#01_01_182_182 >
def rule182(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[2] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 183 - < http://atlas.wolfram.com/01/01/183/01_01_1_183.html#01_01_183_183 >
def rule183(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[1] * block[2], 2)


# Rule 184 - < http://atlas.wolfram.com/01/01/184/01_01_1_184.html#01_01_184_184 >
def rule184(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[1] * block[2], 2)


# Rule 185 - < http://atlas.wolfram.com/01/01/185/01_01_1_185.html#01_01_185_185 >
def rule185(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[2] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 186 - < http://atlas.wolfram.com/01/01/186/01_01_1_186.html#01_01_186_186 >
def rule186(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[1] + block[2] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 187 - < http://atlas.wolfram.com/01/01/187/01_01_1_187.html#01_01_187_187 >
def rule187(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[1] * block[2], 2)


# Rule 188 - < http://atlas.wolfram.com/01/01/188/01_01_1_188.html#01_01_188_188 >
def rule188(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[1] * block[2], 2)


# Rule 189 - < http://atlas.wolfram.com/01/01/189/01_01_1_189.html#01_01_189_189 >
def rule189(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[1] + block[2] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 190 - < http://atlas.wolfram.com/01/01/190/01_01_1_190.html#01_01_190_190 >
def rule190(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] ^ block[1] or block[2]


# Rule 191 - < http://atlas.wolfram.com/01/01/191/01_01_1_191.html#01_01_191_191 >
def rule191(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0]) or not(block[1]) or block[2]


# Rule 192 - < http://atlas.wolfram.com/01/01/192/01_01_1_192.html#01_01_192_192 >
def rule192(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and block[1]


# Rule 193 - < http://atlas.wolfram.com/01/01/193/01_01_1_193.html#01_01_193_193 >
def rule193(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] ^ (block[0] or block[1] or not(block[2])) ^ block[1]


# Rule 194 - < http://atlas.wolfram.com/01/01/194/01_01_1_194.html#01_01_194_194 >
def rule194(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] ^ (block[0] or block[1] or block[2]) ^ block[1]


# Rule 195 - < http://atlas.wolfram.com/01/01/195/01_01_1_195.html#01_01_195_195 >
def rule195(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] ^ (not(block[1]))


# Rule 196 - < http://atlas.wolfram.com/01/01/196/01_01_1_196.html#01_01_196_196 >
def rule196(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return (block[0] or not(block[2])) and block[1]


# Rule 197 - < http://atlas.wolfram.com/01/01/197/01_01_1_197.html#01_01_197_197 >
def rule197(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] or block[1] ^ block[2]) ^ block[1]


# Rule 198 - < http://atlas.wolfram.com/01/01/198/01_01_1_198.html#01_01_198_198 >
def rule198(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[2] + block[0] * block[2], 2)


# Rule 199 - < http://atlas.wolfram.com/01/01/199/01_01_1_199.html#01_01_199_199 >
def rule199(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] ^ (block[0] or not(block[1]) or block[2]) ^ block[1]


# Rule 200 - < http://atlas.wolfram.com/01/01/200/01_01_1_200.html#01_01_200_200 >
def rule200(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return (block[0] or block[2]) and block[1]


# Rule 201 - < http://atlas.wolfram.com/01/01/201/01_01_1_201.html#01_01_201_201 >
def rule201(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] or block[2]) ^ block[1]


# Rule 202 - < http://atlas.wolfram.com/01/01/202/01_01_1_202.html#01_01_202_202 >
def rule202(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * block[1] + block[2] + block[0] * block[2], 2)


# Rule 203 - < http://atlas.wolfram.com/01/01/203/01_01_1_203.html#01_01_203_203 >
def rule203(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] ^ (not (block[1])) or block[1] and block[2]


# Rule 204 - < http://atlas.wolfram.com/01/01/204/01_01_1_204.html#01_01_204_204 >
def rule204(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[1]


# Rule 205 - < http://atlas.wolfram.com/01/01/205/01_01_1_205.html#01_01_205_205 >
def rule205(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] or block[2]) or block[1]


# Rule 206 - < http://atlas.wolfram.com/01/01/206/01_01_1_206.html#01_01_206_206 >
def rule206(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0]) and block[2] or block[1]


# Rule 207 - < http://atlas.wolfram.com/01/01/207/01_01_1_207.html#01_01_207_207 >
def rule207(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] and not(block[1]))


# Rule 208 - < http://atlas.wolfram.com/01/01/208/01_01_1_208.html#01_01_208_208 >
def rule208(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and (block[1] or not(block[2]))


# Rule 209 - < http://atlas.wolfram.com/01/01/209/01_01_1_209.html#01_01_209_209 >
def rule209(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not((block[0] and block[1]) ^ (block[1] or block[2]))


# Rule 210 - < http://atlas.wolfram.com/01/01/210/01_01_1_210.html#01_01_210_210 >
def rule210(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] ^ (block[1] and block[2]) ^ block[2]


# Rule 211 - < http://atlas.wolfram.com/01/01/211/01_01_1_211.html#01_01_211_211 >
def rule211(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] ^ (not(block[0]) or block[1] or block[2]) ^ block[1]


# Rule 212 - < http://atlas.wolfram.com/01/01/212/01_01_1_212.html#01_01_212_212 >
def rule212(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return (block[0] ^ block[1] or block[0] ^ block[2]) ^ block[2]


# Rule 213 - < http://atlas.wolfram.com/01/01/213/01_01_1_213.html#01_01_213_213 >
def rule213(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and block[1] or not(block[2])


# Rule 214 - < http://atlas.wolfram.com/01/01/214/01_01_1_214.html#01_01_214_214 >
def rule214(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and block[1] or block[0] ^ block[1] ^ block[2]


# Rule 215 - < http://atlas.wolfram.com/01/01/215/01_01_1_215.html#01_01_215_215 >
def rule215(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] * block[2] + block[1] * block[2], 2)


# Rule 216 - < http://atlas.wolfram.com/01/01/216/01_01_1_216.html#01_01_216_216 >
def rule216(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 217 - < http://atlas.wolfram.com/01/01/217/01_01_1_217.html#01_01_217_217 >
def rule217(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 218 - < http://atlas.wolfram.com/01/01/218/01_01_1_218.html#01_01_218_218 >
def rule218(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] ^ (block[0] and block[1] and block[2]) ^ block[2]


# Rule 219 - < http://atlas.wolfram.com/01/01/219/01_01_1_219.html#01_01_219_219 >
def rule219(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[1] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 220 - < http://atlas.wolfram.com/01/01/220/01_01_1_220.html#01_01_220_220 >
def rule220(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and not(block[2]) or block[1]


# Rule 221 - < http://atlas.wolfram.com/01/01/221/01_01_1_221.html#01_01_221_221 >
def rule221(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[1] or not(block[2])


# Rule 222 - < http://atlas.wolfram.com/01/01/222/01_01_1_222.html#01_01_222_222 >
def rule222(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] + block[1] + block[0] * block[1] + block[2] + block[1] * block[2], 2)


# Rule 223 - < http://atlas.wolfram.com/01/01/223/01_01_1_223.html#01_01_223_223 >
def rule223(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0] and not(block[1]) and block[2])


# Rule 224 - < http://atlas.wolfram.com/01/01/224/01_01_1_224.html#01_01_224_224 >
def rule224(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and (block[1] or block[2])


# Rule 225 - < http://atlas.wolfram.com/01/01/225/01_01_1_225.html#01_01_225_225 >
def rule225(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[2] + block[1] * block[2], 2)


# Rule 226 - < http://atlas.wolfram.com/01/01/226/01_01_1_226.html#01_01_226_226 >
def rule226(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * block[1] + block[2] + block[1] * block[2], 2)


# Rule 227 - < http://atlas.wolfram.com/01/01/227/01_01_1_227.html#01_01_227_227 >
def rule227(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[2] + block[0] * block[1] * block[2], 2)


# Rule 228 - < http://atlas.wolfram.com/01/01/228/01_01_1_228.html#01_01_228_228 >
def rule228(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 229 - < http://atlas.wolfram.com/01/01/229/01_01_1_229.html#01_01_229_229 >
def rule229(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 230 - < http://atlas.wolfram.com/01/01/230/01_01_1_230.html#01_01_230_230 >
def rule230(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 231 - < http://atlas.wolfram.com/01/01/231/01_01_1_231.html#01_01_231_231 >
def rule231(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 232 - < http://atlas.wolfram.com/01/01/232/01_01_1_232.html#01_01_232_232 >
def rule232(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 233 - < http://atlas.wolfram.com/01/01/233/01_01_1_233.html#01_01_233_233 >
def rule233(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 234 - < http://atlas.wolfram.com/01/01/234/01_01_1_234.html#01_01_234_234 >
def rule234(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(block[0] * block[1] + block[2] + block[0] * block[1] * block[2], 2)


# Rule 235 - < http://atlas.wolfram.com/01/01/235/01_01_1_235.html#01_01_235_235 >
def rule235(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[1] + block[0] * block[2] + block[1] * block[2], 2)


# Rule 236 - < http://atlas.wolfram.com/01/01/236/01_01_1_236.html#01_01_236_236 >
def rule236(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] and block[2] or block[1]


# Rule 237 - < http://atlas.wolfram.com/01/01/237/01_01_1_237.html#01_01_237_237 >
def rule237(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return math.fmod(1 + block[0] + block[0] * block[1] + block[2] + block[1] * block[2], 2)


# Rule 238 - < http://atlas.wolfram.com/01/01/238/01_01_1_238.html#01_01_238_238 >
def rule238(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[1] or block[2]


# Rule 239 - < http://atlas.wolfram.com/01/01/239/01_01_1_239.html#01_01_239_239 >
def rule239(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return not(block[0]) or block[1] or block[2]


# Rule 240 - < http://atlas.wolfram.com/01/01/240/01_01_1_240.html#01_01_240_240 >
def rule240(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0]


# Rule 241 - < http://atlas.wolfram.com/01/01/241/01_01_1_241.html#01_01_241_241 >
def rule241(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] or not(block[1] or block[2])


# Rule 242 - < http://atlas.wolfram.com/01/01/242/01_01_1_242.html#01_01_242_242 >
def rule242(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] or not(block[1]) and block[2]


# Rule 243 - < http://atlas.wolfram.com/01/01/243/01_01_1_243.html#01_01_243_243 >
def rule243(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] or not(block[1])


# Rule 244 - < http://atlas.wolfram.com/01/01/244/01_01_1_244.html#01_01_244_244 >
def rule244(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] or block[1] and not(block[2])


# Rule 245 - < http://atlas.wolfram.com/01/01/245/01_01_1_245.html#01_01_245_245 >
def rule245(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] or not(block[2])


# Rule 246 - < http://atlas.wolfram.com/01/01/246/01_01_1_246.html#01_01_246_246 >
def rule246(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] or block[1] ^ block[2]


# Rule 247 - < http://atlas.wolfram.com/01/01/247/01_01_1_247.html#01_01_247_247 >
def rule247(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] or not(block[1]) or not (block[2])


# Rule 248 - < http://atlas.wolfram.com/01/01/248/01_01_1_248.html#01_01_248_248 >
def rule248(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] or block[1] and block[2]


# Rule 249 - < http://atlas.wolfram.com/01/01/249/01_01_1_249.html#01_01_249_249 >
def rule249(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] or block[1] ^ (not(block[2]))


# Rule 250 - < http://atlas.wolfram.com/01/01/250/01_01_1_250.html#01_01_250_250 >
def rule250(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] or block[2]


# Rule 251 - < http://atlas.wolfram.com/01/01/251/01_01_1_251.html#01_01_251_251 >
def rule251(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] or not(block[1]) or block[2]


# Rule 252 - < http://atlas.wolfram.com/01/01/252/01_01_1_252.html#01_01_252_252 >
def rule252(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] or block[1]


# Rule 253 - < http://atlas.wolfram.com/01/01/253/01_01_1_253.html#01_01_253_253 >
def rule253(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] or block[1] or not(block[2])


# Rule 254 - < http://atlas.wolfram.com/01/01/254/01_01_1_254.html#01_01_254_254 >
def rule254(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return block[0] or block[1] or block[2]


# Rule 255 - < http://atlas.wolfram.com/01/01/255/01_01_1_255.html#01_01_255_255 >
def rule255(block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return 1
