# author: Dabana Intenque
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QPushButton, QApplication, QMessageBox


def close_window_button(self):
    close_win_btn = QPushButton("Force Quit", self)
    close_win_btn.clicked.connect(QApplication.instance().quit)
    close_win_btn.resize(500, 50)
    close_win_btn.move(250, 650)


# ask user before close
def closeEvent(self, event: QCloseEvent):
    reply = QMessageBox.question(
        self,
        'message',
        'Are you sure you want to quit?',
        QMessageBox.Yes | QMessageBox.No)
    if reply == QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()
