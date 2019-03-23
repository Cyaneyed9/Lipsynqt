import sys
from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.uic import loadUi

class About_Window(QtWidgets.QMessageBox):
    """The About_Window class extends the QMessageBox class to implement a viable "About" window that includes the license
    by mangling the hell out of the base class.
    """
    def __init__(self, parent):
        # Normal setup of a very stubborn widget
        app = QtWidgets.QApplication.instance()
        name = app.applicationName()+"\n\n"
        description = "A tool for managing a drag show\n\nCopyright (c) 2019 Brian Davis & Brennen Raimer"
        super().__init__(parent = parent, text = name + description)
        file = QtCore.QFile(str(Path(__file__).parent/"LICENSE"))
        if file.open(QtCore.QFile.ReadOnly):
            license = str(file.readAll(), 'utf-8')
            file.close()
        self.setDetailedText(license)
        # You will do what I tell you to, stupid QMessageBox!  I know where you children live!
        # Be a sensible size!
        description_text_widget = self.children()[1]
        license_text_widget = self.children()[3].children()[2]
        description_text_widget.setFixedWidth(license_text_widget.width() * 0.7)
        license_text_widget.setFixedHeight(license_text_widget.height() * 2)
        # And have the buttons I want you to!
        self.addButton(self.Ok)
        for button in self.buttons():
            if button.text() == "Show Details...":
                button.setText("Show License")
                # and update the button text when I tell you to!
                button.clicked.connect(self._toggle_text)

    def _toggle_text(self):
        """This function updates the text of the License button when you click it
        """
        # Search through all buttons for the button that is not the OK button and change its text
        for button in self.buttons():
            button.update()
            if button.text() == "OK":
                continue
            elif "Hide" in button.text():
                button.setText("Hide License")
                self.adjustSize()
            elif "Show" in button.text():
                button.setText("Show License")
                self.adjustSize()
            else:
                continue

def create_ui():
    """Loads the UI from the .ui file and instantiates it and connects any signals which could not be connected in designer

    Returns:
        QMainWindow: The main window of the application
    """
    main_window = loadUi(Path(__file__).parent/"Lipsynqt.ui")
    #connect the about actions to the corresponding about message they should display when triggered
    main_window.actionAbout_Qt.triggered.connect(QtWidgets.QApplication.instance().aboutQt)
    main_window.actionAbout.triggered.connect(About_Window(parent = main_window).show)
    return main_window

if __name__ == '__main__':
    # create the QApplication that will manage this window
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Lipsynqt")

    # create a window
    main_window = create_ui()
    main_window.show()

    # execute the application
    sys.exit(app.exec_())
