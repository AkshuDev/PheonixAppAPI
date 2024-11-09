from . import *
from typing import *

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
    """
    seperator = str(seperator)
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

            final_str:str = ""

            if backgroundColorEnabled:
                final_str += backgroundColor_code
            if color_code:
                final_str += color_code
            if font_code:
                final_str += font_code

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

            final_str:str = ""

            if backgroundColorEnabled:
                final_str += backgroundColor_code
            if color_code:
                final_str += color_code
            if font_code:
                final_str += font_code

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
