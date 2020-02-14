import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QLineEdit
from map_design import Ui_MapsApp
from PyQt5.QtCore import Qt


class Map(QMainWindow, Ui_MapsApp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.do_request)

    def do_request(self):
        width_txt = self.width.text()
        length_txt = self.length.text()
        self.width_size_txt = self.width_size.text()
        self.length_size_txt = self.lenght_size.text()
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={width_txt},{length_txt}&spn={self.length_size_txt},{self.width_size_txt}&l=map"
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)
        pixmap = QPixmap(self.map_file)
        self.img_lbl.setPixmap(pixmap)

    def closeEvent(self, event):
        os.remove(self.map_file)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            sw = str(int(float(self.width_size_txt)) + 1)
            sl = str(int(float(self.length_size_txt)) + 1)
            self.width_size.setText(sw)
            self.lenght_size.setText(sl)
            self.do_request()
        if event.key() == Qt.Key_PageDown:
            delta = 0
            if (int(float(self.width_size_txt))) <= 1:
                delta = 0.1
            elif (int(float(self.width_size_txt))) >= 14:
                delta = 10
            else:
                delta = 1
            if (int(float(self.width_size_txt)) - delta) < 0:
                sw = '0.001'
            else:
                sw = str(int(self.width_size_txt) - delta)
            if (int(float(self.width_size_txt)) - delta) < 0:
                print(int(float(self.width_size_txt)))
                sl = '0.001'
            else:
                sl = str(int(self.length_size_txt) - delta)
            self.width_size.setText(sw)
            self.lenght_size.setText(sl)
            self.do_request()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.exit(app.exec())
