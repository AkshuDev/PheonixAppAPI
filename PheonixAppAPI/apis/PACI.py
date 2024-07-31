import subprocess
import os
import sys

from PheonixAppAPI.apis.Modules.Pre.PheonixJson import Json

mainDir = os.path.dirname(os.path.abspath(__file__))
settingsJsonFile = os.path.join(mainDir, "settings.json")

SettingsJsonFileManager = Json.JsonFileManager(settingsJsonFile)

settings:dict = SettingsJsonFileManager.JsonToDict()

moduleReg = settings["ModuleRegistry"]

def MakeAccessFile(module_name:str) -> None:
    """Makes an Access File for the module.

    Args:
        module_name (str): The name of the module
    """

def InstallPheonixModule(module_name:str, log:bool=False) -> None:
    """This function allows to install a Pheonix Studios Python Module (ex -> pcd_py (Pheonix Clipped Dictionaries Python))

    Args:
        module_name (str): The name of the module needed to be installed.
        log (bool, optional): Whether to log the installation. Defaults to False.
    """
    #check1
    if module_name in moduleReg["PheonixStudios"]["Names"]:
        #check2
        if module_name in moduleReg["PheonixStudios"]["Modules"][module_name]["Installed"].lower() == "false":
            print(f"Error occurred while installing module [{module_name}]. Error Code [PheonixAppAPI.apis.PACI.InstallPheonixModule.check2]\nError Message -> [The module is not yet published]")
            exit(1)
    #check3
    else:
        print(f"Error occurred while installing module [{module_name}]. Error Code [PheonixAppAPI.apis.PACI.InstallPheonixModule.check3]\nError Message -> [The module doesn't exist or is not a part of PheonixStudios/ModuleRegistry]")
        exit(1)

    # try1
    try:
        if not log:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", module_name, "-q"])
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", module_name, "--verbose"])
    except Exception as e:
        print(f"Error occurred while installing module [{module_name}]. Error Code [PheonixAppAPI.apis.PACI.InstallPheonixModule.try1]\nError Message -> [{e}]")
        exit(1)
