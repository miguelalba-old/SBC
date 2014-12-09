# -*- coding: iso-8859-1 -*-

import kmod


class EstadoGlobo(kmod.Clase):

    color = kmod.Atributo('Color', 'str', None)  # YELLOW, PURPLE
    size = kmod.Atributo('Size', 'str', None)  # LARGE, SMALL
    act = kmod.Atributo('Act', 'str', None)  # STRETCH, DIP
    age = kmod.Atributo('Age', 'str', None)  # ADULT, CHILD
    atributos = (color, size, act, age)

    def __init__(self, nombre):
        super(EstadoGlobo, self).__init__(nombre)


class Inflado(EstadoGlobo):
    def __init__(self):
        super(Inflado, self).__init__('inflado')
        act_rule = kmod.Rverifica('r1', 'igual', None, self.act, 'STRETCH')
        age_rule = kmod.Rverifica('r2', 'igual', None, self.age, 'ADULT')
        self.reglas = (act_rule, age_rule)


class Desinflado(EstadoGlobo):
    def __init__(self):
        super(Desinflado, self).__init__('desinflado')
        act_rule = kmod.Rverifica('r1', 'igual', None, self.act, 'DIP')
        self.reglas = (act_rule, )


def clases():
    return Inflado(), Desinflado()
