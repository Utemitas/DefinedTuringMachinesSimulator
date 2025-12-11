from PyQt6.QtWidgets import QLabel, QPushButton, QApplication, QMainWindow, QLineEdit
from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import QFont, QIcon, QRegularExpressionValidator, QImage, QPixmap
import sys, os
from Palindromes import StepsWindow
from Max import MaxWindow
from Binary_PalindromesTM import *

class WarningWindow(QMainWindow):
    def __init__(self, msgwarning1, msgwarning2, directorio : str = os.path.dirname(os.path.abspath(__file__))):
        super().__init__()
        self.setWindowTitle("Warning")
        self.setGeometry(350, 250, 230, 100)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background-color: black;")
        SegoeScriptFont = QFont()
        SegoeScriptFont.setFamily("Segoe Script")
        SegoeScriptFont.setPointSize(12)
        SegoeScriptFont.setBold(True)

        path_to_close_icon = os.path.join(directorio, "assets", "icons", "close_btn.png")
        self.close_icon_normal = QIcon(path_to_close_icon)
        path_to_close_hover = os.path.join(directorio, "assets", "icons", "close_btn_hover.png")
        self.close_icon_hover = QIcon(path_to_close_hover)

        path_to_warning_image = os.path.join(directorio, "assets", "icons", "warning.png")
        self.warning_image = QImage(path_to_warning_image)
        self.warning_pixmap = QPixmap.fromImage(self.warning_image)
        self.image = QLabel(self)
        self.image.setPixmap(self.warning_pixmap)
        self.image.setGeometry(10, 40, 50, 50)

        self.title_label = QLabel("Advertencia", self)
        self.title_label.setFont(SegoeScriptFont)
        self.title_label.setGeometry(10, 10, 120, 30)
        self.close_button = QPushButton()
        self.close_button.setParent(self)
        self.close_button.setGeometry(190, 10, 30, 30)
        self.close_button.clicked.connect(self.close)
        self.close_button.setIcon(QIcon(path_to_close_icon))
        self.close_button.setIconSize(self.close_button.size())
        self.close_button.setStyleSheet("QPushButton { border: none; }")
        self.close_button.enterEvent = lambda e: self.close_button.setIcon(self.close_icon_hover)
        self.close_button.leaveEvent = lambda e: self.close_button.setIcon(self.close_icon_normal)

        #Warnings
        self.label = QLabel(msgwarning1, self)
        self.label.setGeometry(70, 50, 150, 20)
        self.label2 = QLabel(msgwarning2, self)
        self.label2.setGeometry(70, 70, 120, 20)
        self.label.setFont(QFont("Arial", 10))
        self.label2.setFont(QFont("Arial", 10))

        self.__drag_position = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.__drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.__drag_position is not None:
            self.move(event.globalPosition().toPoint() - self.__drag_position)
            event.accept()




