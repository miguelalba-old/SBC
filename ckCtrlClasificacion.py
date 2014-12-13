#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sun Jan 19 10:28:45 2014

@author: acalvo
"""
from PyQt4 import QtGui
#from PyQt4 import QtCore

import ckModApClasificacion as ma


def eventClasificar(clasificacionDlg):
    pass
    print 'Objeto:', clasificacionDlg.objeto
    print '================================\n'
    mp=ma.MetodoPoda(clasificacionDlg.objeto) #Se crea la instancia del m�todo de la poda
    r,exp=mp.execute()#se ejecuta el m�todo
    clasificacionDlg.results_widget.clear()#Se borra la explicaci�n
    clasificacionDlg.results_widget.appendPlainText(exp)#Se presenta la nueva explicaci�n
    clasificacionDlg.results_widget.moveCursor(QtGui.QTextCursor.Start)
    cs=[]
    for cc in r:
        print '         ->',cc.nombre
        cs.append(cc.nombre)
    clasificacionDlg.selected_class_widget.clear()
    clasificacionDlg.selected_class_widget.addItems(cs) #Se a�aden las clases resultado de la clasificaci�n
                                                                # al control listbox para que lo presente.
    return



