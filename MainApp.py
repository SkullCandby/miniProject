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
        width_txt = self._width.text()
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
        self._width.setDisabled(True)
        self.length.setDisabled(True)
        self.width_size.setDisabled(True)
        self.lenght_size.setDisabled(True)
        self.pushButton.setDisabled(True)
        self.view_box.setDisabled(True)

    def closeEvent(self, event):
        os.remove(self.map_file)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            delta = 0
            if (int(float(self.width_size_txt))) < 1:
                delta = 0.1
            # Проверяю только один параментр потому, что они равны
            elif (int(float(self.width_size_txt))) >= 15 and (int(float(self.width_size_txt)) + 10) < 90:
                delta = 10
            # Проверяю только один параментр потому, что они равны
            elif (int(float(self.width_size_txt)) + 1) < 90:
                delta = 1
            sw = str(round(float(self.width_size_txt) + delta, 1))
            sl = str(round(float(self.length_size_txt) + delta, 1))
            self.width_size.setText(sw)
            self.lenght_size.setText(sl)
            self.do_request()
        if event.key() == Qt.Key_PageDown:
            delta = 0
            # Проверяю только один параментр потому, что они равны
            if (float(self.width_size_txt)) <= 1:
                delta = 0.1
            # Проверяю только один параментр потому, что они равны
            elif (int(float(self.width_size_txt))) > 15:
                delta = 10
            else:
                delta = 1
            # Проверяю только один параментр потому, что они равны
            if (float(self.width_size_txt) - delta) < 0:
                print(delta)
                sw = '0.001'
            else:
                sw = str(round(float(self.width_size_txt) - delta, 1))
            # Проверяю только один параментр потому, что они равны
            if (float(self.width_size_txt) - delta) < 0:
                sl = '0.001'
            else:
                sl = str(round(float(self.length_size_txt) - delta, 1))
            self.width_size.setText(sw)
            self.lenght_size.setText(sl)
            self.do_request()
        if event.key() == Qt.Key_Up:
            if float(self.length.text()) + float(self.lenght_size.text()) <= 90:
                self.length.setText(str(float(self.length.text()) + float(self.lenght_size.text())))
                print(1)
            else:
                self.length.setText(str(float(self.length.text()) + float(self.lenght_size.text() - 90)))
            print(str(float(self._width.text()) + float(self.width_size.text())))
            self.do_request()
        elif event.key() == Qt.Key_Down:
            if float(self.length.text()) - float(self.lenght_size.text()) >= -90:
                self.length.setText(str(float(self.length.text()) - float(self.lenght_size.text())))
                print(1)
            else:
                self.length.setText(str(float(self.length.text()) - float(self.lenght_size.text() + 90)))
            print(str(float(self._width.text()) - float(self.width_size.text())))
            self.do_request()
        elif event.key() == Qt.Key_Left:
            if float(self._width.text()) - float(self.width_size.text()) >= -90:
                self._width.setText(str(float(self._width.text()) - float(self.width_size.text())))
                print(1)
            else:
                self._width.setText(str(float(self._width.text()) + float(self.width_size.text()) + 90))
            print(str(float(self._width.text()) + float(self.width_size.text())))
            self.do_request()
        elif event.key() == Qt.Key_Right:
            print(1)
            if float(self._width.text()) + float(self.width_size.text()) <= 90:
                self._width.setText(str(float(self._width.text()) + float(self.width_size.text())))
                print(1)
            else:
                self._width.setText(str(float(self._width.text()) - float(self.width_size.text()) - 90))
            print(str(float(self._width.text()) + float(self.width_size.text())))
            self.do_request()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.exit(app.exec())
