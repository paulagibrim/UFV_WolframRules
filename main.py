# ######################################################################## #
#   Trabalho de Conclusão de Curso - Departamento de Ciência da Computação #
#               Paula Teresa Mota Gibrim - Matrícula: ES90366              #
#                                                                          #
#   File: main.py                                                          #
# ######################################################################## #

from utils import *
from time import time

# n_composicao = 1
initialTime = time()
for n_composicao in range(2, 6):
    # Gerar as imagens de cada regra com estado inicial aleatório
    genAllRules(n_comp=n_composicao)

    # Gerar todas as composições, de todas as regras
    genAllCompositions(n_comp=n_composicao)

    # Gerar todos os mosaicos, para cada par de regras
    genAllViews(n_comp=n_composicao)

    # Gerar noisy rules
    getAllNoises(n_comp=n_composicao)

finalTime = time()
print(f"Tempo total: {convert(finalTime - initialTime)}")
