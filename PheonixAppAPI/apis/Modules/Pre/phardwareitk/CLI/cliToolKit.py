import sys
import os
from typing import *

from . import *

if not sys.path[PHardwareITK] == PHardwareITK_P:
    sys.path.append(PHardwareITK_P)

from phardwareitk.Extensions import HyperIn, HyperOut
from phardwareitk import Extensions

class Cursor:
    """A Class dedicated to cursor operations in command line.
    """
    @staticmethod
    def MoveCursorX(x: int) -> None:
        """Moves the cursor to the specified X postion.

        Args:
            x (int): X coordinate.
        """
        sys.stdout.write(f"\033[{x}G")
        sys.stdout.flush()
    @staticmethod
    def MoveCursor(x:int, y:int) -> None:
        """Move Cursor to specified position.

        Args:
            x (int): The X coordinate.
            y (int): the Y coordinate.
        """
        sys.stdout.write(f'\033[{y};{x}H')
        sys.stdout.flush()

    @staticmethod
    def HideCursor() -> None:
        """Hide the cursor."""
        sys.stdout.write('\033[?25l')
        sys.stdout.flush()

    @staticmethod
    def ShowCusor() -> None:
        """Show the cursor."""
        sys.stdout.write('\033[?25h')
        sys.stdout.flush()

    @staticmethod
    def MoveCursorUp(n: int) -> None:
        """Move cursor up by n lines."""
        if n == 0:
            return None
        if not n:
            return None
        sys.stdout.write(f'\033[{n}A')
        sys.stdout.flush()

    @staticmethod
    def MoveCursorDown(n: int) -> None:
        """Move cursor down by n lines."""
        if n == 0:
            return None
        if not n:
            return None
        sys.stdout.write(f'\033[{n}B')
        sys.stdout.flush()

    @staticmethod
    def MoveCursorRight(n: int) -> None:
        """Move cursor right by n columns."""
        if n == 0:
            return None
        if not n:
            return None
        sys.stdout.write(f'\033[{n}C')
        sys.stdout.flush()

    @staticmethod
    def MoveCursorLeft(n: int) -> None:
        """Move cursor left by n columns."""
        if n == 0:
            return None
        if not n:
            return None
        sys.stdout.write(f'\033[{n}D')
        sys.stdout.flush()

    @staticmethod
    def SaveCursorPosition() -> None:
        """Save the current cursor position."""
        sys.stdout.write('\033[s')
        sys.stdout.flush()

    @staticmethod
    def RestoreCursorPosition() -> None:
        """Restore the cursor to its last saved position."""
        sys.stdout.write('\033[u')
        sys.stdout.flush()

    @staticmethod
    def SetCursorToBeginningOfLine() -> None:
        """Move the cursor to the beginning of the current line."""
        sys.stdout.write('\033[0G')
        sys.stdout.flush()

    @staticmethod
    def SetCursorToEndOfLine() -> None:
        """Move the cursor to the end of the current line."""
        sys.stdout.write('\033[999C')  # Effectively moves to the end of the line
        sys.stdout.flush()

    @staticmethod
    def HideCursorTemporarily() -> None:
        """Temporarily hide the cursor (until next action)."""
        sys.stdout.write('\033[?25l')
        sys.stdout.flush()

    @staticmethod
    def ShowCursorTemporarily() -> None:
        """Temporarily show the cursor again after it was hidden."""
        sys.stdout.write('\033[?25h')
        sys.stdout.flush()

    @staticmethod
    def SetCursorPositionToHome() -> None:
        """Set the cursor to the top left corner (1, 1)."""
        sys.stdout.write('\033[H')
        sys.stdout.flush()

    @staticmethod
    def SetCursorPositionToEnd() -> None:
        """Set the cursor to the bottom right corner of the terminal."""
        sys.stdout.write('\033[999;999H')  # Moves to the bottom-right of the screen
        sys.stdout.flush()

    @staticmethod
    def MoveToNextWord() -> None:
        """Move the cursor to the next word."""
        sys.stdout.write('\033[W')
        sys.stdout.flush()

    @staticmethod
    def MoveToPreviousWord() -> None:
        """Move the cursor to the previous word."""
        sys.stdout.write('\033[W')
        sys.stdout.flush()

    @staticmethod
    def MoveCursorToTop() -> None:
        """Move the cursor to the top of the terminal."""
        sys.stdout.write('\033[H')
        sys.stdout.flush()

    @staticmethod
    def MoveCursorToBottom() -> None:
        """Move the cursor to the bottom of the terminal."""
        sys.stdout.write('\033[999;999H')  # Effective way to scroll down
        sys.stdout.flush()

    @staticmethod
    def SetCursorVisibility(is_visible: bool) -> None:
        """Set the cursor visibility."""
        sys.stdout.write('\033[?25h' if is_visible else '\033[?25l')
        sys.stdout.flush()

    @staticmethod
    def CurrentCursorPosition() -> tuple:
        """Get the current cursor position using BLOCKING. (row(y), column(x))."""
        sys.stdout.write('\033[6n')  # Request cursor position
        sys.stdout.flush()
        
        cursor_position = sys.stdin.read(6)  # Read the response
        if cursor_position.startswith('\033['):
            y, x = cursor_position[2:-1].split(';')  # Format: '\033[y;xR'
            return (int(y), int(x))
        return (0, 0)  # Default if no valid position is returned

