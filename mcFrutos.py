# -*- coding: iso-8859-1 -*-

import kmod


#----LAS CLASES DE LA BASE DE CONOCIMIENTO DE FRUTOS-----------
class Fruto(kmod.Clase):
    """Describe los atributos por los que se caracterizará a un fruto."""

    color = kmod.Atributo('color', 'str', None)
    diametro = kmod.Atributo('diametro', 'int', 'cm')
    peso = kmod.Atributo('peso', 'int', 'gr')

    atributos = (diametro, peso, color)

    def __init__(self,nombre):
        '''
        @param nombre: Nombre del fruto
        '''
        kmod.Clase.__init__(self,nombre=nombre)


class Naranja(Fruto):
    '''
    El objeto es una naranja si su color es naranja, el peso
    debe de estar en un rango determinado y el diametro debe
    de estar en un rango determinado.

    '''
    def __init__(self):
        super(Naranja, self).__init__('naranja')

        r1 = kmod.Rverifica('r1', 'igual', None, self.color, 'naranja')
        r2 = kmod.Rverifica('r2', 'rango', None, self.diametro, [10,30])
        r3 = kmod.Rverifica('r3', 'rango', None, self.peso, [100,200])
        self.reglas=[r1,r2,r3]


class Limon(Fruto):
    def __init__(self):
        super(Limon, self).__init__('limon')

        r1 = kmod.Rverifica('r1', 'igual', None, self.color, 'amarillo')
        r2 = kmod.Rverifica('r2', 'rango', None, self.diametro, [10,30])
        r3 = kmod.Rverifica('r3', 'rango', None, self.peso, [100,200])
        self.reglas=[r1,r2,r3]


class Sandia(Fruto):
    def __init__(self):
        super(Sandia, self).__init__('sandia')

        r1 = kmod.Rverifica('r1', 'igual', None, self.color, 'verde')
        r2 = kmod.Rverifica('r2', 'rango', None, self.diametro, [100,300])
        r3 = kmod.Rverifica('r3', 'rango', None, self.peso, [1000,8000])
        self.reglas=[r1,r2,r3]


#-----------------------FUNCIONES----------------------------------------------

def clases():
    """Crea una lista de clases candidatas de la base de conocimiento."""
    return Naranja(), Limon(), Sandia()


def create_initial_object():
    "Create fruit initial object."
    initial_values = (180, 6000, 'verde')
    features = (kmod.Caracteristica(att, val)
                for att, val in zip(Fruto.atributos, initial_values))
    return kmod.Objeto('obj', features)