class InputWindow(QMainWindow):
    def __init__(self, directorio : str = os.path.dirname(os.path.abspath(__file__)), variant : int = 1):
        super().__init__()
        self.setWindowTitle("Input Window")
        self.setGeometry(300, 200, 200, 150)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background-color: black;")
        self.variant = variant

        SegoeScriptFont = QFont()
        SegoeScriptFont.setFamily("Segoe Script")
        SegoeScriptFont.setPointSize(12)
        SegoeScriptFont.setBold(True)
        ConsolasFont = QFont()
        ConsolasFont.setFamily("Consolas")
        ConsolasFont.setPointSize(10)
        path_to_close_icon = os.path.join(directorio, "assets", "icons", "close_btn.png")
        self.close_icon_normal = QIcon(path_to_close_icon)
        path_to_close_hover = os.path.join(directorio, "assets", "icons", "close_btn_hover.png")
        self.close_icon_hover = QIcon(path_to_close_hover)
        path_to_minimize_icon = os.path.join(directorio, "assets", "icons", "min_btn.png")
        self.minimize_icon_normal = QIcon(path_to_minimize_icon)
        path_to_minimize_hover = os.path.join(directorio, "assets", "icons", "min_btn_hover.png")
        self.minimize_icon_hover = QIcon(path_to_minimize_hover)
        path_to_start_icon = os.path.join(directorio, "assets", "icons", "st_btn.png")
        self.start_icon_normal = QIcon(path_to_start_icon)
        path_to_start_hover = os.path.join(directorio, "assets", "icons", "st_btn_hover.png")
        self.start_icon_hover = QIcon(path_to_start_hover)

        self.title_label = QLabel("Entrada", self)
        self.title_label.setFont(SegoeScriptFont)
        self.title_label.setGeometry(10, 10, 120, 30)

        self.close_button = QPushButton()
        self.close_button.setParent(self)
        self.close_button.setGeometry(160, 10, 30, 30)
        self.close_button.clicked.connect(self.close)
        self.close_button.setIcon(QIcon(path_to_close_icon))
        self.close_button.setIconSize(self.close_button.size())
        self.close_button.setStyleSheet("QPushButton { border: none; }")
        self.close_button.enterEvent = lambda e: self.close_button.setIcon(self.close_icon_hover)
        self.close_button.leaveEvent = lambda e: self.close_button.setIcon(self.close_icon_normal)

        self.minimize_button = QPushButton()
        self.minimize_button.setParent(self)
        self.minimize_button.setGeometry(130, 10, 30, 30)
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setIcon(QIcon(path_to_minimize_icon))
        self.minimize_button.setIconSize(self.minimize_button.size())
        self.minimize_button.setStyleSheet("QPushButton { border: none; }")
        self.minimize_button.enterEvent = lambda e: self.minimize_button.setIcon(self.minimize_icon_hover)
        self.minimize_button.leaveEvent = lambda e: self.minimize_button.setIcon(self.minimize_icon_normal)

        self.entry_field = QLineEdit(self)
        self.entry_field.setFont(ConsolasFont)
        self.entry_field.setGeometry(20, 60, 160, 30)
        self.entry_field.setStyleSheet(
            """
            QLineEdit {
                border: 2px solid black;
                border-radius: 10px;
            }
            """
        )
        binRegExp = QRegularExpression("^[01\\s]*$")
        binValidator = QRegularExpressionValidator(binRegExp)
        self.entry_field.setValidator(binValidator)

        self.start_button =QPushButton()
        self.start_button.setParent(self)
        self.start_button.setGeometry(20, 100, 160, 30)
        self.start_button.setIcon(QIcon(path_to_start_icon))
        self.start_button.setIconSize(self.start_button.size())
        self.start_button.setStyleSheet("QPushButton { border: none; }")
        self.start_button.enterEvent = lambda e: self.start_button.setIcon(self.start_icon_hover)
        self.start_button.leaveEvent = lambda e: self.start_button.setIcon(self.start_icon_normal)
        self.start_button.clicked.connect(self.validate_input)

        self.__drag_position = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.__drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.__drag_position is not None:
            self.move(event.globalPosition().toPoint() - self.__drag_position)
            event.accept()

    def validate_input(self):
        input_text = self.entry_field.text().replace(" ", "")
        if self. variant == 0:
            if len(input_text) != 8:
                l = 8 - len(input_text)
                if l < 0:
                    l = 0
                string_to_add = "0"*l
                self.entry_field.setText(string_to_add + input_text)
                self.warning_window = WarningWindow("La entrada debe contener", "8 caracteres.")
                self.warning_window.show()
                return False
            win = MaxWindow(chain=input_text)
            win.show()
        else:
            if len(input_text) == 0:
                self.warning_window = WarningWindow("La cadena de entrada no","puede ser vacia.")
                self.warning_window.show()
            else:
                tm = Binary_PalindromesTM()
                tm.load(input_text)
                current_dir = os.path.dirname(os.path.abspath(__file__))
                self.sim_window = StepsWindow(tm, current_dir)
                self.sim_window.show()
        self.close()
        return True

if __name__ == "__main__":
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    app = QApplication(sys.argv)
    window = InputWindow(directorio=directorio_actual, variant=0)
    window.show()
    sys.exit(app.exec())