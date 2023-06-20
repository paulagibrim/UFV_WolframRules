# ######################################################################## #
#   Trabalho de Conclusão de Curso - Departamento de Ciência da Computação #
#               Paula Teresa Mota Gibrim - Matrícula: ES90366              #
#                                                                          #
#   File: utils.py                                                         #
# ######################################################################## #

from random import getrandbits

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from config import *
import os
from tqdm import tqdm


def convert(seconds):
    """
    Função utilizada para converter uma quantidade de segundos em um tempo no formato hh:mm:ss

    :param seconds: Float, quantidade de segundos
    :return: String, tempo formatado
    """
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


def applyRule(rule, inicialState=None, black_cells=1):
    """
    Essa função aplica uma regra de autômato celular de 1D dimensão por um número específico de STEPS

    :param black_cells: Integer, Quantidade de black cells no estado inicial
    :param inicialState: Array, estado inicial previamente definido. Default: None
    :param rule: Function, a regra a ser aplicada
    :return: numpy.ndarray, estado final do autômato celular
    """

    if inicialState is None:
        # Inicializa o estado inicial do autômato celular
        state = np.zeros((STEPS, SIZE), dtype=bool)
        state[0, SIZE // 2] = 1  # Define a célula central como 1 (preto)
        if black_cells > 1:
            for cell in range(1, (black_cells // 2) + 1):
                state[0, (SIZE // 2) + cell] = 1  # Define a célula lateral direita como 1 (preto)
                state[0, (SIZE // 2) - cell] = 1  # Define a célula lateral esquerda como 1 (preto)
            if black_cells % 2 == 0:
                state[0, (SIZE // 2) + (
                        black_cells // 2)] = 0  # Define a última célula lateral direita colorida como 0 (branco)

    else:
        state = np.zeros((STEPS, SIZE), dtype=bool)
        state[0] = inicialState

    # Aplica a regra por um número específico de STEPS
    for k in range(0, STEPS - 1):
        for j in range(SIZE):
            left = state[k, (j - 1) % SIZE]
            center = state[k, j]
            right = state[k, (j + 1) % SIZE]

            block = [left, center, right]

            # Aplica a rule
            state[k + 1, j] = rule(block)

    return state


def applyRuleOnce(rule, inicialState=None, black_cells=1):
    """
    Essa função aplica uma regra de autômato celular de 1D dimensão por apenas 1 vez

    :param black_cells:
    :param inicialState:
    :param rule: function, A regra a ser aplicada
    :return: numpy.ndarray, Estado final do autômato celular
    """
    if inicialState is None:
        # Inicializa o estado inicial do autômato celular
        state = np.zeros((STEPS, SIZE), dtype=bool)
        state[0, SIZE // 2] = 1  # Define a célula central como 1 (preto)
        if black_cells > 1:
            for cell in range(1, (black_cells // 2) + 1):
                state[0, (SIZE // 2) + cell] = 1  # Define a célula lateral direita como 1 (preto)
                state[0, (SIZE // 2) - cell] = 1  # Define a célula lateral esquerda como 1 (preto)
            if black_cells % 2 == 0:
                state[0, (SIZE // 2) + (
                        black_cells // 2)] = 0  # Define a última célula lateral direita colorida como 0 (branco)

    else:
        state = np.zeros((STEPS, SIZE), dtype=bool)
        state[0] = inicialState

    # Aplica a regra uma única vez
    for j in range(SIZE):
        left = state[0, (j - 1) % SIZE]
        center = state[0, j]
        right = state[0, (j + 1) % SIZE]

        block = [left, center, right]

        # Aplica a rule
        state[1, j] = rule(block)

    return state


def composeRules(rule1, rule2, inicialState=None):
    """
    Essa função combina duas regras de autômatos celulares de 1D, aplicando a rule1 seguida da rule2, para um número
    específico de STEPS

    :param inicialState: Array, estado inicial previamente definido. Default: None
    :param rule1: Function, primeira regra a ser aplicada
    :param rule2: Function, segunda regra a ser aplicada
    :return: numpy.ndarray, estado final do autômato celular
    """

    if inicialState is None:
        # Inicializa o estado inicial do autômato celular
        finalState = np.copy(INITIAL_STATE)
    else:
        finalState = np.zeros((STEPS, SIZE), dtype=bool)
        finalState[0] = inicialState

    # Aplica a rule1 seguida da rule2, até aquele número determinado de STEPS
    for state in range(0, STEPS - 1):
        for cell in range(SIZE):

            left = finalState[state, (cell - 1) % SIZE]
            center = finalState[state, cell]
            right = finalState[state, (cell + 1) % SIZE]

            block = [left, center, right]

            if state % 2 == 0:
                # Aplica a rule1
                finalState[state + 1, cell] = rule1(block)
            else:
                # Aplica a rule2
                finalState[state + 1, cell] = rule2(block)

    return finalState


def getImage(state):
    """
    Converte o estado (array) para uma imagem.
    :param state, Estado final do autômato celular
    :return: PIL.Image, Imagem do autômato celular
    """
    arr = state.copy().astype(np.uint8)

    for k in range(STEPS):
        for j in range(SIZE):
            if arr[k][j]:
                arr[k][j] = 0
            else:
                arr[k][j] = 255

    return Image.fromarray(arr)


def genAllRules_ClassI(progress, n_comp=0):
    """
    Gera todas as imagens com estados iniciais da classe I
    :return:
    """
    for k in classI:
        path = "../UFV_WolframRules_Imgs/images/single_rules/rules_random_initial_states" + str(n_comp) + "/classI/"
        state = applyRule(rules[k], inicialState=INITIAL_STATE[0])
        img = getImage(state)
        if not (os.path.exists(path)):
            os.makedirs(path)
        img.save(path + "Rule" + str(k) + ".png")
        progress.update(1)


def genAllRules_ClassII(progress, n_comp=0):
    """
        Gera todas as imagens com estados iniciais da classe II
        :return:
        """
    for k in classII:
        path = "../UFV_WolframRules_Imgs/images/single_rules/rules_random_initial_states" + str(n_comp) + "/classII/"
        state = applyRule(rules[k], inicialState=INITIAL_STATE[0])
        img = getImage(state)
        if not (os.path.exists(path)):
            os.makedirs(path)
        img.save(path + "Rule" + str(k) + ".png")
        progress.update(1)


def genAllRules_ClassIII(progress, n_comp=0):
    """
        Gera todas as imagens com estados iniciais da classe III
        :return:
        """
    for k in classIII:
        path = "../UFV_WolframRules_Imgs/images/single_rules/rules_random_initial_states" + str(n_comp) + "/classIII/"
        state = applyRule(rules[k], inicialState=INITIAL_STATE[0])
        img = getImage(state)
        if not (os.path.exists(path)):
            os.makedirs(path)
        img.save(path + "Rule" + str(k) + ".png")
        progress.update(1)


def genAllRules_ClassIV(progress, n_comp=0):
    """
        Gera todas as imagens com estados iniciais da classe IV
        :return:
        """
    for k in classIV:
        path = "../UFV_WolframRules_Imgs/images/single_rules/rules_random_initial_states" + str(n_comp) + "/classIV/"
        state = applyRule(rules[k], inicialState=INITIAL_STATE[0])
        img = getImage(state)
        if not (os.path.exists(path)):
            os.makedirs(path)
        img.save(path + "Rule" + str(k) + ".png")
        progress.update(1)


def genAllRules(n_comp=0):
    """ Gera todas as imagens de composições """
    with tqdm(total=len(classI), desc="Rules - Class I") as progress:
        genAllRules_ClassI(progress, n_comp)

    with tqdm(total=len(classII), desc="Rules - Class II") as progress:
        genAllRules_ClassII(progress, n_comp)

    with tqdm(total=len(classIII), desc="Rules - Class III") as progress:
        genAllRules_ClassIII(progress, n_comp)

    with tqdm(total=len(classIV), desc="Rules - Class IV") as progress:
        genAllRules_ClassIV(progress, n_comp)


def genCompositions_I_I(progress, n_comp=0):
    """ Gera todas as imagens de composições entre as classes I e I
    :return:
    """

    path = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/I+I/"
    if not (os.path.exists(path)):
        os.makedirs(path)

    for rule1 in classI:
        for rule2 in classI:
            if rule1 == rule2:
                progress.update(1)
                pass
            else:
                filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

                state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
                image = getImage(state)  # Geramos a imagem
                image.save(path + filename)  # Salvamos a imagem

                progress.update(1)


def genCompositions_I_II(progress, n_comp=0):
    """ Gera todas as imagens de composições entre as classes I e II
    :return:
    """
    path = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/I+II/"
    if not (os.path.exists(path)):
        os.makedirs(path)

    for rule1 in classI:
        for rule2 in classII:
            filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

            state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
            image = getImage(state)  # Geramos a imagem
            image.save(path + filename)  # Salvamos a imagem

            progress.update(1)

    for rule1 in classII:
        for rule2 in classI:
            filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

            state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
            image = getImage(state)  # Geramos a imagem
            image.save(path + filename)  # Salvamos a imagem

            progress.update(1)


def genCompositions_I_III(progress, n_comp=0):
    """ Gera todas as imagens de composições entre as classes I e IIII
    :return:
    """
    path = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/I+III/"
    if not (os.path.exists(path)):
        os.makedirs(path)

    for rule1 in classI:
        for rule2 in classIII:
            filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

            state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
            image = getImage(state)  # Geramos a imagem
            image.save(path + filename)  # Salvamos a imagem

            progress.update(1)

    for rule1 in classIII:
        for rule2 in classI:
            filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

            state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
            image = getImage(state)  # Geramos a imagem
            image.save(path + filename)  # Salvamos a imagem

            progress.update(1)


def genCompositions_I_IV(progress, n_comp=0):
    """ Gera todas as imagens de composições entre as classes I e IV
    :return:
    """
    path = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/I+IV/"
    if not (os.path.exists(path)):
        os.makedirs(path)

    for rule1 in classI:
        for rule2 in classIV:
            filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

            state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
            image = getImage(state)  # Geramos a imagem
            image.save(path + filename)  # Salvamos a imagem

            progress.update(1)

    for rule1 in classIV:
        for rule2 in classI:
            filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

            state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
            image = getImage(state)  # Geramos a imagem
            image.save(path + filename)  # Salvamos a imagem

            progress.update(1)


def genCompositions_II_II(progress, n_comp=0):
    """ Gera todas as imagens de composições entre as classes II e II
    :return:
    """
    path = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/II+II/"
    if not (os.path.exists(path)):
        os.makedirs(path)

    for rule1 in classII:
        for rule2 in classII:
            if rule1 == rule2:
                progress.update(1)
                pass
            else:
                filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

                state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
                image = getImage(state)  # Geramos a imagem
                image.save(path + filename)  # Salvamos a imagem

                progress.update(1)


def genCompositions_II_III(progress, n_comp=0):
    """ Gera todas as imagens de composições entre as classes II e III
    :return:
    """
    path = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/II+III/"
    if not (os.path.exists(path)):
        os.makedirs(path)

    for rule1 in classII:
        for rule2 in classIII:
            filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

            state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
            image = getImage(state)  # Geramos a imagem
            image.save(path + filename)  # Salvamos a imagem

            progress.update(1)

    for rule1 in classIII:
        for rule2 in classII:
            filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

            state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
            image = getImage(state)  # Geramos a imagem
            image.save(path + filename)  # Salvamos a imagem

            progress.update(1)


def genCompositions_II_IV(progress, n_comp=0):
    """ Gera todas as imagens de composições entre as classes II e IV
    :return:
    """
    path = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/II+IV/"
    if not (os.path.exists(path)):
        os.makedirs(path)

    for rule1 in classII:
        for rule2 in classIV:
            filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

            state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
            image = getImage(state)  # Geramos a imagem
            image.save(path + filename)  # Salvamos a imagem

            progress.update(1)

    for rule1 in classIV:
        for rule2 in classII:
            filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

            state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
            image = getImage(state)  # Geramos a imagem
            image.save(path + filename)  # Salvamos a imagem

            progress.update(1)


def genCompositions_III_III(progress, n_comp=0):
    """ Gera todas as imagens de composições entre as classes III e III
    :return:
    """
    path = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/III+III/"
    if not (os.path.exists(path)):
        os.makedirs(path)

    for rule1 in classIII:
        for rule2 in classIII:
            if rule1 == rule2:
                progress.update(1)
                pass
            else:
                filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

                state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
                image = getImage(state)  # Geramos a imagem
                image.save(path + filename)  # Salvamos a imagem

                progress.update(1)


def genCompositions_III_IV(progress, n_comp=0):
    """ Gera todas as imagens de composições entre as classes III e IV
    :return:
    """
    path = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/III+IV/"
    if not (os.path.exists(path)):
        os.makedirs(path)

    for rule1 in classIII:
        for rule2 in classIV:
            filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

            state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
            image = getImage(state)  # Geramos a imagem
            image.save(path + filename)  # Salvamos a imagem

            progress.update(1)

    for rule1 in classIV:
        for rule2 in classIII:
            filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

            state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
            image = getImage(state)  # Geramos a imagem
            image.save(path + filename)  # Salvamos a imagem

            progress.update(1)


def genCompositions_IV_IV(progress, n_comp=0):
    """ Gera todas as imagens de composições entre as classes IV e IV
    :return:
    """
    path = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/IV+IV/"
    if not (os.path.exists(path)):
        os.makedirs(path)

    for rule1 in classIV:
        for rule2 in classIV:
            if rule1 == rule2:
                progress.update(1)
                pass
            else:
                filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

                state = composeRules(rules[rule1], rules[rule2])  # Combinamos duas regras
                image = getImage(state)  # Geramos a imagem
                image.save(path + filename)  # Salvamos a imagem

                progress.update(1)


def genAllCompositions_I(n_comp=0):
    """ Gera todas as imagens de composições com a classe I """
    with tqdm(total=n_imgs_I_I) as progress:
        genCompositions_I_I(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_I_II) as progress:
        genCompositions_I_II(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_I_III) as progress:
        genCompositions_I_III(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_I_IV) as progress:
        genCompositions_I_IV(progress, n_comp=n_comp)


def genAllCompositions_II(n_comp=0):
    """ Gera todas as imagens de composições com a classe II """
    with tqdm(total=n_imgs_I_II) as progress:
        genCompositions_I_II(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_II_II) as progress:
        genCompositions_II_II(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_II_III) as progress:
        genCompositions_II_III(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_II_IV) as progress:
        genCompositions_II_IV(progress, n_comp=n_comp)


def genAllCompositions_III(n_comp=0):
    """ Gera todas as imagens de composições com a classe III """
    with tqdm(total=n_imgs_I_III) as progress:
        genCompositions_I_III(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_II_III) as progress:
        genCompositions_II_III(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_III_III) as progress:
        genCompositions_III_III(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_III_IV) as progress:
        genCompositions_III_IV(progress, n_comp=n_comp)


def genAllCompositions_IV(n_comp=0):
    """ Gera todas as imagens de composições com a classe IV """
    with tqdm(total=n_imgs_I_IV) as progress:
        genCompositions_I_IV(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_II_IV) as progress:
        genCompositions_II_IV(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_III_IV) as progress:
        genCompositions_III_IV(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_IV_IV) as progress:
        genCompositions_IV_IV(progress, n_comp=n_comp)


def genAllCompositions(n_comp=0):
    """ Gera todas as imagens de composições """
    with tqdm(total=n_imgs_I_I, desc="Compositions - I e I") as progress:
        genCompositions_I_I(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_I_II, desc="Compositions - I e II") as progress:
        genCompositions_I_II(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_I_III, desc="Compositions - I e III") as progress:
        genCompositions_I_III(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_I_IV, desc="Compositions - I e IV") as progress:
        genCompositions_I_IV(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_II_II, desc="Compositions - II e II") as progress:
        genCompositions_II_II(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_II_III, desc="Compositions - II e III") as progress:
        genCompositions_II_III(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_II_IV, desc="Compositions - II e IV") as progress:
        genCompositions_II_IV(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_III_III, desc="Compositions - III e III") as progress:
        genCompositions_III_III(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_III_IV, desc="Compositions - III e IV") as progress:
        genCompositions_III_IV(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_IV_IV, desc="Compositions - IV e IV") as progress:
        genCompositions_IV_IV(progress, n_comp=n_comp)


def createView(imgs, legs, path, col=2):
    """ Criar os mosaicos (composições) com duas imagens """

    # Largura e altura básicos, de referência, das imagens
    larg = 8
    alt = 6

    n_imagens = len(imgs)
    if len(imgs) < col:
        col = len(imgs)
    lin = n_imagens // col + int(n_imagens % col > 0)

    with plt.style.context("fivethirtyeight"):
        fig = plt.figure(figsize=(larg * col, alt * lin))
        ax = []

        for pos, img in enumerate(imgs):
            ax.append(fig.add_subplot(lin, col, pos + 1))
            ax[-1].axis('off')
            if img.mode == 'L' or img.mode == '1':
                img = img.convert('RGB')
            arr = np.asarray(img)
            ax[-1].imshow(arr)
            ax[-1].set_title(legs[pos])

        fig.tight_layout()

        plt.savefig(path, dpi=300)

    plt.close()


def genViews_I_I(progress, n_comp=0):
    """ Gera todos os mosaicos das composições entre as classes I e I """

    path1 = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/I+I/"
    path2 = "view/"
    if not (os.path.exists(path1 + path2)):
        os.makedirs(path1 + path2)

    for rule1 in classI:
        for rule2 in classI:
            if rule1 == rule2:
                pass
            elif rule1 < rule2:
                imgs = [
                    Image.open(path1 + "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"),
                    Image.open(path1 + "Rule" + str(rule2) + " + Rule" + str(rule1) + ".png")
                ]

                legs = [
                    "Rule" + str(rule1) + " + Rule" + str(rule2),
                    "Rule" + str(rule2) + " + Rule" + str(rule1)
                ]

                filename = path1 + path2 + "Rule" + str(rule1) + "+ Rule" + str(rule2) + ".png"

                createView(imgs, legs, filename)

                progress.update(1)


def genViews_I_II(progress, n_comp=0):
    """ Gera todos os mosaicos das composições entre as classes I e II """

    path1 = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/I+II/"
    path2 = "view/"
    if not (os.path.exists(path1 + path2)):
        os.makedirs(path1 + path2)

    for rule1 in classI:
        for rule2 in classII:
            imgs = [
                Image.open(path1 + "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"),
                Image.open(path1 + "Rule" + str(rule2) + " + Rule" + str(rule1) + ".png")
            ]

            legs = [
                "Rule" + str(rule1) + " + Rule" + str(rule2),
                "Rule" + str(rule2) + " + Rule" + str(rule1)
            ]

            filename = path1 + path2 + "Rule" + str(rule1) + "+ Rule" + str(rule2) + ".png"

            createView(imgs, legs, filename)

            progress.update(1)


def genViews_I_III(progress, n_comp=0):
    """ Gera todos os mosaicos das composições entre as classes I e III """

    path1 = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/I+III/"
    path2 = "view/"
    if not (os.path.exists(path1 + path2)):
        os.makedirs(path1 + path2)

    for rule1 in classI:
        for rule2 in classIII:
            imgs = [
                Image.open(path1 + "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"),
                Image.open(path1 + "Rule" + str(rule2) + " + Rule" + str(rule1) + ".png")
            ]

            legs = [
                "Rule" + str(rule1) + " + Rule" + str(rule2),
                "Rule" + str(rule2) + " + Rule" + str(rule1)
            ]

            filename = path1 + path2 + "Rule" + str(rule1) + "+ Rule" + str(rule2) + ".png"

            createView(imgs, legs, filename)

            progress.update(1)


def genViews_I_IV(progress, n_comp=0):
    """ Gera todos os mosaicos das composições entre as classes I e IV """

    path1 = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/I+IV/"
    path2 = "view/"
    if not (os.path.exists(path1 + path2)):
        os.makedirs(path1 + path2)

    for rule1 in classI:
        for rule2 in classIV:
            imgs = [
                Image.open(path1 + "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"),
                Image.open(path1 + "Rule" + str(rule2) + " + Rule" + str(rule1) + ".png")
            ]

            legs = [
                "Rule" + str(rule1) + " + Rule" + str(rule2),
                "Rule" + str(rule2) + " + Rule" + str(rule1)
            ]

            filename = path1 + path2 + "Rule" + str(rule1) + "+ Rule" + str(rule2) + ".png"

            createView(imgs, legs, filename)

            progress.update(1)


def genViews_II_II(progress, n_comp=0):
    """ Gera todos os mosaicos das composições entre as classes II e II """

    path1 = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/II+II/"
    path2 = "view/"
    if not (os.path.exists(path1 + path2)):
        os.makedirs(path1 + path2)

    for rule1 in classII:
        for rule2 in classII:
            if rule1 == rule2:
                pass
            elif rule1 < rule2:
                imgs = [
                    Image.open(path1 + "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"),
                    Image.open(path1 + "Rule" + str(rule2) + " + Rule" + str(rule1) + ".png")
                ]

                legs = [
                    "Rule" + str(rule1) + " + Rule" + str(rule2),
                    "Rule" + str(rule2) + " + Rule" + str(rule1)
                ]

                filename = path1 + path2 + "Rule" + str(rule1) + "+ Rule" + str(rule2) + ".png"

                createView(imgs, legs, filename)

                progress.update(1)


def genViews_II_III(progress, n_comp=0):
    """ Gera todos os mosaicos das composições entre as classes II e III """

    path1 = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/II+III/"
    path2 = "view/"
    if not (os.path.exists(path1 + path2)):
        os.makedirs(path1 + path2)

    for rule1 in classII:
        for rule2 in classIII:
            imgs = [
                Image.open(path1 + "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"),
                Image.open(path1 + "Rule" + str(rule2) + " + Rule" + str(rule1) + ".png")
            ]

            legs = [
                "Rule" + str(rule1) + " + Rule" + str(rule2),
                "Rule" + str(rule2) + " + Rule" + str(rule1)
            ]

            filename = path1 + path2 + "Rule" + str(rule1) + "+ Rule" + str(rule2) + ".png"

            createView(imgs, legs, filename)

            progress.update(1)


def genViews_II_IV(progress, n_comp=0):
    """ Gera todos os mosaicos das composições entre as classes II e IV """

    path1 = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/II+IV/"
    path2 = "view/"
    if not (os.path.exists(path1 + path2)):
        os.makedirs(path1 + path2)

    for rule1 in classII:
        for rule2 in classIV:
            imgs = [
                Image.open(path1 + "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"),
                Image.open(path1 + "Rule" + str(rule2) + " + Rule" + str(rule1) + ".png")
            ]

            legs = [
                "Rule" + str(rule1) + " + Rule" + str(rule2),
                "Rule" + str(rule2) + " + Rule" + str(rule1)
            ]

            filename = path1 + path2 + "Rule" + str(rule1) + "+ Rule" + str(rule2) + ".png"

            createView(imgs, legs, filename)

            progress.update(1)


def genViews_III_III(progress, n_comp=0):
    """ Gera todos os mosaicos das composições entre as classes III e III """

    path1 = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/III+III/"
    path2 = "view/"
    if not (os.path.exists(path1 + path2)):
        os.makedirs(path1 + path2)

    for rule1 in classIII:
        for rule2 in classIII:
            if rule1 == rule2:
                pass
            elif rule1 < rule2:
                imgs = [
                    Image.open(path1 + "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"),
                    Image.open(path1 + "Rule" + str(rule2) + " + Rule" + str(rule1) + ".png")
                ]

                legs = [
                    "Rule" + str(rule1) + " + Rule" + str(rule2),
                    "Rule" + str(rule2) + " + Rule" + str(rule1)
                ]

                filename = path1 + path2 + "Rule" + str(rule1) + "+ Rule" + str(rule2) + ".png"

                createView(imgs, legs, filename)

                progress.update(1)


def genViews_III_IV(progress, n_comp=0):
    """ Gera todos os mosaicos das composições entre as classes III e IV """

    path1 = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/III+IV/"
    path2 = "view/"
    if not (os.path.exists(path1 + path2)):
        os.makedirs(path1 + path2)

    for rule1 in classIII:
        for rule2 in classIV:
            imgs = [
                Image.open(path1 + "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"),
                Image.open(path1 + "Rule" + str(rule2) + " + Rule" + str(rule1) + ".png")
            ]

            legs = [
                "Rule" + str(rule1) + " + Rule" + str(rule2),
                "Rule" + str(rule2) + " + Rule" + str(rule1)
            ]

            filename = path1 + path2 + "Rule" + str(rule1) + "+ Rule" + str(rule2) + ".png"

            createView(imgs, legs, filename)

            progress.update(1)


def genViews_IV_IV(progress, n_comp=0):
    """ Gera todos os mosaicos das composições entre as classes IV e IV """

    path1 = "../UFV_WolframRules_Imgs/images/compositions/composition" + str(n_comp) + "/IV+IV/"
    path2 = "view/"
    if not (os.path.exists(path1 + path2)):
        os.makedirs(path1 + path2)

    for rule1 in classIV:
        for rule2 in classIV:
            if rule1 == rule2:
                pass
            elif rule1 < rule2:
                imgs = [
                    Image.open(path1 + "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"),
                    Image.open(path1 + "Rule" + str(rule2) + " + Rule" + str(rule1) + ".png")
                ]

                legs = [
                    "Rule" + str(rule1) + " + Rule" + str(rule2),
                    "Rule" + str(rule2) + " + Rule" + str(rule1)
                ]

                filename = path1 + path2 + "Rule" + str(rule1) + "+ Rule" + str(rule2) + ".png"

                createView(imgs, legs, filename)

                progress.update(1)


def genAllViews(n_comp=0):
    """ Gera todas as imagens de composições """
    with tqdm(total=comb_I, desc="Views - I e I") as progress:
        genViews_I_I(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_I_II / 2, desc="Views - I e II") as progress:
        genViews_I_II(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_I_III / 2, desc="Views - I e III") as progress:
        genViews_I_III(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_I_IV / 2, desc="Views - I e IV") as progress:
        genViews_I_IV(progress, n_comp=n_comp)

    with tqdm(total=comb_II, desc="Views - II e II") as progress:
        genViews_II_II(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_II_III / 2, desc="Views - II e III") as progress:
        genViews_II_III(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_II_IV / 2, desc="Views - II e IV") as progress:
        genViews_II_IV(progress, n_comp=n_comp)

    with tqdm(total=comb_III, desc="Views - III e III") as progress:
        genViews_III_III(progress, n_comp=n_comp)

    with tqdm(total=n_imgs_III_IV / 2, desc="Views - III e IV") as progress:
        genViews_III_IV(progress, n_comp=n_comp)

    with tqdm(total=comb_IV, desc="Views - IV e IV") as progress:
        genViews_IV_IV(progress, n_comp=n_comp)


def getNoise(progress, n_rule, noise=75, n_comp=0):
    initialState1 = INITIAL_STATE[0]
    initialState2 = np.copy(initialState1)
    aux1 = initialState2[noise]
    if aux1:
        initialState2[noise] = False
    else:
        initialState2[noise] = True

    finalState10 = applyRule(rules[n_rule], initialState1)
    finalState11 = applyRule(rules[n_rule], initialState2)

    finalState1 = finalState11 ^ finalState10

    imgs = [
        getImage(finalState10),
        getImage(finalState11),
        getImage(finalState1)
    ]

    legs = [
        "Rule" + str(n_rule),
        "Rule" + str(n_rule) + " with noise",
        "Difference between then (xor)"
    ]

    path = "../UFV_WolframRules_Imgs/images/noises/noise" + str(n_comp) + "/"
    if not (os.path.exists(path)):
        os.makedirs(path)

    path = path + "XOR Rule" + str(n_rule) + ".png"

    createView(imgs, legs, path, col=3)

    progress.update(1)


def getAllNoises(noise=75, n_comp=0):
    with tqdm(total=256, desc="Noisy rules") as progress:
        for rule in range(256):
            getNoise(progress, rule, noise=noise, n_comp=n_comp)


def testTheorem1(progress, n_comp=0):

    allClasses = [classI, classII, classIII, classIV]
    path = "../UFV_WolframRules_Imgs/images/theorems/theorem1/exec" + str(n_comp) + "/"
    if not (os.path.exists(path)):
        os.makedirs(path)

    for class1 in allClasses:
        for class2 in allClasses:
            for rule1 in class1:
                for rule2 in class2:
                    if rule1 == rule2:
                        pass
                    elif rule1 < rule2:
                        filename = "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png"

                        init = INITIAL_STATE[0]
                        init2 = applyRuleOnce(rules[rule1], inicialState=init)[1]
                        state1 = composeRules(rules[rule1], rules[rule2], inicialState=init)  # Combinamos duas regras
                        state2 = composeRules(rules[rule2], rules[rule1], inicialState=init2)
                        diff = state1 ^ state2
                        images = [
                            getImage(state1),  # Geramos a imagem
                            getImage(state2),
                            getImage(diff)
                        ]

                        legs = [
                            "Rule" + str(rule1) + " + Rule" + str(rule2) + ".png",
                            "Rule" + str(rule2) + " + Rule" + str(rule1) + " displaced.png",
                            "Difference between then (xor)"
                        ]

                        createView(images, legs, path=path+filename, col=3)

                        progress.update(1)


def testAllTheorem1(n_comp=0):
    """ Gera todas as imagens de composições com a classe I """
    with tqdm(total=comb_all) as progress:
        testTheorem1(progress, n_comp=n_comp)


