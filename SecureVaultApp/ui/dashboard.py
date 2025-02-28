from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QStackedWidget, QLineEdit
from PyQt5.QtGui import QFont

class SecureDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Secure Data Sharing - Dashboard")
        self.setGeometry(100, 100, 800, 500)
        
        main_layout = QHBoxLayout()
        
        # Sidebar (Initially Hidden)
        self.sidebar = QVBoxLayout()
        self.home_btn = QPushButton("Home")
        self.file_manager_btn = QPushButton("Upload File")
        self.retrieve_file_btn = QPushButton("Retrieve File")
        self.chat_btn = QPushButton("Secure Chat")
        self.logout_btn = QPushButton("Logout")
        
        for btn in [self.home_btn, self.file_manager_btn, self.retrieve_file_btn, self.chat_btn, self.logout_btn]:
            btn.setFont(QFont("Arial", 12))
            btn.hide()  # Hide buttons initially
            self.sidebar.addWidget(btn)
        
        # Main Content Area
        self.stack = QStackedWidget()
        
        # Login Page
        self.login_page = QLabel("Welcome to Secure Data Sharing Platform")
        self.login_page = QWidget()
        login_layout = QVBoxLayout()
        login_layout.addWidget(QLabel("Email:"))
        self.email_input = QLineEdit()
        login_layout.addWidget(self.email_input)
        login_layout.addWidget(QLabel("Password:"))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        login_layout.addWidget(self.password_input)
        self.login_button = QPushButton("Login")
        login_layout.addWidget(self.login_button)
        self.register_button = QPushButton("Register")
        login_layout.addWidget(self.register_button)
        self.login_page.setLayout(login_layout)
        
        # Home Page
        self.home_page = QLabel("Welcome to Secure Data Sharing Platform")
        self.home_page.setFont(QFont("Arial", 14))
        
        # Other Pages
        self.file_manager_page = QLabel("[Upload Files to Cloud UI Here]")
        self.file_manager_page.setFont(QFont("Arial", 14))
        self.retrieve_file_page = QLabel("[Retrieve Files from Cloud UI Here]")
        self.retrieve_file_page.setFont(QFont("Arial", 14))
        self.chat_page = QLabel("[Secure Chat UI Here]")
        self.chat_page.setFont(QFont("Arial", 14))
        
        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.file_manager_page)
        self.stack.addWidget(self.retrieve_file_page)
        self.stack.addWidget(self.chat_page)
        
        # Sidebar Navigation Actions
        self.home_btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.home_page))
        self.file_manager_btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.file_manager_page))
        self.retrieve_file_btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.retrieve_file_page))
        self.chat_btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.chat_page))
        self.logout_btn.clicked.connect(self.logout)
        
        # Login Button Action
        self.login_button.clicked.connect(self.login)
        
        # Adding layouts
        main_layout.addLayout(self.sidebar, 1)
        main_layout.addWidget(self.stack, 3)
        
        self.setLayout(main_layout)
        
    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        
        if email and password:  # Placeholder condition, replace with actual authentication logic
            self.stack.setCurrentWidget(self.home_page)
            for btn in [self.home_btn, self.file_manager_btn, self.retrieve_file_btn, self.chat_btn, self.logout_btn]:
                btn.show()  # Show sidebar options after login
        
    def logout(self):
        self.stack.setCurrentWidget(self.login_page)
        for btn in [self.home_btn, self.file_manager_btn, self.retrieve_file_btn, self.chat_btn, self.logout_btn]:
            btn.hide()  # Hide options after logout
        self.email_input.clear()
        self.password_input.clear()
        
if __name__ == "__main__":
    app = QApplication([])
    window = SecureDashboard()
    window.show()
    app.exec_()
