# ######################################################################## #
#  Trabalho de Conclusão de Curso - Departamento de Ciência da Computação  #
#               Paula Teresa Mota Gibrim - Matrícula: ES90366              #
#                                                                          #
#   File: main.py                                                          #
# ######################################################################## #

import rules as rl
import utils


# Valores constantes para o trabalho
SIZE = 101
STEPS = 50


state = utils.apply_rule(rl.rule19, SIZE, STEPS, need_more=True)

image = utils.get_image(state, SIZE, STEPS)

image.show()
