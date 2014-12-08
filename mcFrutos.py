#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sun Jan 19 12:19:10 2014

@author: acalvo
"""

import kmod


#----LAS CLASES DE LA BASE DE CONOCIMIENTO DE FRUTOS-----------
class Fruto(kmod.Clase):
    """Describe los atributos por los que se caracterizará a un fruto."""

    color = kmod.Atributo('color', 'str', None)
    diametro = kmod.Atributo('diametro', 'int', 'cm')
    peso = kmod.Atributo('peso', 'int', 'gr')

    atributos = [color, peso, diametro]

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


if __name__ == '__main__':
    cont='s'
    while cont=='s':
        ej=input('Entre la prueba (1,2,3,4,5):' )

        if ej==1:#Crea la lista de atributos que va a usar la base de conocimiento
            atributos=kmod.creaAtributosBC([('diametro','int','cm'),('color','str',None),('peso','int','gr')])
            print atributos
            for at in atributos:
                print at.nombre, at.tipo, at.unidad

        if ej==2:#Crear un objeto porporcionando una lista de atributos
            lcts=[]
            ct1=kmod.Caracteristica(kmod.Atributo('diametro','int','cm'),30)
            lcts.append(ct1)
            ct2=kmod.Caracteristica(kmod.Atributo('peso','int','gr'),60)
            lcts.append(ct2)
            ob=kmod.Objeto('ob1',lcts) #Crea el objeto
            for ct in ob.caracteristicas:
                print ct.atributo.nombre,ct.atributo.tipo, ct.valor,ct.atributo.unidad
            print
            ob.describeObjeto()
            #print clases()
        if ej==25:#Crear un conjunto de características
            c1=kmod.Caracteristica(kmod.Atributo('diametro','int','cm'),30)
            print c1.atributo.nombre, c1.atributo.tipo,c1.atributo.unidad,c1.valor
            pass
        if ej==3:#Crea un objeto pasando su identificador y los valores de los atributos

            lct=[[kmod.Atributo('diametro','int','cm'),30],[kmod.Atributo('peso','int','gr'),30],[kmod.Atributo('color','str',None),'verde']]
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
            #Se crean instancias de atributos a usar
            atColor=kmod.Atributo('color','str',None)
            atDiametro=kmod.Atributo('diametro','int','cm')
            atPeso=kmod.Atributo('peso','int','gr')
            #Se crear reglas de tipo verifica
            #r1=Rverifica(idRegla='r1',tipo='igual',subtipo=None,atributo=atColor,valorEsperado='rojo')
            #r2=Rverifica(idRegla='r2',tipo='rango',subtipo=None,atributo=atDiametro,valorEsperado=[10,30])
            #r3=Rverifica(idRegla='r3',tipo='rango',subtipo=None,atributo=atPeso,valorEsperado=[100,200])
            #reglas=[r1,r2,r3]
            cNaranja=Naranja()
            print 'descripcion de Naranja', cNaranja.descripcion()


            ob=kmod.Objeto('p1',kmod.creaCaracteristicas([[kmod.Atributo('peso','int','gr'),150],[kmod.Atributo('diametro','int','cm'),15],[kmod.Atributo('color','str',None),'verde']]))#se crea un objeto a partir de las instancias de la lista de atributos
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
            rb=kmod.buscaReglaComparableEnUnaClase(ob.caracteristicas[2],cNaranja)

        cont = raw_input('Desea continuar(s/n): ')

