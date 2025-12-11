from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication
import sys, os

class MaxWindow(QMainWindow):
    def __init__(self, directorio : str = os.path.dirname(os.path.abspath(__file__)), chain : str = "00110011"):
        super().__init__()
        self.setWindowTitle("Maximo entre 0 y cadena")
        self.setGeometry(300, 200, 400, 200)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background-color: white;")
        self.directorio = directorio

        SegoeScriptFont = QFont("Segoe Script", 12, QFont.Weight.Bold)
        ConsolasFont = QFont("Consolas", 10)

        Title = QLabel("Función Max", self)
        Title.setFont(SegoeScriptFont)
        Title.setStyleSheet("color: black;")
        Title.setGeometry(10, 10, 200, 30)
        self.chain = chain + "B"

        self.close_button = QPushButton(self)
        self.close_button.setGeometry(360, 10, 30, 30)
        self.close_button.clicked.connect(self.close)
        path_to_close = os.path.join(directorio, "assets", "icons", "close_btn.png")
        close_icon_normal = QIcon(path_to_close)
        path_to_close_hover = os.path.join(directorio, "assets", "icons", "close_btn_hover.png")
        close_icon_hover = QIcon(path_to_close_hover)
        self.close_button.setIcon(close_icon_normal)
        self.close_button.setIconSize(self.close_button.size())
        self.close_button.setStyleSheet("QPushButton { border: none; }")
        self.close_button.enterEvent = lambda e: self.close_button.setIcon(close_icon_hover)
        self.close_button.leaveEvent = lambda e: self.close_button.setIcon(close_icon_normal)

        self.minimize_button = QPushButton(self)
        self.minimize_button.setGeometry(330, 10, 30, 30)
        self.minimize_button.clicked.connect(self.showMinimized)
        path_to_minimize = os.path.join(directorio, "assets", "icons", "min_btn.png")
        minimize_icon_normal = QIcon(path_to_minimize)
        path_to_minimize_hover = os.path.join(directorio, "assets", "icons", "min_btn_hover.png")
        minimize_icon_hover = QIcon(path_to_minimize_hover)
        self.minimize_button.setIcon(minimize_icon_normal)
        self.minimize_button.setIconSize(self.minimize_button.size())
        self.minimize_button.setStyleSheet("QPushButton { border: none; }")
        self.minimize_button.enterEvent = lambda e: self.minimize_button.setIcon(minimize_icon_hover)
        self.minimize_button.leaveEvent = lambda e: self.minimize_button.setIcon(minimize_icon_normal)

        self.tape = []
        for i in range(8):
            self.tape.append(QLabel(chain[i], self))
            self.tape[i].setFont(ConsolasFont)
            self.tape[i].setStyleSheet("color: black; border: 1px solid gray; border-radius: 4px;")
            self.tape[i].setGeometry(30 + i*40, 120, 30, 30)
            self.tape[i].setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tape.append(QLabel("", self))

        self.btn_compute = QPushButton()
        self.btn_compute.setParent(self)
        self.btn_compute.setGeometry(120, 160, 160, 30)
        path_to_start = os.path.join(directorio, "assets", "icons", "st_btn.png")
        start_icon_normal = QIcon(path_to_start)
        path_to_start_hover = os.path.join(directorio, "assets", "icons", "st_btn_hover.png")
        start_icon_hover = QIcon(path_to_start_hover)
        self.btn_compute.setIcon(start_icon_normal)
        self.btn_compute.clicked.connect(self.startMachine)
        self.btn_compute.setIconSize(self.btn_compute.size())
        self.btn_compute.setStyleSheet("QPushButton { border: none; }")
        self.btn_compute.enterEvent = lambda e: self.btn_compute.setIcon(start_icon_hover)
        self.btn_compute.leaveEvent = lambda e: self.btn_compute.setIcon(start_icon_normal)

        self.arrow_label = QLabel("↓", self)
        self.arrow_label.setFont(QFont("Consolas", 20))
        self.arrow_label.setStyleSheet("color: red;")
        self.arrow_label.setGeometry(30, 90, 30, 30)
        self.arrow_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.arrow_pos = 0

        self.state_label = QLabel("Estado: q0; Pasos: 0", self)
        self.state_label.setFont(ConsolasFont)
        self.state_label.setStyleSheet("color: black;")
        self.state_label.setGeometry(30, 60, 300, 30)
        self.state_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.state = "q0"
        self.steps = 0

        self.__drag_position = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.__drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.__drag_position is not None:
            self.move(event.globalPosition().toPoint() - self.__drag_position)
            event.accept()
    
    def startMachine(self):
        if self.arrow_pos == len(self.chain) - 2:
            ConsolasFont = QFont("Consolas", 10)
            self.tape[8].setText("B")
            self.tape[8].setFont(ConsolasFont)
            self.tape[8].setStyleSheet("color: black; border: 1px solid gray; border-radius: 4px;")
            self.tape[8].setGeometry(350, 120, 30, 30)
            self.tape[8].setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.steps += 1
        if self.state == "q0":
            if self.chain[self.arrow_pos] == '1':
                self.state = "q1"
                #q1 cambia todo a 0 y se mueve a la derecha
                self.tape[self.arrow_pos].setText('0')
            else:
                self.state = "q2"
                #q2 deja todo igual y se mueve a la derecha
        elif self.state == "q1":
            if self.chain[self.arrow_pos] == 'B':
                self.state = "q3"
            else:
                self.tape[self.arrow_pos].setText('0')
        elif self.state == "q2":
            if self.tape[self.arrow_pos] == 'B':
                self.state = "q3"
        elif self.state == "q3":
            self.close()
        self.arrow_pos += 1
        self.state_label.setText(f"Estado: {self.state}; Pasos: {self.steps}")
        self.arrow_label.setGeometry(30 + self.arrow_pos*40, 90, 30, 30)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MaxWindow(chain="10011001")
    window.show()
    sys.exit(app.exec())