# UFV_WolframRules

Esse projeto está sendo desenvolvido como proposta de trabalho acerca das regras de Autômatos Celulares de Stephen 
Wolfram.

## Arquivos
Se encontra no arquivo `rules.py` a implementação das regras de Wolfram. Já foram implementadas as regras de
0 a 49, e todas as regras seguem o mesmo padrão:
```python
# Rule [NUMBER] ([TYPE]) - < [LINK] >
def rule[NUMBER](block):
    """
        :param block: 3-size block
        :return: int (0 or 1)
    """
    return [ALGEBRAIC OR BOOLEAN FORM]
```
onde os seguintes termos representam:
- [NUMBER] - o número da regra;
- [TYPE] - classe da regra (chaotic, periodic, null, etc);
- [LINK] - link do site [Wolfram Atlas](http://atlas.wolfram.com/) correspondente aos detalhes daquela regra;
- [ALGEBRAIC OR BOOLEAN FORM] - a implementação da regra, em sua forma algébrica ou booleana.

No arquivo `utils.py` estão localizadas as implementações das funções necessárias para o programa. São elas: 
- `apply_rule()`: aplica uma regra a um autômato celular, e retorna seu estado final
- `compose_rules()`: combina a aplicação de duas regras a um autômato celular, e retorna seu estado final
- `get_image()`: transforma o estado final de um autômato celular em uma imagem

O arquivo `main.py` é responsável por apresentar um exemplo de aplicação dessas funções.

## Veja também

- `Elementary Cellular Automaton <https://en.wikipedia.org/wiki/Elementary_cellular_automaton>`__, Wikipedia;
- `Rule 30 <https://en.wikipedia.org/wiki/Rule_30>`__, Wikipedia;
- `Elementary Cellular Automaton <http://mathworld.wolfram.com/ElementaryCellularAutomaton.html>`__, Wolfram MathWorld;
- `Cellular Automata <https://plato.stanford.edu/entries/cellular-automata/index.html>`__, Stanford Encyclopedia of Philosophy;
- `The 256 Rules <https://plato.stanford.edu/entries/cellular-automata/supplement.html>`__, Stanford Encyclopedia of Philosophy.
