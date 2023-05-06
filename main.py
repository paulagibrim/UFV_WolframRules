# ######################################################################## #
#  Trabalho de Conclusão de Curso - Departamento de Ciência da Computação  #
#               Paula Teresa Mota Gibrim - Matrícula: ES90366              #
#                                                                          #
#   File: main.py                                                          #
# ######################################################################## #

import rules as rl
import utils


# Valores contantes da aplicação (pode mudar conforme a visualização desejada)
SIZE = 155
STEPS = 60

# Para apenas aplicar uma regra, utilize a função:
# state = utils.apply_rule(rl.rule2, SIZE, STEPS, begin=0)

# Para combinar duas regras, utilize a função:
state = utils.compose_rules(rl.rule20, rl.rule31, SIZE, STEPS)

# Para transformar o seu estado atual em imagem, utilize a função:
image = utils.get_image(state, SIZE, STEPS)

# Para exibir a imagem, utilize o método:
image.show()
