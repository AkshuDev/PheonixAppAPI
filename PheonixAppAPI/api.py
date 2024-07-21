import os
import sys
import typing

from PheonixAppAPI.pheonixapp.files import (PSSbridge)
from PheonixAppAPI.pheonixapp.files.Mapper import (map)
from PheonixAppAPI import (bin_worker)

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
        4. 'Map' Encodes through a given map.
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

    def Encode_Map(self, map:dict) -> str:
        """
        Encodes the message using the specified map.

        Returns:
            str: The encoded message.
        """
        return PATF.Encode(self.msg, "map", map)

    def remove_maps(self, mode:str="one", names:list=[]) -> None:
        """A class to create, store, and retrieve a map for an encoder.

        Attributes:
        mode (str): The name of the map.

        Available ->
        1. one: Only removes the map that is at the first of the names list.
        2. list: Removes all the maps that are present in the names list.
        3. all: Removes all the maps except the default ones.

        names(list): The list of names to remove. If [mode] is [one] then only the first map in this list is removed.

        Raises:
        Exception: No Map File to begin with.

        Returns:
        None: Nothing.
        """
        return map.Map("").remove_maps(mode, names)

    def create_map(self, keys:str="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~") -> dict:
        """
        Creates a dictionary where each key is a character and each value is a unique, randomly assigned character.

        Args:
        keys (str, optional): The string of characters to use as keys and values. Defaults to a comprehensive set of keyboard characters.

        Returns:
        dict: A dictionary mapping each character to a unique, random character.
        """
        return map.Map("").create_map(keys)

    def push_map(self, name:str, map_:dict={}) -> None:
        """
        Writes the map to an encrypted file. Creates the file if it does not exist.
        """
        map.Map(name, map_).push_map()

    def get_map(self, name:str, map_:dict={}) -> None:
        """
        Retrieves and decrypts the map from the encrypted file.

        Returns:
        dict: The decrypted map.

        Raises:
        Exception: If the map file does not exist.
        """
        return map.Map(name, map_).get_map()

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
        4. 'Map' Encodes through a given map.
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

    def Decode_Map(self, map:dict) -> str:
        """
        Decodes the message using the specified map.

        Returns:
            str: The decoded message.
        """
        return PATF.Decode(self.msg, "map", map)

    def remove_maps(self, mode:str="one", names:list=[]) -> None:
        """A class to create, store, and retrieve a map for an encoder.

        Attributes:
        mode (str): The name of the map.

        Available ->
        1. one: Only removes the map that is at the first of the names list.
        2. list: Removes all the maps that are present in the names list.
        3. all: Removes all the maps except the default ones.

        names(list): The list of names to remove. If [mode] is [one] then only the first map in this list is removed.

        Raises:
        Exception: No Map File to begin with.

        Returns:
        None: Nothing.
        """
        return map.Map("").remove_maps(mode, names)

    def create_map(self, keys:str="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~") -> dict:
        """
        Creates a dictionary where each key is a character and each value is a unique, randomly assigned character.

        Args:
        keys (str, optional): The string of characters to use as keys and values. Defaults to a comprehensive set of keyboard characters.

        Returns:
        dict: A dictionary mapping each character to a unique, random character.
        """
        return map.Map("").create_map(keys)

    def push_map(self, name:str, map_:dict={}) -> None:
        """
        Writes the map to an encrypted file. Creates the file if it does not exist.
        """
        map.Map(name, map_).push_map()

    def get_map(self, name:str, map_:dict={}) -> None:
        """
        Retrieves and decrypts the map from the encrypted file.

        Returns:
        dict: The decrypted map.

        Raises:
        Exception: If the map file does not exist.
        """
        return map.Map(name, map_).get_map()

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

def create_map(keys:str="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~") -> dict:
    """
    Creates a dictionary where each key is a character and each value is a unique, randomly assigned character.

    Args:
    keys (str, optional): The string of characters to use as keys and values. Defaults to a comprehensive set of keyboard characters.

    Returns:
    dict: A dictionary mapping each character to a unique, random character.
    """
    return map.Map("").create_map(keys)

def push_map(name:str, map_:dict={}) -> None:
    """
    Writes the map to an encrypted file. Creates the file if it does not exist.

    Args:
    name (str): The name of the map to push.
    map_ (dict, optional): The dictionary map to push. Default Value is set to [{}].

    Returns:
    None: Nothing.
    """
    map.Map(name, map_).push_map()

