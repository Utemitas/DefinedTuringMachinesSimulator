from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
import sys, os
from creditos import CreditsWindow
from input import InputWindow

class MainWindow(QMainWindow):
    def __init__(self, directorio : str = os.path.dirname(os.path.abspath(__file__))):
        super().__init__()
        self.setWindowTitle("Maquinas de Turing")
        self.setGeometry(200, 100, 330, 350)
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
        path_to_minimize_icon = os.path.join(directorio, "assets", "icons", "min_btn.png")
        path_to_minimize_hover = os.path.join(directorio, "assets", "icons", "min_btn_hover.png")
        self.minimize_icon_normal = QIcon(path_to_minimize_icon)
        self.minimize_icon_hover = QIcon(path_to_minimize_hover)
        path_to_credit_icon = os.path.join(directorio, "assets", "icons", "credit_btn.png")
        path_to_credit_hover = os.path.join(directorio, "assets", "icons", "credit_btn_hover.png")
        self.credit_icon_normal = QIcon(path_to_credit_icon)
        self.credit_icon_hover = QIcon(path_to_credit_hover)
        path_to_max_icon = os.path.join(directorio, "assets", "icons", "max_btn.png")
        path_to_max_hover = os.path.join(directorio, "assets", "icons", "max_btn_hover.png")
        self.max_icon_normal = QIcon(path_to_max_icon)
        self.max_icon_hover = QIcon(path_to_max_hover)
        path_to_pal_icon = os.path.join(directorio, "assets", "icons", "pal_btn.png")
        path_to_pal_hover = os.path.join(directorio, "assets", "icons", "pal_btn_hover.png")
        self.pal_icon_normal = QIcon(path_to_pal_icon)
        self.pal_icon_hover = QIcon(path_to_pal_hover)

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
        self.minimize_button.setGeometry(260, 10, 30, 30)
        self.minimize_button.clicked.connect(self.showMinimized)
        self.minimize_button.setIcon(QIcon(path_to_minimize_icon))
        self.minimize_button.setIconSize(self.minimize_button.size())
        self.minimize_button.setStyleSheet("QPushButton { border: none; }")
        self.minimize_button.enterEvent = lambda e: self.minimize_button.setIcon(self.minimize_icon_hover)
        self.minimize_button.leaveEvent = lambda e: self.minimize_button.setIcon(self.minimize_icon_normal)

        self.creditButton = QPushButton()
        self.creditButton.setParent(self)
        self.creditButton.setGeometry(290, 310, 30, 30)
        self.creditButton.clicked.connect(self.displayCredits)
        self.creditButton.setIcon(QIcon(path_to_credit_icon))
        self.creditButton.setIconSize(self.creditButton.size())
        self.creditButton.setStyleSheet("QPushButton { border: none; }")
        self.creditButton.enterEvent = lambda e: self.creditButton.setIcon(self.credit_icon_hover)
        self.creditButton.leaveEvent = lambda e: self.creditButton.setIcon(self.credit_icon_normal)


        #-----------max-----------------------
        self.max_button = QPushButton()
        self.max_button.setParent(self)
        self.max_button.setGeometry(20, 70, 135, 220)
        self.max_button.setStyleSheet("QPushButton { border: none; }")
        self.max_button.setIcon(QIcon(path_to_max_icon))
        self.max_button.setIconSize(self.max_button.size())
        self.max_button.clicked.connect(self.openInputWindowMax)
        self.max_button.enterEvent = lambda e: self.max_button.setIcon(self.max_icon_hover)
        self.max_button.leaveEvent = lambda e: self.max_button.setIcon(self.max_icon_normal)
        self.max_button.setToolTip("""
            <div style='background-color: #f0f0f0; 
                        padding: 10px; 
                        border: 2px solid #333; 
                        border-radius: 10px;'>
                <b>Máquina Max</b><br>
                Retorna el valor máximo entre 0 y la cadena binaria de 8 bits ingresada
            </div>
        """)
        
        # Configurar duración del tooltip
        self.max_button.setToolTipDuration(7000)


        #-----------pal----------------
        self.pal_button = QPushButton()
        self.pal_button.setParent(self)
        self.pal_button.setGeometry(175, 70, 135, 220)
        self.pal_button.setStyleSheet("QPushButton { border: none; }")
        self.pal_button.setIcon(QIcon(path_to_pal_icon))
        self.pal_button.setIconSize(self.pal_button.size())
        self.pal_button.clicked.connect(self.openInputWindowPal)
        self.pal_button.enterEvent = lambda e: self.pal_button.setIcon(self.pal_icon_hover)
        self.pal_button.leaveEvent = lambda e: self.pal_button.setIcon(self.pal_icon_normal)
        self.pal_button.setToolTip("""
            <div style='background-color: #f0f0f0; 
                        padding: 10px; 
                        border: 2px solid #333; 
                        border-radius: 10px;'>
                <b>Máquina Pal</b><br>
                Acepta únicamente cadenas de palindromos
            </div>
        """)
        
        # Configurar duración del tooltip
        self.pal_button.setToolTipDuration(7000)

        self.__drag_position = None
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.__drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.__drag_position is not None:
            self.move(event.globalPosition().toPoint() - self.__drag_position)
            event.accept()
    
    def displayCredits(self):
        self.credits_window = CreditsWindow()
        self.credits_window.show()
    
    def openInputWindowMax(self):
        self.input_window = InputWindow(variant=0)
        self.input_window.show()
    def openInputWindowPal(self):
        self.input_window = InputWindow(variant=1)
        self.input_window.show()


if __name__ == "__main__":
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    app = QApplication(sys.argv)
    window = MainWindow(directorio_actual)
    window.show()
    sys.exit(app.exec())