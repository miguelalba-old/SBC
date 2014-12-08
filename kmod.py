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


class Atributo():
    '''Clase Atributo. permite especificar las propiedades
    de los atributos que van a usarse en la base de conocimiento para
    describir un objeto.
    '''
    def __init__(self,nombre,tipo,unidad):
        self.nombre=nombre
        self.tipo=tipo
        self.unidad=unidad


class Caracteristica():
    u'''Clase característica que establece el valor para un atributo'''
    def __init__(self,atributo,valor):
        self.atributo=atributo
        self.valor=valor


# Funciones
def creaCaracteristicas(lct=[[Atributo('diametro','int','cm'),30]]):
    '''Dada una lista de atributos en forma de lista donde
    se especifica el  atributo y el valor
   se crean las inancias de dichos atributos
    @return: Devuelve una lista de caracteristicas.
    '''
    print lct
    carats=[]
    for ct in lct:
        print ct[0],ct[1]
        caract=Caracteristica(ct[0],ct[1])
        carats.append(caract)
    return carats

def creaAtributosBC(lat=[('diametro','int','unidad')]):
    '''Dada una lista de atributos en forma de tupla donde
    se especifica el nombre del atributo, el tipo se  obtiene la lista de
    atributos con la que se trabaja en la base de conocimiento.'''
    return [Atributo(at[0], at[1], at[2]) for at in lat]


def buscaReglaComparableEnUnaClase(ct,clase):
    for r in clase.reglas:
        if r.atributo.nombre==ct.atributo.nombre:
            rb=r
            break

    print rb.atributo.nombre
    return rb
