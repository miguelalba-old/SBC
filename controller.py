#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from view import View


class Controller(object):

    def __init__(self, model):
        self.model = model
        self.view = View(self, model)
        self.view.create_ui()

    def show_candidate_classes(self):
        self.view.update_candidate_classes_widget()

    def change_object(self, feature_num, feature_val):
        feature = self.model.objeto.caracteristicas[feature_num]
        if feature.atributo.tipo == 'int':
            feature.valor = int(feature_val)
        else:
            feature.valor = feature_val

    def classify(self):
        self.model.classify()

    def clear(self):
        self.view.results_widget.clear()
