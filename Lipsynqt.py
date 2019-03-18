import sys
from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.uic import loadUi

if __name__ == '__main__':
    # create the QApplication that will manage this window
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Lipsynqt")

    # create a window
    main_window = loadUi(Path(__file__).parent/"Lipsynqt.ui")
    main_window.show()
    # execute the application
    sys.exit(app.exec_())
