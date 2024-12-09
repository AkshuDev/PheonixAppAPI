from . import *
from typing import *
import sys
import os

if not sys.path[PHardwareITK] == PHardwareITK_P:
    sys.path.append(PHardwareITK_P)

def printH(*values:object, seperator:Union[str, None]=" ", endl:Union[str, None]="\n", File:Union[str, None]=None, Flush:bool=False, backgroundColorEnabled:bool=False, FontEnabled:bool=False, Font:TextFont=TextFont()) -> None:
    """A Hyper version of Python's print function.

    Args:
        seperator (Union[str, None], optional): Seperator between values in [*values]. Defaults to " ".
        endl (Union[str, None], optional): The ending string to include at the end of the values. None is don't want. Defaults to "\n".
        File (Union[str, None], optional): Wether to save the print contents in a file before printing in console. Defaults to None.
        Flush (bool, optional): Wether to use Flush during printing. Defaults to False.
        backgroundColorEnabled (bool, optional): Wether to enable background-color. Defaults to False.
        FontEnabled (bool, optional): Wether to enable custom font. Defaults to False.
        Font (TextFont, optional): The font. Defaults to TextFont().

    NOTE: The font-size is not universally supported in all Terminals. Terminals like -> Xterm, ITerm2 (MacOS), etc do support it, but please check.
    """
    seperator = str(seperator)

    if not endl:
        endl = ""

    endl = str(endl)
    
    if not File:
        if not FontEnabled:
            i = 0
            for value in values:
                if i == 0:
                    print(str(value), end="", flush=Flush)
                else:
                    if seperator:
                        print(seperator+str(value), end="", flush=Flush)
                    else:
                        print(str(value), end="", flush=Flush)

            if endl:
                print(endl, end="", flush=Flush)
        else:
            font_code = Font.to_font_code()
            color_code = Font.color.to_rgb_code()
            backgroundColor_code = Font.background_color.to_background_code()
            resetCode = Font.to_reset_code()

            FontSize_Code = Font.to_font_size_code()

            final_str:str = ""

            if backgroundColorEnabled:
                final_str += backgroundColor_code
            if color_code:
                final_str += color_code
            if font_code:
                final_str += font_code
            if FontSize_Code:
                final_str += FontSize_Code

            i = 0
            for value in values:
                if i == 0:
                    final_str += str(value)
                else:
                    if seperator:
                        final_str += seperator + str(value)
                    else:
                        final_str += str(value)
                i += 1
            
            final_str += resetCode
            if endl:
                final_str += endl
            print(final_str, end="", flush=Flush)
    else:
        value = ""
        i = 0
        for val in values:
            if i == 0:
                value += str(val)
            else:
                value += seperator + str(val)

        if endl:
            value += endl

        with open(File, 'w') as f:
            f.write(value)
            f.close()
        
        if not FontEnabled:
            final_ = ""
            i = 0
            for value in values:
                if i == 0:
                    final_ = str(value)
                else:
                    if seperator:
                        final_ += seperator+str(value)
                    else:
                        final += str(value)

            if endl:
                final_ += endl

            print(final_, end="", flush=Flush, file=File)
        else:
            font_code = Font.to_font_code()
            color_code = Font.color.to_rgb_code()
            backgroundColor_code = Font.background_color.to_background_code()
            resetCode = Font.to_reset_code()
            FontSize_Code = Font.to_font_size_code()

            final_str:str = ""

            if backgroundColorEnabled:
                final_str += backgroundColor_code
            if color_code:
                final_str += color_code
            if font_code:
                final_str += font_code
            if FontSize_Code:
                final_str += FontSize_Code

            i = 0
            for value in values:
                if i == 0:
                    final_str += str(value)
                else:
                    if seperator:
                        final_str += seperator + str(value)
                    else:
                        final_str += str(value)
                i += 1
            
            final_str += resetCode
            if endl:
                final_str += endl
            print(final_str, end="", flush=Flush, file=File)
    
    sys.stdout.flush()

