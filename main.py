from PyQt6.QtWidgets import     (QMainWindow,
                                QApplication,
                                QLabel,
                                QPushButton,
                                QVBoxLayout,
                                QWidget)
from PyQt6.QtCore import Qt
from random import randint


app = QApplication([])
win = QWidget()

win.setWindowTitle("Pygame top")
win.resize(500, 400)

text_1 = QLabel("Toper")
text_num = QLabel("?")

button = QPushButton("Random 100%")
main_line = QVBoxLayout()

main_line.addWidget(text_1, alignment = Qt.AlignmentFlag.AlignCenter)
main_line.addWidget(text_num, alignment = Qt.AlignmentFlag.AlignCenter)
main_line.addWidget(button, alignment = Qt.AlignmentFlag.AlignCenter)




win.setLayout(main_line)

def click():
    rand_num = randint(1, 100000)
    text_num.setText(str(rand_num))

button.clicked.connect(click)

win.show()
app.exec()