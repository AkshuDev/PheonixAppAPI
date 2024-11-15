"""GUI Library using SDL.

NOTE: Still under development.
"""

from . import *

if __name__ == '__main__':
    exit()

import os
import sys

import ctypes

from typing import *

from sdl2 import *

from . import *

if not sys.path[PHardwareITK] == PHardwareITK_P:
    sys.path.append(PHardwareITK_P)

from phardwareitk.ErrorSystem.ErrorSystem import *
from phardwareitk.Extensions import *

class WidgetPack():
    """A type for a single PACKED Widget.
    """
    def __init__(self, Widget:PWidget, MainFunc:object, MainFuncParams:list) -> None:
        """INITALIZE func.

        Args:
            Widget (PWidget): The Widget class.
            MainFunc (function): The main function of the widget.
            MainFuncParams (list): The parameters of the main function.
        """
        self.Widget = Widget
        self.MainFunc = MainFunc
        self.MainFuncParams = MainFuncParams

def initialize() -> None:
    """Initializes the SDL and PHardware GUI.

    Raises:
        PheonixException: Incase SDL does not initialize properly.
    """
    if SDL_Init(SDL_INIT_VIDEO) != 0:
        raise PheonixException("Could not initialize SDL. - ["+str(SDL_GetError())+"]")
    
def SetBackgroundColor(window: Any, color:Color=Color("white")) -> None:
    """Sets the background color of the specified window.

    Args:
        window (Any): The window
        color (Color, optional): The color. [phardwareitk.Extensions.Color]. Defaults to Color("white").
    """
    windowSurface = SDL_GetWindowSurface(window)
    if not windowSurface:
        return None
    
    r,g,b = color.color

    sdl_color = SDL_Color(r=r, g=g, b=b, a=color.alpha)
    SDL_FillRect(windowSurface, None, SDL_MapRGBA(windowSurface.contents.format, sdl_color.r, sdl_color.g, sdl_color.b, sdl_color.a))
    SDL_UpdateWindowSurface(window)

def SetSurfaceBackgroundColor(surface:Any, color:Color=Color("white")) -> None:
    """Sets the background color of the specified surface.

    Args:
        surface (Any): The surface
        color (Color, optional): The color. [phardwareitk.Extensions.Color]. Defaults to Color("white").
    """
    if not surface:
        return None
    
    r,g,b = color.color
    
    sdl_color = SDL_Color(r=r, g=g, b=b, a=color.alpha)
    SDL_FillRect(surface, None, SDL_MapRGBA(surface.contents.format, sdl_color.r, sdl_color.g, sdl_color.b, sdl_color.a))
    
def AddIcon(window:Any, icon:PIcon) -> None:
    """Adds an icon to the window.

    Args:
        window (Any): Window.
        icon (PIcon): Icon. [phardwareitk.Extensions.PIcon]
    """
    icon.SetIconSDL2(window)
    
def WindowSurface(window:Any) -> Any:
    """Returns the SDL2 window surface.

    Args:
        window (Any): The window returned by 'CreateWindow' Function.

    Returns:
        Any: Window surface.
    """
    return SDL_GetWindowSurface(window)

def LoadBMP(image:str="") -> Any:
    """Loads the specified BMP image.

    Args:
        image (str, optional): The image path in string. Defaults to "".

    Returns:
        Any: The returned value of SDL2.'LoadBMP' Function.
    """
    return SDL_LoadBMP(ToBytes(image))

def UpdateWindow(window:Any) -> None:
    """Updates the window.

    Args:
        window (Any): The window.
    """
    SDL_UpdateWindowSurface(window)

def BlitSurfaceScaled(src:Any, srcrect:Any, dst:Any, dstrect:Any, scaleMode:Any) -> bool:
    """_summary_

    Args:
        src (Any): the SDL_Surface structure to be copied from.
        srcrect (Any): the SDL_Rect structure representing the rectangle to be copied, or NULL to copy the entire surface.
        dst (Any): the SDL_Surface structure that is the blit target.
        dstrect (Any): the SDL_Rect structure representing the target rectangle in the destination surface, or NULL to fill the entire destination surface.
        scaleMode (Any): the SDL_ScaleMode to be used.
    """
    return SDL_BlitScaled

