#    _____              .___       __________            _____   __           .__          ___.   .__
#   /     \ _____     __| _/____   \______   \___.__.   /  _  \ |  | __  _____|  |__   ____\_ |__ |  |__ ___.__._____
#  /  \ /  \\__  \   / __ |/ __ \   |    |  _<   |  |  /  /_\  \|  |/ / /  ___/  |  \ /  _ \| __ \|  |  <   |  |\__  \
# /    Y    \/ __ \_/ /_/ \  ___/   |    |   \\___  | /    |    \    <  \___ \|   Y  (  <_> ) \_\ \   Y  \___  | / __ \_
# \____|__  (____  /\____ |\___  >  |______  // ____| \____|__  /__|_ \/____  >___|  /\____/|___  /___|  / ____|(____  /
#         \/     \/      \/    \/          \/ \/              \/     \/     \/     \/           \/     \/\/          \/
#     ___ ___________                      .___             ___
#    /  / \_   _____/___  __ __  ____    __| _/___________  \  \
#   /  /   |    __)/  _ \|  |  \/    \  / __ |/ __ \_  __ \  \  \
#  (  (    |     \(  <_> )  |  /   |  \/ /_/ \  ___/|  | \/   )  )
#   \  \   \___  / \____/|____/|___|  /\____ |\___  >__|     /  /
#    \__\      \/                   \/      \/    \/        /__/






# __________.__                        .__           _________ __            .___.__
# \______   \  |__   ____  ____   ____ |__|__  ___  /   _____//  |_ __ __  __| _/|__| ____  ______
#  |     ___/  |  \_/ __ \/  _ \ /    \|  \  \/  /  \_____  \\   __\  |  \/ __ | |  |/  _ \/  ___/
#  |    |   |   Y  \  ___(  <_> )   |  \  |>    <   /        \|  | |  |  / /_/ | |  (  <_> )___ \
#  |____|   |___|  /\___  >____/|___|  /__/__/\_ \ /_______  /|__| |____/\____ | |__|\____/____  >
#                \/     \/           \/         \/         \/                 \/               \/

import sys
import os
import time

# Todo: Change current working directory

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.join("..", ""))

sys.path.append(os.getcwd())

from PheonixAppAPI.pheonixapp.files.GUI.assets import GAsset
from PheonixAppAPI.pheonixapp.files import LIB
from PheonixAppAPI.pheonixapp.files import PheonixStudioStarter as PSStarter
from PheonixStudioStarter import PATFHandler


from PyQt5 import *
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import (Qt, QPropertyAnimation, QEasingCurve, QByteArray, QRect, QRectF)
from PyQt5.QtGui import (QIcon, QFont, QPixmap)
import qdarkstyle

from ctypes import *

from validate_email import validate_email


WinDLL("Shell32").SetCurrentProcessExplicitAppUserModelID(LIB.PA_ID)

