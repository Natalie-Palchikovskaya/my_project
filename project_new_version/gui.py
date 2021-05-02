import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
    QInputDialog, QPushButton, QMessageBox, QLineEdit




def dialog():
    mbox = QMessageBox()
    mbox.setText("Here you can choose an image from your computer")
    mbox.setDetailedText("It will work. maybe...")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) #стандартная кнопка
    mbox.exec_()
    get_path()



def get_path():
    le = QLineEdit()
    le.move(130, 22)
    path, ok = QInputDialog.getText('Input',
            'Enter path to flower:')
    if ok:
        path = le.setText(str(path))



if __name__ == "__main__":
    app = QApplication(sys.argv)#нужно для pyqt, иначе ошибки
    w = QWidget() #все кнопки, окна
    w.resize(1000,1000)
    w.setWindowTitle('Guess the flower')

    label = QLabel(w) #для вывода нередактируемого текста
    label.setText("What kind of flower is it? Just download.")
    label.move(500, 470)
    label.show()

    btn = QPushButton(w) #кликабельная кнопка
    btn.setText('Download')
    btn.move(500, 500)
    btn.show()
    btn.clicked.connect(dialog)


    w.show()
    sys.exit(app.exec_())