#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from view import View


class Controller(object):

    def __init__(self, model):
        self.model = model
        self.view = View(self, model)
        self.view.create_ui()
        self.view.update_candidate_classes_widget()

    def show_candidate_classes(self):
        """Update the candidate_classes_widget."""
        self.view.update_candidate_classes_widget()

    def change_object(self, feature_num, feature_val):
        """Change a feature of the object.
        @param feature_num: Number of the feature in the list of features.
        @param feature_val: Feature value.
        """
        feature = self.model.objeto.caracteristicas[feature_num]
        if feature.atributo.tipo == 'int':
            feature.valor = int(feature_val)
        else:
            feature.valor = feature_val

    def classify(self):
        """Classify current object."""
        self.model.classify()

    def clear(self):
        """Clear the results_widget."""
        self.view.results_widget.clear()
