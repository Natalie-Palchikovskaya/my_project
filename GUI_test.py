import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication)
from PyQt5.QtGui import QColor
from neuroflowers import predict

class main_gui(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.btn = QPushButton('Download picture', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.btn1 = QPushButton('What is the flower?', self)
        self.btn1.move(20, 48)
        self.btn1.clicked.connect(self.flower)
        # # self.btn1.clicked.connect(predict(self.path))
        self.le1 = QLineEdit(self)
        self.le1.move(130, 50)


        self.setGeometry(1000, 500, 500, 250)
        self.setWindowTitle('Guess the flower')
        self.show()

    def flower(self):
        label, percent = predict(str(path))
        self.le1.setText(label)
        print(path)


    def showDialog(self):
        img_path, ok = QInputDialog.getText(self, 'Input',
            'Enter path to flower:')
        global path
        path = img_path

        if ok:
            self.le.setText(str(path))
            print(path)
            return path




if __name__ == '__main__':

    app = QApplication(sys.argv)
    gui = main_gui()
    sys.exit(app.exec_())