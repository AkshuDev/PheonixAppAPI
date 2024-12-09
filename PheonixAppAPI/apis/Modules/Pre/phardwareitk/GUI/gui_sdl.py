"""GUI Library using SDL.

NOTE: Still under development.
"""

import sdl2.ext
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

DWMWA_USE_IMMERSIVE_DARK_MODE = "Only Windows!"
WM_SETICON = "Only Windows!"
ICON_SMALL = "Only Windows!"
ICON_BIG = "Only Windows!"

if Windows:
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    WM_SETICON = 0x0080
    ICON_SMALL = 0
    ICON_BIG = 1

PError:bool = False
title:Optional[str] = None

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

def InitializePError() -> None:
    """Initializes Pheonix/Print Error."""
    global PError
    PError = True

def DeinitializePError() -> None:
    """Deinitializes Pheonix/Print Error."""
    global PError
    PError = False

def initialize() -> None:
    """Initializes the SDL and PHardware GUI.

    Raises:
        PheonixException: Incase SDL does not initialize properly.
    """
    if SDL_Init(SDL_INIT_VIDEO) != 0:
        raise PheonixException("Could not initialize SDL. - ["+str(SDL_GetError())+"]")

def ExtensionsInit(video:bool=True, audio:bool=False, timer:bool=False, joystick:bool=False, controller:bool=False, haptic:bool=False, sensor:bool=False, events:bool=True) -> None:
    """Initializes the SDL2 Extensions.

    Args:
        video (bool, optional): Video. Defaults to True.
        audio (bool, optional): Audio. Defaults to False.
        timer (bool, optional): Timer. Defaults to False.
        joystick (bool, optional): Joystick. Defaults to False.
        controller (bool, optional): Controller. Defaults to False.
        haptic (bool, optional): Haptic. Defaults to False.
        sensor (bool, optional): Sensor. Defaults to False.
        events (bool, optional): Events. Defaults to True.
    """
    return sdl2.ext.init(video, audio, timer, joystick, controller, haptic, sensor, events)

