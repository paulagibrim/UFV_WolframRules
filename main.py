# ######################################################################## #
#  Trabalho de Conclusão de Curso - Departamento de Ciência da Computação  #
#               Paula Teresa Mota Gibrim - Matrícula: ES90366              #
#                                                                          #
#   File: main.py                                                          #
# ######################################################################## #

import rules as rl
import utils


# Valores contantes da aplicação (pode mudar conforme a visualização desejada)
SIZE = 150
STEPS = 75

# Para apenas aplicar uma regra, utilize a função:
state = utils.apply_rule(rl.rule107, SIZE, STEPS, begin=1)

# Para combinar duas regras, utilize a função:
# state = utils.compose_rules(rl.rule30, rl.rule41, SIZE, STEPS, begin=0)

# Para transformar o seu estado atual em imagem, utilize a função:
image = utils.get_image(state, SIZE, STEPS)

# Para exibir a imagem, utilize o método:
image.show()
