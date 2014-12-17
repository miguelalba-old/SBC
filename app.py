import sys

from PyQt4 import QtGui

from model import Model
from controller import Controller

app = QtGui.QApplication(sys.argv)
app_model = Model()
app_controller = Controller(app_model)
sys.exit(app.exec_())
