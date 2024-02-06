import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_main_d.ui', self)

        self.zoom = 7
        self.ll = "30.368710,59.925945"
        self.l = 'map'
        self.radioButton_2.setChecked(True)
        self.radioButton.toggled.connect(self.satellite)
        self.radioButton_2.toggled.connect(self.scheme)
        self.radioButton_3.toggled.connect(self.gibrid)
        self.init_map()

    def satellite(self):
        self.l = "sat"
        self.init_map()

    def scheme(self):
        self.l = "map"
        self.init_map()

    def gibrid(self):
        self.l = "sat,skl"
        self.init_map()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp and self.zoom < 17:
            self.zoom += 1
        if event.key() == Qt.Key_PageDown and self.zoom > 0:
            self.zoom -= 1

        ll = list(map(float, self.ll.split(',')))
        delta = 1.5

        if event.key() == Qt.Key_Left and ll[0] > -180:
            ll[0] -= delta
        if event.key() == Qt.Key_Right and ll[0] < 180:
            ll[0] += delta
        if event.key() == Qt.Key_Up and ll[1] < 90:
            ll[1] += delta
        if event.key() == Qt.Key_Down and ll[1] > -90:
            ll[1] -= delta
        self.ll = f"{ll[0]},{ll[1]}"

        self.init_map()

    def init_map(self):
        params = {
            "ll": self.ll,
            "l": self.l,
            'z': self.zoom
        }
        response = requests.get('https://static-maps.yandex.ru/1.x/',
                                params=params)
        with open('tmp.png', mode='wb') as tmp:
            tmp.write(response.content)

        pixmap = QPixmap('tmp.png')

        #self.image.move(40, 60)
        self.label.resize(600, 450)
        self.label.setPixmap(pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
