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
    # window = MainWindow()
    # window.show()
    test = FormLOTRConfrontation.FormLOTRConfrontation()
    test.show()

    # Main window
    # window = PySide2.QtWidgets.QMainWindow()
    # button1 = PySide2.QtWidgets.QPushButton("One")
    # button2 = PySide2.QtWidgets.QPushButton("2")
    # button3 = PySide2.QtWidgets.QPushButton("3")
    #
    # # Layout
    # layout = PySide2.QtWidgets.QGridLayout()
    # layout.addWidget(button1, 0,0)
    # layout.addWidget(button2, 0,1)
    # layout.addWidget(button3, 2,0)
    #
    # # To be central widget
    # central = PySide2.QtWidgets.QGraphicsView()
    #
    # # Make central widget main window's central widget
    # window.setCentralWidget(central)
    #
    # # Set central widget's layout
    # central.setLayout(layout)
    #
    # window.show()

    sys.exit(app.exec_())