def exitH(ExitCode:Optional[int], *ExitMsg:Optional[object], seperator:Optional[str]=" ", endl:Optional[str]="\n", File:Optional[str]=None, Flush:bool=False, backgroundColorEnabled:bool=False, FontEnabled:bool=False, Font:TextFont=TextFont()) -> None:
    """A hyper version of Python's exit function.

    Args:
        ExitCode (Optional[int]): The ExitCode.
        seperator (Union[str, None], optional): Seperator between values in [*ExitMsg]. Defaults to " ".
        endl (Union[str, None], optional): The ending string to include at the end of the ExitMsg. None is don't want. Defaults to "\n".
        File (Union[str, None], optional): Wether to save the print contents in a file before printing in console. Defaults to None.
        Flush (bool, optional): Wether to use Flush during printing. Defaults to False.
        backgroundColorEnabled (bool, optional): Wether to enable background-color. Defaults to False.
        FontEnabled (bool, optional): Wether to enable custom font. Defaults to False.
        Font (TextFont, optional): The font. Defaults to TextFont().
    """
    if ExitMsg:
        printH("Status: Exit. Exit Code -> ["+str(ExitCode)+"]; Message: ", *ExitMsg, seperator=seperator, endl=endl, File=File, Flush=Flush, backgroundColorEnabled=backgroundColorEnabled, FontEnabled=FontEnabled, Font=Font)

    exit(ExitCode)

def evalH(source:Union[str, Any], globals:Optional[dict[str, Any]]=None, locals:Optional[Mapping[str, object]]=None, Log:bool=False) -> Any:
    """A Hyper version of Python's eval.

    Enhancements:
        Security: Restrics specific functions that can cause harm to OS/Files/etc. ONLY FOR STRING LITERALS.
        Log: Logging functionality.

    Args:
        source (Union[str, Any]): The source string/ReadableBuffer/CodeType object.
        globals (Optional[dict[str, Any]], optional): The globals in eval. Defaults to None.
        locals (Optional[Mapping[str, object]], optional): The locals in eval. Defaults to None.
        Log (bool, optional): Log evaluate. Defaults to False.

    Returns:
        Any: Compiled expr.
    """
    if isinstance(source, str): # Only for string literals.
        if "os." in source or "sys." in source:
            return "Cannot compile expressions with OS/Sys modules as they can/cannot harm the computer and can be used to get system info."

    if Log:
        print("Globals:", globals, "\nLocals:", locals, "\nSource:", source, "\nRunning, Eval...")

    out = eval(source, globals, locals)

    if Log:
        print("Output:", out)
    
    return out

