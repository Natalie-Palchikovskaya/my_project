import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication, QLabel)
from PyQt5.QtGui import QColor, QPalette, QIcon
from PyQt5.QtGui import QPixmap
from neuroflowers import predict

class main_gui(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.btn = QPushButton('Download picture', self)
        self.btn.setStyleSheet("background-color: white;")
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.setStyleSheet("background-color: white;")
        self.le.move(130, 22)

        self.btn1 = QPushButton('What is the flower?', self)
        self.btn1.setStyleSheet("background-color: white;")
        self.btn1.move(20, 48)
        self.btn1.clicked.connect(self.flower)
        self.le1 = QLineEdit(self)
        self.le1.setStyleSheet("background-color: white;")
        self.le1.move(130, 50)

        self.lab = QLabel(self)  # для вывода нередактируемого текста
        self.lab.setText("Accuracy, %:")
        self.lab.move(130, 70)

        # palette =QPalette()
        # palette.setColor(QPalette.Window, QColor(255, 192, 203))
        self.setWindowIcon(QIcon('D:\ПРОГРАММИРОВАНИЕ2020\my project\icon2.jpg'))
        self.setStyleSheet("background-color: pink;")
        self.setGeometry(1000, 500, 750, 400)
        self.setWindowTitle('Guess the flower')
        self.show()

    def flower(self):
        self.le1.setText("Processing...")
        label, percent = predict(str(path))
        self.le1.setText(label)


        self.lab1 = QLabel(self)  # для вывода нередактируемого текста
        self.lab1.setText(str(percent))
        self.lab1.move(200, 70)
        self.lab1.show()



    def showDialog(self):
        img_path, ok = QInputDialog.getText(self, 'Input',
            'Enter path to flower:')
        global path
        path = img_path

        if ok:
            self.le.setText(str(path))
            pixmap = QPixmap(str(path))
            pixmap = pixmap.scaled(256,256)
            self.lbl = QLabel(self)
            self.lbl.setPixmap(pixmap)
            self.lbl.move(350, 20)
            self.lbl.show()
            print(path)





if __name__ == '__main__':

    app = QApplication(sys.argv)
    gui = main_gui()
    sys.exit(app.exec_())