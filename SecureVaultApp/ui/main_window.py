from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from ui.file_sharing import FileSharingWindow
from ui.chat_window import ChatWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SecureOrgApp Dashboard")
        self.setGeometry(200, 150, 400, 250)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.file_sharing_button = QPushButton("Secure File Sharing")
        self.file_sharing_button.clicked.connect(self.open_file_sharing)
        layout.addWidget(self.file_sharing_button)

        self.chat_button = QPushButton("Private Encrypted Chat")
        self.chat_button.clicked.connect(self.open_chat)
        layout.addWidget(self.chat_button)

        self.setLayout(layout)

    def open_file_sharing(self):
        self.file_sharing_window = FileSharingWindow()
        self.file_sharing_window.show()

    def open_chat(self):
        self.chat_window = ChatWindow()
        self.chat_window.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
