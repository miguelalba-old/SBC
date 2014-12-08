#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sat Jan 18 11:29:53 2014

@author: acalvo
"""


import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import ckCtrlClasificacion as ctrl

#import mcIris as mc    #Cambiar al cambiar el MC


class ClasificacionDlg(QtGui.QWidget):
    def __init__(self,objeto=None):
        super(ClasificacionDlg, self).__init__()
        self.objeto=objeto 
        #Label
        labelTableWidgetObjeto=QtGui.QLabel("Objeto",self)  
        labelClasesCandidatas=QtGui.QLabel("Clases candidatas",self)
        labelTextDescripcionClases=QtGui.QLabel(u"Descripción de las clases",self)

        
        labelListClasesSeleccionadas=QtGui.QLabel("Clases seleccionadas",self)
        labelTextjustificacionL=QtGui.QLabel(u"Justificación de la clasificación",self)
        labelTextjustificacionR=QtGui.QLabel(u"",self)
        
        labelComboxMetodo=QtGui.QLabel(u"Método",self)
        
        #Widget
        header = ['ATRIBUTO', 'VALOR']
        #posiblesFallos = Fallos(self,   observables_list, header)
        self.tableWidgetObjeto = QtGui.QTableWidget(len(objeto.caracteristicas),2) #Crea la tabla de elementos observables de dps columnas
        self.tableWidgetObjeto.setColumnWidth(0, 140) #Asignan ancho a las columnas
        self.tableWidgetObjeto.setColumnWidth(1, 200) #Asignan ancho a las columnas
        self.tableWidgetObjeto.setHorizontalHeaderLabels(header) #Asigna etiquetas a las columnas
        #print observables
        i=0
        for at in objeto.caracteristicas:
            print at
            print  at.atributo.nombre,at.atributo.tipo, at.valor,type(at.valor),at.atributo.unidad#,
            item1 = QtGui.QTableWidgetItem(at.atributo.nombre) #Crea un item y le asigna el nombre de la observable
            #item1.setCheckState(QtCore.Qt.Checked) # Establece propiedades a las celdas de la primera columna de la tabla
            item1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled) #Establece propiedades a las celdas de la primera columna

            if at.atributo.tipo=='multiple':#Si el tipo de observable es múltiple creamos un combox
                combobox = QtGui.QComboBox()
                #for j in observables[i].valoresPermitidos:#añadimmos al combox los valeores permitidos
                 #   combobox.addItem(j) 
                #self.tableWidgetPosiblesFallos.setCellWidget(i, 1, combobox)#Establecemos en la celda i el combox
            elif at.atributo.tipo=='boleano':#Si es boleano creamos otro combox con dos posibles valores
                combobox = QtGui.QComboBox()
                combobox.addItem('True') 
                combobox.addItem('False') 
                self.tableWidgetPosiblesFallos.setCellWidget(i, 1, combobox)
            self.tableWidgetObjeto.setItem(i, 0, item1)#Establecemos el item en la columna 0
            if  isinstance(at.valor,int):
                item2 = QtGui.QTableWidgetItem(str(at.valor))
            elif  isinstance(at.valor,str):
                item2 = QtGui.QTableWidgetItem(at.valor)
            self.tableWidgetObjeto.setItem(i, 1, item2)#Establecemos el item en la columna 0
            i+=1
        
        #List
        self.listWidgetClasesCandidatas = QtGui.QListWidget()
        self.cc=ctrl.ma.mc.clases()
        if self.cc is not None:
            pass
            stringList=[]
            for c in self.cc:
                stringList.append(c.nombre)
                
            self.listWidgetClasesCandidatas.addItems(stringList)
            self.listWidgetClasesCandidatas.setCurrentRow(0)
    
        self.plainTextEditDescripcionClases = QtGui.QPlainTextEdit()#Cuadro de texto de descripcion de la clase
        self.listWidgetClasesSeleccionadas = QtGui.QListWidget()
        self.plainTextEditExplicacion = QtGui.QPlainTextEdit()#Cuadro de texto    de la explicación
        
        #Método
        self.comboboxWidgetMetodo = QtGui.QComboBox()
        self.comboboxWidgetMetodo.addItem('Poda')
        self.comboboxWidgetMetodo.addItem('Semi Poda') 
        
        #Botones
        self.clasificarButtom=QtGui.QPushButton('Clasificar')
        self.borrarButtom=QtGui.QPushButton('Borrar')
        self.salirButtom=QtGui.QPushButton('Salir') 
        self.buttomsLayout = QtGui.QHBoxLayout()
        self.buttomsLayout.addStretch()
        self.buttomsLayout.addWidget(self.clasificarButtom)
        self.buttomsLayout.addWidget(self.borrarButtom)
        self.buttomsLayout.addWidget(self.salirButtom)
        self.buttomsLayout.addStretch()
        
        #Rejilla de distribución de los controles
        grid = QtGui.QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(labelTableWidgetObjeto, 0, 0)
        grid.addWidget(self.tableWidgetObjeto, 1, 0)
        grid.addWidget(labelClasesCandidatas, 0, 1)
        grid.addWidget(self.listWidgetClasesCandidatas, 1, 1)
        grid.addWidget(labelTextDescripcionClases, 0, 2)
        grid.addWidget(self.plainTextEditDescripcionClases, 1, 2)
        
        grid.addWidget(labelListClasesSeleccionadas, 2, 0)
        
        
        grid.addWidget(labelTextjustificacionL, 2, 1)
        grid.addWidget(labelTextjustificacionR, 2, 2)
        grid.addWidget(self.plainTextEditExplicacion, 3, 1,3,2)
        
        grid.addWidget(self.listWidgetClasesSeleccionadas, 3, 0)
        
        grid.addWidget(labelComboxMetodo, 4, 0)
        grid.addWidget(self.comboboxWidgetMetodo, 5, 0)
        
        
        
        
        #Diseño principal
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(self.buttomsLayout)
        self.setLayout(mainLayout)
        
    
        self.setGeometry(300, 300, 1200, 800)
        self.setWindowTitle(u"TAREA DE CLASIFICACION")
        self.show()
 
        self.center()
        #Conexiones:
        #==========
        self.listWidgetClasesCandidatas.itemClicked.connect(self.showCc)
        self.tableWidgetObjeto.itemChanged.connect(self.changeObj)
        #self.generarButtom.clicked.connect(self.generar)
        self.clasificarButtom.clicked.connect(self.clasificar)
        self.salirButtom.clicked.connect(self.close)


    def generar(self):
        print 'generar'
        ctrl.eventGenerar(self)
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showCc(self):
        row = self.listWidgetClasesCandidatas.currentRow()
        #print row
        #print self.cc[row].nombre
        #print self.cc[row].descripcion()
        self.plainTextEditDescripcionClases.clear()
        self.plainTextEditDescripcionClases.appendPlainText(self.cc[row].descripcion())
        pass
    
    def changeObj(self):
        '''
        Cambia los valores del objeto tomando los datos de la tabla.
        '''
        print 'objeto cambiado'
        for i in range(self.tableWidgetObjeto.rowCount()):
        #print i
            item1=self.tableWidgetObjeto.item(i,0)
            item2=self.tableWidgetObjeto.item(i,1)
            print item1, item1.text(),self.objeto.caracteristicas[i].atributo.nombre,self.objeto.caracteristicas[i].valor
            print item2, item2.text()
            if self.objeto.caracteristicas[i].atributo.tipo=='str':
                self.objeto.caracteristicas[i].valor=self.tableWidgetObjeto.item(i,1).text()
            elif self.objeto.caracteristicas[i].atributo.tipo=='int':
                print '---->',self.tableWidgetObjeto.item(i,1).text()
                self.objeto.caracteristicas[i].valor=int(self.tableWidgetObjeto.item(i,1).text())

        for at in self.objeto.caracteristicas:
            print at.atributo.nombre, at.valor
            pass
    
    def clasificar(self):
        print 'clasificar'
        ctrl.eventClasificar(self)
    



if __name__ == "__main__":
    import mcFrutos as mc #Cambiar al cambiar el MC
    #import mcIris as mc #Cambiar al cambiar el MC
   
    lct1=[[mc.Atributo('diametro','int','cm'),180],[mc.Atributo('peso','int','gr'),6000],[mc.Atributo('color','str',None),'verde']]
    llct1=mc.creaCaracteristicas(lct1)
    ob1=mc.Objeto('ob2',llct1)
    ob1.describeObjeto()

    
    lct=[[mc.Atributo('Ancho sepalo','int','mm'),25],[mc.Atributo('Largo sepalo','int','mm'),110],[mc.Atributo('Ancho petalo','int','mm'),30],
                  [mc.Atributo('Largo petalo','int','mm'),95]]
    llct=mc.creaCaracteristicas(lct)
    ob=mc.Objeto('ob1',llct)#creo el objeto
    print ob
    ob.describeObjeto()
    app = QtGui.QApplication(sys.argv)
    form = ClasificacionDlg(ob1)
    sys.exit(app.exec_())


 