"""
Under Development. The provided functions in gui_sdl and renderGUI are just for making the gui process simple.
You can use this file to use SDL and OpenGL functions to create whatever you want.

NOTES:
1. Uses SDL2 (Simple DirectMedia Layer) and OpenGL (Open Graphics Library)

2. Both SDL2 and OpenGL are cross-platform.

3. OpenGL may vary depending on graphics card.

4. To use OpenGL follow the steps below ->

 a. Change the directory to phardwareitk Folder.

 b. Do - '''pip install cython'''


 c. Do - '''cythonize -i GUI/renderGUI.pyx'''


 d. Download GCC


 e. Run - '''gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I/[Path to Main Python Folder] -o GUI/renderGUI.[so in linux and pyd in windows] GUI/renderGUI.c'''


 f. The functions from renderGUI will be imported as OpenGUI.[functions]

5. SDL2 Only supports 2d and provides more simple functions. Whereas OpenGL is known for its complexity and performance. OpenGL directly communicates with the GPU and hence needs to be written in C. OpenGL supports both 2D and 3D and complex shapes.

6. Better to import phardwareitk.Extensions, for classes like PIcon, PWidget, Color, TextFont, it also provides HyperIn and HyperOut files, including better versions of python buitins"""

from . import *

from sdl2 import *
from OpenGL import *

import sdl2
import OpenGL.GL

from OpenGL.GL import *

import sys
import os

if not sys.path[PHardwareITK] == PHardwareITK_P:
    sys.path.append(PHardwareITK_P)

from phardwareitk.GUI.gui_sdl import *
from phardwareitk import LIB


# sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from phardwareitk.ErrorSystem import ErrorSystem as Errors

if Unknown_os:
    Errors.PheonixOsError("Unknown OS detected. Program doesn't know will this GUI system work properly in this OS. To Test, please SET the Windows/Linux/Unix to True and Unknown OS to False in GUI.__init__.")

if os.path.exists(LIB.Paths.renderGUIPYD_GUI) or os.path.exists(LIB.Paths.renderGUISO_GUI):
    from phardwareitk.GUI import renderGUI as OpenGui

class ToStandaloneApplication():
    """Convert the GUI app to a standalone application. [.EXE/.ELF/...]
    """
    def __init__(self, getRequirements:bool, icon:Optional[str], file:str, windowed:bool=False) -> None:
        """Initialize function of ToStandaloneApplication.

        Args:
            getRequirements (bool): Download the requirements?
            icon (Optional[str]): The icon to be used. Leave for default.
            file (str): The main .py file.
            windowed (bool): Whether to run the app inside a window. NOTE: If the app is a GUI application then it is recommended to Set this to False.
        """
        self.gr = getRequirements
        self.file = file
        self.icon = icon
        self.windowed = windowed
        self.cmd = ""

        if self.gr:
            self.getReq()

        self.makeCmd()

        if self.windowed == True:
            self.addWIN()

        if (self.icon != "" and self.icon) and windowed:
            self.addIcon()

        self.runCmds1()
        self.MakeStandaloneApplication()

    def runCmds1(self):
        self.cmd += self.file

    def makeCmd(self):
        self.cmd += f"pyinstaller --onefile"

    def addWIN(self):
        self.cmd += f"--windowed "

    def addIcon(self):
        self.cmd += f"--icon={self.icon} "

    def getReq(self):
        os.system("pip install pyinstaller")

    def MakeStandaloneApplication(self):
        """Makes a standalone application.
        """
        os.system(self.cmd)