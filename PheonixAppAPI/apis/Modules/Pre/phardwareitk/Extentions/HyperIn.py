from . import *
from typing import *

def inputH(*values:object, seperator:Union[str, None]=" ", endl:Union[str, None]=None, backgroundColorEnabled:bool=False, FontEnabled:bool=False, Font:TextFont=TextFont()) -> str:
    """Hyper version of Python's input function.

    Args:
        seperator (Union[str, None], optional): The seperator between [*values]. Defaults to " ".
        endl (Union[str, None], optional): The string to add at the end of [*values]. None if don't want. Defaults to None.
        backgroundColorEnabled (bool, optional): Wether to enable background-color. Defaults to False.
        FontEnabled (bool, optional): Wether to enable the custom font. Defaults to False.
        Font (TextFont, optional): The font. Defaults to TextFont().

    Returns:
        str: The user provided input
    """
    if not FontEnabled:
        i = 0
        value = ""

        for val in values:
            if i == 0:
                value += str(val)
            else:
                value += str(seperator) + str(val)

        if endl != "":
            value += str(endl)
        
        return input(value)
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

        return input(final_str)