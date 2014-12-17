#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

# import mcFrutos as mc #Cambiar al cambiar el MC
# import mcIris as mc #Cambiar al cambiar el MC
# import mcGlobos as mc
import mcEbola as mc


class Tarea(object):

    def __init__(self):
        self.objetivo = ''
        self.descripcion = ''


class Clasificacion(Tarea):

    def __init__(self, bc, objeto):
        self.objetivo = u'''    '''
        self.objeto = objeto
        self.bc = bc
        self.metodo = 'poda'
        self.salida = None

    def execute(self):
        if self.metodo == 'poda':
            mt = MetodoPoda()


class MetodoPoda():

    """Dado un objeto clasificarlo como perteneciente a una clase."""

    def __init__(self, obj):
        self.obj = obj
        self.clasesCandidatas = []
        self.lAtributosUsados = []
        self.conjuntoNuevosValores = []
        self.explicacion = u''

    def execute(self):
        # Se generan las posibles clases candidatas
        g = Generar(self.obj)
        self.clasesCandidatas = g.execute()
        self.explicacion += u'Se generam las clases candidatas que son:\n'
        self.explicacion += "\n".join(
            [cc.nombre for cc in self.clasesCandidatas])
        self.explicacion += '\n'

        newSolucion = True
        while newSolucion and self.clasesCandidatas:
            esp = Especificar(self.clasesCandidatas, self.lAtributosUsados)
            newLatr = esp.execute()  # Se especifica el nuevo atributo

            if not newLatr == (None, None):  # Si sigue habiendo atributos:
                self.lAtributosUsados = newLatr[1]
                self.explicacion += 'Seleccionamos el atributo {} '.format(
                    newLatr[0].nombre)

                obt = Obtener(self.obj, newLatr[0])
                at = obt.execute()

                self.explicacion += 'con el valor: {}\n'.format(at.valor)
                self.conjuntoNuevosValores.append(at)

                newcc = []
                for cc in self.clasesCandidatas:
                    self.explicacion += '    Probamos la clase candidata {}\n'.format(cc.nombre)
                    eq = Equiparar(cc, self.conjuntoNuevosValores)
                    result, expl = eq.execute()
                    self.explicacion += expl
                    self.explicacion += '      Resultado de equiparar clase candidata {0} {1}\n'.format(cc.nombre, result)
                    if result:
                        newcc.append(cc)

            else:
                newSolucion = False  # No quedan más atributos por explorar
                continue

            self.clasesCandidatas = newcc
            self.explicacion += u'\n Clases candidatas tras la equiparación: '
            for cc in self.clasesCandidatas:
                self.explicacion += ' {0}\n{1}\n'.format(cc.nombre,
                                                         cc.descripcion())
            self.explicacion += '\n'

        return self.clasesCandidatas, self.explicacion


class Inferencia(object):

    def __init__(self):
        pass

    def execute(self):
        pass


class Equiparar(Inferencia):
    ''''''

    def __init__(self, candidata, nuevosValores):
        super(Equiparar, self).__init__()
        self.candidata = candidata
        self.nuevosValores = nuevosValores
        self.explicacion = u''

    def execute(self):
        """
        Equipara una clase candidata con el conjunto de nuevos
        valores devolviendo False si es rechazada la clase candidata.
        """
        for nv in self.nuevosValores:
            self.explicacion += '\t Equiparar el atributo {0}= {1}\n'.format(
                nv.atributo.nombre, nv.valor)

            for r in self.candidata.reglas:
                if r.atributo.nombre == nv.atributo.nombre:
                    if r.tipo == 'igual':
                        if r.valorEsperado != nv.valor:
                            return False, self.explicacion
                    if r.tipo == 'rango':
                        if not (nv.valor < r.valorEsperado[1]
                                and nv.valor >= r.valorEsperado[0]):
                            return False, self.explicacion
        return True, self.explicacion


class Generar(Inferencia):

    """Dado un objeto genera un conjunto de clases candidatas
       Esta inferencia es básica se devuelven todas las clases
       candidatas que ofrece la base de conocimiento.
    """

    def __init__(self, objeto):
        super(Generar, self).__init__()
        self.objeto = objeto

    def execute(self):
        return mc.clases()


class Obtener(Inferencia):

    """Dado un aributo obtener un valor para ese atributo en
       el objeto a clasificar.
    """

    def __init__(self, objeto, atributo):
        super(Obtener, self).__init__()
        self.objeto = objeto
        self.atributo = atributo

    def execute(self):
        for cat in self.objeto.caracteristicas:
            if self.atributo.nombre == cat.atributo.nombre:
                return cat


class Especificar(Inferencia):

    """Dado un conjunto de clases candidatas no vacío
       especifica un atributo para extraer su valor en otra inferencia.
    """

    def __init__(self, clasesCandidatas, lAtributosUsados):
        """
        @param lLlasesCandidatas: Lista de clases candidatas
        @param lAtributosUsados: Lista de atributos ya seleccionados
        """
        super(Especificar, self).__init__()
        self.cc = clasesCandidatas
        self.lAtributosUsados = lAtributosUsados

    def execute(self):
        """Ejecución del método de la inferencia
        @return: Devuelve en una tupla el atributo especificado y la lista de
        atributos ya usados.
        """
        if self.cc:
            for at in self.cc[0].atributos:
                used_attributes = [attribute.nombre
                                   for attribute in self.lAtributosUsados]
                if at.nombre not in used_attributes:
                    self.lAtributosUsados.append(at)
                    return at, self.lAtributosUsados
        return None, None


class Model(object):
    "Application model."

    def __init__(self):
        """Initialize model."""
        self.objeto = mc.create_initial_object()
        self.candidate_classes = mc.clases()
        self.selected_class = None
        self.class_desc = u''  # class description
        self.output = u''  # classification results
        self.view = None

    def classify(self):
        """Classify current object and update the view."""
        pruning_method = MetodoPoda(self.objeto)
        candidate_classes, reason = pruning_method.execute()

        self.view.update_results(reason)
        self.view.update_selected_classes(candidate_classes)
