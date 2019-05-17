import FormLOTRConfrontation
import PySide2.QtWidgets
import PySide2.QtGui
import PySide2.QtCore
import sys
import Game


class MainWindow(PySide2.QtWidgets.QMainWindow):
    def __init__(self):
        PySide2.QtWidgets.QMainWindow.__init__(self)

        self.setLayout(PySide2.QtWidgets.QFormLayout())
        self.button_boromir = PySide2.QtWidgets.QPushButton("Boromir")
        self.button_boromir.adjustSize()
        self.layout().addWidget(self.button_boromir)
        self.setGeometry(50, 50, 800, 600)


if __name__ == "__main__":
    app = PySide2.QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())