from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
#from database.chat_model import store_chat

class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Private Encrypted Chat")
        self.setGeometry(300, 200, 400, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.receiver_label = QLabel("Recipient Username:")
        self.receiver_input = QLineEdit()
        layout.addWidget(self.receiver_label)
        layout.addWidget(self.receiver_input)

        self.message_label = QLabel("Message:")
        self.message_input = QLineEdit()
        layout.addWidget(self.message_label)
        layout.addWidget(self.message_input)

        self.send_button = QPushButton("Send Secure Message")
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        layout.addWidget(self.chat_display)

        self.setLayout(layout)

    def send_message(self):
        receiver = self.receiver_input.text()
        message = self.message_input.text()
        #store_chat("john_doe", receiver, message)
        self.chat_display.append(f"Sent to {receiver}: {message}")

if __name__ == "__main__":
    app = QApplication([])
    window = ChatWindow()
    window.show()
    app.exec_()
