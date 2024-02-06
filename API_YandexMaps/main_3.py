import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_main1.ui', self)

        self.zoom = 3
        self.ll = "30.368710,59.925945"
        self.l = 'map'

        self.init_map()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp and self.zoom < 17:
            self.zoom += 1
        if event.key() == Qt.Key_PageDown and self.zoom > 0:
            self.zoom -= 1

        ll = list(map(int, self.ll.split(',')))

        if event.key() == Qt.Key_Left:
            ll[0] -= 0.1
        if event.key() == Qt.Key_Right:
            ll[0] += 0.1
        if event.key() == Qt.Key_Up:
            ll[1] -= 0.1
        if event.key() == Qt.Key_Down:
            ll[1] += 0.1
        self.ll = f"{ll[0]},{ll[1]}"

        params = {
            "ll": self.ll,
            "l": self.l,
            'z': self.zoom
        }
        response = requests.get('https://static-maps.yandex.ru/1.x/',
                                params=params)
        with open('tmp.png', mode='wb') as tmp:
            tmp.write(response.content)

        self.pixmap = QPixmap('tmp.png')
        self.image.setPixmap(self.pixmap)

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

        self.pixmap = QPixmap('tmp.png')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
