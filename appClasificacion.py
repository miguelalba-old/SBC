#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
"""
Created on Sat Jan 18 11:29:53 2014

@author: acalvo
"""

import sys
from PyQt4 import QtGui
import ckVtsClasificacion
import kmod


# Flor
lct1 = [
    [kmod.Atributo('Ancho sepalo', 'int', 'mm'), 25],
    [kmod.Atributo('Largo sepalo', 'int', 'mm'), 110],
    [kmod.Atributo('Ancho petalo', 'int', 'mm'), 30],
    [kmod.Atributo('Largo petalo', 'int', 'mm'), 95]]
llct1 = kmod.creaCaracteristicas(lct1)
ob1 = kmod.Objeto('ob1', llct1)
ob1.describeObjeto()

# Fruto
lct = [
    [kmod.Atributo('diametro', 'int', 'cm'), 180],
    [kmod.Atributo('peso', 'int', 'gr'), 6000],
    [kmod.Atributo('color', 'str', None), 'verde']]
llct = kmod.creaCaracteristicas(lct)
ob = kmod.Objeto('ob2', llct)
ob.describeObjeto()

# Globo (mcGlobo)
import mcGlobos
caracteristicas = kmod.creaCaracteristicas(
    ((mcGlobos.EstadoGlobo.color, 'YELLOW'),
     (mcGlobos.EstadoGlobo.size, 'LARGE'),
     (mcGlobos.EstadoGlobo.act, 'STRETCH'),
     (mcGlobos.EstadoGlobo.age, 'ADULT')))
globo = kmod.Objeto('ob3', caracteristicas)
ob.describeObjeto()

# Ebola (mcEbola)
import mcEbola
caracteristicas = kmod.creaCaracteristicas(
    ((mcEbola.EstadoPasajero.temperatura, 38),
     (mcEbola.EstadoPasajero.pais, 'RIESGO'),
     (mcEbola.EstadoPasajero.contacto, 'NO')))
ebola = kmod.Objeto('ob4', caracteristicas)
ob.describeObjeto()



app = QtGui.QApplication(sys.argv)
form = ckVtsClasificacion.ClasificacionDlg(ebola)
sys.exit(app.exec_())
