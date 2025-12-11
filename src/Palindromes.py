from PyQt6.QtWidgets import QLabel, QPushButton, QApplication, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
import sys, os


class StepsWindow(QMainWindow):
    def __init__(self, tm, directorio: str):
        super().__init__()
        self.tm = tm
        self.steps = 0
        self.directorio = directorio

        self.text_mode = False

        self.setWindowTitle("Palindrome")
        self.setGeometry(300, 200, 600, 450)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background-color: white;")

        SegoeScriptFont = QFont("Segoe Script", 12, QFont.Weight.Bold)
        ConsolasFont = QFont("Consolas", 16)
        ArialFont = QFont("Arial", 10)

        path_to_close = os.path.join(directorio, "assets", "icons", "close_btn.png")
        self.close_icon_normal = QIcon(path_to_close)
        path_to_close_hover = os.path.join(directorio, "assets", "icons", "close_btn_hover.png")
        self.close_icon_hover = QIcon(path_to_close_hover)

        path_to_step = os.path.join(directorio, "assets", "icons", "st_btn.png")
        self.step_icon_normal = QIcon(path_to_step)
        path_to_step_hover = os.path.join(directorio, "assets", "icons", "st_btn_hover.png")
        self.step_icon_hover = QIcon(path_to_step_hover)


        #Ttulo
        self.title_label = QLabel("Comprobación de cadena", self)
        self.title_label.setFont(SegoeScriptFont)
        self.title_label.setStyleSheet("color: black;")
        self.title_label.setGeometry(10, 10, 300, 30)

        self.close_button = QPushButton(self)
        self.close_button.setGeometry(560, 10, 30, 30)
        self.close_button.clicked.connect(self.close)
        self.close_button.setIcon(self.close_icon_normal)
        self.close_button.setIconSize(self.close_button.size())
        self.close_button.setStyleSheet("QPushButton { border: none; }")
        self.close_button.enterEvent = lambda e: self.close_button.setIcon(self.close_icon_hover)
        self.close_button.leaveEvent = lambda e: self.close_button.setIcon(self.close_icon_normal)

        self.lbl_state = QLabel("Estado: q0 | Pasos: 0", self)
        self.lbl_state.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.lbl_state.setStyleSheet("color: black;")
        self.lbl_state.setGeometry(20, 50, 400, 30)

        self.lbl_t1_title = QLabel("Cinta 1:", self)
        self.lbl_t1_title.setFont(ArialFont)
        self.lbl_t1_title.setStyleSheet("color: gray;")
        self.lbl_t1_title.setGeometry(20, 90, 200, 20)

        self.lbl_tape1 = QLabel(self)
        self.lbl_tape1.setFont(ConsolasFont)
        self.lbl_tape1.setStyleSheet(
            "background-color: #B0B0B0; color: black; border-radius: 5px; padding: 5px; border: 1px solid #333;")
        self.lbl_tape1.setGeometry(20, 115, 560, 60)

        self.lbl_t2_title = QLabel("Cinta 2:", self)
        self.lbl_t2_title.setFont(ArialFont)
        self.lbl_t2_title.setStyleSheet("color: gray;")
        self.lbl_t2_title.setGeometry(20, 185, 200, 20)

        self.lbl_tape2 = QLabel(self)
        self.lbl_tape2.setFont(ConsolasFont)
        self.lbl_tape2.setStyleSheet(
            "background-color: #B0B0B0; color: white; border-radius: 5px; padding: 5px; border: 1px solid #333;")
        self.lbl_tape2.setGeometry(20, 210, 560, 60)

        self.lbl_result = QLabel("", self)
        self.lbl_result.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_result.setGeometry(20, 350, 560, 40)
        self.lbl_result.hide()

        self.step_button = QPushButton(self)
        self.step_button.setGeometry(200, 290, 200, 40)
        self.step_button.setIcon(self.step_icon_normal)
        self.step_button.setIconSize(self.step_button.size())
        self.step_button.setStyleSheet("QPushButton { border: none; }")
        self.step_button.clicked.connect(self.execute_step)

        self.step_button.enterEvent = self.on_step_enter
        self.step_button.leaveEvent = self.on_step_leave

        self.__drag_position = None
        self.update_ui()

    def on_step_enter(self, event):
        if not self.text_mode:
            self.step_button.setIcon(self.step_icon_hover)

    def on_step_leave(self, event):
        if not self.text_mode:
            self.step_button.setIcon(self.step_icon_normal)

    def execute_step(self):
        if not self.text_mode:
            self.text_mode = True
            self.step_button.setIcon(QIcon())
            self.step_button.setText("Siguiente Paso")

            self.step_button.setStyleSheet("""
                QPushButton { 
                    border: none; 
                    color: black; 
                    font-weight: bold; 
                    font-size: 16px; 
                }
                QPushButton:hover { color: #494949; } 
            """)

        moved = self.tm.step()
        self.steps += 1
        self.update_ui()

        is_finished = False
        result_text = ""
        result_color = ""

        if self.tm.current_state in self.tm.final_states:
            is_finished = True
            result_text = "¡Es un palindromo!"
            result_color = "#00b100"
            self.lbl_state.setText(f"Estado: {self.tm.current_state} (FINAL) | Pasos: {self.steps}")

        elif not moved and self.tm.current_state not in self.tm.final_states:
            is_finished = True
            result_text = "No es un palindromo (Sin transición)"
            result_color = "#b51f1f"  # Rojo

        if is_finished:
            self.lbl_result.setText(result_text)
            self.lbl_result.setStyleSheet(
                f"color: {result_color}; border: 1px solid {result_color}; border-radius: 5px;")
            self.lbl_result.show()

            self.step_button.setText("Finalizar")
            self.step_button.setStyleSheet(f"""
                QPushButton {{ 
                    border: none; 
                    color: {result_color}; 
                    font-weight: bold; 
                    font-size: 16px; 
                }}
                QPushButton:hover {{ color: #494949; }}
            """)

            self.step_button.clicked.disconnect()
            self.step_button.clicked.connect(self.close)

    def update_ui(self):
        self.lbl_state.setText(f"Estado: {self.tm.current_state} | Pasos: {self.steps}")
        self.lbl_tape1.setText(self.get_html_tape(self.tm.tape_1, self.tm.head_1))
        self.lbl_tape2.setText(self.get_html_tape(self.tm.tape_2, self.tm.head_2))

    def get_html_tape(self, tape, head):
        tape_line_html = ""
        arrow_line_html = ""

        highlight_color = "#b42424"
        normal_color = "black"
        arrow_char = "↑"
        spacer = "&nbsp;"

        for i, char in enumerate(tape):
            tape_line_html += f"<span style='color: {normal_color};'>{spacer}{char}{spacer}</span>"

            if i == head:
                arrow_line_html += f"<span style='color: {highlight_color}; font-weight:bold;'>{spacer}{arrow_char}{spacer}</span>"
            else:
                arrow_line_html += f"<span>{spacer}{spacer}{spacer}</span>"
        final_html = f"<div>{tape_line_html}<br>{arrow_line_html}</div>"
        return final_html

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.__drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.__drag_position is not None:
            self.move(event.globalPosition().toPoint() - self.__drag_position)
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    from Binary_PalindromesTM import Binary_PalindromesTM

    tm = Binary_PalindromesTM()
    tm.load("10101", run_type=True)

    window = StepsWindow(tm, os.path.dirname(os.path.abspath(__file__)))
    window.show()
    sys.exit(app.exec())