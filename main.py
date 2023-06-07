# ######################################################################## #
#  Trabalho de Conclusão de Curso - Departamento de Ciência da Computação  #
#               Paula Teresa Mota Gibrim - Matrícula: ES90366              #
#                                                                          #
#   File: main.py                                                          #
# ######################################################################## #

import allrules as rl
import utils

# Vetor com todas as regras, onde rules[0] corresponde à função da regra 0, assim por diante.
rules = [
    rl.rule0, rl.rule1, rl.rule2, rl.rule3, rl.rule4, rl.rule5, rl.rule6, rl.rule7,
    rl.rule8, rl.rule9, rl.rule10, rl.rule11, rl.rule12, rl.rule13, rl.rule14, rl.rule15,
    rl.rule16, rl.rule17, rl.rule18, rl.rule19, rl.rule20, rl.rule21, rl.rule22, rl.rule23,
    rl.rule24, rl.rule25, rl.rule26, rl.rule27, rl.rule28, rl.rule29, rl.rule30, rl.rule31,
    rl.rule32, rl.rule33, rl.rule34, rl.rule35, rl.rule36, rl.rule37, rl.rule38, rl.rule39,
    rl.rule40, rl.rule41, rl.rule42, rl.rule43, rl.rule44, rl.rule45, rl.rule46, rl.rule47,
    rl.rule48, rl.rule49, rl.rule50, rl.rule51, rl.rule52, rl.rule53, rl.rule54, rl.rule55,
    rl.rule56, rl.rule57, rl.rule58, rl.rule59, rl.rule60, rl.rule61, rl.rule62, rl.rule63,
    rl.rule64, rl.rule65, rl.rule66, rl.rule67, rl.rule68, rl.rule69, rl.rule70, rl.rule71,
    rl.rule72, rl.rule73, rl.rule74, rl.rule75, rl.rule76, rl.rule77, rl.rule78, rl.rule79,
    rl.rule80, rl.rule81, rl.rule82, rl.rule83, rl.rule84, rl.rule85, rl.rule86, rl.rule87,
    rl.rule88, rl.rule89, rl.rule90, rl.rule91, rl.rule92, rl.rule93, rl.rule94, rl.rule95,
    rl.rule96, rl.rule97, rl.rule98, rl.rule99, rl.rule100, rl.rule101, rl.rule102, rl.rule103,
    rl.rule104, rl.rule105, rl.rule106, rl.rule107, rl.rule108, rl.rule109, rl.rule110, rl.rule111,
    rl.rule112, rl.rule113, rl.rule114, rl.rule115, rl.rule116, rl.rule117, rl.rule118, rl.rule119,
    rl.rule120, rl.rule121, rl.rule122, rl.rule123, rl.rule124, rl.rule125, rl.rule126, rl.rule127,
    rl.rule128, rl.rule129, rl.rule130, rl.rule131, rl.rule132, rl.rule133, rl.rule134, rl.rule135,
    rl.rule136, rl.rule137, rl.rule138, rl.rule139, rl.rule140, rl.rule141, rl.rule142, rl.rule143,
    rl.rule144, rl.rule145, rl.rule146, rl.rule147, rl.rule148, rl.rule149, rl.rule150, rl.rule151,
    rl.rule152, rl.rule153, rl.rule154, rl.rule155, rl.rule156, rl.rule157, rl.rule158, rl.rule159,
    rl.rule160, rl.rule161, rl.rule162, rl.rule163, rl.rule164, rl.rule165, rl.rule166, rl.rule167,
    rl.rule168, rl.rule169, rl.rule170, rl.rule171, rl.rule172, rl.rule173, rl.rule174, rl.rule175,
    rl.rule176, rl.rule177, rl.rule178, rl.rule179, rl.rule180, rl.rule181, rl.rule182, rl.rule183,
    rl.rule184, rl.rule185, rl.rule186, rl.rule187, rl.rule188, rl.rule189, rl.rule190, rl.rule191,
    rl.rule192, rl.rule193, rl.rule194, rl.rule195, rl.rule196, rl.rule197, rl.rule198, rl.rule199,
    rl.rule200, rl.rule201, rl.rule202, rl.rule203, rl.rule204, rl.rule205, rl.rule206, rl.rule207,
    rl.rule208, rl.rule209, rl.rule210, rl.rule211, rl.rule212, rl.rule213, rl.rule214, rl.rule215,
    rl.rule216, rl.rule217, rl.rule218, rl.rule219, rl.rule220, rl.rule221, rl.rule222, rl.rule223,
    rl.rule224, rl.rule225, rl.rule226, rl.rule227, rl.rule228, rl.rule229, rl.rule230, rl.rule231,
    rl.rule232, rl.rule233, rl.rule234, rl.rule235, rl.rule236, rl.rule237, rl.rule238, rl.rule239,
    rl.rule240, rl.rule241, rl.rule242, rl.rule243, rl.rule244, rl.rule245, rl.rule246, rl.rule247,
    rl.rule248, rl.rule249, rl.rule250, rl.rule251, rl.rule252, rl.rule253, rl.rule254, rl.rule255
]

