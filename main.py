import FormLOTRConfrontation
import PySide2.QtWidgets
import PySide2.QtCore
import sys


if __name__ == "__main__":
    app = PySide2.QtWidgets.QApplication([])
    # window = MainWindow()
    # window.show()
    test = FormLOTRConfrontation.FormLOTRConfrontation()
    # test.show()
    sys.exit(app.exec_())