class SignupForm(QDialog):
    def __init__(self, initial_mode:str="dark"):
        super().__init__()
        self.dark_mode = True
        if initial_mode == "dark":
            pass
        elif initial_mode == "light":
            self.dark_mode = False
        else:
            print(f"No type of [{initial_mode}] is identified, available are -> [dark, light]")
            exit(1)

        self.initial_mode = initial_mode
        self.init_ui()

    def init_ui(self):
        icon = QIcon(GAsset.get("pheonixstudios", True))
        self.setWindowIcon(icon)
        self.setFixedSize(800,600)

        self.main_layout = QVBoxLayout(self)
        self.fields_layout = QGridLayout()
        self.main_layout.addLayout(self.fields_layout)

        # Todo: Apply Theme
        self.toggle_mode(f"init {self.initial_mode}")

        # Todo: Make Fonts
        self.mainFont = QFont("Roboto", 18)
        self.LFont = QFont("Roboto", 50, 100)

        self.main_label = QLabel("SignUp")
        self.main_label.setFont(self.LFont)
        self.main_label.show()
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Todo: Create labels and input fields
        self.name_label = QLabel("Name:")
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Enter your name")
        self.name_label.setFont(self.mainFont)
        self.name_edit.setFont(self.mainFont)

        #self.name_icon = QPixmap(GAsset.get("usernamedark")).scaled(24, 24)
        name_icon_label = QLabel()
        name_icon_label.setPixmap(self.name_icon)

        self.email_label = QLabel("Email:")
        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("Enter your email")
        self.email_label.setFont(self.mainFont)
        self.email_edit.setFont(self.mainFont)

        #self.email_icon = QPixmap(GAsset.get("maildark")).scaled(24, 24)
        email_icon_label = QLabel()
        email_icon_label.setPixmap(self.email_icon)

        self.password_label = QLabel("Password:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_label.setFont(self.mainFont)
        self.password_edit.setFont(self.mainFont)

        #self.password_icon = QPixmap(GAsset.get("passworddark")).scaled(24, 24)
        password_icon_label = QLabel()
        password_icon_label.setPixmap(self.password_icon)

        self.confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_edit = QLineEdit()
        self.confirm_password_edit.setEchoMode(QLineEdit.Password)
        self.confirm_password_label.setFont(self.mainFont)
        self.confirm_password_edit.setFont(self.mainFont)

        #self.confirm_password_icon = QPixmap(GAsset.get("passworddark")).scaled(24, 24)
        confirm_password_icon_label = QLabel()
        confirm_password_icon_label.setPixmap(self.confirm_password_icon)

        # Todo: Create Theme button
        #self.mode_button.setIcon(QIcon(GAsset.get("mswitchdark")))
        self.mode_button.setFixedSize(50, 50)
        self.mode_button.clicked.connect(self.toggle_mode)

        # Todo: Create Return button
        self.return_button.setFixedSize(50, 50)
        self.return_button.clicked.connect(self.changeWin)

        # Todo: Add widgets to layout
        self.fields_layout.addWidget(self.mode_button, 0, 0, Qt.AlignmentFlag.AlignLeft)

        self.fields_layout.addWidget(self.main_label, 0, 1, Qt.AlignmentFlag.AlignCenter)

        self.fields_layout.addWidget(self.name_label, 1, 0)
        self.fields_layout.addWidget(self.name_edit, 1, 1, 1, 2)
        self.fields_layout.addWidget(name_icon_label, 1, 3)

        self.fields_layout.addWidget(self.email_label, 2, 0)
        self.fields_layout.addWidget(self.email_edit, 2, 1, 1, 2)
        self.fields_layout.addWidget(email_icon_label, 2, 3)

        self.fields_layout.addWidget(self.password_label, 3, 0)
        self.fields_layout.addWidget(self.password_edit, 3, 1, 1, 2)
        self.fields_layout.addWidget(password_icon_label, 3, 3)

        self.fields_layout.addWidget(self.confirm_password_label, 4, 0)
        self.fields_layout.addWidget(self.confirm_password_edit, 4, 1, 1, 2)
        self.fields_layout.addWidget(confirm_password_icon_label, 4, 3)

        self.fields_layout.addWidget(self.return_button, 6, 0, Qt.AlignmentFlag.AlignLeft)

        # Todo: Create and add sign up button
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setFont(self.mainFont)
        self.signup_button.setGeometry(325, 400, 150, 40)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.signup_button)

        self.main_layout.addLayout(self.button_layout)

        # self.button_layout = self.main_layout.itemAt(self.main_layout.indexOf(self.signup_button)).geometry()

        self.button_animation = QPropertyAnimation(self.signup_button, b"geometry")
        self.button_animation.setDuration(100)  # Adjust animation duration (ms)
        self.button_animation.setEasingCurve(QEasingCurve.InOutCubic)

        self.signup_button.setGeometry(325, 450, 150, 40)
        self.signup_button.show()

        # Todo: Calculate original geometry for animation (maintain current position)
        self.original_geometry = self.signup_button.geometry()
        original_geometry_ = QRect(self.original_geometry.x(), self.original_geometry.y(), self.original_geometry.width(), self.original_geometry.height())

        original_width = self.original_geometry.width()
        original_height = self.original_geometry.height()

        # Todo: Define expanded dimensions
        expanded_width = original_width + 10
        expanded_height = original_height + 10

        # Todo: Define expanded geometry for animation with adjusted margins
        self.expanded_geometry = QRect(self.original_geometry.x(), self.original_geometry.y(), expanded_width, expanded_height)
        # Todo: Connect hover events to start/stop animation
        self.signup_button.enterEvent = self.handle_enter_event
        self.signup_button.leaveEvent = self.handle_leave_event

        self.main_layout.addWidget(self.signup_button)

        self.fields_layout.addWidget(self.signup_button, 5, 1, Qt.AlignmentFlag.AlignCenter)
        # Todo: Set window properties
        self.setWindowTitle("Phoenix App")
        # Todo: Adjust window size
        self.setLayout(self.main_layout)
        self.show()

        self.name_edit.textChanged.connect(self.check_validity)
        self.email_edit.textChanged.connect(self.check_validity)
        self.password_edit.textChanged.connect(self.check_validity)
        self.confirm_password_edit.textChanged.connect(self.check_validity)

        # Todo: Connect button click to a function
        self.signup_button.clicked.connect(self.handle_signup_click)
        self.signup_button.setEnabled(False)

    def toggle_mode(self, mode:str="init dark"):
        # Todo: If dark mode is on, change to light mode

        dark_mode = self.dark_mode

        self.mode_button = QPushButton()
        self.return_button = QPushButton()

        if not mode:
            if dark_mode == True:
                app.setStyleSheet("")
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.LightPalette()))
                self.name_icon = QPixmap(GAsset.get("username")).scaled(24, 24)
                self.email_icon = QPixmap(GAsset.get("mail")).scaled(24, 24)
                self.password_icon = QPixmap(GAsset.get("password")).scaled(24, 24)
                self.confirm_password_icon = QPixmap(GAsset.get("password")).scaled(24, 24)
                self.mode_button.setIcon(QIcon(GAsset.get("mswitch")))
                self.return_button.setIcon(QIcon(GAsset.get("return")))
                dark_mode = False
                self.refresh_window("light")
            else:
                app.setStyleSheet("")
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.DarkPalette()))
                self.name_icon = QPixmap(GAsset.get("usernamedark")).scaled(24, 24)
                self.email_icon = QPixmap(GAsset.get("maildark")).scaled(24, 24)
                self.password_icon = QPixmap(GAsset.get("passworddark")).scaled(24, 24)
                self.confirm_password_icon = QPixmap(GAsset.get("passworddark")).scaled(24, 24)
                self.mode_button.setIcon(QIcon(GAsset.get("mswitchdark")))
                self.return_button.setIcon(QIcon(GAsset.get("returndark")))
                dark_mode = True
                self.refresh_window("dark")
        else:
            if mode == "init dark":
                self.name_icon = QPixmap(GAsset.get("usernamedark")).scaled(24, 24)
                self.email_icon = QPixmap(GAsset.get("maildark")).scaled(24, 24)
                self.password_icon = QPixmap(GAsset.get("passworddark")).scaled(24, 24)
                self.confirm_password_icon = QPixmap(GAsset.get("passworddark")).scaled(24, 24)
                self.mode_button.setIcon(QIcon(GAsset.get("mswitchdark")))
                self.return_button.setIcon(QIcon(GAsset.get("returndark")))
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.DarkPalette()))
            elif mode == "init light":
                self.name_icon = QPixmap(GAsset.get("username")).scaled(24, 24)
                self.email_icon = QPixmap(GAsset.get("mail")).scaled(24, 24)
                self.password_icon = QPixmap(GAsset.get("password")).scaled(24, 24)
                self.confirm_password_icon = QPixmap(GAsset.get("password")).scaled(24, 24)
                self.mode_button.setIcon(QIcon(GAsset.get("mswitch")))
                self.return_button.setIcon(QIcon(GAsset.get("return")))
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.LightPalette()))

    def refresh_window(self, mode:str="dark"):
        self.close()

        new_window = SignupForm(mode)
        new_window.show()

    def changeWin(self, event, win:str="init", mode:str="dark"):
        if win.lower() == "init":
            self.close()
            time.sleep(1)
            new_win = InitScreen(mode)
            new_win.show()
        elif win.lower() == "signup":
            self.refresh_window()
        elif win.lower() == "login":
            self.close()
            time.sleep(1)
            new_win = LoginForm(mode)
            new_win.show()

    def check_TEXT_validity(self, text):
        # Todo: Check if name is not empty
        self.is_valid = len(text.strip()) > 0
        return self.is_valid

    def check_email_validity(self, text):
        # Todo: Email Validation
        valid = validate_email(text)
        if valid:
            return True
        else:
            return False

    def check_validity(self):
        v1 = self.check_TEXT_validity(self.name_edit.text())
        v2 = self.check_email_validity(self.email_edit.text())
        v3 = self.check_TEXT_validity(self.password_edit.text())
        v4 = self.check_TEXT_validity(self.confirm_password_edit.text())

        if v1 and v2:
            if v3 and v4:
                if self.password_edit.text() == self.confirm_password_edit.text():
                    self.update_button_state()

    def update_button_state(self):
        self.signup_button.setEnabled(True)

    def handle_enter_event(self, event):
        self.button_animation.setStartValue(QRectF(self.original_geometry))
        self.button_animation.setEndValue(QRectF(self.expanded_geometry))
        self.button_animation.start()

    def handle_leave_event(self, event):
        self.button_animation.setStartValue(QRectF(self.expanded_geometry))
        self.button_animation.setEndValue(QRectF(self.original_geometry))
        self.button_animation.start()

    def handle_signup_click(self):
        v1 = self.check_TEXT_validity(self.name_edit.text())
        v2 = self.check_email_validity(self.email_edit.text())
        v3 = self.check_TEXT_validity(self.password_edit.text())
        v4 = self.check_TEXT_validity(self.confirm_password_edit.text())

        name = self.name_edit.text()
        email = self.email_edit.text()
        password = self.password_edit.text()
        confirm_password = self.confirm_password_edit.text()

        message = f"Successfully signed up [{name}] with email [{email}]"

        if v1 and v2:
            self.name_edit.setPlaceholderText("Name")
            self.email_edit.setPlaceholderText("Email")
            if v3 and v4:
                self.password_edit.setPlaceholderText("Password")
                self.confirm_password_edit.setPlaceholderText("Confirm Password")
                if self.password_edit.text() == self.confirm_password_edit.text():
                    self.password_edit.setPlaceholderText("Password")
                    self.confirm_password_edit.setPlaceholderText("Confirm Password")
                    print(message)
                    PATFHandler(False, email, name, password).run()
                else:
                    print("Passwords don't match!")
                    self.password_edit.setPlaceholderText("Passwords Don't Match")
                    self.confirm_password_edit.setPlaceholderText("Passwords Don't Match")
            else:
                print("Passwords are required!")
                self.password_edit.setPlaceholderText("Required")
                self.confirm_password_edit.setPlaceholderText("Required")
        else:
            print("Name and Email should be valid not invalid or blank!")
            self.name_edit.setPlaceholderText("Required")
            self.email_edit.setPlaceholderText("Required")

