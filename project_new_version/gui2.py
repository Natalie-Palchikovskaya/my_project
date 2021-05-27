import sys
import os
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication, QLabel, QPlainTextEdit, QFileDialog, QMessageBox)
from PyQt5.QtGui import QColor, QPalette, QIcon
from PyQt5.QtGui import QPixmap
from neuroflowers import predict
from PyQt5 import QtGui

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

        self.btn2 = QPushButton('Help', self)
        self.btn2.setStyleSheet("background-color: white;")
        self.btn2.move(650, 5)
        self.btn2.clicked.connect(self.showHelp)

        # palette =QPalette()
        # palette.setColor(QPalette.Window, QColor(255, 192, 203))
        self.setWindowIcon(QIcon('icon2.jpg'))
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
        self.lab1.setStyleSheet("""
                                font: bold italic;
                                color: black
                            """)
        self.lab1.show()

        self.lab2 = QLabel(self)  # для вывода нередактируемого текста
        self.lab2.setStyleSheet("""font: bold italic;
                                    color: black;
                                    font-size: 18pt
                                        """)
        self.lab2.setText(str(label))
        self.lab2.move(100, 90)
        self.lab2.show()

        self.textbox = QLabel(self)  # для вывода нередактируемого текста
        if label=="tulip":
            self.textbox.setText("-род многолетних травянистых луковичных\n растений семейства Лилейные (Liliaceae),\n в современных систематиках включающий\n более 80 видов.\n"
                             "Центр происхождения и наибольшего\n разнообразия видов тюльпанов — горы\n северного Ирана, Памиро-Алай и Тянь-Шань.")

        if label=="rose":
           self.textbox.setText("— собирательное название видов\n и сортов представителей рода\n Шиповник (лат. Rósa), выращиваемых\n человеком и растущих в дикой природе.\n "
                                "Большая часть сортов роз\n получена в результате длительной\n селекции путём многократных повторных\n скрещиваний и отбора.")

        if label == "sunflower":
            self.textbox.setText("- род растений семейства Астровые (Asteraceae).\n Наиболее известные виды — подсолнечник\n однолетний и подсолнечник клубненосный.")

        if label == "narcissus":
            self.textbox.setText("(лат. Narcissus) — род однодольных растений\n из семейства амариллисовых.")

        if label=="dandelion":
            self.textbox.setText("(лат. Taráxacum) — род многолетних\n травянистых растений семейства\n Астровые, или Сложноцветные (Asteraceae).\n"
                                 " Типовой вид рода — Одуванчик лекарственный\n — хорошо известное растение с\n розеткой прикорневых листьев и"
                                 " крупными\n ярко-жёлтыми соцветиями-корзинками\n из язычковых цветков.")

        if label == "poppy":
            self.textbox.setText("-род травянистых растений семейства\n Маковые (Papaveraceae).Встречается в\n умеренной,субтропической и реже\n в холодных зонах.")

        if label == "iris":
            self.textbox.setText("-род многолетних корневищных растений\n семейства Ирисовые, или Касатиковые.\n"
                                 " Ирисы встречаются на всех\n континентах. Род насчитывает около\n 800 видов с богатейшим разнообразием\n форм и оттенков.")

        if label == "daisy":
            self.textbox.setText("(лат. Matricária) — род многолетних\n цветковых растений семейства Астровые,\n или Сложноцветные (Asteraceae),"
                                 " объединяет\n около двадцати видов невысоких\n пахучих трав, цветущих с первого\n года жизни. "
                                 "Наиболее известный\n вид — Ромашка аптечная (Matricaria\n chamomilla, syn. Matricaria recutita),\n "
                                 "это растение широко используется\n в лечебных и косметических целях.")

        if label == "lavender":
            self.textbox.setText("(лат. Lavandula) — род растений семейства\n яснотковых (Lamiaceae или Labiatae).\n Включает примерно 47 видов.\n"
                                 " Произрастает на Канарских островах,\n в северной и восточной Африке, в Австралии,\n на юге Европы, в"
                                 " Крыму, в Аравии \n и в Индии.")


        if label == "lily":
            self.textbox.setText(" (лат. Lílium) — род растений семейства\n Лилейные (Liliaceae). Многолетние травы,\n снабжённые луковицами, "
                                 "состоящими из\n мясистых низовых листьев, расположенных\n черепитчато, белого, розоватого\n или желтоватого цвета.")

        if label == "lilac":
            self.textbox.setText("(лат. Syrínga) — род кустарников,\n принадлежащий семейству Маслиновые.\n"
                                 "Род включает около тридцати\n видов, распространённых "
                                 "в диком состоянии\n в Юго-Восточной Европе (Венгрия,\n Балканы) и в Азии, преимущественно\n в Китае.")

        if label == "lotus":
            self.textbox.setText("(лат. Nelúmbo) — род двудольных \n растений, "
                                 "единственный представитель\n семейства Лотосовые (лат. Nelumbonaceae).")

        if label == "orchid":
            self.textbox.setText("(лат. Orchidáceae) — крупнейшее семейство\n однодольных растений."
                                 "В наше время\n орхидные найдены на всех\n континентах, кроме Антарктиды.")

        if label == "peony":
            self.textbox.setText("-род травянистых многолетников\n и листопадных кустарников (древовидные\n пионы)."
                                 "Пионы цветут в\n конце весны, ценятся садоводами\n за пышную листву, "
                                 "эффектные\n цветы и декоративные плоды\n (у некоторых видов).")

        if label == "sakura":
            self.textbox.setText("название нескольких деревьев\n подсемейства сливовые; зачастую обозначает\n вишню мелкопильчатую."
                                 " Многие виды,\n называемые «сакурой», используются\n в культуре "
                                 "только как декоративные\n растения и либо не плодоносят\n вообще, "
                                 "либо дают мелкий\n и несъедобный плод.")


        self.textbox.move(20, 120)
        self.textbox.setFixedSize(310, 160)

        # self.lab3.setGeometry(20, 120, 100, 200)
        self.textbox.setStyleSheet("""
                                font: bold italic;
                                color: black;
                                font-size: 9pt
                                    """)
        self.textbox.show()


    def showDialog(self):
        # img_path, ok = QInputDialog.getText(self, 'Input',
        #     'Enter path to flower:')
        filename, filter = QFileDialog.getOpenFileName(self, "Input picture", "",
                                                       "Image (*.png *.jpg)")

        global path
        path = filename
        print(path)
        if os.path.exists(path):
            self.le.setText(str(path))
            pixmap = QPixmap(str(path))
            pixmap = pixmap.scaled(256,256)
            self.lbl = QLabel(self)
            self.lbl.setPixmap(pixmap)
            self.lbl.move(350, 20)
            self.lbl.show()

        if not filename:
            return

    def showHelp(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setWindowTitle("Help")
        self.msgBox.setText("1.Нажмите клавишу 'Download picture'\n 2.Выберите изображение для загрузки и нажмите "
                            "'Открыть'\n "
                            "3.Нажмите клавишу 'What is the flower?' и получите ответ")
        self.msgBox.exec()






if __name__ == '__main__':

    app = QApplication(sys.argv)
    gui = main_gui()
    sys.exit(app.exec_())