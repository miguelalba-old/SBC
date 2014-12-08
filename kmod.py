# -*- coding: iso-8859-1 -*-


class Clase(object):

    u"""Clase en la jerarquía más alta."""

    def __init__(self, nombre):
        u'''
        @param: Nombre de la clase.
        '''

        self.nombre = nombre  # La clase tiene un nombre
        self.reglas = []  # Lista de reglas que caracteriza a la clase
        # self.reglas=reglas #los elementos de la clase deben de cumplir unas
        # reglas

    def descripcion(self):
        """Devuelve el texto de la descripción de una clase."""

        descripcion = u''
        descripcion += self.nombre + '\n'
        descripcion += '\n'.join([rule.descripcion() for rule in self.reglas])
        return descripcion


# ----------------------TIPOS DE REGLAS----------------------------------------
class Regla(object):

    '''
    Describe aspectos generales de una regla
    '''

    def __init__(self, idRegla, tipo):
        self.idRegla = idRegla
        self.tipo = tipo


class Rverifica(Regla):

    '''
    Esta regla verifica si los valores de un atributo satisfacen
    las restricciones de la regla de la clase. P.e.
    -  La clase naranja debe de tener el atributo cuyo nombre es color naranja
    '''

    def __init__(self, idRegla, tipo, subtipo, atributo, valorEsperado):
        Regla.__init__(self, idRegla, tipo)
        self.subtipo = subtipo
        self.atributo = atributo
        self.valorEsperado = valorEsperado

    def execute(self, at):
        '''
        Verifica que un atributo-valor satisface la regla de una clase.
        '''
        # Deben de coincidor los nombres de los atributos
        if self.atributo.nombre == at.nombre:
            if self.tipo == 'igual':  # Si el atributo es de tipo igual
                return self.valorEsperado == at.valor

            if self.tipo == 'rango':  # Si el atributo es de tipo rango
                print 'evaluo rango'
                return at.valor in range(self.valorEsperado[0],
                                         self.valorEsperado[1])
        else:
            return None

    def descripcion(self):
        descripcion = u''
        valor_esperado = ''
        if isinstance(self.valorEsperado, str):
            valor_esperado = self.valorEsperado
        elif isinstance(self.valorEsperado, (int, float)):
            valor_esperado = str(self.valorEsperado)
        elif isinstance(self.valorEsperado, list):
            valor_esperado = ' '.join([str(i) for i in self.valorEsperado])

        campos_regla = (self.idRegla, self.tipo, self.atributo.nombre, 'None',
                        valor_esperado)
        descripcion = ' '.join(campos_regla)

        return descripcion


# -------------------------LOS OBJETOS-----------------------------------------
class Objeto():

    def __init__(self, identificador, caracteristicas):
        """Se inicia la clase especificando el nombre y los atributos del
        objeto"""
        print 'e va a crear'
        self.identificador = identificador
        self.caracteristicas = caracteristicas
        self.clase = None
        print 'objeto creado'

    def describeObjeto(self):
        print 'Identificador= ', self.identificador
        for ct in self.caracteristicas:
            print ct.atributo.nombre, ct.atributo.tipo, ct.valor,
            print ct.atributo.unidad


class Atributo():

    '''Clase Atributo. permite especificar las propiedades
    de los atributos que van a usarse en la base de conocimiento para
    describir un objeto.
    '''

    def __init__(self, nombre, tipo, unidad):
        self.nombre = nombre
        self.tipo = tipo
        self.unidad = unidad


class Caracteristica():

    u'''Clase característica que establece el valor para un atributo'''

    def __init__(self, atributo, valor):
        self.atributo = atributo
        self.valor = valor


# Funciones
def creaCaracteristicas(lct=[[Atributo('diametro', 'int', 'cm'), 30]]):
    '''Dada una lista de atributos en forma de lista donde
    se especifica el  atributo y el valor
    se crean las inancias de dichos atributos
    @return: Devuelve una lista de caracteristicas.
    '''
    print lct
    carats = []
    for ct in lct:
        print ct[0], ct[1]
        caract = Caracteristica(ct[0], ct[1])
        carats.append(caract)
    return carats


def creaAtributosBC(lat=[('diametro', 'int', 'unidad')]):
    '''Dada una lista de atributos en forma de tupla donde
    se especifica el nombre del atributo, el tipo se  obtiene la lista de
    atributos con la que se trabaja en la base de conocimiento.'''
    return [Atributo(at[0], at[1], at[2]) for at in lat]


def buscaReglaComparableEnUnaClase(ct, clase):
    for r in clase.reglas:
        if r.atributo.nombre == ct.atributo.nombre:
            rb = r
            break

    print rb.atributo.nombre
    return rb