class LoginForm(QDialog):
    def __init__(self, initial_mode:str="dark"):
        super().__init__()
        self.dark_mode = True
        if initial_mode == "dark":
            pass
        elif initial_mode == "light":
            self.dark_mode = False
        else:
            print(f"No type of [{initial_mode}] is identified, available are -> [dark, light]")
            exit(1)

        self.initial_mode = initial_mode
        self.init_ui()

    def init_ui(self):
        icon = QIcon(GAsset.get("pheonixstudios", True))
        self.setWindowIcon(icon)
        self.setFixedSize(800,500)

        self.main_layout = QVBoxLayout(self)
        self.fields_layout = QGridLayout()
        self.main_layout.addLayout(self.fields_layout)

        # Todo: Apply Theme
        self.toggle_mode(f"init {self.initial_mode}")

        # Todo: Make Fonts
        self.mainFont = QFont("Roboto", 18)
        self.LFont = QFont("Roboto", 50, 100)

        self.main_label = QLabel("Login")
        self.main_label.setFont(self.LFont)
        self.main_label.show()
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Todo: Create labels and input fields
        self.name_label = QLabel("Name:")
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Enter your name")
        self.name_label.setFont(self.mainFont)
        self.name_edit.setFont(self.mainFont)

        #self.name_icon = QPixmap(GAsset.get("usernamedark")).scaled(24, 24)
        name_icon_label = QLabel()
        name_icon_label.setPixmap(self.name_icon)

        self.password_label = QLabel("Password:")
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_label.setFont(self.mainFont)
        self.password_edit.setFont(self.mainFont)

        #self.password_icon = QPixmap(GAsset.get("passworddark")).scaled(24, 24)
        password_icon_label = QLabel()
        password_icon_label.setPixmap(self.password_icon)

        # Todo: Create Theme button

        #self.mode_button.setIcon(QIcon(GAsset.get("mswitchdark")))
        self.mode_button.setFixedSize(50, 50)
        self.mode_button.clicked.connect(self.toggle_mode)

        # Todo: Create Return button
        self.return_button.setFixedSize(50, 50)
        self.return_button.clicked.connect(self.changeWin)

        # Todo: Add widgets to layout
        self.fields_layout.addWidget(self.mode_button, 0, 0, Qt.AlignmentFlag.AlignLeft)

        self.fields_layout.addWidget(self.main_label, 0, 1, Qt.AlignmentFlag.AlignCenter)

        self.fields_layout.addWidget(self.name_label, 3, 0)
        self.fields_layout.addWidget(self.name_edit, 3, 1, 1, 2)
        self.fields_layout.addWidget(name_icon_label, 3, 3)

        self.fields_layout.addWidget(self.password_label, 4, 0)
        self.fields_layout.addWidget(self.password_edit, 4, 1, 1, 2)
        self.fields_layout.addWidget(password_icon_label, 4, 3)

        self.fields_layout.addWidget(self.return_button, 6, 0, Qt.AlignmentFlag.AlignLeft)

        # Todo: Create and add sign up button
        self.login_button = QPushButton("Login")
        self.login_button.setFont(self.mainFont)
        self.login_button.setGeometry(325, 400, 150, 40)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.login_button)

        self.main_layout.addLayout(self.button_layout)

        # self.button_layout = self.main_layout.itemAt(self.main_layout.indexOf(self.signup_button)).geometry()

        self.button_animation = QPropertyAnimation(self.login_button, b"geometry")
        self.button_animation.setDuration(100)  # Adjust animation duration (ms)
        self.button_animation.setEasingCurve(QEasingCurve.InOutCubic)

        self.login_button.setGeometry(325, 450, 150, 40)
        self.login_button.show()

        # Todo: Calculate original geometry for animation (maintain current position)
        self.original_geometry = self.login_button.geometry()
        original_geometry_ = QRect(self.original_geometry.x(), self.original_geometry.y(), self.original_geometry.width(), self.original_geometry.height())

        original_width = self.original_geometry.width()
        original_height = self.original_geometry.height()

        # Todo: Define expanded dimensions
        expanded_width = original_width + 10
        expanded_height = original_height + 10

        # Todo: Define expanded geometry for animation with adjusted margins
        self.expanded_geometry = QRect(self.original_geometry.x(), self.original_geometry.y(), expanded_width, expanded_height)
        # Todo: Connect hover events to start/stop animation
        self.login_button.enterEvent = self.handle_enter_event
        self.login_button.leaveEvent = self.handle_leave_event

        self.main_layout.addWidget(self.login_button)

        self.fields_layout.addWidget(self.login_button, 5, 1, Qt.AlignmentFlag.AlignCenter)
        # Todo: Set window properties
        self.setWindowTitle("Phoenix App")
        # Todo: Adjust window size
        self.setLayout(self.main_layout)
        self.show()

        self.name_edit.textChanged.connect(self.check_validity)
        self.password_edit.textChanged.connect(self.check_validity)

        # Todo: Connect button click to a function
        self.login_button.clicked.connect(self.handle_login_click)
        self.login_button.setEnabled(False)

    def toggle_mode(self, mode:str="init dark"):
        # Todo: If dark mode is on, change to light mode

        dark_mode = self.dark_mode

        self.mode_button = QPushButton()
        self.return_button = QPushButton()

        if not mode:
            if dark_mode == True:
                app.setStyleSheet("")
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.LightPalette()))
                self.name_icon = QPixmap(GAsset.get("username")).scaled(24, 24)
                self.password_icon = QPixmap(GAsset.get("password")).scaled(24, 24)
                self.mode_button.setIcon(QIcon(GAsset.get("mswitch")))
                self.return_button.setIcon(QIcon(GAsset.get("return")))
                dark_mode = False
                self.refresh_window("light")
            else:
                app.setStyleSheet("")
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.DarkPalette()))
                self.name_icon = QPixmap(GAsset.get("usernamedark")).scaled(24, 24)
                self.password_icon = QPixmap(GAsset.get("passworddark")).scaled(24, 24)
                self.mode_button.setIcon(QIcon(GAsset.get("mswitchdark")))
                self.return_button.setIcon(QIcon(GAsset.get("returndark")))
                dark_mode = True
                self.refresh_window("dark")
        else:
            if mode == "init dark":
                self.name_icon = QPixmap(GAsset.get("usernamedark")).scaled(24, 24)
                self.password_icon = QPixmap(GAsset.get("passworddark")).scaled(24, 24)
                self.mode_button.setIcon(QIcon(GAsset.get("mswitchdark")))
                self.return_button.setIcon(QIcon(GAsset.get("returndark")))
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.DarkPalette()))
            elif mode == "init light":
                self.name_icon = QPixmap(GAsset.get("username")).scaled(24, 24)
                self.password_icon = QPixmap(GAsset.get("password")).scaled(24, 24)
                self.mode_button.setIcon(QIcon(GAsset.get("mswitch")))
                self.return_button.setIcon(QIcon(GAsset.get("return")))
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.LightPalette()))

    def refresh_window(self, mode:str="dark"):
        self.close()

        new_window = LoginForm(mode)
        new_window.show()

    def changeWin(self, event, win:str="init", mode:str="dark"):
        if win.lower() == "init":
            self.close()
            time.sleep(1)
            new_win = InitScreen(mode)
            new_win.show()
        elif win.lower() == "login":
            self.refresh_window()
        elif win.lower() == "signup":
            self.close()
            time.sleep(1)
            new_win = LoginForm(mode)
            new_win.show()

    def check_TEXT_validity(self, text):
        # Todo: Check if name is not empty
        self.is_valid = len(text.strip()) > 0
        return self.is_valid

    def check_validity(self):
        v1 = self.check_TEXT_validity(self.name_edit.text())
        v3 = self.check_TEXT_validity(self.password_edit.text())

        if v1:
            if v3:
                self.update_button_state()

    def update_button_state(self):
        self.login_button.setEnabled(True)

    def handle_enter_event(self, event):
        self.button_animation.setStartValue(QRectF(self.original_geometry))
        self.button_animation.setEndValue(QRectF(self.expanded_geometry))
        self.button_animation.start()

    def handle_leave_event(self, event):
        self.button_animation.setStartValue(QRectF(self.expanded_geometry))
        self.button_animation.setEndValue(QRectF(self.original_geometry))
        self.button_animation.start()

    def handle_login_click(self):
        v1 = self.check_TEXT_validity(self.name_edit.text())
        v3 = self.check_TEXT_validity(self.password_edit.text())

        name = self.name_edit.text()
        password = self.password_edit.text()

        message = f"Successfully logged in [{name}]"

        if v1:
            self.name_edit.setPlaceholderText("Name")
            if v3:
                self.password_edit.setPlaceholderText("Password")
                print(message)
            else:
                print("Passwords are required!")
                self.password_edit.setPlaceholderText("Required")
        else:
            print("Name should be valid not invalid or blank!")
            self.name_edit.setPlaceholderText("Required")

