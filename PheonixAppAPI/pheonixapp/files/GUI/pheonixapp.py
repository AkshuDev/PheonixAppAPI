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
from PheonixAppAPI.pheonixapp.files.PheonixStudioStarter import PATFHandler
from PheonixAppAPI.pheonixapp.files.GUI import PAFhandler

from PyQt5 import *
from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFrame, QSizePolicy, QMenuBar, QMainWindow, QMenu, QAction,
                            QCheckBox, QToolButton)
from PyQt5.QtCore import (Qt, QPropertyAnimation, QEasingCurve, QByteArray, QRect, QRectF, QObject, QEvent)
from PyQt5.QtGui import (QIcon, QFont, QPixmap, QTextFrame)
import qdarkstyle

from ctypes import *

WinDLL("Shell32").SetCurrentProcessExplicitAppUserModelID(LIB.PA_ID)

# class Settings(QWidget):
    # def __init__(self, parent:None):
    #     super().__init__(parent)

    #     # Todo: Make Sliding Animation
    #     self.slide_animation = QPropertyAnimation(self, b"geometry")
    #     self.slide_animation.setDuration(250)
    #     self.slide_animation.setEasingCurve(QEasingCurve.InOutCubic)

    #     self.init_ui()

    # def init_ui(self):
    #     layout = QVBoxLayout()

    #     label = QLabel("Settings")
    #     label.setFont(QFont("Roboto", 16))
    #     label.setStyleSheet("color: white;")
    #     layout.addWidget(label)

    #     # Todo: Make the Frame

    #     self.panel = QFrame(self)
    #     self.panel.setStyleSheet("border-radius: 5px; background-color: black; color: white;")
    #     layout.addWidget(self.panel)

    #     #Todo: Make Theme Changer
    #     self.theme_checkbox = QCheckBox("Enable Dark Mode")
    #     self.theme_checkbox.setStyleSheet("color: white; border-radius: 20px; background-color: grey;")
    #     layout.addWidget(self.theme_checkbox)

    #     # Todo: Make Save settings Button
    #     save_button = QPushButton("Save Settings")
    #     save_button.setStyleSheet("background-color: #4CAF50; color: white; border: none; padding: 10px; border-radius: 20px;")
    #     layout.addWidget(save_button)

    #     layout.addStretch()
    #     self.setLayout(layout)

    # def show_sidebar(self):
    #     # Todo: Calculate target geometry for open state
    #     target_geom = QRect(self.width(), 0, self.width(), self.height())
    #     self.slide_animation.setStartValue(self.geometry())
    #     self.slide_animation.setEndValue(target_geom)
    #     self.slide_animation.start()
    #     self.show()

    # def hide_sidebar(self):
    #     # Todo: Calculate target geometry for closed state (replace with your desired position)
    #     target_geom = QRect(-self.width(), 0, self.width(), self.height())
    #     self.slide_animation.setStartValue(self.geometry())
    #     self.slide_animation.setEndValue(target_geom)
    #     self.slide_animation.start()
    #     self.hide()

