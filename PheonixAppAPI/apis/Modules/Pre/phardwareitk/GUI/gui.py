from . import *

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from phardwareitk.GUI.gui_sdl import *

# sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from phardwareitk.ErrorSystem import ErrorSystem as es

if Unknown_os:
    es.PheonixOsError("Unknown OS detected. Program doesn't know will this GUI system work properly in this OS. To Test, please SET the Windows/Linux/Unix to True and Unknown OS to False in GUI.__init__.")

from phardwareitk.GUI import renderGUI

from OpenGL.GL import *
import time