class Screen:
    @staticmethod
    def ClearCurrentLine() -> None:
        """Clear the current line."""
        sys.stdout.write('\033[2K')
        sys.stdout.flush()

    @staticmethod
    def ClearLine(y: int) -> None:
        """Clear a specified line."""
        sys.stdout.write(f'\033[{y};1H\033[2K')
        sys.stdout.flush()

    @staticmethod
    def ClearScreen() -> None:
        """Clear the entire screen."""
        sys.stdout.write('\033[2J')
        sys.stdout.flush()

    @staticmethod
    def ClearScreenFromCursorDown() -> None:
        """Clear the screen from the cursor's current position to the bottom."""
        sys.stdout.write('\033[J')
        sys.stdout.flush()

    @staticmethod
    def ClearScreenFromCursorUp() -> None:
        """Clear the screen from the cursor's current position to the top."""
        sys.stdout.write('\033[1J')
        sys.stdout.flush()

    @staticmethod
    def SetScreenBackgroundColor(color: str) -> None:
        """Set the background color of the terminal."""
        sys.stdout.write(f'\033[{color}m')
        sys.stdout.flush()

    @staticmethod
    def SetScreenForegroundColor(color: str) -> None:
        """Set the foreground color of the terminal."""
        sys.stdout.write(f'\033[{color}m')
        sys.stdout.flush()

    @staticmethod
    def SetScreenColorReset() -> None:
        """Reset the screen's colors to default."""
        sys.stdout.write('\033[0m')
        sys.stdout.flush()

    @staticmethod
    def HideScreenCursor() -> None:
        """Hide the terminal cursor."""
        sys.stdout.write('\033[?25l')
        sys.stdout.flush()

    @staticmethod
    def ShowScreenCursor() -> None:
        """Show the terminal cursor."""
        sys.stdout.write('\033[?25h')
        sys.stdout.flush()

    @staticmethod
    def GetTerminalSize() -> tuple:
        """Get the current terminal size (rows, columns)."""
        size = os.popen('stty size', 'r').read().split()
        return (int(size[0]), int(size[1]))

    @staticmethod
    def SetTerminalSize(rows: int, cols: int) -> None:
        """Set the terminal size."""
        sys.stdout.write(f'\033[8;{rows};{cols}t')
        sys.stdout.flush()

    @staticmethod
    def EnableAlternateScreenBuffer() -> None:
        """Enable the alternate screen buffer."""
        sys.stdout.write('\033[?1049h')
        sys.stdout.flush()

    @staticmethod
    def DisableAlternateScreenBuffer() -> None:
        """Disable the alternate screen buffer."""
        sys.stdout.write('\033[?1049l')
        sys.stdout.flush()

    @staticmethod
    def ScrollUp(n: int) -> None:
        """Scroll up n lines in the terminal."""
        if n == 0:
            return None
        if not n:
            return None
        sys.stdout.write(f'\033[{n}S')
        sys.stdout.flush()

    @staticmethod
    def ScrollDown(n: int) -> None:
        """Scroll down n lines in the terminal."""
        if n == 0:
            return None
        if not n:
            return None
        sys.stdout.write(f'\033[{n}T')
        sys.stdout.flush()

    @staticmethod
    def ClearTabs() -> None:
        """Clear all tab stops in the terminal."""
        sys.stdout.write('\033[3g')
        sys.stdout.flush()

    @staticmethod
    def SetTab() -> None:
        """Set a tab stop at the current cursor position."""
        sys.stdout.write('\033[H')
        sys.stdout.flush()

    @staticmethod
    def ResetTerminal() -> None:
        """Reset the terminal to its default state."""
        sys.stdout.write('\033c')
        sys.stdout.flush()

    @staticmethod
    def SetCursorStyle(style: int) -> None:
        """Set the cursor style (0: block, 1: underline, 2: bar)."""
        sys.stdout.write(f'\033[{style} q')
        sys.stdout.flush()

    @staticmethod
    def EnableRawMode() -> None:
        """Enable raw mode (no input processing)."""
        sys.stdout.write('\033[?1049h')  # Use alternate buffer
        sys.stdout.flush()

    @staticmethod
    def DisableRawMode() -> None:
        """Disable raw mode."""
        sys.stdout.write('\033[?1049l')  # Return to normal buffer
        sys.stdout.flush()

    @staticmethod
    def ClearFromCursorToTop() -> None:
        """Clear The Screen from the cursor to the top of the screen.
        """
        sys.stdout.write('\033[1J')
        sys.stdout.flush()

    @staticmethod
    def ClearFromCursorToBottom() -> None:
        """Clear The Screen from the cursor to the bottom of the screen
        """
        sys.stdout.write('\033[J')
        sys.stdout.flush()

    @staticmethod
    def ClearFromCursorToEndOfLine() -> None:
        """Clear The Screen from the cursor to the end of the line
        """
        sys.stdout.write('\033[K')
        sys.stdout.flush()

    @staticmethod
    def ClearCharacter(x: int, y: int) -> None:
        """Clear the character at the specified location (x, y)."""
        Cursor.MoveCursor(x, y)
        sys.stdout.write(' ')  # Write a space to clear the character
        sys.stdout.flush()

