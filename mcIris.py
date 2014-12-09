#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sun Jan 19 12:19:10 2014

@author: acalvo
"""

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


if __name__ == '__main__':
    cont='s'
    while cont=='s':
        ej=input('Entre la prueba (1,2,3,4,5):' )

        if ej==1:#Crea la lista de atributos que va a usar la base de conocimiento
            atributos=kmod.creaAtributosBC([('atAS','int','mm'),('atLS','int','mm'),('atAP','int','mm'),('atLP','int','mm')])
            print atributos
            for at in atributos:
                print at.nombre, at.tipo, at.unidad

        if ej==2:#Crear un objeto porporcionando una lista de atributos
            lcts=[]
            ct1=kmod.Caracteristica(kmod.Atributo('atAS','int','mm'),30)
            lcts.append(ct1)
            ct2=kmod.Caracteristica(kmod.Atributo('atAP','int','mm'),60)
            lcts.append(ct2)
            ob=kmod.Objeto('ob1',lcts) #Crea el objeto
            for ct in ob.caracteristicas:
                print ct.atributo.nombre,ct.atributo.tipo, ct.valor,ct.atributo.unidad
            print
            ob.describeObjeto()
            #print clases()
        if ej==25:#Crear un conjunto de características
            c1=kmod.Caracteristica(kmod.Atributo('atAS','int','mm'),30)
            print c1.atributo.nombre, c1.atributo.tipo,c1.atributo.unidad,c1.valor
            pass
        if ej==3:#Crea un objeto pasando su identificador y los valores de los atributos

            lct=[[kmod.Atributo('atAS','int','mm'),30],[kmod.Atributo('atAP','int','mm'),30],[kmod.Atributo('atLP','int','mm'),45]]
            print lct
            llct=kmod.creaCaracteristicas(lct)#Se crean instancias de la lista de atributos
            ob=kmod.Objeto('p1',llct)#se crea un objeto a partir de las instancias de la lista de atributos
            ob.describeObjeto()#de describe el objeto.

            pass
        if ej==4:
            print clases()
            for c in clases():
                print c.nombre
            cls=clases()

        if ej==5:

            cVirginica=Virginica()
            print 'descripcion de Naranja', cVirginica.descripcion()
            lct=[[kmod.Atributo('Ancho Sepalo','int','mm'),30],[kmod.Atributo('Largo sepalo','int','mm'),30],[kmod.Atributo('Ancho petalo','int','mm'),45]]
            print lct
            llct=kmod.creaCaracteristicas(lct)#Se crean instancias de la lista de atributos


            ob=kmod.Objeto('p1',llct)#se crea un objeto a partir de las instancias de la lista de atributos
            ob.describeObjeto()#de describe el objeto.

            #r2.descripcion()
            #print r2.execute(ob.atributos[1])

            #Probar si los atributos de un objeto satisface una regla comparable de una clase
            #Buscar una ragla comparable para un atributo de una regla
            #for r in cNaranja.reglas:
            #    if r.atributo.nombre==ob.atributos[1].nombre:
            #        rb=r
            #        break

            #print rb.atributo.nombre
            #print
            #print 'buscando regla'
            rb=kmod.buscaReglaComparableEnUnaClase(ob.caracteristicas[2],cVirginica)

        cont = raw_input('Desea continuar(s/n): ')

