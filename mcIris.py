# -*- coding: iso-8859-1 -*-

import kmod


#----LAS CLASES DE LA BASE DE CONOCIMIENTO DE FRUTOS-----------
class Flor(kmod.Clase):
    """Describe los atributos por los que se caracterizará a un fruto."""

    atAS = kmod.Atributo('Ancho sepalo', 'int', 'mm')
    atLS = kmod.Atributo('Largo sepalo', 'int', 'mm')
    atAP = kmod.Atributo('Ancho petalo', 'int', 'mm')
    atLP = kmod.Atributo('Largo petalo', 'int', 'mm')
    atributos = [atAS, atLS, atAP, atLP]

    def __init__(self, nombre):
        '''
        @param nombre: Nombre de la flor
        '''
        kmod.Clase.__init__(self,nombre=nombre)


class Setosa(Flor):

    def __init__(self):
        super(Setosa, self).__init__('setosa')

        r1 = kmod.Rverifica('r1', 'rango', None, self.atAS, [10, 30])
        r2 = kmod.Rverifica('r2', 'rango', None, self.atLS, [100, 120])
        r3 = kmod.Rverifica('r3', 'rango', None, self.atAP, [10, 40])
        r4 = kmod.Rverifica('r4', 'rango', None, self.atLP, [90, 100])
        self.reglas = [r1, r2, r3, r4]


class Virginica(Flor):

    def __init__(self):
        super(Virginica, self).__init__('vrginica')

        r1 = kmod.Rverifica('r1', 'rango', None, self.atAS, [10, 30])
        r2 = kmod.Rverifica('r2', 'rango', None, self.atLS, [100, 200])
        r3 = kmod.Rverifica('r3', 'rango', None, self.atAP, [10, 30])
        r4 = kmod.Rverifica('r4', 'rango', None, self.atLP, [100, 200])
        self.reglas = [r1, r2, r3, r4]


class Versicolor(Flor):

    def __init__(self):
        super(Versicolor, self).__init__('versicolor')

        r1 = kmod.Rverifica('r1', 'rango', None, self.atAS, [10, 30])
        r2 = kmod.Rverifica('r2', 'rango', None, self.atLS, [100, 200])
        r3 = kmod.Rverifica('r3', 'rango', None, self.atAP, [10, 30])
        r4 = kmod.Rverifica('r4', 'rango', None, self.atLP, [100, 200])
        self.reglas = [r1, r2, r3, r4]


#-----------------------FUNCIONES----------------------------------------------
def clases():
    """Crea una lista de clases candidatas de la base de conocimiento."""
    return Setosa(), Virginica(), Versicolor()


def create_initial_object():
    "Create iris initial object."
    initial_values = (25, 110, 30, 95)
    features = (kmod.Caracteristica(att, val)
                for att, val in zip(Flor.atributos, initial_values))
    return kmod.Objeto('obj', features)
