import importlib.util
import subprocess
import os
import sys
import importlib

from PheonixAppAPI.apis.Modules.Pre.PheonixJson import Json, Psaaf
from PheonixAppAPI.apis.Modules.Pre.PheonixExceptions.Exceptions import *

mainDir = os.path.dirname(os.path.abspath(__file__))
settingsJsonFile = os.path.join(mainDir, "settings.json")

SettingsJsonFileManager = Json.JsonFileManager(settingsJsonFile)

settings:dict = SettingsJsonFileManager.JsonToDict()

moduleReg = settings["ModuleRegistry"]

lib_Path = os.path.join(mainDir, "apis", "Modules", "lib")

def ReadAccessFile(moduleName:str) -> dict:
    """Reads the Access file of a module and returns the dictionary.

    Args:
        moduleName (str): The name of the module.

    Returns:
        dict: The output dictionary.
    """
    # try1
    try:
        return Psaaf.PheonixStudiosAccessFile(lib_Path).read(moduleName)
    except Exception as e:
        raise PheonixException(f"Error reading the Access file. Error code [PheonixAppAPI.apis.PACI.ReadAccessFile.try1]\nError message -> [{e}]")

def ReturnModulePath(module_name:str) -> str:
    """Returns the module Path through its Access File.

    Args:
        module_name (str): The module name.

    Returns:
        str: The output Path.
    """
    # try1
    try:
        data = ReadAccessFile(module_name)
        data = data["Important Variables"]
        path = data["PATH"]

        return path()
    except Exception as e:
        raise PheonixException(f"Error finding module path. Error Code [PheonixAppAPI.apis.PACI.ReturnModulePath.try1]\nError Message -> [{e}]")

def MakeAccessFile(module_name:str, module_version:str="latest") -> None:
    """Makes an Access File for the module.

    Args:
        module_name (str): The name of the module.
        module_version (str, optional): The version of the module. Set it to 'latest' to define the latest version. Defaults to 'latest'.
    """
    if module_version.lower() == "latest":
        module_version = "(latest)"

    # check1
    spec = importlib.util.find_spec(module_name)

    if not spec or spec == None:
        raise ModuleDoesntExist(f"Error occurred while creating the access file. Error Code [PheonixAppAPI.apis.PACI.MakeAccessFile.check1]\nError Message -> [The module provided [{module_name}] does not exist]")

    # try1
    try:
        metadata = {"Name": module_name,
                    "Version": module_version}

        access = {"PATH": os.path.dirname(os.path.abspath(importlib.util.find_spec(module_name).origin))}
        Psaaf.PheonixStudiosAccessFile(lib_Path).create(module_name, metadata, access)
    except Exception as e:
        raise ErrorWhileCreatingFile(f"Error creating Access File of module [{module_name}]. Error Code [PheonixAppAPI.apis.PACI.MakeAccessFile.try1]\nError Message -> [{e}]")

def InstallPheonixModule(module_name:str, module_version:str="latest", log:bool=False) -> None:
    """This function allows to install a Pheonix Studios Python Module (ex -> pcd_py (Pheonix Clipped Dictionaries Python))

    Args:
        module_name (str): The name of the module needed to be installed.
        module_version (str, optional): The version of the module. Set it to 'latest' to define the latest version. Defaults to 'latest'.
        log (bool, optional): Whether to log the installation. Defaults to False.
    """
    if module_version.lower() == "latest":
        module_version = ""
    else:
        module_version = f"=={module_version}"

    # check1
    if module_name in moduleReg["PheonixStudios"]["Names"]:
        # check2
        if module_name in moduleReg["PheonixStudios"]["Modules"][module_name]["Active"].lower() == "false":
            raise ErrorOccuredWhileInstallingModule(f"Error occurred while installing module [{module_name}]. Error Code [PheonixAppAPI.apis.PACI.InstallPheonixModule.check2]\nError Message -> [The module is not yet published]")
    # check3
    else:
        raise ErrorOccuredWhileInstallingModule(f"Error occurred while installing module [{module_name}]. Error Code [PheonixAppAPI.apis.PACI.InstallPheonixModule.check3]\nError Message -> [The module doesn't exist or is not a part of PheonixStudios/ModuleRegistry]")

    # try1
    try:
        if not log:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", f"{module_name}{module_version}", "-q"])
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", f"{module_name}{module_version}", "--verbose"])
    except Exception as e:
        raise ErrorOccuredWhileInstallingModule(f"Error occurred while installing module [{module_name}]. Error Code [PheonixAppAPI.apis.PACI.InstallPheonixModule.try1]\nError Message -> [{e}]")