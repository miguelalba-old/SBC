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
class Flor(Clase):
    '''Describe los atributos por los que se caracterizar� a un fruto.
    '''
    def __init__(self,nombre):
        '''
        @param nombre: Nombre de la flor
        '''
        Clase.__init__(self,nombre=nombre)

        self.atAS=Atributo('Ancho sepalo','int','mm')
        self.atLS=Atributo('Largo sepalo','int','mm')
        self.atAP=Atributo('Ancho petalo','int','mm')
        self.atLP=Atributo('Largo petalo','int','mm')


        #Se establece la lista de atributos que posee esta clase
        self.atributos=[self.atAS,self.atLS,self.atAP,self.atLP]

#Setosa,Virginica, Versicolor
class Setosa(Flor):
    '''
    El objeto es una naranja si su color es naranja, el peso
    debe de estar en un rango determinado y el diametro debe
    de estar en un rango determinado.

    '''
    def __init__(self):
        Flor.__init__(self,nombre='setosa')# Se inicia con el nombre naranja
        #Reglas que debe de verificar la naranj
        r1=Rverifica(idRegla='r1',tipo='rango',subtipo=None,atributo=self.atAS,valorEsperado=[10,30])
        r2=Rverifica(idRegla='r2',tipo='rango',subtipo=None,atributo=self.atLS,valorEsperado=[100,120])
        r3=Rverifica(idRegla='r3',tipo='rango',subtipo=None,atributo=self.atAP,valorEsperado=[10,40])
        r4=Rverifica(idRegla='r4',tipo='rango',subtipo=None,atributo=self.atLP,valorEsperado=[90,100])
        self.reglas=[r1,r2,r3,r4]
        pass

class Virginica(Flor):
    def __init__(self):
        Flor.__init__(self,nombre='vrginica')
        r1=Rverifica(idRegla='r1',tipo='rango',subtipo=None,atributo=self.atAS,valorEsperado=[10,30])
        r2=Rverifica(idRegla='r2',tipo='rango',subtipo=None,atributo=self.atLS,valorEsperado=[100,200])
        r3=Rverifica(idRegla='r3',tipo='rango',subtipo=None,atributo=self.atAP,valorEsperado=[10,30])
        r4=Rverifica(idRegla='r4',tipo='rango',subtipo=None,atributo=self.atLP,valorEsperado=[100,200])

        self.reglas=[r1,r2,r3,r4]


class Versicolor(Flor):
    def __init__(self):
        Flor.__init__(self,nombre='versicolor')
        r1=Rverifica(idRegla='r1',tipo='rango',subtipo=None,atributo=self.atAS,valorEsperado=[10,30])
        r2=Rverifica(idRegla='r2',tipo='rango',subtipo=None,atributo=self.atLS,valorEsperado=[100,200])
        r3=Rverifica(idRegla='r3',tipo='rango',subtipo=None,atributo=self.atAP,valorEsperado=[10,30])
        r4=Rverifica(idRegla='r4',tipo='rango',subtipo=None,atributo=self.atLP,valorEsperado=[100,200])
        self.reglas=[r1,r2,r3,r4]


#-----------------------FUNCIONES----------------------------------------------
def clases():
    '''
    Crea una lista de clases candidatas de la base de conocimiento.
    '''
    #Setosa,Virginica, Versicolor
    setosa=Setosa()
    virginica=Virginica()
    versicolor=Versicolor()
    lClases=[setosa,virginica,versicolor]
    return lClases


if __name__ == '__main__':
    cont='s'
    while cont=='s':
        ej=input('Entre la prueba (1,2,3,4,5):' )

        if ej==1:#Crea la lista de atributos que va a usar la base de conocimiento
            atributos=creaAtributosBC([('atAS','int','mm'),('atLS','int','mm'),('atAP','int','mm'),('atLP','int','mm')])
            print atributos
            for at in atributos:
                print at.nombre, at.tipo, at.unidad

        if ej==2:#Crear un objeto porporcionando una lista de atributos
            lcts=[]
            ct1=Caracteristica(Atributo('atAS','int','mm'),30)
            lcts.append(ct1)
            ct2=Caracteristica(Atributo('atAP','int','mm'),60)
            lcts.append(ct2)
            ob=Objeto('ob1',lcts) #Crea el objeto
            for ct in ob.caracteristicas:
                print ct.atributo.nombre,ct.atributo.tipo, ct.valor,ct.atributo.unidad
            print
            ob.describeObjeto()
            #print clases()
        if ej==25:#Crear un conjunto de caracter�sticas
            c1=Caracteristica(Atributo('atAS','int','mm'),30)
            print c1.atributo.nombre, c1.atributo.tipo,c1.atributo.unidad,c1.valor
            pass
        if ej==3:#Crea un objeto pasando su identificador y los valores de los atributos

            lct=[[Atributo('atAS','int','mm'),30],[Atributo('atAP','int','mm'),30],[Atributo('atLP','int','mm'),45]]
            print lct
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

            cVirginica=Virginica()
            print 'descripcion de Naranja', cVirginica.descripcion()
            lct=[[Atributo('Ancho Sepalo','int','mm'),30],[Atributo('Largo sepalo','int','mm'),30],[Atributo('Ancho petalo','int','mm'),45]]
            print lct
            llct=creaCaracteristicas(lct)#Se crean instancias de la lista de atributos


            ob=Objeto('p1',llct)#se crea un objeto a partir de las instancias de la lista de atributos
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
            rb=buscaReglaComparableEnUnaClase(ob.caracteristicas[2],cVirginica)

        cont = raw_input('Desea continuar(s/n): ')

