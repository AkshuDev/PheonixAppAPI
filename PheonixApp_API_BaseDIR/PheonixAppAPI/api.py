import os
import sys

from PheonixAppAPI.pheonixapp.files import (PSSbridge)

PATF = None

def set_parent(parent:object) -> None:
    """
    Sets the global parent object for the API.

    Args:
        parent (object): The parent object to set as the global PATF.
    """
    global PATF

    PATF = parent

class GUI():
    """
    A class to handle the GUI operations of Pheonix App.
    """
    def __init__(self) -> None:
        """
        Initializes the GUI class.
        """
        pass

    def start(self) -> None:
        """
        Starts the PheonixApp GUI.
        """
        PATF.run("gui start")

class MiniGames():
    """
    A class to handle mini-games within PheonixAppAPI.
    """
    def __init__(self) -> None:
        """
        Initializes the MiniGames class.
        """
        pass

    def GuessTheNumber(self) -> None:
        """
        Starts the 'Guess The Number' mini-game.
        """
        PATF.run("fun !minigame guessthenumber")

class PATF_API():
    """
    A class to interact with the PATF API.

    Args:
        useFileData (bool): Whether to use PATF file data.
        email (str): The email address for login.
        username (str): The username for login.
        password (str): The password for login.
    """
    def __init__(self, useFileData:bool=False, email:str="", username:str="", password:str="") -> None:
        """
        Initializes the PATF_API class.
        """
        self.useFileData = useFileData
        self.email = email
        self.username = username
        self.password = password
        self.patf = PATF

    def run(self, cmd:str="terminal --createfile") -> None:
        """
        Runs a specified command.

        Args:
            cmd (str): The command to run.
        """
        self.patf.run(cmd)

    def CheckModules(self, mode:str="all", list:list=[], module:str="") -> None:
        """
        Checks the specified modules.

        Args:
            mode (str): The mode for checking modules:
            Available Modes are ->
            1. 'all' This mode checks for all PheonixApp required Modules.
            2. 'list' This mode checks for the specified list.
            3. 'module' This mode checks for a specified module.


            list (list): The list of modules to check.
            module (str): The specific module to check.
        """
        self.patf.CheckModules(mode, list, module)

    def createfile(self):
        """
        Creates a PATF file.
        """
        self.patf.run("terminal --createfile")

    def GetCertificatePath(self, code:str="", flag:str="+BOOL"):
        """
        Gets the user saved certificate path.

        Args:
            code (str): The code for using the certificate path function.
            flag (str): The flag for the certificate path.

        Returns:
            str: The certificate path.
        """
        return self.patf.getCertificatePath(code, flag)

class Encoder():
    """
    A class to handle encoding messages.

    Args:
        msg (str): The message to encode.
        type (str): The encoding type:

        Available Are ->
        1. 'Hype_Space' Encodes all letters, numbers and symbols
        2. 'Pheonix_utx' Encodes only some lowercase letters, numbers and symbols
        3. 'Pheonixntx_H1' Encodes only lowercase letters
    """
    def __init__(self, msg:str="", type_:str="Hype_Space") -> None:
        self.msg = msg
        self.type_ = type_

    def Encode(self) -> str:
        """
        Encodes the message using the specified type.

        Returns:
            str: The encoded message.
        """
        return PATF.Encode(self.msg, self.type_)

class Decoder():
    """
    A class to handle decoding messages.

    Args:
        msg (str): The message to decode.
        type_ (str): The decoding type. If don't know then put -> '' (empty string):

        Available Are ->
        1. 'Hype_Space' Encodes all letters, numbers and symbols
        2. 'Pheonix_utx' Encodes only some lowercase letters, numbers and symbols
        3. 'Pheonixntx_H1' Encodes only lowercase letters
    """
    def __init__(self, msg:str="", type_:str="Hype_Space") -> None:
        self.msg = msg
        self.type_ = type_

    def Decode(self) -> str:
        """
        Decodes the message using the specified type.

        Returns:
            str: The decoded message.
        """
        return PATF.Decode(self.msg, self.type_)

class Utilities():
    """
    A class to handle utility functions within Pheonix App.
    """
    def __init__(self) -> None:
        """
        Initializes the Utilities class.
        """
        pass

    def Calc_Terminal(self) -> None:
        """
        Starts the calculator utility in the terminal.
        """
        PATF.Utilities_Calc_Terminal()
        return None

    def Wiki_Terminal(self) -> None:
        """
        Starts the Wikipedia search utility in the terminal.
        """
        PATF.Utilities_Wiki_Terminal
        return None

def Error(type_:BaseException, name:str, details:str, log:bool=False, mode:str="") -> None:
    """
    Logs an error.

    Args:
        type_ (BaseException): The type of the exception.
        name (str): The name of the error.
        details (str): The details of the error.
        log (bool): Whether to display the error as a log.
        mode (str): The mode of the error:

        Available Are ->
        1. DEFAULT: '' Normal Mode. Raises the error and stops the code.
        2. 'DECL' This mode will raise the error and will not stop the code.
    """
    PATF.Error_(type_, name, details, log, mode)
    return None

class Extra_Commands():
    """
    A class to handle extra terminal commands.

    Args:
        cmd (str): The command to run.
    """
    def __init__(self, cmd:str) -> None:
        self.cmd = cmd

    def Terminal_run(self) -> None:
        """
        Runs the specified terminal command.
        """
        PATF.Terminal_run(self.cmd)
        return None

class Extra():
    """
    A class to handle extra functions within PheonixAppAPI.
    """
    def __init__(self) -> None:
        """
        Initializes the Extra class.
        """
        pass

    def Object_Detector(self) -> None:
        """
        Runs the object detector function. NOTE: This function will run forever until the code is stopped.
        """
        PATF.Object_Detector()
        return None

    def HaCline(self) -> None:
        """
        Runs the HaCline (In development. Do not use.).
        """
        PATF.HaCline()
        return None