class PheonixApp(QMainWindow):
    def __init__(self, initial_mode:str="dark") -> None:
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

        # Todo: Adjust window size
        self.setWindowIcon(icon)
        self.setMinimumSize(1000, 600)
        self.setMaximumSize(1700, 800)

        self.fields_layout = QGridLayout()

        self.top_bar_layout = QHBoxLayout()

        self.setLayout(self.fields_layout)

        # Todo: Apply Theme
        self.toggle_mode(f"init {self.initial_mode}")

        # Todo: Make Fonts
        self.mainFont = QFont("Roboto", 24)
        self.topFont = QFont("Roboto", 12, 100)
        self.LFont = QFont("Roboto", 50, 100)

        # Todo: Set window properties
        self.setWindowTitle("Phoenix App")

        # self.setLayout(self.main_layout)

        self.MLabel = QLabel("Pheonix Studios")
        self.MLabel.setFont(self.topFont)

        # Todo: Make Menubar
        self.menubar = QMenuBar(self)

        self.menubar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.setMenuBar(self.menubar)

        # Todo: Add Items to Menubar
        self.accountMenu = self.menubar.addMenu(QIcon(GAsset.get("username")), "&Account")
        self.settingsMenu = self.menubar.addMenu(QIcon(GAsset.get("settings")), "&Settings")
        self.homeMenu = self.menubar.addMenu(QIcon(GAsset.get("home")), "&Home")

        self.settingsMenu.addSeparator()
        self.accountMenu.addSeparator()

        # Todo: Make the Sidebar
        self.settings_sidebar = QFrame(self)
        self.settings_sidebar.setStyleSheet("border-radius: 10px; background-color: black;")
        self.settings_sidebar.setFixedSize(500, 500)
        self.settings_sidebar.setGeometry(0, 70, self.settings_sidebar.width(), self.settings_sidebar.height())

        # Todo: Make Actions
        # self.sidebar_action = QToolButton(self)
        # self.sidebar_action.setText("Settings")
        # self.sidebar_action.setIcon(QIcon(GAsset.get("settings")))
        # self.sidebar_action.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        # self.sidebar_action.setMenu(self.settingsMenu)

        # Todo: Connect Action To a Function
        # self.sidebar_action.clicked.connect(self.handle_menu_action)

        # Todo: Connect Actions
        self.settingsMenu.triggered.connect(self.handle_menu_action)

        self.menubar.setFont(self.topFont)
        MStyleSheet = ""
        MHStyleSheet = ""

        if PAFhandler.PAFhandler("get", {}, True, "", "GUI", "def_theme").run() == "dark":
            MStyleSheet = "background-color: white; color:black; border-radius:5px"
            MHStyleSheet = "background-color: grey; color:black; border-radius:5px"
        else:
            MStyleSheet = "background-color: grey; color:white; border-radius:5px;"
            MHStyleSheet = "background-color: black; color:white; border-radius:5px;"

        self.menubar.setStyleSheet(MStyleSheet)

        self.setBaseSize(1000, 600)
        self.show()

    def handle_menu_action(self, text:str="&Settings"):
        if text == "&Settings":
            if not self.settings_sidebar.isVisible():
                self.settings_sidebar.show()
            else:
                self.settings_sidebar.hide()

    def refresh_window(self, initial_mode:str="dark"):
        self.close()
        new_window = PheonixApp(initial_mode)
        new_window.show()

    def toggle_mode(self, mode:str="dark"):
        dark_mode = self.dark_mode

        self.mode_button = QPushButton()
        self.settings_button = QPushButton()

        if not mode:
            if dark_mode == True:
                app.setStyleSheet("")
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.LightPalette()))
                self.mode_button.setIcon(QIcon(GAsset.get("mswitch")))
                self.settings_button.setIcon(QIcon(GAsset.get("settings")))
                dark_mode = False
                self.refresh_window("light")
            else:
                app.setStyleSheet("")
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.DarkPalette()))
                self.mode_button.setIcon(QIcon(GAsset.get("mswitchdark")))
                self.settings_button.setIcon(QIcon(GAsset.get("settingsdark")))
                dark_mode = True
                self.refresh_window("dark")
        else:
            if mode == "init dark":
                self.mode_button.setIcon(QIcon(GAsset.get("mswitchdark")))
                self.settings_button.setIcon(QIcon(GAsset.get("settingsdark")))
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.DarkPalette()))
            elif mode == "init light":
                self.mode_button.setIcon(QIcon(GAsset.get("mswitch")))
                self.settings_button.setIcon(QIcon(GAsset.get("settings")))
                app.setStyleSheet(qdarkstyle._load_stylesheet('pyqt5', qdarkstyle.LightPalette()))

# Custom event filter to suppress mouse grab error
class MouseGrabFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.WindowActivate:
            print("Window Activated!")
            print(obj)
            if hasattr(obj, 'setMouseGrabEnabled'):
                print("No2")
                obj.setMouseGrabEnabled(False)
        return super().eventFilter(obj, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mouse_grab_filter = MouseGrabFilter()
    app.installEventFilter(mouse_grab_filter)
    App = PheonixApp("dark")
    sys.exit(app.exec_())