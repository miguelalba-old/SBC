#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-


from PyQt4 import QtCore
from PyQt4 import QtGui

import controller as ctrl


class View(QtGui.QWidget):

    def __init__(self, controller, model):
        super(View, self).__init__()

        self.controller = controller
        model.view = self  # Register view
        self.model = model

    def create_ui(self):
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

        # Object widget
        table_headers = ['ATRIBUTO', 'VALOR']
        # Crea la tabla de elementos observables de dos columnas
        objeto = self.model.objeto
        self.object_widget = QtGui.QTableWidget(len(objeto.caracteristicas), 2)
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
        candidate_classes = self.model.candidate_classes
        if candidate_classes:
            classes_names = [c.nombre for c in candidate_classes]
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

        # Buttons
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
            self.controller.show_candidate_classes)
        self.object_widget.itemChanged.connect(self.item_changed)
        classify_button.clicked.connect(self.controller.classify)
        clear_button.clicked.connect(self.controller.clear)
        quit_button.clicked.connect(self.close)

    def center(self):
        "Center dialog"
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def update_candidate_classes_widget(self):
        "Update candidate classes box"
        row = self.candidate_classes_widget.currentRow()
        class_description = self.model.candidate_classes[row].descripcion()

        self.class_description_widget.clear()
        self.class_description_widget.appendPlainText(class_description)

    def update_results(self, reason):
        """Update the results_widget."""
        widget = self.results_widget
        widget.clear()
        widget.appendPlainText(reason)
        widget.moveCursor(QtGui.QTextCursor.Start)

    def update_selected_classes(self, candidates):
        """Update selected_class_widget."""
        selected_classes = [candidate.nombre for candidate in candidates]
        widget = self.selected_class_widget
        widget.clear()
        widget.addItems(selected_classes)

    def item_changed(self, item):
        """Event produced when an item from the object table is changed."""
        feature_num = item.row()
        feature_value = item.text()
        self.controller.change_object(feature_num, feature_value)

    def classify(self):
        "Classification event."
        ctrl.eventClasificar(self)