class Text:
    @staticmethod
    def WriteText(*values:object, seperator:Union[str, None]=" ", endl:Union[str, None]="", File:Union[str, None]=None, Flush:bool=False, backgroundColorEnabled:bool=False, FontEnabled:bool=False, Font:Extensions.TextFont=Extensions.TextFont()) -> None:
        """Writes the specified text. (USES phardwareitk.Extensions.HyperOut.printH)

        Args:
            seperator (Union[str, None], optional): Seperator between values in [*values]. Defaults to " ".
            endl (Union[str, None], optional): The ending string to include at the end of the values. None is don't want. Defaults to "\n".
            File (Union[str, None], optional): Wether to save the print contents in a file before printing in console. Defaults to None.
            Flush (bool, optional): Wether to use Flush during printing. Defaults to False.
            backgroundColorEnabled (bool, optional): Wether to enable background-color. Defaults to None.
            FontEnabled (bool, optional): Wether to enable custom font. Defaults to False.
            Font (Extensions.TextFont, optional): The font. Defaults to Extensions.TextFont().
        """
        HyperOut.printH(*values, seperator=seperator, endl=endl, File=File, Flush=Flush, backgroundColorEnabled=backgroundColorEnabled, FontEnabled=FontEnabled, Font=Font)

    def InputText(*values:object, seperator:Union[str, None]=" ", endl:Union[str, None]="\n", backgroundColorEnabled:bool=False, FontEnabled:bool=False, Font:Extensions.TextFont=Extensions.TextFont()) -> str:
        """Returns the entered user data from input. (USES phardwareitk.Extensions.HyperIn.inputH)

        Args:
            seperator (Union[str, None], optional): Seperator between values in [*values]. Defaults to " ".
            endl (Union[str, None], optional): The ending string to include at the end of the values. None is don't want. Defaults to "\n".
            backgroundColorEnabled (bool, optional): Wether to enable background-color. Defaults to False.
            FontEnabled (bool, optional): Wether to enable custom font. Defaults to False.
            Font (Extensions.TextFont, optional): The font. Defaults to Extensions.TextFont().
        
        Returns:
            str: The user inputted string.
        """
        return HyperIn.inputH(*values, seperator=seperator, endl=endl, backgroundColorEnabled=backgroundColorEnabled, FontEnabled=FontEnabled, Font=Font)
    
    @staticmethod
    def DeleteChar() -> None:
        """Simulates Delete Key in terminal.
        """
        sys.stdout.write("\033[3~")
        sys.stdout.flush()

    @staticmethod
    def BackSpaceChar() -> None:
        """Simulates Backspace in terminal.
        """
        sys.stdout.write("\b")
        sys.stdout.write(" ")
        sys.stdout.write("\b")
        sys.stdout.flush()