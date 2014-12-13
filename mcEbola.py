# -*- coding: iso-8859-1 -*-

import kmod


class EstadoPasajero(kmod.Clase):

    temperatura = kmod.Atributo('Temperatura Pasajero', 'int', None) 
    pais = kmod.Atributo('Pais de origen', 'str', None)  # RIESGO, SEGURO 
    contacto = kmod.Atributo('Contacto con contagiado', 'str', None)  # SI, NO

    atributos = (temperatura, pais, contacto)

    def __init__(self, nombre):
        super(EstadoPasajero, self).__init__(nombre)


class Contagio(EstadoPasajero):
    def __init__(self):
        super(Contagio, self).__init__('Contagio')
        temperatura_rule = kmod.Rverifica('r1', 'rango', None, self.temperatura, [37,40])
        pais_rule = kmod.Rverifica('r2', 'igual', None, self.pais, 'RIESGO')
        contacto_rule = kmod.Rverifica('r3', 'igual', None, self.contacto, 'SI')
        self.reglas = (temperatura_rule, pais_rule, contacto_rule)

class ProbableContagio(EstadoPasajero):
    def __init__(self):
        super(ProbableContagio, self).__init__('Probable Contagio')
        temperatura_rule = kmod.Rverifica('r1', 'rango', None, self.temperatura, [37,40])
        pais_rule = kmod.Rverifica('r2', 'igual', None, self.pais, 'RIESGO')
        contacto_rule = kmod.Rverifica('r3', 'igual', None, self.contacto, 'NO')
        self.reglas = (temperatura_rule, pais_rule, contacto_rule)

class RiesgoLeve(EstadoPasajero):
    def __init__(self):
        super(RiesgoLeve, self).__init__('Riesgo Leve')
        temperatura_rule = kmod.Rverifica('r1', 'rango', None, self.temperatura, [37,40])
        pais_rule = kmod.Rverifica('r2', 'igual', None, self.pais, 'SEGURO')
        self.reglas = (temperatura_rule, pais_rule)

class NoContagio(EstadoPasajero):
    def __init__(self):
        super(NoContagio, self).__init__('No Contagio')
        temperatura_rule = kmod.Rverifica('r1', 'rango', None, self.temperatura, [35,37])
        self.reglas = (temperatura_rule,)


def clases():
    return Contagio(), ProbableContagio(), RiesgoLeve(), NoContagio()
