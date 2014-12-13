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

# import mcIris as mc    #Cambiar al cambiar el MC


class ClasificacionDlg(QtGui.QWidget):

    def __init__(self, objeto=None):
        super(ClasificacionDlg, self).__init__()
        self.objeto = objeto

        # boxes labels
        object_label = QtGui.QLabel("Objeto", self)
        candidate_classes_label = QtGui.QLabel("Clases candidatas", self)
        class_description_label = QtGui.QLabel(
            u"Descripción de las clases", self)
        selected_class_label = QtGui.QLabel("Clases seleccionadas", self)
        results_label_L = QtGui.QLabel(
            u"Justificación de la clasificación", self)
        results_label_R = QtGui.QLabel(u"", self)
        method_label = QtGui.QLabel(u"Método", self)

        # Widget
        table_headers = ['ATRIBUTO', 'VALOR']

        # Crea la tabla de elementos observables de dos columnas
        self.object_widget = QtGui.QTableWidget(
            len(objeto.caracteristicas), 2)
        self.object_widget.setColumnWidth(0, 140)  # 1st col width
        self.object_widget.setColumnWidth(1, 200)  # 2nd col width
        self.object_widget.setHorizontalHeaderLabels(table_headers)

        for num_feature, feature in enumerate(objeto.caracteristicas):
            item1 = QtGui.QTableWidgetItem(feature.atributo.nombre)
            item1.setFlags(
                QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            self.object_widget.setItem(num_feature, 0, item1)

            item2 = QtGui.QTableWidgetItem(str(feature.valor))
            self.object_widget.setItem(num_feature, 1, item2)

        # Candidate classes box
        self.candidate_classes_widget = QtGui.QListWidget()
        self.candidate_classes = ctrl.ma.mc.clases()
        if self.candidate_classes:
            classes_names = [c.nombre for c in self.candidate_classes]
            self.candidate_classes_widget.addItems(classes_names)
            self.candidate_classes_widget.setCurrentRow(0)

        # Class description box
        self.class_description_widget = QtGui.QPlainTextEdit()

        # Selected class box
        self.selected_class_widget = QtGui.QListWidget()

        # Results box (widget with the classification output)
        self.results_widget = QtGui.QPlainTextEdit()

        # Method box
        self.method_widget = QtGui.QComboBox()
        self.method_widget.addItem('Poda')
        self.method_widget.addItem('Semi Poda')

        # Botones
        classify_button = QtGui.QPushButton('Clasificar')
        clear_button = QtGui.QPushButton('Borrar')
        quit_button = QtGui.QPushButton('Salir')

        buttons_layout = QtGui.QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(classify_button)
        buttons_layout.addWidget(clear_button)
        buttons_layout.addWidget(quit_button)
        buttons_layout.addStretch()

        # Rejilla de distribución de los controles
        grid = QtGui.QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(object_label, 0, 0)
        grid.addWidget(self.object_widget, 1, 0)
        grid.addWidget(candidate_classes_label, 0, 1)
        grid.addWidget(self.candidate_classes_widget, 1, 1)
        grid.addWidget(class_description_label, 0, 2)
        grid.addWidget(self.class_description_widget, 1, 2)

        grid.addWidget(selected_class_label, 2, 0)

        grid.addWidget(results_label_L, 2, 1)
        grid.addWidget(results_label_R, 2, 2)
        grid.addWidget(self.results_widget, 3, 1, 3, 2)

        grid.addWidget(self.selected_class_widget, 3, 0)

        grid.addWidget(method_label, 4, 0)
        grid.addWidget(self.method_widget, 5, 0)

        # Diseño principal
        main_layout = QtGui.QVBoxLayout()
        main_layout.addLayout(grid)
        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)

        self.setGeometry(300, 300, 1200, 800)
        self.setWindowTitle(u"TAREA DE CLASIFICACION")
        self.show()

        self.center()

        # Conexiones:
        # ==========
        self.candidate_classes_widget.itemClicked.connect(
            self.show_candidate_classes)
        self.object_widget.itemChanged.connect(self.change_object)
        classify_button.clicked.connect(self.classify)
        clear_button.clicked.connect(self.results_widget.clear)
        quit_button.clicked.connect(self.close)

    def center(self):
        "Center dialog"
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def show_candidate_classes(self):
        "Update candidate classes box"
        row = self.candidate_classes_widget.currentRow()
        self.class_description_widget.clear()
        self.class_description_widget.appendPlainText(
            self.candidate_classes[row].descripcion())

    def change_object(self):
        "Cambia los valores del objeto tomando los datos de la tabla."
        for i in range(self.object_widget.rowCount()):
            feature = self.objeto.caracteristicas[i]
            feature_value = self.object_widget.item(i, 1).text()
            if feature.atributo.tipo == 'int':
                feature_value = int(feature_value)
            feature.valor = feature_value

    def classify(self):
        "Classification event."
        ctrl.eventClasificar(self)


if __name__ == "__main__":
    import mcFrutos as mc  # Cambiar al cambiar el MC
    # import mcIris as mc #Cambiar al cambiar el MC

    lct1 = [
        [mc.Atributo('diametro', 'int', 'cm'), 180],
        [mc.Atributo('peso', 'int', 'gr'), 6000],
        [mc.Atributo('color', 'str', None), 'verde']]
    llct1 = mc.creaCaracteristicas(lct1)
    ob1 = mc.Objeto('ob2', llct1)
    ob1.describeObjeto()

    lct = [
        [mc.Atributo('Ancho sepalo', 'int', 'mm'), 25],
        [mc.Atributo('Largo sepalo', 'int', 'mm'), 110],
        [mc.Atributo('Ancho petalo', 'int', 'mm'), 30],
        [mc.Atributo('Largo petalo', 'int', 'mm'), 95]]
    llct = mc.creaCaracteristicas(lct)
    ob = mc.Objeto('ob1', llct)  # creo el objeto
    print ob
    ob.describeObjeto()
    app = QtGui.QApplication(sys.argv)
    form = ClasificacionDlg(ob1)
    sys.exit(app.exec_())
