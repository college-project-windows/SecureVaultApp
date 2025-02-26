from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from database.db_setup import users_collection
import bcrypt
import qrcode
import os

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure Login")
        self.setGeometry(300, 200, 400, 300)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.otp_label = QLabel("Enter OTP (Check email/QR):")
        self.otp_input = QLineEdit()
        layout.addWidget(self.otp_label)
        layout.addWidget(self.otp_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.verify_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def verify_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        otp = self.otp_input.text()

        user = users_collection.find_one({"username": username})
        if user and bcrypt.checkpw(password.encode(), user["password"]):
            # Validate OTP (dummy check for now)
            if otp == "123456":
                QMessageBox.information(self, "Success", "Login Successful")
                self.close()
            else:
                QMessageBox.warning(self, "Error", "Invalid OTP")
        else:
            QMessageBox.warning(self, "Error", "Invalid Credentials")

if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    window.show()
    app.exec_()
