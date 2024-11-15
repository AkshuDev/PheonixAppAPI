from . import *
from typing import *
import time

if not sys.path[PHardwareITK] == PHardwareITK_P:
    sys.path.append(PHardwareITK_P)



def inputH(*values:object, seperator:Union[str, None]=" ", endl:Union[str, None]=None, backgroundColorEnabled:bool=False, FontEnabled:bool=False, Font:TextFont=TextFont(), mask:bool=False, maskCharacter:str="*", History:Optional[list]=None, Regex_ReEntry:Optional[str]=None, Regex_Msg: Optional[str]=None, Regex_Time: Optional[float]=None, DefaultVal:Optional[str]=None, cpuHoggin:float=0.005) -> str:
    """Hyper version of Python's input function.

    
    NOTE: This function uses custom key input detection and, if any bug occurs, please post in [https://github.com/AkshuDev/PHardwareITK/issues]

    
    Args:
        seperator (Union[str, None], optional): The seperator between [*values]. Defaults to " ".
        endl (Union[str, None], optional): The string to add at the end of [*values]. None if don't want. Defaults to None.
        backgroundColorEnabled (bool, optional): Wether to enable background-color. Defaults to False.
        FontEnabled (bool, optional): Wether to enable the custom font. Defaults to False.
        Font (TextFont, optional): The font. Defaults to TextFont().
        mask (bool, optional): Whether to mask the input text. Defaults to False.
        maskCharacter (str, optional): The character used to mask the input text. Defaults to '*'.
        History (Optional[list], optional): If not None, Upon receiving arrow keys, The old prompts/History will appear (User choice to enter history or not). Defaults to None.
        Regex_ReEntry (Optional[str], optional): If not None, The input will be going through a validation via the given regex. Defaults to None.
        Regex_Msg (Optional[str], optional): If not None and if the Regex_ReEntry is not None, then if match fails, then this msg will be printed, without newline. Please add newline before if you want. Defaults to None.
        Regex_Time (Optional[float], optional): If not None and if the Regex_ReEntry is not None, then if match fails, then this specifies the time, the message will be shown for. Defaults to None.
        DefaultVal (Optional[str], optional): If not None, If the input is empty, the provided Value will be returned.
        cpuHoggin (float, optional): Cpu Hogging is very much required for programs like this. This is a complex input function, so unlike python's input function, it cannot avoid CPU usage. To prevent it a small delay is added at the end of the loop. IT CANNOT BE 0 as it can harm the CPU. Defaults to 0.005 seconds or 5 milliseconds.

    Returns:
        str: The user provided input
    """
    import string
    from phardwareitk.CLI import cliToolKit
    if not endl:
        endl = ""
    
    if Regex_ReEntry:
        import re

    final_Str = ""

    for i, val in enumerate(values):
        if i == 0:
            final_Str += val
        elif seperator == "" or not seperator:
            final_Str += val
        else:
            final_Str += seperator
            final_Str += val
    
    if endl and not endl == "":
        final_Str += endl

    if cpuHoggin < 0.003:
        cpuHoggin = 0.003

    cliToolKit.Text.WriteText(final_Str, Flush=True, seperator=seperator, endl=endl, backgroundColorEnabled=backgroundColorEnabled, FontEnabled=FontEnabled, Font=Font)

    buffer = ""
    bufferL:list = []
    key_pressed:bool = False
    key_pressedB:bool = False
    key_pressedHis: bool = False
    key_pressedL:bool = False
    key_pressedR:bool = False

    chars:int = 0
    cPrompt:int = 0
    cPos:int = 0

    bufferPrompt:str = ""

    import keyboard

    while True:
        key_ = keyboard.read_event(suppress=True)
        if key_.event_type == keyboard.KEY_DOWN:
            if key_.name in string.printable:
                if len(buffer) > 0:
                    buffer = buffer[:cPos]
                    buffer += key_.name + bufferPrompt[cPos:]
                else:
                    buffer = key_.name
                bufferPrompt = buffer
                if len(bufferL) > 0:
                    bufferL.insert(cPos + 1, key_.name)
                else:
                    bufferL.append(key_.name)
                chars += 1
                cPos += 1
                if not mask:
                    cliToolKit.Text.WriteText(key_.name, Flush=True, endl=None, backgroundColorEnabled=backgroundColorEnabled, FontEnabled=FontEnabled, Font=Font)
                    if buffer[cPos:] != "":
                        cliToolKit.Text.WriteText(buffer[cPos:], Flush=True, endl=None, backgroundColorEnabled=backgroundColorEnabled, FontEnabled=FontEnabled, Font=Font)
                        cliToolKit.Cursor.MoveCursorLeft(len(buffer[cPos:]))
                else:
                    cliToolKit.Text.WriteText(maskCharacter, Flush=True, endl=None, backgroundColorEnabled=backgroundColorEnabled, FontEnabled=FontEnabled, Font=Font)
                    if buffer[cPos:] != "": 
                        cliToolKit.Text.WriteText(maskCharacter*len(buffer[cPos:]), Flush=True, endl=None, backgroundColorEnabled=backgroundColorEnabled, FontEnabled=FontEnabled, Font=Font)
                        cliToolKit.Cursor.MoveCursorLeft(len(buffer[cPos:]))
            
            elif key_.name == "enter":
                if not key_pressed:
                    key_pressed = True
                    if not Regex_ReEntry:
                        print("\n", flush=True)
                        keyboard.unhook_all()
                        return buffer
                    else:
                        result = re.match(Regex_ReEntry, buffer)
                        if result:
                            if DefaultVal and (DefaultVal != "" and buffer == ""):
                                buffer = DefaultVal
                            print("\n", flush=True)
                            keyboard.unhook_all()
                            return buffer
                        else:
                            if not Regex_Msg or Regex_Msg == "":
                                continue
                            cliToolKit.Text.WriteText(Regex_Msg, Flush=True, backgroundColorEnabled=backgroundColorEnabled, FontEnabled=FontEnabled, Font=Font)
                            cliToolKit.Cursor.MoveCursorLeft(len(Regex_Msg))
                            if Regex_Time and Regex_Time > 0:
                                time.sleep(Regex_Time)
                            cliToolKit.Text.WriteText(" "*len(Regex_Msg))
                            cliToolKit.Cursor.MoveCursorLeft(len(Regex_Msg))
                            continue
            elif key_.name == "backspace":
                if not (key_pressedB and buffer != "") and (cPos > 0 and chars > 0):
                    key_pressedB = True
                    bufferL.pop(cPos - 1)
                    buffer = "".join(bufferL)
                    bufferPrompt = buffer
                    # Remove old text
                    if chars == cPos:
                        cliToolKit.Cursor.MoveCursorLeft(chars)
                    else:
                        cliToolKit.Cursor.MoveCursorLeft(cPos)
                    cliToolKit.Text.WriteText(" "*chars, FontEnabled=FontEnabled, Font=Font, Flush=True)
                    cliToolKit.Cursor.MoveCursorLeft(chars)
                    # Add new text
                    if not mask:
                        cliToolKit.Text.WriteText(buffer, FontEnabled=Font, backgroundColorEnabled=backgroundColorEnabled, Font=Font, Flush=True)
                    else:
                        cliToolKit.Text.WriteText(maskCharacter*(chars - 1), FontEnabled=Font, backgroundColorEnabled=backgroundColorEnabled, Font=Font, Flush=True)
                    chars -= 1
                    cPos -= 1
                    if not cPos == chars:
                        cliToolKit.Cursor.MoveCursorLeft(chars - cPos)
            elif key_.name == "space":
                if len(buffer) > 0:
                    buffer = buffer[:cPos]
                    buffer += " " + bufferPrompt[cPos:]
                else:
                    buffer = " "
                bufferPrompt = buffer
                if len(bufferL) > 0:
                    bufferL.insert(cPos + 1, " ")
                else:
                    bufferL.append(" ")
                chars += 1
                cPos += 1
                if not mask:
                    cliToolKit.Text.WriteText(" ", Flush=True, endl=None, backgroundColorEnabled=backgroundColorEnabled, FontEnabled=FontEnabled, Font=Font)
                    if buffer[cPos:] != "":
                        cliToolKit.Text.WriteText(buffer[cPos:], Flush=True, endl=None, backgroundColorEnabled=backgroundColorEnabled, FontEnabled=FontEnabled, Font=Font)
                        cliToolKit.Cursor.MoveCursorLeft(len(buffer[cPos:]))
                else:
                    cliToolKit.Text.WriteText(maskCharacter, Flush=True, endl=None, backgroundColorEnabled=backgroundColorEnabled, FontEnabled=FontEnabled, Font=Font)
                    if buffer[cPos:] != "": 
                        cliToolKit.Text.WriteText(maskCharacter*len(buffer[cPos:]), Flush=True, endl=None, backgroundColorEnabled=backgroundColorEnabled, FontEnabled=FontEnabled, Font=Font)
                        cliToolKit.Cursor.MoveCursorLeft(len(buffer[cPos:]))
            elif key_.name == "up":
                if History:
                    if not key_pressedHis:
                        try:
                            prompt = History[cPrompt]
                            buffer = prompt
                            if chars != 0:
                                if cPos == chars:
                                    cliToolKit.Cursor.MoveCursorLeft(chars)
                                else:
                                    cliToolKit.Cursor.MoveCursorLeft(cPos)
                                cliToolKit.Text.WriteText(" " * chars, Flush=True, FontEnabled=FontEnabled, Font=Font)
                                cliToolKit.Cursor.MoveCursorLeft(chars)
                            cliToolKit.Text.WriteText(prompt, Flush=True, backgroundColorEnabled=backgroundColorEnabled, FontEnabled=FontEnabled, Font=Font)
                            cPrompt += 1
                            chars = len(prompt)
                            cPos = chars
                        except IndexError:
                            cPrompt = 0
                            prompt = bufferPrompt
                            buffer = prompt
                            if cPos == chars:
                                cliToolKit.Cursor.MoveCursorLeft(chars)
                            else:
                                cliToolKit.Cursor.MoveCursorLeft(cPos)
                            cliToolKit.Text.WriteText(" " * chars, Flush=True, FontEnabled=FontEnabled, Font=Font)
                            cliToolKit.Cursor.MoveCursorLeft(chars)
                            cliToolKit.Text.WriteText(prompt, Flush=True, backgroundColorEnabled=backgroundColorEnabled, FontEnabled=FontEnabled, Font=Font)
                            chars = len(prompt)
                            cPos = chars
                        
                        key_pressedHis = True
                
            elif key_.name == "left":
                if not key_pressedL:
                    if cPos > 0:
                        cliToolKit.Cursor.MoveCursorLeft(1)
                        cPos -= 1
                    key_pressedL = True
            elif key_.name == "right":
                if not key_pressedR:
                    if cPos < chars:
                        cliToolKit.Cursor.MoveCursorRight(1)
                        cPos += 1
                    key_pressedR = True

        time.sleep(cpuHoggin) # Prevents hogging
        key_pressed = False
        key_pressedL = False
        key_pressedR = False
        key_pressedB = False
        key_pressedHis = False