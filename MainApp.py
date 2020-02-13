import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from map_design import Ui_MapsApp


class Map(QMainWindow, Ui_MapsApp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.do_request)
    def do_request(self):
        self.width_txt = self.width.text()
        self.lenght_txt = self.lenght.text()
        self.width_size_txt = self.width_size.text()
        self.lenght_size_txt = self.lenght_size.text()
        print(self.width_txt)
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={self.width_txt},{self.lenght_txt}&spn={self.lenght_size_txt},{self.width_size_txt}&l=map"
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Map()
    ex.show()
    sys.exit(app.exec())