def BlitSurface(src:Any, srcrect:Any, dst:Any, dstrect:Any) -> bool:
    """Same as SDL2.BlitSurface.

    Args:
        src (Any): the SDL_Surface structure to be copied from.
        srcrect (Any): the SDL_Rect structure representing the rectangle to be copied, or NULL to copy the entire surface.
        dst (Any): the SDL_Surface structure that is the blit target.
        dstrect (Any): the SDL_Rect structure representing the x and y position in the destination surface, or NULL for (0,0). The width and height are ignored, and are copied from srcrect. If you want a specific width and height, you should use BlitSurfaceScaled().
    """
    return SDL_BlitSurface(src, srcrect, dst, dstrect)


def FreeSurface(image:Any) -> None:
    """Frees the specified BMP image.

    Args:
        image (Any): The image returned from 'LoadBMP' function.
    """
    SDL_FreeSurface(image)
    
def CreateWindow(name:str="PHardware GUI", width:int=800, height:int=400, WindowPos:Union[None, Any]=SDL_WINDOWPOS_CENTERED) -> Any:
    """Creates a window.

    Args:
        name (str, optional): The Title of the window. Defaults to "PHardware GUI".
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

    name = ToBytes(name)

    window = SDL_CreateWindow(name, WindowPos, WindowPos, width, height, SDL_WINDOW_SHOWN)
    if not window:
        raise PheonixException("Could not create window. - ["+str(SDL_GetError())+"]")
    else:
        return window
    
def DestroyWindow(window:Any, icon:Optional[PIcon]=None, renderer:Optional[SDL_Renderer]=None) -> None:
    """Destroyes the specified window.

    Args:
        window (Any): The window.
        icon (Optional[PIcon]): If used, the icon provided in 'AddIcon' function.
        renderer (Optional[SDL_Renderer]): If used, the renderer provided in MakeRenderer, RenderText function
    """
    SDL_DestroyWindow(window)
    if icon:
        icon.Free()
    
    if renderer:
        SDL_DestroyRenderer(renderer)

def Quit() -> None:
    """Quits the Window.
    """
    SDL_Quit()
    
def EventLoop(quit_OnMessage:bool=False, window:Any=None, WidgetPacks:Optional[list[WidgetPack]]=None, icon:Optional[PIcon]=None, renderer:Optional[SDL_Renderer]=None) -> Union[bool, SDL_Event]:
    """Checks if any events are in event queue and reteives the next event.

    Args:
        quit_OnMessage (bool, optional): If set to True, will run loop (Button and such widgets will not work), upon receiving Quit event (e.g. On Window Quit) the program will destroy the window. Else False. Defaults to False
        window (Any, optional): If quit_OnMessage set to true, the provide the window
        WidgetPacks (Optional[list[WidgetPack]]): If any, the program will provide events to the widget.
        ....: Parameter to DestroyWindow.
        
    Returns:
        Union[bool, SDL_Event]: True for Quit, otherwise the event.
    """
    event = SDL_Event()

    run = True
    while run:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if WidgetPacks != None and WidgetPacks != []:
                for i, v in enumerate(WidgetPacks):
                    if not v.MainFunc:
                        continue

                    if v.MainFuncParams == None or v.MainFuncParams == []:
                        v.MainFunc(event)
                    else:
                        params = tuple(v.MainFuncParams)
                        v.MainFunc(event, *params)
                
            if event.type == SDL_QUIT:
                if quit_OnMessage:
                    if not icon and not renderer:
                        DestroyWindow(window)
                    elif icon and not renderer:
                        DestroyWindow(window, icon)
                    elif not icon and renderer:
                        DestroyWindow(window, renderer=renderer)
                    elif icon and renderer:
                        DestroyWindow(window, icon, renderer)

                    Quit()
                else:
                    return True
                run = False
                break

def MakeRenderer(window:Any, index:int=-1, flags:Any=0) -> Any:
    """Returns a renderer.

    Args:
        window (Any): The Window.
        index (int, optional): The index of the rendering device to activate. -1 for default. Defaults to -1.
        flags (Any, optional): The flags for Renderer.

    Returns:
        Any: The renderer.
    """
    return SDL_CreateRenderer(window, index, flags)

def RenderText(window:Any, widget_rect:SDL_Rect, text:str, font:TextFont=TextFont(font_color=Color("black")), fontFile:Optional[str]=None) -> Union[SDL_Renderer, bytes]:
    """Renders text.

    Args:
        window (Any): The window to render the text in.
        widget_rect (SDL_Rect): The rectangle inside which the text should be rendered. (RECT will be invisible)
        text (str): The text to be rendered.
        font (TextFont): The text font to be rendered.
        fontFile (Optional[str], optional): The Font file, if not present -> None. Defaults to None._
    """
    from sdl2 import sdlttf
    if sdlttf.TTF_Init() > 0:
        return None
    
    render_ = MakeRenderer(window)
    r,g,b = font.color.color
    SDL_SetRenderDrawColor(render_, r,g,b,font.color.alpha)
    SDL_RenderClear(render_)

    font_ = None

    if Windows and not fontFile:
        font_ = sdlttf.TTF_OpenFont(ToBytes(f"C:\\Windows\\Fonts\\{font.font}.ttf"), 64)
    elif Linux and not fontFile:
        font_ = sdlttf.TTF_OpenFont(ToBytes(f"usr/share//fonts//{font.font}.ttf"), 64)
    elif Unix and not fontFile:
        font_ = sdlttf.TTF_OpenFont(ToBytes(f"usr/share/fonts//{font.font}.ttf"), 64)
    elif Unknown_os and not fontFile:
        return b"Unknown OS"
    
    if not font_:
        return ToBytes(FromBytes(SDL_GetError()) + " !PHardware -> font == None")

    if fontFile:
        font_ = sdlttf.TTF_OpenFont(ToBytes(fontFile), 64)

    color = SDL_Color(r, g, b, font.color.alpha)
    tsurface = sdlttf.TTF_RenderText_Solid(font_, ToBytes(text), color)  

    if not tsurface: return ToBytes(FromBytes(SDL_GetError()) + " !PHardware -> Tsurface == None")

    ttexture = SDL_CreateTextureFromSurface(render_, tsurface)

    if not ttexture: return ToBytes(FromBytes(SDL_GetError()) + " !PHardware -> Ttexture == None")

    SDL_FreeSurface(tsurface)

    SDL_RenderCopy(render_, ttexture, None, widget_rect)
    SDL_RenderPresent(render_)

    SDL_DestroyTexture(ttexture)

    return render_

class Button(PWidget):
    """A Button widget

    Args:
        PWidget (PWidget): phardwareitk.Extensions.PWidget
    """

    def __init__(self, x:int, y:int, width:int, height:int, label:str="ClickMe", bg_color:Color=Color("gray"), Font:TextFont=TextFont()) -> None:
        """Initialize the Button.

        Args:
            x (int): X coordinate.
            y (int): Y coordinate.
            width (int): Width.
            height (int): Height.
            label (str, optional): Label for the button. Defaults to "Button".
            bg_color (Color, optional): Background-Color. Defaults to Color("gray").
            Font (TextFont, optional): Font for the label. Defaults to TextFont().
        """

        super().__init__(x, y, width, height, 0, bg_color, True, Font, label)

        self.callback:object = None
        self.params:tuple = None

    def Draw(self, window:Any) -> SDL_Renderer:
        """Draws the button widget.

        Args:
            window (Any): The window to draw the widget.
        """
        surface = WindowSurface(window)
        pixel_format = surface.contents.format
        r,g,b = self.bgColor.color
        mapped_color = SDL_MapRGBA(pixel_format, r, g, b, self.bgColor.alpha)

        SDL_FillRect(surface, SDL_Rect(self.x, self.y, self.width, self.height), mapped_color)

        return RenderText(window, SDL_Rect(self.x, self.y, self.width, self.height), self.text, self.textFont) if self.text else None

    def onClick(self, callback:object, params:Optional[tuple]=None) -> WidgetPack:
        """Runs the following function if Mouse is clicked upon the button.

        Args:
            callback (object): The callback function.
            params (Optional[tuple], optional): If any, parameters for the callback. Defaults to None.

        Returns:
            WidgetPack: Use it inside the EventLoop.
        """
        self.callback = callback
        self.params = params

        return WidgetPack(Button, lambda event: self._onevent(event), [])
    
    def _onevent(self, event:SDL_Event) -> None:
        """Event handler. DO NOT CALL DIRECTLY. RECOMMENDED TO CALL VIA EVENT_LOOP.
        """
        if event.type == SDL_MOUSEBUTTONDOWN:
            mx = ctypes.c_int(0)
            my = ctypes.c_int(0)
            SDL_GetMouseState(ctypes.byref(mx), ctypes.byref(my))

            mx = mx.value
            my = my.value

            if self.x <= mx <= self.x + self.width and self.y <= my <= self.y + self.height:
                if self.callback:
                    if not self.params:
                        self.callback()
                    else:
                        self.callback(*self.params)