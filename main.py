#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
import time

from Source.VoltranWindow import VoltranMainWindow

app = QtGui.QApplication(sys.argv)



window = VoltranMainWindow()
window.show()

# Start/Exit Phase
exit_code = app.exec_()
print "App exited with code", exit_code
sys.exit(exit_code)
