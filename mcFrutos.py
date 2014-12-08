#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sun Jan 19 12:19:10 2014

@author: acalvo
"""

from kmod import Clase
from kmod import Regla
from kmod import Rverifica
from kmod import Objeto
from kmod import Atributo
from kmod import Caracteristica
from kmod import creaCaracteristicas
from kmod import creaAtributosBC
from kmod import buscaReglaComparableEnUnaClase


#----LAS CLASES DE LA BASE DE CONOCIMIENTO DE FRUTOS-----------
class Fruto(Clase):
    '''Describe los atributos por los que se caracterizará a un fruto.
    '''
    def __init__(self,nombre):
        '''
        @param nombre: Nombre del fruto
        '''
        Clase.__init__(self,nombre=nombre)

        atColor=Atributo('color','str',None)
        atDiametro=Atributo('diametro','int','cm')
        atPeso=Atributo('peso','int','gr')
        #Se establece la lista de atributos que posee esta clase
        self.atributos=[atColor,atPeso,atDiametro]

class Naranja(Fruto):
    '''
    El objeto es una naranja si su color es naranja, el peso
    debe de estar en un rango determinado y el diametro debe
    de estar en un rango determinado.

    '''
    def __init__(self):
        Fruto.__init__(self,nombre='naranja')# Se inicia con el nombre naranja
        #Reglas que debe de verificar la naranja
        atColor=Atributo('color','str',None)
        atDiametro=Atributo('diametro','int','cm')
        atPeso=Atributo('peso','int','gr')

        r1=Rverifica(idRegla='r1',tipo='igual',subtipo=None,atributo=atColor,valorEsperado='naranja')
        #El diametro debe de estar entre 10 y 30
        r2=Rverifica(idRegla='r2',tipo='rango',subtipo=None,atributo=atDiametro,valorEsperado=[10,30])
        #el peso debe de estar entre 100 y 200
        r3=Rverifica(idRegla='r3',tipo='rango',subtipo=None,atributo=atPeso,valorEsperado=[100,200])
        self.reglas=[r1,r2,r3]
        pass

class Limon(Fruto):
    def __init__(self):
        Fruto.__init__(self,nombre='limon')
        atColor=Atributo('color','str',None)
        atDiametro=Atributo('diametro','int','cm')
        atPeso=Atributo('peso','int','gr')
        r1=Rverifica(idRegla='r1',tipo='igual',subtipo=None,atributo=atColor,valorEsperado='amarillo')
        r2=Rverifica(idRegla='r2',tipo='rango',subtipo=None,atributo=atDiametro,valorEsperado=[10,30])
        r3=Rverifica(idRegla='r3',tipo='rango',subtipo=None,atributo=atPeso,valorEsperado=[100,200])
        self.reglas=[r1,r2,r3]


class Sandia(Fruto):
    def __init__(self):
        Fruto.__init__(self,nombre='sandia')
        atColor=Atributo('color','str',None)
        atDiametro=Atributo('diametro','int','cm')
        atPeso=Atributo('peso','int','gr')
        r1=Rverifica(idRegla='r1',tipo='igual',subtipo=None,atributo=atColor,valorEsperado='verde')
        r2=Rverifica(idRegla='r2',tipo='rango',subtipo=None,atributo=atDiametro,valorEsperado=[100,300])
        r3=Rverifica(idRegla='r3',tipo='rango',subtipo=None,atributo=atPeso,valorEsperado=[1000,8000])
        self.reglas=[r1,r2,r3]


#-----------------------FUNCIONES----------------------------------------------

def clases():
    '''
    Crea una lista de clases candidatas de la base de conocimiento.
    '''
    naranja=Naranja()
    limon=Limon()
    sandia=Sandia()
    lClases=[naranja,limon,sandia]
    return lClases


if __name__ == '__main__':
    cont='s'
    while cont=='s':
        ej=input('Entre la prueba (1,2,3,4,5):' )

        if ej==1:#Crea la lista de atributos que va a usar la base de conocimiento
            atributos=creaAtributosBC([('diametro','int','cm'),('color','str',None),('peso','int','gr')])
            print atributos
            for at in atributos:
                print at.nombre, at.tipo, at.unidad

        if ej==2:#Crear un objeto porporcionando una lista de atributos
            lcts=[]
            ct1=Caracteristica(Atributo('diametro','int','cm'),30)
            lcts.append(ct1)
            ct2=Caracteristica(Atributo('peso','int','gr'),60)
            lcts.append(ct2)
            ob=Objeto('ob1',lcts) #Crea el objeto
            for ct in ob.caracteristicas:
                print ct.atributo.nombre,ct.atributo.tipo, ct.valor,ct.atributo.unidad
            print
            ob.describeObjeto()
            #print clases()
        if ej==25:#Crear un conjunto de características
            c1=Caracteristica(Atributo('diametro','int','cm'),30)
            print c1.atributo.nombre, c1.atributo.tipo,c1.atributo.unidad,c1.valor
            pass
        if ej==3:#Crea un objeto pasando su identificador y los valores de los atributos

            lct=[[Atributo('diametro','int','cm'),30],[Atributo('peso','int','gr'),30],[Atributo('color','str',None),'verde']]
            llct=creaCaracteristicas(lct)#Se crean instancias de la lista de atributos
            ob=Objeto('p1',llct)#se crea un objeto a partir de las instancias de la lista de atributos
            ob.describeObjeto()#de describe el objeto.

            pass
        if ej==4:
            print clases()
            for c in clases():
                print c.nombre
            cls=clases()

        if ej==5:
            #Se crean instancias de atributos a usar
            atColor=Atributo('color','str',None)
            atDiametro=Atributo('diametro','int','cm')
            atPeso=Atributo('peso','int','gr')
            #Se crear reglas de tipo verifica
            #r1=Rverifica(idRegla='r1',tipo='igual',subtipo=None,atributo=atColor,valorEsperado='rojo')
            #r2=Rverifica(idRegla='r2',tipo='rango',subtipo=None,atributo=atDiametro,valorEsperado=[10,30])
            #r3=Rverifica(idRegla='r3',tipo='rango',subtipo=None,atributo=atPeso,valorEsperado=[100,200])
            #reglas=[r1,r2,r3]
            cNaranja=Naranja()
            print 'descripcion de Naranja', cNaranja.descripcion()


            ob=Objeto('p1',creaCaracteristicas([[Atributo('peso','int','gr'),150],[Atributo('diametro','int','cm'),15],[Atributo('color','str',None),'verde']]))#se crea un objeto a partir de las instancias de la lista de atributos
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
            rb=buscaReglaComparableEnUnaClase(ob.caracteristicas[2],cNaranja)

        cont = raw_input('Desea continuar(s/n): ')

