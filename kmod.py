# -*- coding: iso-8859-1 -*-


class Clase(object):
    u"""Clase en la jerarquía más alta."""

    def __init__(self,nombre):
        u'''
        @param: Nombre de la clase.
        '''

        self.nombre=nombre #La clase tiene un nombre
        self.reglas=[]#Lista de reglas que caracteriza a la clase
        #self.reglas=reglas #los elementos de la clase deben de cumplir unas reglas

    def descripcion(self):
        """Devuelve el texto de la descripción de una clase."""

        descripcion=u''
        #print 'Nombre: ', self.nombre
        descripcion+=self.nombre+'\n'
        for r in self.reglas:
            #print r.idRegla,r.tipo, r.subtipo, r.atributo.nombre, r.valorEsperado
            descripcion+=r.idRegla+' '+r.tipo+' '+ 'None' +' ' + r.atributo.nombre+' '
            if isinstance(r.valorEsperado,str):
                descripcion+=' '+r.valorEsperado+'\n'
            elif isinstance(r.valorEsperado,int)or isinstance(r.valorEsperado,float):
                descripcion+=' '+str(r.valorEsperado)+'\n'
            elif isinstance(r.valorEsperado,list):
                for i in r.valorEsperado:
                    descripcion+=' '+str(i)+' '
                descripcion+='\n'
        return descripcion
