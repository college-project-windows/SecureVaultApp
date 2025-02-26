from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
from database.file_model import store_file
import os

class FileSharingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure File Sharing")
        self.setGeometry(300, 200, 400, 300)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.upload_button = QPushButton("Upload & Encrypt File")
        self.upload_button.clicked.connect(self.upload_file)
        layout.addWidget(self.upload_button)

        self.setLayout(layout)

    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Upload")
        if file_path:
            file_name = os.path.basename(file_path)
            with open(file_path, "r") as file:
                file_content = file.read()
            store_file(file_name, file_content, "john_doe", "Manager")
            QMessageBox.information(self, "Success", "File Encrypted & Stored Successfully!")

if __name__ == "__main__":
    app = QApplication([])
    window = FileSharingWindow()
    window.show()
    app.exec_()
