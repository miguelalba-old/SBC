# -*- coding: iso-8859-1 -*-

import kmod


class EstadoPasajero(kmod.Clase):

    temperature = kmod.Atributo('Temperatura Pasajero', 'int', None)
    country = kmod.Atributo('Pais de origen', 'str', None)  # RIESGO, SEGURO
    contact = kmod.Atributo('Contacto con contagiado', 'str', None)  # SI, NO

    atributos = (temperature, country, contact)

    def __init__(self, nombre):
        super(EstadoPasajero, self).__init__(nombre)


class Contagio(EstadoPasajero):

    def __init__(self):
        super(Contagio, self).__init__('Contagio')
        temperature_rule = kmod.Rverifica('r1', 'rango', None,
                                          self.temperature, [37, 40])
        country_rule = kmod.Rverifica('r2', 'igual', None, self.pais, 'RIESGO')
        contact_rule = kmod.Rverifica('r3', 'igual', None, self.contacto, 'SI')
        self.reglas = (temperature_rule, country_rule, contact_rule)


class ProbableContagio(EstadoPasajero):

    def __init__(self):
        super(ProbableContagio, self).__init__('Probable Contagio')
        temperature_rule = kmod.Rverifica('r1', 'rango', None,
                                          self.temperature, [37, 40])
        country_rule = kmod.Rverifica('r2', 'igual', None, self.pais, 'RIESGO')
        contact_rule = kmod.Rverifica('r3', 'igual', None, self.contacto, 'NO')
        self.reglas = (temperature_rule, country_rule, contact_rule)


class RiesgoLeve(EstadoPasajero):

    def __init__(self):
        super(RiesgoLeve, self).__init__('Riesgo Leve')
        temperature_rule = kmod.Rverifica('r1', 'rango', None,
                                          self.temperature, [37, 40])
        country_rule = kmod.Rverifica('r2', 'igual', None, self.pais, 'SEGURO')
        self.reglas = (temperature_rule, country_rule)


class NoContagio(EstadoPasajero):

    def __init__(self):
        super(NoContagio, self).__init__('No Contagio')
        temperature_rule = kmod.Rverifica('r1', 'rango', None,
                                          self.temperatura, [35, 37])
        self.reglas = (temperature_rule,)


def clases():
    return Contagio(), ProbableContagio(), RiesgoLeve(), NoContagio()


def create_initial_object():
    "Create fruit initial object."
    initial_values = (38, 'RIESGO', 'NO')
    features = (kmod.Caracteristica(att, val)
                for att, val in zip(EstadoPasajero.atributos, initial_values))
    return kmod.Objeto('obj', features)
