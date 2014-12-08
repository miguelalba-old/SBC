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


#-----------------------TIPOS DE REGLAS----------------------------------------
class Regla(object):
    '''
    Describe aspectos generales de una regla
    '''
    def __init__(self,idRegla,tipo):
        self.idRegla=idRegla
        self.tipo=tipo
        pass


class Rverifica(Regla):
    '''
    Esta regla verifica si los valores de un atributo satisfacen
    las restricciones de la regla de la clase. P.e.
    -  La clase naranja debe de tener el atributo cuyo nombre es color naranja
    '''
    def __init__(self,idRegla,tipo,subtipo,atributo,valorEsperado):
        Regla.__init__(self,idRegla,tipo)
        self.subtipo=subtipo
        self.atributo=atributo
        self.valorEsperado=valorEsperado
    def execute(self,at):
        '''
        Verifica que un atributo-valor satisface la regla de una clase.
        '''
        if self.atributo.nombre==at.nombre: #Deben de coincidor los nombres de los atributos

            if self.tipo=='igual':#Si el atributo es de tipo igual
                if self.valorEsperado==at.valor:
                    return True
                else:
                    return False

            if self.tipo=='rango':#Si el atributo es de tipo rango
                print 'evaluo rango'
                if at.valor <self.valorEsperado[1] and at.valor >=self.valorEsperado[0]:
                    return True
                else:
                    return False
        else:
            return None

    def descripcion(self):
        descripcion=u''
        descripcion+='idRegla: '+self.idRegla+'\n'
        descripcion+='Tipo: '+self.tipo+'\n'
        descripcion+='Atributo: '+self.atributo.nombre+'\n'
        if isinstance(self.valorEsperado,str):
            descripcion+='Valor esperado: '+self.valorEsperado+'\n'
        elif isinstance(self.valorEsperado,int) or isinstance(self.valorEsperado,float):
            descripcion+='Valor esperado: '+str(self.valorEsperado)+'\n'
        elif isinstance(self.valorEsperado,list) :
            for ve in self.valorEsperado:
                descripcion+='Valor esperado: '+str(self.valorEsperado)+'  '

        return descripcion


#--------------------------LOS OBJETOS-----------------------------------------
class Objeto():
    def __init__(self,identificador,caracteristicas):
        '''Se inicia la clase especificando el nombre y los atributos del objeto'''
        print 'e va a crear'
        self.identificador=identificador
        self.caracteristicas=caracteristicas
        self.clase=None
        print 'objeto creado'
        pass
    def describeObjeto(self):
        print 'Identificador= ',self.identificador
        for ct in self.caracteristicas:
            print ct.atributo.nombre, ct.atributo.tipo, ct.valor, ct.atributo.unidad
