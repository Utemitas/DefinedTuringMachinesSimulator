from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
import sys, os
import webbrowser

class CreditsWindow(QMainWindow):
    def __init__(self, directorio : str = os.path.dirname(os.path.abspath(__file__))):
        super().__init__()
        self.setWindowTitle("Créditos")
        self.setGeometry(250, 150, 420, 400)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background-color: white;")

        SegoeScriptFont = QFont()
        SegoeScriptFont.setFamily("Segoe Script")
        SegoeScriptFont.setPointSize(12)
        SegoeScriptFont.setBold(True)
        LucidaConsoleFont = QFont()
        LucidaConsoleFont.setFamily("Lucida Console")
        LucidaConsoleFont.setPointSize(10)

        path_to_close_icon = os.path.join(directorio, "assets", "icons", "close_btn.png")
        self.close_icon_normal = QIcon(path_to_close_icon)
        path_to_close_hover = os.path.join(directorio, "assets", "icons", "close_btn_hover.png")
        self.close_icon_hover = QIcon(path_to_close_hover)
        path_to_minimize_icon = os.path.join(directorio, "assets", "icons", "min_btn.png")
        self.minimize_icon_normal = QIcon(path_to_minimize_icon)
        path_to_minimize_hover = os.path.join(directorio, "assets", "icons", "min_btn_hover.png")
        self.minimize_icon_hover = QIcon(path_to_minimize_hover)

        self.title_label = QLabel("Créditos", self)
        self.title_label.setFont(SegoeScriptFont)
        self.title_label.setGeometry(10, 10, 200, 30)

        self.first_line = QLabel("Aplicación sin fines de lucro desarrollada como", self)
        self.first_line.setGeometry(20, 50, 400, 20)
        self.first_line.setFont(LucidaConsoleFont)
        self.second_line = QLabel("proyecto final para la materia \"Teoría de la", self)
        self.second_line.setGeometry(20, 70, 400, 20)
        self.second_line.setFont(LucidaConsoleFont)
        self.third_line = QLabel("Computación\" por:", self)
        self.third_line.setGeometry(20, 90, 400, 20)
        self.third_line.setFont(LucidaConsoleFont)
        
        self.teban_btn = QPushButton("Esteban de Jesús Santiago Torres", self)
        self.teban_btn.setGeometry(50, 110, 300, 20)
        self.teban_btn.setFont(LucidaConsoleFont)
        self.teban_btn.setStyleSheet("""
            QPushButton {
                border: none;
                text-align: left;
            }
            QPushButton:hover {
                text-decoration: underline;
                color: blue;
            }""")
        self.teban_btn.clicked.connect(self.tebanlink)

        self.close_button = QPushButton()
        self.close_button.setParent(self)
        self.close_button.setGeometry(380, 10, 30, 30)
        self.close_button.clicked.connect(self.close)
        self.close_button.setIcon(QIcon(path_to_close_icon))
        self.close_button.setIconSize(self.close_button.size())
        self.close_button.setStyleSheet("QPushButton { border: none; }")
        self.close_button.enterEvent = lambda e: self.close_button.setIcon(self.close_icon_hover)
        self.close_button.leaveEvent = lambda e: self.close_button.setIcon(self.close_icon_normal)

        self.minimize_button = QPushButton()
        self.minimize_button.setParent(self)
        self.minimize_button.setGeometry(350, 10, 30, 30)
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setIcon(QIcon(path_to_minimize_icon))
        self.minimize_button.setIconSize(self.minimize_button.size())
        self.minimize_button.setStyleSheet("QPushButton { border: none; }")
        self.minimize_button.enterEvent = lambda e: self.minimize_button.setIcon(self.minimize_icon_hover)
        self.minimize_button.leaveEvent = lambda e: self.minimize_button.setIcon(self.minimize_icon_normal)

        self.__drag_position = None
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.__drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.__drag_position is not None:
            self.move(event.globalPosition().toPoint() - self.__drag_position)
            event.accept()

    def tebanlink(self):
        webbrowser.open("https://www.instagram.com/est.stgo/")

if __name__ == "__main__":
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    app = QApplication(sys.argv)
    ventana_creditos = CreditsWindow(directorio_actual)
    ventana_creditos.show()
    sys.exit(app.exec())