import platform
import sdl2

import sys
import os

PHardwareITK = len(sys.path) - 1
PHardwareITK_P = os.path.join(os.path.dirname(__file__), "..", "..")

if not sys.path[PHardwareITK] == PHardwareITK_P:
    sys.path.append(PHardwareITK_P)

from phardwareitk.Extensions import HyperOut
from phardwareitk import Extensions

from typing import *

def get_platform() -> str:
    return platform.system().lower()

def SafeExitSDL(msg:Optional[Union[str, int, dict, bool, list, tuple]], DestroyFunc:object, DestroyFuncParams:tuple) -> None:
    """Safe Exit for SDL.

    Args:
        msg (Optional[Union[str, int, dict, bool, list, tuple]]): Message.
        DestroyFunc (object): The DestroyFunc in gui_sdl.py.
        DestroyFuncParams (tuple): The DestroyFunc Parameters in gui_sdl.py.
    """
    DestroyFunc(*DestroyFuncParams)
    if msg:
        msg = str(msg)
        if msg != "":
            HyperOut.printH(msg, FontEnabled=True, Font=Extensions.TextFont(font_color=Extensions.Color("red")))

    sdl2.SDL_Quit()

#Check Platform
OS:str = get_platform()
Linux:bool = False
Windows:bool = False
Darwin:bool = False
Unix:bool = False
Unknown_os:bool = True

QUIT = 256 #SDL_QUIT

if OS == "windows":
    Windows = True
    Unknown_os = False
elif OS == "linux":
    Linux = True
    Unknown_os = False
elif OS == "darwin":
    Darwin = True
    Unknown_os = False
elif OS == "unix":
    Unix = True
    Unknown_os = False
else:
    Unknown_os = True

# Constants
WM_DESTROY:int = 2
WM_PAINT:int = 15