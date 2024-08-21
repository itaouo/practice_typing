import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QFont

class SimpleApp(QWidget):
    def __init__(self, lines):
        super().__init__()
        self.lines = lines
        self.line = lines[0]
        self.which_line = 0
        self.wrong_times = 0

        self.setWindowTitle('Pratice typing')
        self.setGeometry(560, 440, 800, 200)
        large_font = QFont("Arial", 18)

        self.label = QLabel(self.line)
        self.label.setFont(large_font)

        self.text_input = QLineEdit(self)
        self.text_input.setFont(large_font)

        self.label2 = QLabel('', self)
        self.label2.setFont(large_font)

        self.text_input.returnPressed.connect(self.nextLine)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.label2)

        self.setLayout(layout)

    def updateLabel(self, text):
        self.label.setText(text)

    def updateLabel2(self, text):
        self.label2.setText(f"Wrong times: {text}")

    def update_input(self, text):
        self.text_input.setText(text)

    def nextLine(self):
        self.countWrongTimes()
        if not self.isNextColumnExisted():
            self.updateLabel2(self.wrong_times)
            return
        self.which_line += 1
        self.line = lines[self.which_line]
        self.updateLabel(self.line)
        self.update_input("")

    def isNextColumnExisted(self):
        if self.which_line < len(self.lines) - 1:
           return True
        return False
    
    def countWrongTimes(self):
        inp = self.text_input.text()
        min_len = min(len(self.line), len(inp))
        for i in range(min_len):
            if inp[i] != self.line[i]:
                self.wrong_times += 1
        self.wrong_times += max(len(self.line), len(inp)) - min_len

# Main execution
if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('test_info/1.java', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    lines = [s.strip() for s in lines]
    lines = [s for s in lines if s.strip()]
    window = SimpleApp(lines)
    window.show()
    sys.exit(app.exec_())