def GetHwnd(Title:Optional[str]=None) -> Optional[Any]:
    """Returns the windows handle for the specific window with the specified title.

    Args:
        Title (Optional[str], optional): The title of the created window, If None uses the title of the latest window. Defaults to None.

    Returns:
        Optional[Any]: Windows Handle, used in Windows OS, OR None incase of error. HWND.
    """
    if Windows:
        import ctypes
        if not Title:
            return ctypes.windll.user32.FindWindowW(None, title)
        else:
            return ctypes.windll.user32.FindWindowW(None, Title)
    else:
        if PError:
            HyperOut.printH("Not Windows OS!", FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
        return None

def LoadHIcon(icon:PIcon, Title:Optional[str]=None) -> Any:
    """Loads the windows handle icon for the specific window with the specified title.

    Args:
        icon (PIcon): The icon for the HWnd. NOTE: Can use 'exe' format too, it will fetch the icon of the 'exe' file.
        Title (Optional[str], optional): The title of the created window, If None uses the title of the latest window. Defaults to None.

    Returns:
        The loaded HIcon
    """
    if not Title:
        Title = title

    if Windows:
        import ctypes

        kernel32 = ctypes.windll.kernel32

        hwnd = GetHwnd(Title)

        return kernel32.LoadImageW(None, icon.iconPath, 1, 0, 0, 0x10)
    else:
        if PError:
            HyperOut.printH("Not Windows OS!", FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
        return None

def GetNSWindow() -> None:
    """Returns the native macOS window object. Gets the latest opened window."""
    if not Darwin:
        if PError:
            HyperOut.printH("OS is not MacOS!", FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
        return None

    import importlib.util
    if not importlib.util.find_spec("AppKit"):
        if PError:
            HyperOut.printH("AppKit required for such process in MacOS!", FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
        return None
    else:
        from AppKit import NSApp # type: ignore

        return NSApp.windows()[0]

def SetBackgroundColor(window: Any, color:Color=Color("white")) -> None:
    """Sets the background color of the specified window.

    Args:
        window (Any): The window
        color (Color, optional): The color. [phardwareitk.Extensions.Color]. Defaults to Color("white").
    """
    windowSurface = SDL_GetWindowSurface(window)
    if not windowSurface:
        if PError:
            HyperOut.printH(FromBytes(SDL_GetError()) + "!PHardware -> windowSurface == None", FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
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
        if PError:
            HyperOut.printH("!PHardware -> surface == None", FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
        return None

    r,g,b = color.color

    sdl_color = SDL_Color(r=r, g=g, b=b, a=color.alpha)
    SDL_FillRect(surface, None, SDL_MapRGBA(surface.contents.format, sdl_color.r, sdl_color.g, sdl_color.b, sdl_color.a))

def AddIcon(window:Any, icon:PIcon, taskbarIncluded:bool=True, Title: Optional[str]=None) -> None:
    """Adds an icon to the window.

    Args:
        window (Any): Window.
        icon (PIcon): Icon. [phardwareitk.Extensions.PIcon]
        taskbarIncluded (bool, optional): If True, depending on Os, the taskbar window icon will change from python to the specified icon with the icon on the window. Defaults to True.
        Title (Optional[str], optional): The title of the window, If 'None' the title of the latest window will be used. Defaults to None.
    """
    icon.SetIconSDL2(window)

    if not Title:
        Title = title

    if taskbarIncluded:
        if Windows:
            import ctypes
            hwnd = GetHwnd(Title)
            hIcon = LoadHIcon(icon, Title)

            user32 = ctypes.windll.user32
            user32.SendMessageW(hwnd, WM_SETICON, ICON_SMALL, hIcon)
            user32.SendMessageW(hwnd, WM_SETICON, ICON_BIG, hIcon)

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

def CreateWindow(name:str="PHardware GUI", width:int=800, height:int=400, WindowPos:Union[None, Any]=SDL_WINDOWPOS_CENTERED, WindowType:Optional[Any]=None, x:int=0, y:int=0) -> Any:
    """Creates a window.

    Args:
        name (str, optional): The Title of the window. Defaults to "PHardware GUI".
        width (int, optional): The width of the window. Defaults to 800.
        height (int, optional): The height of the window. Defaults to 400.
        WindowPos (Union[None, Any], optional): The position of the window. Only accept SDL_WINDOWPOS_[Something]. Defaults to SDL_WINDOWPOS_CENTERED
        WindowType (Optional[Any], optional): If not NONE, The provided SDL_WINDOW_[type] will be used for the window type. Example -> SDL_WINDOW_FULLSCREEN or SDL_WINDOW_BORDERLESS. None for normal. Defaults to None
        x (int): If WindowType is not None, this will be used as the X position. Defaults to 0.
        y (int): If WindowType is not None, this will be used as the Y position. Defaults to 0.

    Raises:
        PheonixException: Incase window creation failed.

    Returns:
        Any: Window Handle
    """
    global title

    title = name

    if not WindowType:
        if WindowPos == None:
            WindowPos = SDL_WINDOWPOS_CENTERED

        name = ToBytes(name)

        window = SDL_CreateWindow(name, WindowPos, WindowPos, width, height, SDL_WINDOW_SHOWN)
        if not window:
            raise PheonixException("Could not create window. - ["+str(SDL_GetError())+"]")
        else:
            return window
    else:
        if WindowPos == None:
            WindowPos = SDL_WINDOWPOS_CENTERED

        ExtensionsInit()
        import sdl2.ext
        window = sdl2.ext.Window(name, size=(width, height), position=(x, y), flags=WindowType)
        return window

def Quit() -> None:
    """Quits the Window.
    """
    SDL_Quit()

def DestroyWindow(window:Any, icon:Optional[PIcon]=None, renderer:Optional[SDL_Renderer]=None) -> None:
    """Destroys the Window and any remaining resources.

    Args:
        window (Any): The Window.
        icon (Optional[PIcon], optional): If any, The icon used. Defaults to None.
        renderer (Optional[SDL_Renderer], optional): If any, the renderer used. Defaults to None.
    """
    if renderer:
        SDL_DestroyRenderer(renderer)
    if icon:
        icon.Free()

    return SDL_DestroyWindow(window)

def EventLoop(quit_OnMessage:bool=False, window:Any=None, WidgetPacks:Optional[list[WidgetPack]]=None, icon:Optional[PIcon]=None, renderer:Optional[SDL_Renderer]=None, SafeExitOnError:bool=True) -> Union[bool, SDL_Event]:
    """Checks if any events are in event queue and reteives the next event.

    Args:
        quit_OnMessage (bool, optional): If set to True, will run loop (Button and such widgets will not work), upon receiving Quit event (e.g. On Window Quit) the program will destroy the window. Else False. Defaults to False
        window (Any, optional): If quit_OnMessage set to true, the provide the window
        WidgetPacks (Optional[list[WidgetPack]]): If any, the program will provide events to the widget.
        ....: Parameter to DestroyWindow.

    Returns:
        Union[bool, SDL_Event]: True for Quit, otherwise the event.
    """
    try:
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
    except Exception as e:
        if SafeExitOnError:
            SafeExitSDL(f"Safe Exit Acitvated! Error -> {e}")
        else:
            raise Exception(e)

def MakeRenderer(window:Any, index:int=-1, flags:Union[0, Any]=SDL_RENDERER_ACCELERATED) -> Any:
    """Returns a renderer.

    Args:
        window (Any): The Window.
        index (int, optional): The index of the rendering device to activate. -1 for default. Defaults to -1.
        flags (Any, optional): The flags for Renderer.

    Returns:
        Any: The renderer.
    """
    return SDL_CreateRenderer(window, index, flags)

def RenderText(renderer:SDL_Renderer, widget_rect:SDL_Rect, text:str, font:TextFont=TextFont(font_color=Color("black")), fontFile:Optional[str]=None) -> Union[SDL_Renderer, bytes]:
    """Renders text.

    Args:
        renderer (SDL_Renderer): The renderer to use.
        widget_rect (SDL_Rect): The rectangle inside which the text should be rendered. (RECT will be invisible)
        text (str): The text to be rendered.
        font (TextFont): The text font to be rendered.
        fontFile (Optional[str], optional): The Font file, if not present -> None. Defaults to None._
    """
    from sdl2 import sdlttf

    # Initialize SDL_ttf if not already done
    if not sdlttf.TTF_WasInit():
        sdlttf.TTF_Init()

    render_ = renderer
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
        if PError:
            HyperOut.printH("Unknown OS!", FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
        else:
            return b"Unknown OS"

        return None

    if not font_:
        if PError:
            HyperOut.printH(FromBytes(SDL_GetError()) + "!PHardware -> font == None", FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
        else:
            return ToBytes(FromBytes(SDL_GetError()) + " !PHardware -> font == None")

        return None

    if fontFile:
        font_ = sdlttf.TTF_OpenFont(ToBytes(fontFile), 64)

    color = SDL_Color(r, g, b, font.color.alpha)
    tsurface = sdlttf.TTF_RenderText_Solid(font_, ToBytes(text), color)

    if not tsurface:
        if PError:
            HyperOut.printH(FromBytes(SDL_GetError()) + "!PHardware -> Tsurface == None", FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
        else:
            return ToBytes(FromBytes(SDL_GetError()) + " !PHardware -> Tsurface == None")

        return None

    # Convert to correct surface format
    OptimTsurface = SDL_ConvertSurfaceFormat(tsurface, SDL_PIXELFORMAT_ARGB8888, 0)
    if not OptimTsurface:
        if PError:
            HyperOut.printH(FromBytes(SDL_GetError()) + "!PHardware -> OptimTsurface == None", FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
        else:
            return ToBytes(FromBytes(SDL_GetError()) + " !PHardware -> OptimTsurface == None")

        return None

    ttexture = SDL_CreateTextureFromSurface(render_, tsurface)

    if not ttexture:
        if PError:
            HyperOut.printH(FromBytes(SDL_GetError()) + "!PHardware -> Ttexture == None", FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
        else:
            return ToBytes(FromBytes(SDL_GetError()) + " !PHardware -> Ttexture == None")

        return None

    SDL_FreeSurface(tsurface)
    SDL_FreeSurface(OptimTsurface)

    SDL_RenderCopy(render_, ttexture, None, widget_rect)
    SDL_RenderPresent(render_)

    SDL_DestroyTexture(ttexture)

    return render_

def Delay(time:int) -> None:
    """Creates a delay of specified seconds, in that time, all the processes will be paused. Since, it is a window, normal time.sleep doesn't work.

    Args:
        time (int): The time to delay in seconds.
    """
    time = time * 1000
    SDL_Delay(time)
    return None

def TitleBarWindows(Title:Optional[str]=None, mode:Optional[str]=None, color:Color=Color("white")) -> None:
    """Modifies the orignal titleBar, to the specified color or mode. WINDOWS SPECIFIC

    Args:
        Title (Optional[str]): the title of the window, that needs to be modified, If 'None', uses the title of the main window. Defaults to None
        mode (Optional[str], optional): The mode to use. Available -> dark, light, None (Default). Defaults to None.
        color (Color, optional): The color of the titleBar, used incase 'mode' is set to None. Defaults to Color("black").
    """
    if not Title:
        Title = title

    if Windows:
        import ctypes

        HWnd = GetHwnd(Title)

        if not mode or mode == "":
            # Define COLORREF
            r, g, b = color.color
            colorref = (r | (g << 8) | (b << 16))

            ctypes.windll.dwmapi.DwmSetWindowAttribute(HWnd, 20, ctypes.byref(ctypes.c_int(colorref)), ctypes.sizeof(ctypes.c_int)) # Set Window Attrib
        else:
            mode = mode.lower()

            if mode == "dark":
                value = ctypes.c_int(1)
            else:
                value = ctypes.c_int(0)

            ctypes.windll.dwmapi.DwmSetWindowAttribute(HWnd, DWMWA_USE_IMMERSIVE_DARK_MODE, ctypes.byref(value), ctypes.sizeof(value)) # Set Window Attrib
    else:
        if PError:
            HyperOut.printH("Not Windows OS!", FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
        return None

def TitleBarMacOS(mode:Optional[str]=None) -> None:
    """Modifies the orignal titleBar, to the specified color or mode. MACOS SPECIFIC. DOESN't SUPPORT COLOR!

    Args:
        mode (Optional[str], optional): The mode to use. Available -> dark, light, None (Default). Defaults to None.
    """
    import importlib.util

    if not Darwin:
        if PError:
            HyperOut.printH("OS is not MacOS!", FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
        return None

    if not importlib.util.find_spec("AppKit"):
        if PError:
            HyperOut.printH("AppKit required for such process in MacOS!", FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
        return None
    else:
        from AppKit import NSApplication, NSApp, NSWindow, NSAppearance, NSAppearanceNameAqua, NSAppearanceNameDarkAqua # type: ignore
        nsWindow = GetNSWindow()

        if mode:
            appearence = NSAppearance.appearanceNamed_(NSAppearanceNameDarkAqua if mode.lower == "dark" else NSAppearanceNameAqua)
            nsWindow.setAppearance(appearence)
            nsWindow.display()
            return None

class TitleBar(PWidget):
    """A title bar class. Allows you to create custom title bars. To use this keep window creation to SDL_Window_BORDERLESS.

    NOTE: Still Under development, hence some bugs might occur.

    NOTE: The main action buttons do not work! please use with care! (Under Development)"""
    def __init__(self, window:Any, width:Optional[int]=None, height:int=50, title:str="PHardwareITK", bgcolor:Color=Color("black")) -> None:
        """Init func of TitleBar Class.

        NOTE: Still Under development, hence some bugs might occur.

        NOTE: The main action buttons do not work! please use with care! (Under Development)

        Args:
            window (Any): The window to draw the titleBar on.
            width (Optional[int], optional): The width of the title bar, None for using Window Size Width. Defaults to None.
            height (int, optional): The height of the title bar. Defaults to 50.
            title (str, optional): The title text. Defaults to "PHardwareITK".
            bgcolor (Color, optional): The background color of the title bar. Defaults to Color("black").
        """
        self.height = height
        self.width = width

        if not width:
            self.width = SDL_GetWindowSize(window)[0]

        self.window = window
        self.colors = {"bg": bgcolor}
        self.text = {"title": {"text": title, "font": TextFont(font_size=16, font_color=Color("white")), "x": "default", "y": "default", "enabled": True}}
        self.icons = {"close": PIcon(None, width - 30, 10, 20, 20), "minimize": PIcon(None, width - 90, 10, 20, 20), "maximize": PIcon(None, width - 60, 10, 20, 20)}
        self.interactivity = {"draggable": True}
        self.size = [SDL_GetWindowSize(window)[0], height]
        self.position = {"x": 0, "y": 0}
        self.iconSurfaces = {}
        self.iconTextures = {}

    def SetBackgroundColor(self, color:Color) -> None:
        """Changes the orignal background color of the title bar.

        Args:
            color (Color): The color.
        """
        self.colors["bg"] = color

    def DisableTitle(self) -> None:
        """Disables the title from the title bar"""
        self.text["title"]["enabled"] = False

    def SetTitle(self, title:str="PHardwareITK", font:TextFont=TextFont(font_size=16)) -> None:
        """Changes the orignal title of the title bar.

        Args:
            title (str, optional): The title. Defaults to "PHardwareITK".
            font (TextFont, optional): The font of the title. Defaults to TextFont(font_size=16).
        """
        self.text["title"]["text"] = title
        self.text["title"]["font"] = title

    def AddText(self, name:str, text:str, font:TextFont=TextFont(font_size=16), x:int=0, y:int=0, enabled:bool=True) -> None:
        """Adds a new text to the title bar at the specified locations.

        Args:
            name (str): The name of the object. (should be Unique and not previously used)
            text (str): The text of the object.
            font (TextFont, optional): The font of the object. Defaults to TextFont(font_size=16).
            x (int, optional): The X coordinate (in the titlebar). Defaults to 0.
            y (int, optional): The X coordinate (in the titlebar)The X coordinate (in the titlebar). Defaults to 0.
            enabled (bool, optional): Wether to enable it or not for the time being. Defaults to True.
        """
        try:
            self.text[name] = {"text": text, "font": font, "x": x, "y": y, "enabled": enabled}
        except Exception as e:
            if PError:
                HyperOut.printH("TitleBar.AddText -> " + e, FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
            return None

    def ModifyTitle(self, text:Optional[str]=None, font:Optional[TextFont]=None, x:Optional[int]=None, y:Optional[int]=None, enabled:Optional[bool]=None) -> None:
        """Modifies the Title of the title bar.

        Set parameter to 'None' to define no change.

        Args:
            text (Optional[str], optional): Text. Defaults to None.
            font (Optional[TextFont], optional): Font. Defaults to None.
            x (Optional[int], optional): X coordinate. (of the titlebar). Defaults to None.
            y (Optional[int], optional): Y coordinate. (of the titlebar). Defaults to None.
            enabled (Optional[bool], optional): Wether it is enabled or not. Defaults to None.
        """

        list_ = [text, "text", font, "font", x, "x", y, "y", enabled, "enabled"]

        skip = False
        for i, param in enumerate(list_):
            if param and not skip:
                try:
                    self.text["title"][list_[i + 1]] = param
                    skip = True
                except Exception as e:
                    if PError:
                        HyperOut.printH("TitleBar.ModifyTitle -> " + e, FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
                    return None
            if skip:
                skip = False

    def ModifyText(self, name:str, text:Optional[str]=None, font:Optional[TextFont]=None, x:Optional[int]=None, y:Optional[int]=None, enabled:Optional[bool]=None) -> None:
        """Modifies the specified Text object of the title bar.

        Set parameter to 'None' to define no change.

        Args:
            name (str): The name of the object.
            text (Optional[str], optional): Text. Defaults to None.
            font (Optional[TextFont], optional): Font. Defaults to None.
            x (Optional[int], optional): X coordinate. (of the titlebar). Defaults to None.
            y (Optional[int], optional): Y coordinate. (of the titlebar). Defaults to None.
            enabled (Optional[bool], optional): Wether it is enabled or not. Defaults to None.
        """

        list_ = [text, "text", font, "font", x, "x", y, "y", enabled, "enabled"]

        skip = False
        for i, param in enumerate(list_):
            if param and not skip:
                try:
                    self.text[name][list_[i + 1]] = param
                    skip = True
                except Exception as e:
                    if PError:
                        HyperOut.printH("TitleBar.ModifyText -> " + e, FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
                    return None
            if skip:
                skip = False

    def EnableText(self, name:str) -> None:
        """Enables the specified text object in the title bar.

        Args:
            name (str): The name of the object.
        """
        return self.ModifyText(name, enabled=True)

    def EnableTitle(self) -> None:
        """Enables the title in the title bar.
        """
        return self.ModifyTitle(enabled=True)

    def SetIcon(self, name:str, icon:PIcon) -> None:
        """Adds a new icon to the title bar at the specified x, y coordinates.

        Args:
            name (str): The name of the icon object. (Should be Unique and not previously used)
            icon (PIcon): The icon itself.
        """
        try:
            self.icons[name] = icon
        except Exception as e:
            if PError:
                HyperOut.printH("TitleBar.SetIcon -> " + e, FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
            return None

    def RemoveIcon(self, name:str) -> None:
        """Removes the specified icon from the title bar.

        Args:
            name (str): The name of the icon to remove.
        """
        try:
            del self.icons[name]
        except Exception as e:
            if PError:
                HyperOut.printH("TitleBar.RemoveIcon -> " + e, FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
            return None

    def ModifyInteractivityOptions(self, draggable:Optional[bool]=None, close_action:Optional[bool]=None, on_click:Optional[bool]=None) -> None:
        """Modifies the pre-made options for the titlebar.

        NOTE: Use 'None' to define no change.

        NOTE: Be Careful while using this, incase you set close_action to 'False', try to use some kind of program like task manager to kill the python process.

        Args:
            draggable (Optional[bool], optional): Is it draggable. Defaults to None.
            close_action (Optional[bool], optional): Can it be closed. Defaults to None.
            on_click (Optional[bool], optional): Is it clickable. Defaults to None.
        """

        list_ = [draggable, "draggable", close_action, "close_action", on_click, "on_click"]

        skip = False
        for i, v in enumerate(list_):
            if v and not skip:
                try:
                    self.interactivity[list_[i + 1]] = v
                    skip = True
                except Exception as e:
                    if PError:
                        HyperOut.printH("TitleBar.ModifyInteractivityOptions -> " + e, FontEnabled=True, Flush=True, TextFont=TextFont(font_color=Color("red")))
                    return None
            if skip:
                skip = False

    def LoadIcons(self, renderer:SDL_Renderer):
        """Loads the icons for drawing."""
        if len(self.icons) <= 0:
            return None

        for key, v in self.icons.items():
            if v.iconPath:
                self.iconSurfaces[key] = v.LoadImageSDL2()
                if self.iconSurfaces[key]:
                    self.iconTextures[key] = SDL_CreateTextureFromSurface(renderer, self.iconSurfaces[key])

    def Draw(self, renderer:SDL_Renderer) -> WidgetPack:
        """Draws the title bar based on the information.

        Args:
            renderer (SDL_Renderer): The renderer to use.

        Returns:
            WidgetPack: Pass it as a list into the EventLoop."""
        bgColor = self.colors["bg"]
        SDL_SetRenderDrawColor(renderer, *bgColor.color, bgColor.alpha)
        SDL_RenderFillRect(renderer, SDL_Rect(0, SDL_GetWindowSize(self.window)[1], self.size["width"], self.size["height"]))

        # Draw Title if any
        if "title" in self.text.keys():
            if self.text["title"]["enabled"]:
                titleSurf = None
                if self.text["title"]["x"] and self.text["title"]["y"] == "default":
                    titleSurf = RenderText(renderer, SDL_Rect(self.size["width"] // 2 - 50, SDL_GetWindowSize(self.window)[1] + (self.height // 2), len(self.text["title"]["text"]) * 2, 50), self.text["title"]["text"], self.text["title"]["font"])
                elif self.text["title"]["x"].isdigit() and self.text["title"]["y"].isdigit():
                    titleSurf = RenderText(renderer, SDL_Rect(self.text["title"]["x"], self.text["title"]["y"], len(self.text["title"]["text"]) * 2, 50), self.text["title"]["text"], self.text["title"]["font"])
                if isinstance(titleSurf, bytes):
                    return None

        for key, val in self.text.items():
            if key and val:
                if isinstance(val, dict):
                    keySurf = RenderText(renderer, SDL_Rect(self.text[key]["x"], self.text[key]["y"], len(self.text[key]["text"]) * 2, 50), self.text[key]["text"], self.text[key]["font"])
                    if isinstance(keySurf, bytes): return None

        # Draw icons
        if len(self.icons) > 0:
            for iconName, icon in self.icons.items():
                if icon:
                    if icon.iconPath:
                        SDL_RenderCopy(renderer, self.iconTextures[iconName], None, SDL_Rect(icon.x, icon.y, icon.width, icon.height))

        SDL_RenderPresent(renderer)

        return WidgetPack(TitleBar, lambda event: self._onevent(event), [])

    def _onevent(self, event:SDL_Event) -> None:
        """Do not call directly, Recommended to call via EVENT LOOP!"""

        # Interactivity stuff
        if "draggable" in self.interactivity.keys():
            self._handle_drag()

    def _handle_drag(self) -> None:
        """Private func do not use!"""
        if not hasattr(self, "_drag_state"):
            # Init drag state
            self._drag_state = {"dragging": False, "off_x": 0, "off_y": 0}

        mouse_event = self._get_mouse_event()

        if mouse_event["LEFTbutton_down"]:
            mouseX, mouseY = mouse_event["pos"]
            if 0 <= mouseX <= self.size["width"] and 0 <= mouseY <= self.size["height"]:
                self._drag_state["dragging"] = True
                self._drag_state["off_x"] = mouseX
                self._drag_state["off_y"] = mouseY

        elif mouse_event["LEFTbutton_up"]:
            # Stop Dragging
            self._drag_state["dragging"] = False

        elif self._drag_state["dragging"]:
            # Update position while dragging
            new_mouse_x, new_mouse_y = mouse_event["pos"]
            delta_x = new_mouse_x - self._drag_state["off_x"]
            delta_y = new_mouse_y - self._drag_state["off_y"]

            # Adjust title bar position
            self.position["x"] += delta_x
            self.position["y"] += delta_y

            # Update the drag offset
            self._drag_state["off_x"] = new_mouse_x
            self._drag_state["off_y"] = new_mouse_y

            # Move the window as well
            SDL_SetWindowPosition(self.window, self.position["x"], self.position["y"])

    def _get_mouse_event(self) -> dict[str, Union[bool, tuple[int, int]]]:
        """Private func do not use!"""
        mouse_state = SDL_GetMouseState()
        button_down = mouse_state & SDL_BUTTON(SDL_BUTTON_LEFT)
        button_up = not button_down
        mouseX, mouseY = SDL_GetMouseState(None, None)

        return {
            "LEFTbutton_down": bool(button_down),
            "LEFTbutton_up": bool(button_up),
            "pos": (mouseX, mouseY)
        }

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

class Label(PWidget):
    """Creates a label.
    """
    def __init__(self, label:str, x:int=0, y:int=0, width:int=5, height:int=5, font:TextFont=TextFont()) -> None:
        """INIT Function for Label class.

        Args:
            label (str): The Text.
            x (int, optional): The X coordinate. Defaults to 0.
            y (int, optional): The Y coordinate. Defaults to 0.
            width (int, optional): The width of the label. Defaults to 5.
            height (int, optional): The height of the label. Defaults to 5.
            font (TextFont, optional): The font of the label. Defaults to TextFont().
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.label = label

    def Draw(self, window:Any) -> SDL_Renderer:
        """Draws the label on the screen.

        Args:
            window (Any): The window to draw on.

        Returns:
            SDL_Renderer: The renderer object. Should be passed onto the list of renderers in DestroyWindow function.
        """
        surface = WindowSurface(window)
        pixel_format = surface.contents.format
        r,g,b = self.font.background_color
        mapped_color = SDL_MapRGBA(pixel_format, r, g, b, self.font.background_color.alpha)

        SDL_FillRect(surface, SDL_Rect(self.x, self.y, self.width, self.height), mapped_color)

        return RenderText(window, SDL_Rect(self.x, self.y, self.width, self.height), self.label, self.font) if self.label else None

class Quadrilateral(PWidget):
    """Creates a Quadrilateral."""
    def __init__(self, width:int=5, height:int=8, x:int=0, y:int=0, color:Color=Color("white")) -> None:
        """INIT function of Quadrilateral class.

        Args:
            width (int, optional): The width of the quadrilateral. Defaults to 5.
            height (int, optional): The height of the quadrilateral. Defaults to 8.
            x (int, optional): The X coordinate. Defaults to 0.
            y (int, optional): The Y coordinate. Defaults to 0.
            color (Color, optional): The color of the quadrilateral. Defaults to Color("white").
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color

    def Draw(self, window:Any) -> None:
        """Draws the quadrilateral.

        Args:
            window (Any): The window to draw the quadrilateral.
        """
        surface = WindowSurface(window)
        pixelFormat = surface.contents.format
        r,g,b = self.color.color
        mappedColor = SDL_MapRGBA(pixelFormat, r, g, b, self.color.alpha)

        SDL_FillRect(surface, SDL_Rect(self.x, self.y, self.width, self.height), mappedColor)
        return None

class Shape(PWidget):
    """Creates a shape."""
    def __init__(self, vertex:tuple, x:int=0, y:int=0, wireframe:bool=False, bgcolor:Color=Color("white"), color:Color=Color("white")) -> None:
        """INIT function of Shape Class.

        Args:
            vertex (tuple): The vertexes of the shape.
            x (int, optional): X coordinate. ADDS TO VERTEX POS, FOR ACCURATE VERTEX POS KEEP 0. Defaults to 0.
            y (int, optional): Y coordinate. ADDS TO VERTEX POS, FOR ACCURATE VERTEX POS KEEP 0. Defaults to 0.
            wireframe (bool, optional): If True, the shape will be a wireframe shape. Defaults to False.
            bgcolor (Color, optional): The background color of the shape. Defaults to Color("white").
            color (Color, optional): The color of the lines. Defaults to Color("white").
        """
        self.vertex = vertex
        self.x = x
        self.y = y
        self.wireframe = wireframe
        self.bgcolor = bgcolor
        self.color = color

    def Draw(self, renderer:SDL_Renderer) -> SDL_Renderer:
        """Draws the Shape.

        Args:
            renderer (SDL_Renderer): The renderer to use.

        Returns:
            SDL_Renderer: The renderer of the shape.
        """
        r, g, b = self.color.color

        SDL_SetRenderDrawColor(renderer, r, g, b, self.color.alpha)

        if self.wireframe:
            numPoints = len(self.vertex)

            for i in range(1, numPoints):
                x1, y1 = self.vertex[i]
                x2, y2 = self.vertex[(i + 1) % numPoints] # Wrap around to the first point
                SDL_RenderDrawLine(renderer, x1 + self.x, y1 + self.y, x2 + self.x, y2 + self.y)
        else:
            # Filled shape rendering
            r, g, b = self.bgcolor.color
            vertex_list = []

            for v in range(0, len(self.vertex) - 1):
                vx, vy = self.vertex[v]
                vertex_list.append(
                    SDL_Vertex(
                        position=sdl2.SDL_FPoint(vx + self.x, vy + self.y),
                        color=sdl2.SDL_Color(r, g, b, self.bgcolor.alpha),
                        tex_coord=sdl2.SDL_FPoint(0, 0)  # No texture coordinates for solid colors
                    )
                )

            # Convert to SDL_Vertex array
            vert_array = (SDL_Vertex * len(vertex_list))(*vertex_list)
            SDL_RenderGeometry(renderer, None, vert_array, len(vertex_list), None, 0)

        # Present the renderer (required to display the drawing)
        SDL_RenderPresent(renderer)
        return renderer

class AdvQuadrilateral(PWidget):
    """Creates a Advanced Quadrilateral."""
    def __init__(self, p1:int, p1w:int, p2:int, p2w:int, p3:int, p3w:int, p4:int, p4w:int, x:int=0, y:int=0, wireframe:bool=False, bgcolor:Color=Color("white"), color:Color=Color("white")) -> None:
        """INIT function of AdvQuadrilateral Class.

        Args:
            p1 (int): Vertex X.
            p1w (int): Vertex Y.
            ....... Continued
            x (int, optional): X coordinate. ADDS TO VERTEX POS, FOR ACCURATE VERTEX POS KEEP 0. Defaults to 0.
            y (int, optional): Y coordinate. ADDS TO VERTEX POS, FOR ACCURATE VERTEX POS KEEP 0. Defaults to 0.
            wireframe (bool, optional): Whether to make the shape wireframe. Defaults to False.
            bgcolor (Color, optional): The background color of the shape. Defaults to Color("white").
            color (Color, optional): The color. Defaults to Color("white").
        """
        self.p1 = p1
        self.p1w = p1w
        self.p2 = p2
        self.p2w = p2w
        self.p3 = p3
        self.p3w = p3w
        self.p4 = p4
        self.p4w = p4w
        self.x = x
        self.y =y
        self.wireframe = wireframe
        self.bgcolor = bgcolor
        self.color = color

    def Draw(self, renderer:SDL_Renderer) -> SDL_Renderer:
        """Draws the shape

        Args:
            renderer (SDL_Renderer): The renderer to draw using.

        Returns:
            SDL_Renderer: The renderer of the shape.
        """
        return Shape(((self.p1, self.p1w), (self.p2, self.p2w), (self.p3, self.p3w), (self.p4, self.p4w)), self.x, self.y, self.wireframe, self.bgcolor, self.color).Draw(renderer)