# Vetores para cada classe
classI = [0, 8, 32, 40, 128, 136, 160, 168, 255, 64, 239, 253, 251, 96, 235, 249, 254, 192, 238,
          252, 250, 224, 234, 248]
classII = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 19, 23, 24, 25, 26, 27, 28, 29, 33, 34,
           127, 16, 191, 247, 17, 63, 119, 223, 95, 20, 159, 215, 21, 31, 87, 65, 111, 125, 80, 175,
           245, 47, 81, 117, 68, 207, 221, 69, 79, 93, 84, 143, 213, 85, 55, 66, 189, 231, 61, 67,
           103, 82, 167, 181, 39, 53, 83, 70, 157, 199, 71, 123, 48, 187, 243, 35, 49, 59, 115, 36,
           219, 37, 91, 38, 52, 155, 211, 42, 112, 171, 241, 43, 113, 44, 100, 203, 217, 46, 116, 139,
           209, 50, 179, 51, 56, 98, 185, 227, 57, 99, 58, 114, 163, 177, 62, 118, 131, 145, 72, 237,
           73, 109, 74, 88, 173, 229, 76, 205, 77, 78, 92, 141, 197, 94, 133, 104, 233, 108, 201, 130,
           144, 190, 246, 132, 222, 134, 148, 158, 214, 138, 174, 208, 224, 140, 196, 206, 220, 142,
           212, 152, 188, 194, 230, 154, 166, 180, 210, 156, 198, 162, 176, 186, 242, 164, 218, 170,
           240, 172, 202, 216, 228, 178, 184, 226, 200, 236, 204, 232]
classIII = [18, 22, 30, 45, 60, 90, 105, 122, 126, 146, 150, 183, 151, 86, 135, 149, 75, 89, 101,
            102, 153, 195, 165, 161, 129, 182]
classIV = [41, 54, 106, 110, 97, 107, 121, 147, 120, 169, 225, 124, 137, 193]

# Valores contantes da aplicação (pode mudar conforme a visualização desejada)

SIZE = 150
STEPS = 75

# Generating I+I imgs
"""
for rule1 in classI:
    for rule2 in classI:
        filename = "compos/I+I/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/"+filename)
"""

# Generating I+II imgs
""" 
for rule1 in classI:
    for rule2 in classII:
        filename = "compos/I+II/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/"+filename)
"""

# Generating I+III imgs
for rule1 in classI:
    for rule2 in classIII:
        filename = "compos/I+III/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/"+filename)

# Generating I+IV imgs
for rule1 in classI:
    for rule2 in classIV:
        filename = "compos/I+IV/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/"+filename)

# Generating II+I imgs
""" 
for rule1 in classII:
    for rule2 in classI:
        filename = "compos/II+I/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/" + filename)
"""

# Generating II+II imgs
"""
for rule1 in classII:
    for rule2 in classII:
        filename = "compos/II+II/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/" + filename)
"""

# Generating II+III imgs
for rule1 in classII:
    for rule2 in classIII:
        filename = "compos/II+III/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/" + filename)

# Generating II+IV imgs
for rule1 in classII:
    for rule2 in classIV:
        filename = "compos/II+IV/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/" + filename)


# Generating III+I imgs
for rule1 in classIII:
    for rule2 in classI:
        filename = "compos/III+I/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/" + filename)


# Generating III+II imgs
for rule1 in classIII:
    for rule2 in classII:
        filename = "compos/III+II/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/" + filename)

# Generating III+III imgs
for rule1 in classIII:
    for rule2 in classIII:
        filename = "compos/III+III/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/" + filename)

# Generating III+IV imgs
for rule1 in classIII:
    for rule2 in classIV:
        filename = "compos/III+IV/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/" + filename)


# Generating IV+I imgs
for rule1 in classIV:
    for rule2 in classI:
        filename = "compos/IV+I/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/" + filename)


# Generating IV+II imgs
for rule1 in classIV:
    for rule2 in classII:
        filename = "compos/IV+II/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/" + filename)

# Generating IV+III imgs
for rule1 in classIV:
    for rule2 in classIII:
        filename = "compos/IV+III/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/" + filename)

# Generating IV+IV imgs
for rule1 in classIV:
    for rule2 in classIV:
        filename = "compos/IV+IV/" + str(rule1) + "+" + str(rule2) + ".png"

        # Para apenas aplicar uma regra, utilize a função:
        # state = utils.apply_rule(rules[RULE], SIZE, STEPS, begin=0)

        # Para combinar duas regras, utilize a função
        state = utils.compose_rules(rules[rule1], rules[rule2], SIZE, STEPS, begin=0)

        # Para transformar o seu estado atual em imagem, utilize a função:
        image = utils.get_image(state, SIZE, STEPS)

        # Para exibir a imagem, utilize o método:
        image.save("imgs/" + filename)
