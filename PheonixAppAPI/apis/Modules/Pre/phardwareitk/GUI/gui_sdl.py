from . import *

if __name__ == '__main__':
    exit()

import os
import sys

from typing import *

from sdl2 import *

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from ErrorSystem.ErrorSystem import *

def initialize() -> None:
    """Initializes the SDL and PHardware GUI.

    Raises:
        PheonixException: Incase SDL does not initialize properly.
    """
    if SDL_Init(SDL_INIT_VIDEO) != 0:
        raise PheonixException("Could not initialize SDL. - ["+str(SDL_GetError())+"]")
    
def CreateWindow(name:bytes=b"PHardware GUI", width:int=800, height:int=400, WindowPos:Union[None, Any]=SDL_WINDOWPOS_CENTERED) -> Any:
    """Creates a window.

    Args:
        name (bytes, optional): The Title of the window (Encoded). Defaults to b"PHardware GUI".
        width (int, optional): The width of the window. Defaults to 800.
        height (int, optional): The height of the window. Defaults to 400.
        WindowPos (Union[None, Any], optional): The position of the window. Only accept SDL_WINDOWPOS_[Something]. Defaults to SDL_WINDOWPOS_CENTERED

    Raises:
        PheonixException: Incase window creation failed.

    Returns:
        Any: Window Handle
    """

    if WindowPos == None:
        WindowPos = SDL_WINDOWPOS_CENTERED

    window = SDL_CreateWindow(name, WindowPos, width, height, SDL_WINDOW_SHOWN)
    if not window:
        raise PheonixException("Could not create window. - ["+str(SDL_GetError())+"]")
    else:
        return window
    
def PollEvents() -> bool:
    """Checks if any events are in event queue and reteives the next event.

    Returns:
        bool: False (0) if no events are found, otherwise True.
    """
    event = SDL_Event()
    while True:
        if SDL_PollEvent(event) != 0:
            if event.type == SDL_QUIT:
                return False
            elif event.type == SDL_KEYDOWN:
                if event.key.keysym.sym == SDLK_ESCAPE:
                    return False
                
    return True

def Quit() -> None:
    """Quits the Window.
    """
    SDL_Quit()