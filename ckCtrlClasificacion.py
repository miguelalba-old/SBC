#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from PyQt4 import QtGui

import ckModApClasificacion as ma


def eventClasificar(clasificacionDlg):
    "Classification event"
    pruning_method = ma.MetodoPoda(clasificacionDlg.objeto)
    candidate_classes, reason = pruning_method.execute()

    # Update results_widget
    clasificacionDlg.results_widget.clear()
    clasificacionDlg.results_widget.appendPlainText(reason)
    clasificacionDlg.results_widget.moveCursor(QtGui.QTextCursor.Start)

    # Update selected_class_widget
    selected_classes = [candidate_class.nombre
                        for candidate_class in candidate_classes]
    clasificacionDlg.selected_class_widget.clear()
    clasificacionDlg.selected_class_widget.addItems(selected_classes)
