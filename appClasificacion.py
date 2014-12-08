#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sat Jan 18 11:29:53 2014

@author: acalvo
"""

import sys
from PyQt4 import QtGui
import ckVtsClasificacion
#import mcFrutos as mc #Cambiar al cambiar el MC
import mcIris as mc #Cambiar al cambiar el MC


lct1=[[mc.Atributo('Ancho sepalo','int','mm'),25],[mc.Atributo('Largo sepalo','int','mm'),110],[mc.Atributo('Ancho petalo','int','mm'),30],[mc.Atributo('Largo petalo','int','mm'),95]]
llct1=mc.creaCaracteristicas(lct1)
ob1=mc.Objeto('ob1',llct1)
ob1.describeObjeto()

lct=[[mc.Atributo('diametro','int','cm'),180],[mc.Atributo('peso','int','gr'),6000],[mc.Atributo('color','int',None),'verde']]
llct=mc.creaCaracteristicas(lct)
ob=mc.Objeto('ob2',llct)
ob.describeObjeto()

app = QtGui.QApplication(sys.argv)
form = ckVtsClasificacion.ClasificacionDlg(ob1)
sys.exit(app.exec_())