class InitScreen(QDialog):
    def __init__(self, initial_mode:str="dark"):
        super().__init__()
        self.dark_mode = True
        if initial_mode == "dark":
            pass
        elif initial_mode == "light":
            self.dark_mode = False
        else:
            print(f"No type of [{initial_mode}] is identified, available are -> [dark, light]")
            exit(1)

        self.initial_mode = initial_mode
        self.init_ui()

    def init_ui(self):
        icon = QIcon(GAsset.get("pheonixstudios", True))
        self.setWindowIcon(icon)
        self.setFixedSize(1000,600)

        self.main_layout = QVBoxLayout(self)
        self.fields_layout = QGridLayout()
        self.main_layout.addLayout(self.fields_layout)

        # Todo: Apply Theme
        self.toggle_mode(f"init {self.initial_mode}")

        # Todo: Make Fonts
        self.mainFont = QFont("Roboto", 24)
        self.LFont = QFont("Roboto", 50, 100)

        self.main_label = QLabel("Pheonix Studios")
        self.main_label.setFont(self.LFont)
        self.main_label.show()
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Todo: Create buttons
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.setFont(self.mainFont)
        self.signup_button.setFixedSize(300, 80)
        self.signup_button.show()

        self.login_button = QPushButton("Login")
        self.login_button.setFont(self.mainFont)
        self.login_button.setFixedSize(300, 80)
        self.login_button.show()

        self.mode_button.setFixedSize(50, 50)
        self.mode_button.clicked.connect(self.toggle_mode)

        # Todo: Add widgets to layout
        self.fields_layout.addWidget(self.mode_button, 0, 0, Qt.AlignmentFlag.AlignLeft)

        self.fields_layout.addWidget(self.main_label, 0, 0, Qt.AlignmentFlag.AlignCenter)

        self.fields_layout.addWidget(self.signup_button, 2, 0, Qt.AlignmentFlag.AlignCenter)

        self.fields_layout.addWidget(self.login_button, 4, 0, Qt.AlignmentFlag.AlignCenter)

        # Todo: Set window properties
        self.setWindowTitle("Phoenix App")
        # Todo: Adjust window size
        self.setLayout(self.main_layout)
        self.show()

        # Todo: Connect button click to a function
        self.signup_button.clicked.connect(self.SignUp)
        self.login_button.clicked.connect(self.Login)

    def toggle_mode(self, mode:str="init dark"):
        # Todo: If dark mode is on, change to light mode

        dark_mode = self.dark_mode

        self.mode_button = QPushButton()

        if not mode:
            if dark_mode == True:
                app.setStyleSheet("")
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.LightPalette()))
                self.mode_button.setIcon(QIcon(GAsset.get("mswitch")))
                dark_mode = False
                self.refresh_window("light")
            else:
                app.setStyleSheet("")
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.DarkPalette()))
                self.mode_button.setIcon(QIcon(GAsset.get("mswitchdark")))
                dark_mode = True
                self.refresh_window("dark")
        else:
            if mode == "init dark":
                self.mode_button.setIcon(QIcon(GAsset.get("mswitchdark")))
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.DarkPalette()))
            elif mode == "init light":
                self.mode_button.setIcon(QIcon(GAsset.get("mswitch")))
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.LightPalette()))

    def refresh_window(self, mode:str="dark"):
        self.close()

        new_window = InitScreen(mode)
        new_window.show()

    def SignUp(self):
        self.close()
        SignupForm(self.initial_mode).show()

    def Login(self):
        self.close()
        LoginForm(self.initial_mode).show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = InitScreen("dark")
    sys.exit(app.exec_())