def progressH(update:bool=False, basePos:tuple[Union[str, int]]=(0, "CPos+1"), cvalue:int=0, maxValue:int=100, useP:str="#", useNP:str="-", Pcolor:Color=Color("green"), msgColor:Color=Color("white"), NPcolor:Color=Color("red"), onMaxMsg:Optional[str]=None, defMsg:Optional[str]=None, First:bool=True, HideCursor:bool=True) -> Union[str, None]:
    """Progress Indicator Hyper.

    Args:
        update (bool, optional): Wether to update a single value, give the value to update in cvalue. Defaults to False.
        basePos (tuple[Union[str, int]], optional): The base position for the progressbar. (x, y). Use CPos to define Current Pos and you can add +/- after it to define the lines/chars. Defaults to (0, "CPos+1").
        cvalue (int, optional): The current value. Defaults to 0.
        maxValue (int, optional): The max value. Defaults to 100.
        useP (str, optional): The character to use for the parts which is already progressed. Defaults to "#".
        useNP (str, optional): The character to use for the parts which are not progressed. Defaults to "-".
        Ncolor (Color, optional): The color of the Progressed Section of the Bar. Defaults to Color("green").
        NPcolor (Color, optional): The color of the Unprogressed Section of the Bar. Defaults to Color("red").
        MsgColor (Color, optional): The color of the message. Defaults to Color("white").
        onMaxMsg (Optional[str], optional): The message to include if fully progressed. NOTE: Include ' ' before the message. Defaults to None.
        defMsg (Optional[str], optional): The default message to include after the progress Bar. Defaults to None.
        First (bool, optional): If first time called, then set to True, otherwise set to False. Defaults to True.
        HideCursor (bool, optional): If True, the cursor is hidden. Defaults to True.

    Returns:
        Union[str, None]: Str if an error occurred, otherwise None. STR 'MAX' is returned if current Value == max Value.
    """
    if cvalue > maxValue:
        return "CValue can't be greater than maxValue."
    
    x = basePos[0]
    y = basePos[1]
        
    progressBar:str = ""

    if cvalue == 0:
        progressBar = useNP * maxValue
    else:
        progressBar = useP * cvalue
        progressBar += useNP * (maxValue - cvalue)
    
    if defMsg and defMsg != "":
        progressBar += defMsg
    
    #Init cursor Pos

    from phardwareitk.CLI import cliToolKit

    if First:
        if isinstance(x, int) and isinstance(y, int):
            cliToolKit.Cursor.MoveCursor(x, y)
        elif isinstance(x, int) and not isinstance(y, int):
            cliToolKit.Cursor.MoveCursorX(x)
            if "cpos" in y.lower():
                if "+" in y.lower():
                    cliToolKit.Cursor.MoveCursorUp(y.split("+")[1])
                elif "-" in y.lower():
                    cliToolKit.Cursor.MoveCursorDown(y.split("-")[1])
        elif not isinstance(x, int) and isinstance(y, int):
            cliToolKit.Cursor.MoveCursor(0, y)
            if "cpos" in x.lower():
                if "+" in x.lower():
                    cliToolKit.Cursor.MoveCursorRight(x.split("+")[1])
                elif "-" in x.lower():
                    cliToolKit.Cursor.MoveCursorLeft(x.split("-")[1])
        else:
            if "cpos" in y.lower():
                if "+" in y.lower():
                    cliToolKit.Cursor.MoveCursorUp(y.split("+")[1])
                elif "-" in y.lower():
                    cliToolKit.Cursor.MoveCursorDown(y.split("-")[1])

            if "cpos" in x.lower():
                if "+" in x.lower():
                    cliToolKit.Cursor.MoveCursorRight(x.split("+")[1])
                elif "-" in x.lower():
                    cliToolKit.Cursor.MoveCursorLeft(x.split("-")[1])

    if HideCursor:
        cliToolKit.Cursor.HideCursor()

    if update:
        cliToolKit.Cursor.MoveCursorRight(cvalue - 1)
        printH(useNP, FontEnabled=True, endl="", Font=TextFont(font_color=NPcolor))
        return None
    
    for char in progressBar:
        color = None
        if char == useNP:
            color = NPcolor
        else:
            color = Pcolor
        printH(char, FontEnabled=True, endl="", Font=TextFont(font_color=color))

    if cvalue == maxValue:
        if onMaxMsg and onMaxMsg != "":
            printH(onMaxMsg, FontEnabled=True, endl="", Font=TextFont(font_color=msgColor))

    if cvalue != maxValue or (not onMaxMsg or onMaxMsg == ""):
        cliToolKit.Cursor.MoveCursorLeft(maxValue)
    else:
        cliToolKit.Cursor.MoveCursorRight(maxValue - len(onMaxMsg))
        print("\n")
    
    if cvalue == maxValue:
        cliToolKit.Cursor.ShowCusor()

    if cvalue == maxValue:
        return "MAX"
    
    return None

def cacheH(path:str, callable:Optional[object]=None, expiration:Optional[int]=None) -> Union[Optional[str], Any]:
    """Cache Hyper function. 
    
    Generates Cache files, Incase file already exists, returns the function output.


    Useful For:

        1. Large Functions that cannot be run easily.

        2. Cache functions.

        3. Large Data.

        4. Easy Loading and Unloading.

    Args:
        path (str): The Path to the Cache file.
        callable (Optional[object], optional): The function to cache. Defaults to None.
        expiration (Optional[int], optional): If not None, The expiration time, in hours. Defaults to None.

    Returns:
        None | str | Any: string, for success, if string includes '$Error$' at the start there is a Error. In case file already exists, the result of the callable function will be returned.
    """

    import time

    if expiration:
        expiration = int(expiration) * 3600 # Covert to seconds:

    cache_data:Any = None

    if os.path.exists(path):
        try:
            with open(path, 'rb') as f:
                cache_data = f.read()

            pbin = PBin(header=None)
            stringD, CBFlag, CB_data = pbin.Deserialize(cache_data) # Deserialize

            #Extract timestamp
            timestamp = CB_data.split('##SEPERATOR##')[1]
            result = CB_data.split('##SEPERATOR##')[0]

            nameSpace = {}
            exec(result, nameSpace)
            funcName = result.split("(")[0].split()[-1]
            result = nameSpace[funcName]

            if not expiration:
                return result

            # If expriation, check if it is expired or not.
            if time.time() - timestamp < expiration:
                return result
            
        except Exception as e:
            return f"$Error$ Error loading cache data. -> {e}"
        
    import inspect

    result = inspect.getsource(callable)

    cTimeStamp = int(time.time())
    cache_data_ = result + f"##SEPERATOR##{cTimeStamp}"

    pbin = PBin(header=PHeader())
    binResult = pbin.Serialize(cache_data_, CB_flag=True)

    with open(path, 'wb') as f:
        f.write(binResult)

    return result