def get_map(name:str, map_:dict={}) -> None:
    """
    Retrieves and decrypts the map from the encrypted file.

    Args:
    name (str): The name of the map to get.
    map_ (dict, optional): This is not required by the user as it is only used for creating the object.

    Returns:
    dict: The decrypted map.

    Raises:
    Exception: If the map file does not exist.
    """
    return map.Map(name, map_).get_map()

def remove_maps(mode:str="one", names:list=[]) -> None:
    """A function to remove maps from the file.

    Attributes:
    mode (str): The name of the map.

    Available ->
    1. one: Only removes the map that is at the first of the names list.
    2. list: Removes all the maps that are present in the names list.
    3. all: Removes all the maps except the default ones.

    names(list): The list of names to remove. If [mode] is [one] then only the first map in this list is removed.

    Raises:
    Exception: No Map File to begin with.

    Returns:
    None: Nothing.
    """
    return map.Map("").remove_maps(mode, names)

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

def BIN(path: str = "./aol_var-dict.aolvd", format: str = "vardict-v0.001JSON", encoding: str = "utf-16", encode: bool = False, content: str = "", content_dict: dict = {},
            use_base64: bool = False, use_pheonixApp_encoder: bool = True, compressed: bool = False, hyper_compressed: bool = False) -> bin_worker.BIN:
    """Returns the BIN class of bin_worker.py for working with binary.

    Args:
        path (str, optional): the path of the file while pushing data into file. Defaults to "./aol_var-dict.aolvd".
        format (str, optional): The format to set the content_dict into while pushing dict. Defaults to "vardict-v0.001JSON".
        encoding (str, optional): Encoding for the content or content_dict. Defaults to "utf-16".
        encode (bool, optional): To Encode The Data. Recommended to leave it as it is. Defaults to False.
        content (str, optional): The content in String. Defaults to "".
        content_dict (dict, optional): The content in dictionary. Defaults to {}.
        use_base64 (bool, optional): To encode using base64. NOTE: [low storage taking but less safe]. Defaults to False.
        use_pheonixApp_encoder (bool, optional): To encode using our Encoder. NOTE: [High Storage taking in compare to base64 but more safe (3 Layer Encryption)]. Defaults to True.
        compressed (bool, optional): To compress the size. After setting it to True the file will take less space but the Encryption will lose 1 layer. Defaults to False.
        hyper_compressed (bool, optional): To hyper-compress the size. After setting it to True the file will take less space but the Encryption will lose 2 layers. Defaults to False.

        NOTE: [This file is copied from our another program known as AOL(Assembly Orientated Language) and some of its functions are removed to match this Module]
    Returns:
        bin_worker.BIN: The class for working with binary
    """
    return PATF.BIN(path, format, encoding, encode, content, content_dict, use_base64, use_pheonixApp_encoder, compressed, hyper_compressed)

def str_to_bin(data: typing.Union[str, int, dict]) -> str:
    """
    Convert a string, integer, or dictionary to its binary string representation.

    Args:
    data (typing.Union[str, int, dict]): The data to convert to binary.

    Returns:
    str: The binary string representation of the input data.
    """
    return PATF.str_to_bin(data)

def bin_to_str(data: str) -> str:
    """
    Convert a binary string back to its original string representation.

    Args:
    data (str): The binary string to convert.

    Returns:
    str: The original string representation of the binary input.
    """
    return PATF.bin_to_str(data)

def str_to_bytes(data: typing.Union[str, int, dict], encoding: str = "utf-16") -> bytes:
    """
    Convert a string, integer, or dictionary to its byte representation.

    Args:
    data (typing.Union[str, int, dict]): The data to convert to bytes.
    encoding (str, optional): The encoding to use for the conversion. Defaults to "utf-16".

    Returns:
    bytes: The byte representation of the input data.
    """
    return PATF.str_to_bytes(data, encoding)

def bytes_to_str(data: bytes, encoding: str = "utf-16") -> str:
    """
    Convert bytes back to a string using the specified encoding.

    Args:
    data (bytes): The byte data to convert.
    encoding (str, optional): The encoding to use for the conversion. Defaults to "utf-16".

    Returns:
    str: The string representation of the byte input.
    """
    return PATF.bytes_to_str(data, encoding)

def to_binINT(data_dict: dict = {}, data_str: str = "", useString: bool = True) -> int:
    """
    Convert a dictionary or string to a binary integer.

    Args:
    data_dict (dict, optional): The dictionary to convert. Defaults to an empty dictionary.
    data_str (str, optional): The string to convert. Defaults to an empty string.
    useString (bool, optional): Flag to indicate if data_str should be used. Defaults to True.

    Returns:
    int: The binary integer representation of the input data.
    """
    return PATF.to_binINT(data_dict, data_str, useString)