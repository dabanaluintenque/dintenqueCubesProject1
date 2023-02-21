# author: Dabana Intenque
import sys

from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from variables import windowWidth, windowHeight, x, y
from buttons import close_window_button
from text_box import prefix, first_name, last_name, title, organization_name


# Bringing all the widgets and vents needed to build the application from pyside6 Library

class cubesWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setGeometry(x, y, windowWidth, windowHeight)
        # buttons

        close_window_button(self)
        # text boxes
        prefix(self)
        first_name(self)
        last_name(self)
        title(self)
        organization_name(self)

        self.setWindowTitle('Cubes Form')
        self.show()


def run():
    app = QApplication(sys.argv)

    ex = cubesWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    run()
