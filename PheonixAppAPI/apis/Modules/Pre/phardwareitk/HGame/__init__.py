"""Hardware Hyper Game (HGame).

Base Functions:
    Initialize: The first function to be called before any other.

Classes:
    Screen: Classic Screen Class. Uses Tkinter. (Fast but not very fast)
    Draw: Classic Draw Class. Uses Tkinter. (Fast but not very fast)
    Screen_ADV: Advanced Screen Class. Uses PHardwareGUI (Very Fast and efficient. Recommended for Complex apps)
    Draw_ADV: Advanced Draw Class. Uses PHardwareGUI (Very Fast and efficient. Recommended for Complex apps)
    Screen_X: Expert Level Screen Class. Uses OpenGL (Provides Low level interactions and hence is the fastest. Recommended for Very complex apps and 3D apps).
    Draw_X: Expert Level Screen Class. Uses OpenGL (Provides Low level interactions and hence is the fastest. Recommended for Very complex apps and 3D apps).
"""

import tkinter
import os
import sys

PHardwareITK = len(sys.path) - 1
PHardwareITK_P = os.path.join(os.path.dirname(__file__), "..", "..")

if not sys.path[PHardwareITK] == PHardwareITK_P:
    sys.path.append(PHardwareITK_P)

import phardwareitk.LIB
from phardwareitk.CLI import cliToolKit
from phardwareitk.ErrorSystem import ErrorSystem as es

from phardwareitk.Extensions.HyperOut import *

global Debug
global Stdout
global Stdin
global OpenGl
global Gd

Debug:bool = False
Stdout:str = ""
Stdin:str = ""
Stdout_Stdin_list:list = ["console", "ext_window", "window"]

OpenGl:bool = False

Gd:str = ""

G_dictList:list = ["2d", "3d"]

def Initialize(debug_stdout:bool=False, stdout:str="console", stdin:str="window", G_2D_3D:int=0, G_dict:dict[0,str]={0: "2d", 1: "3d"}, OpenGL:bool=False) -> None:
    global Debug
    global Stdout
    global Stdin
    global Stdout_Stdin_list
    global OpenGl
    global Gd
    global G_dictList
    
    Debug = debug_stdout
    if stdout in Stdout_Stdin_list:
        Stdout = stdout
    else:
        es.PheonixArgumentError(f"Stdout must be specified or must be present in the list of stdout-compatible streams. LISTS [{Stdout_Stdin_list}]")
    if stdin in Stdout_Stdin_list:
        Stdin = stdin
    else:
        es.PheonixArgumentError(f"Stdin must be specified or must be present in the list of the stdin-compatible streams. LISTS [{Stdout_Stdin_list}]")
    
    if G_2D_3D in G_dict.keys():
        if G_dict[G_2D_3D].lower() in G_dictList:
            Gd = G_dict[G_2D_3D].lower()
        else:
            es.PheonixArgumentError(f"G_dict values must be supported. LISTS [{G_dictList}]")
    else:
        es.PheonixArgumentError(f"G_2d_3D must be specified or must be present in the G_dict. G_dict -> [{G_dict}]")

    OpenGl = OpenGL

    if Debug and Stdout == "console":
        printH(f"\n HGame Settings -> \n debug-stdout: {debug_stdout} \n stdout: {stdout} \n stdin: {stdin} \n Mode: {Gd} \n OpenGL: {OpenGl} ", FontEnabled=True, backgroundColorEnabled=True, Font=TextFont(font="Futura", font_color=Color("black"), font_background_color=Color("red")))

    return None

class Screen():
    """Screen class that controls the screen and is the first class to be used after initialization.
    NOTE: Uses [tkinter] and not [PHardware GUI] to boost performance as [tkinter] is a module developed only for this purpose wheras [PHardwareITK] is a module that provides a hardware interface toolkit and other functions.
    """
    global Debug
    global Stdout
    global Stdin
    global Stdout_Stdin_list
    global OpenGl
    global Gd
    global G_dictList

    def __init__(self, name:str="HGame", width:int=800, height:int=400, x:int=0, y:int=0, backgroundColor:Color=Color(), icon:str="") -> None:
        self.name:str = name
        self.width:int = width
        self.height:int = height
        self.x:int = x
        self.y:int = y
        self.backgroundColor:Color = backgroundColor

        self.icon:str = icon

        if Debug == True and Stdout == "console":
            printH(f"\nCreating Window:\n1.Name: {name}\n2.Width: {width}\n3.Height: {height}\n4.X: {x}\n5.Y: Y\n6.Background Color: {backgroundColor.color}\n")

        self.root:tkinter.Tk = tkinter.Tk()

        if icon:
            self.root.iconphoto(False, icon)

        self.root.title(name)
        self.root.geometry(f"{width}x{height}")

        self.grid:bool = False

    def GridMode(self) -> None:
        """Initializes the grid mode.
        """
        self.grid = True
        return None

    def Loop(self) -> None:
        """Creates the game loop.
        """
        self.root.mainloop()

class Draw:
    def __init__(self, screen:Screen) -> None:
        self.root = screen.root
        self.screen = screen