import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QGridLayout, QPushButton, QLabel, QTextEdit, QComboBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QClipboard

class BitConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("bitvis - Bit Converter")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.center_window()

        # Main layout
        layout = QVBoxLayout()

        # Input layout
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter a number")
        self.input_field.setFont(QFont("Consolas", 24))  # Use Consolas font
        self.input_field.textChanged.connect(self.update_display)
        self.input_field.returnPressed.connect(self.handle_enter)  # Custom handler for Enter key

        self.format_selector = QComboBox(self)
        self.format_selector.setFixedWidth(100)
        self.format_selector.addItems(["Dec", "Hex", "Bin"])
        self.format_selector.setToolTip("Select input format (Dec, Hex, Bin)")
        self.format_selector.currentIndexChanged.connect(self.update_display)
        self.format_selector.setFont(QFont("Consolas", 12))

        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.format_selector)

        # Display area
        self.result_display = QTextEdit(self)
        self.result_display.setReadOnly(True)
        self.result_display.setFont(QFont("Consolas", 12))

        # Bit position display
        self.bit_display = QWidget()
        self.bit_layout = QGridLayout()
        self.bit_display.setLayout(self.bit_layout)

        layout.addLayout(input_layout)
        layout.addWidget(self.result_display)
        layout.addWidget(QLabel("Bit Positions:", self))
        layout.addWidget(self.bit_display)

        self.setLayout(layout)

        # Styling
        self.setStyleSheet("""
            QWidget {
                background-color: palette(window);
                border-radius: 25px; /* More rounded corners */
            }
            QLineEdit, QTextEdit, QComboBox, QLabel {
                font-family: Consolas;
                border: 1px solid palette(dark);
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton {
                margin: 2px;
                font-size: 8px;
                width: 16px;
                height: 16px;
                background-color: palette(button);
                border: 1px solid palette(light);
                border-radius: 8px; /* More rounded for circular appearance */
            }
            QPushButton:checked {
                background-color: palette(highlight);
                border: 1px solid palette(highlighted-text);
            }
        """)

        # Initialize bit positions
        self.display_bit_positions(0)

    def center_window(self):
        screen = QApplication.primaryScreen().availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen.center())
        self.move(window_geometry.topLeft())

    def update_display(self):
        input_value = self.input_field.text()
        format_type = self.format_selector.currentText()

        try:
            if format_type == "Dec":
                value = int(input_value) if input_value else 0
            elif format_type == "Hex":
                value = int(input_value, 16) if input_value else 0
            elif format_type == "Bin":
                value = int(input_value, 2) if input_value else 0
            else:
                value = 0

            self.display_number_formats(value)
            self.display_bit_positions(value)
        except ValueError:
            self.result_display.setText("Invalid input")
            self.display_bit_positions(0)

    def display_number_formats(self, value):
        decimal = value
        hexadecimal = hex(value)
        binary = bin(value)

        self.result_display.setText(
            f"Dec: {decimal:,}\n\nHex: {hexadecimal}\n\nBin: {binary}".replace(",", ".")
        )

    def display_bit_positions(self, value):
        self.clear_bit_positions()
        for i in range(31, -1, -1):
            bit_set = (value & (1 << i)) != 0

            #
            row = 0 if i >= 16 else 1
            col_bit = i % 16
            col_space = col_bit // 4
            col = 15 - col_bit
            # 
            bit_layout2 = QVBoxLayout()
            button = QPushButton(self)
            button.setCheckable(True)
            button.setChecked(bit_set)
            button.clicked.connect(lambda _, pos=i: self.toggle_bit(pos))
            button.setFixedWidth(22)
            label = QLabel(str(i), self)
            label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            label.setFont(QFont("Consolas", 8))
            if (col_bit % 4 == 0) and (col_bit != 0):
                label.setMinimumWidth(50)
            else:
                label.setMinimumWidth(30)
            bit_layout2.addWidget(button)
            bit_layout2.addWidget(label)
            self.bit_layout.addLayout(bit_layout2, row, col)
            
    def clear_bit_positions(self):
        for i in reversed(range(self.bit_layout.count())):
            layout_item = self.bit_layout.itemAt(i)
            while layout_item.count():
                widget = layout_item.takeAt(0).widget()
                if widget:
                    widget.deleteLater()

    def toggle_bit(self, position):
        try:
            input_value = self.input_field.text()
            format_type = self.format_selector.currentText()

            if format_type == "Dec":
                value = int(input_value) if input_value else 0
            elif format_type == "Hex":
                value = int(input_value, 16) if input_value else 0
            elif format_type == "Bin":
                value = int(input_value, 2) if input_value else 0
            else:
                value = 0

            value ^= (1 << position)  # Toggle the bit

            if format_type == "Dec":
                self.input_field.setText(str(value))
            elif format_type == "Hex":
                self.input_field.setText(hex(value)[2:])
            elif format_type == "Bin":
                self.input_field.setText(bin(value)[2:])

        except ValueError:
            pass

    def mousePressEvent(self, event):
        if not self.bit_display.geometry().contains(event.pos()):
            self.input_field.setFocus()
        super().mousePressEvent(event)

    def handle_enter(self):
        if not self.input_field.hasFocus():
            self.input_field.setFocus()
        else:
            self.input_field.clearFocus()

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.AltModifier:
            if event.key() == Qt.Key.Key_1:
                self.format_selector.setCurrentIndex(0)  # Set "Dec" as selected
            elif event.key() == Qt.Key.Key_2:
                self.format_selector.setCurrentIndex(1)  # Set "Hex" as selected
            elif event.key() == Qt.Key.Key_3:
                self.format_selector.setCurrentIndex(2)  # Set "Bin" as selected
        elif event.modifiers() == Qt.KeyboardModifier.ControlModifier and event.key() == Qt.Key.Key_C:
            clipboard = QApplication.clipboard()
            clipboard.setText(self.input_field.text())
        elif event.key() == Qt.Key.Key_Escape:
            if self.input_field.hasFocus():
                self.input_field.clearFocus()
            elif self.input_field.text():
                self.input_field.clear()
                self.result_display.clear()
                self.display_bit_positions(0)
            else:
                QApplication.quit()
        elif event.key() == Qt.Key.Key_Return:
            self.handle_enter()
        else:
            super().keyPressEvent(event)

def main():
    app = QApplication(sys.argv)
    window = BitConverterApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BitConverterApp()
    window.show()
    sys.exit(app.exec())