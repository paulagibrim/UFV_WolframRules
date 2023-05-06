# ######################################################################## #
#  Trabalho de Conclusão de Curso - Departamento de Ciência da Computação  #
#               Paula Teresa Mota Gibrim - Matrícula: ES90366              #
#                                                                          #
#   File: main.py                                                          #
# ######################################################################## #

import rules as rl
import utils


# Valores constantes para o trabalho
SIZE = 155
STEPS = 60


# state = utils.apply_rule(rl.rule2, SIZE, STEPS, begin=0)


state = utils.compose_rules(rl.rule20, rl.rule31, SIZE, STEPS)

image = utils.get_image(state, SIZE, STEPS)

image.show()
