from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
import sys, os

class MainWindow(QMainWindow):
    def __init__(self, directorio = os.path.dirname(os.path.abspath(__file__))):
        super().__init__()
        self.setWindowTitle("Maquinas de Turing")
        self.setGeometry(200, 100, 330, 400)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background-color: white;")

        SegoeScriptFont = QFont()
        SegoeScriptFont.setFamily("Segoe Script")
        SegoeScriptFont.setPointSize(12)
        SegoeScriptFont.setBold(True)

        path_to_close_icon = os.path.join(directorio, "assets", "icons", "close_btn.png")
        path_to_close_hover = os.path.join(directorio, "assets", "icons", "close_btn_hover.png")
        self.close_icon_normal = QIcon(path_to_close_icon)
        self.close_icon_hover = QIcon(path_to_close_hover)

        self.title_label = QLabel("Máquinas de Turing", self)
        self.title_label.setFont(SegoeScriptFont)
        self.title_label.setGeometry(10, 10, 200, 30)

        self.close_button = QPushButton()
        self.close_button.setParent(self)
        self.close_button.setGeometry(290, 10, 30, 30)
        self.close_button.clicked.connect(self.close)
        self.close_button.setIcon(QIcon(path_to_close_icon))
        self.close_button.setIconSize(self.close_button.size())
        self.close_button.setStyleSheet("QPushButton { border: none; }")
        self.close_button.enterEvent = lambda e: self.close_button.setIcon(self.close_icon_hover)
        self.close_button.leaveEvent = lambda e: self.close_button.setIcon(self.close_icon_normal)

        self.minimize_button = QPushButton()
        self.minimize_button.setParent(self)
        self.minimize_button.setGeometry(250, 10, 30, 30)
        self.minimize_button.clicked.connect(self.showMinimized)

        self.creditButton = QPushButton()
        self.creditButton.setParent(self)
        self.creditButton.setGeometry(210, 10, 30, 30)

        self.__drag_position = None
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.__drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.__drag_position is not None:
            self.move(event.globalPosition().toPoint() - self.__drag_position)
            event.accept()

if __name__ == "__main__":
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    app = QApplication(sys.argv)
    window = MainWindow(directorio_actual)
    window.show()
    sys.exit(app.exec())