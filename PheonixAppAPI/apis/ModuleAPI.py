import os
import sys
from importlib import util
from PheonixAppAPI.pheonixapp.files import LIB

def CheckModules(prompt:bool=True, mode:str="list", module:str="PheonixAppAPI", module_list:list=["PheonixAppAPI"], log:bool=False) -> tuple[list, bool]:
    """Checks the specified modules. Script Version.

        Args:
            prompt(bool, optional): This defines shall the script prompt the user for downloading the modules. If it is false it doesn't download modules. Default to False.
            mode (str, optional): The mode for checking modules. Default to 'list':
            Available Modes are ->
                1. 'all' This mode checks for all PheonixApp required Modules.
                2. 'list' This mode checks for the specified list.
                3. 'module' This mode checks for a specified module.

            module (str, optional): The specific module to check. Defaults to 'PheonixAppAPI'.
            module_list (list, optional): The list of modules to check. Defaults to ['PheonixAppAPI'].
            log (bool, optional): If prompt is active log wil give info about the download. Defaults to False.

        Returns:
            tuple[list, bool]: The tuple's first part is the uninstalled modules from the provided list [module_list]. The second part is True if the module/all modules from the provided list [module_list]  are installed, else False.
    """

    not_installed = []

    if mode.lower() == "module":
        module_list_ = [module]
    elif mode.lower() == "list":
        module_list_ = module_list
    elif mode.lower() == "all":
        module_list_ = LIB.PSS.nonDEF_modules
    else:
        raise ValueError("Invalid [mode]. [PheonixAppAPI.apis.ModuleAPI.CheckModules]")

    for i, v in enumerate(module_list_):
        spec = util.find_spec(v)

        if spec == None:
            not_installed.append(v)

    if prompt:
        prompt_ = input(f"Do you want to install these modules? -> [{not_installed}] <- (Yes/No/Y/N): ").lower()
        if prompt_ == "yes" or prompt_ == "y":
            try:
                print("Installing Modules..")
                DownloadModules(prompt=False, mode="list", module_list=not_installed, log=log)
            except Exception:
                return not_installed, False
        else:
            print("Operation Cancelled by User.")
            return not_installed, False
    else:
        return not_installed, True

def DownloadModules(prompt:bool=False, mode:str="list", module="PheonixAppAPI", module_list=["PheonixAppAPI"], log:bool=False, upgraded_module:bool=True) -> tuple[list, bool]:
    """Downloads the specified modules. Script Version.

        Args:
            prompt(bool, optional): This defines shall the script prompt the user for downloading the modules. If it is false it doesn't ask the user for permission to download modules. Default to False.
            mode (str, optional): The mode for downloading modules. Default to 'list':
            Available Modes are ->
                1. 'all' This mode downloads for all PheonixApp required Modules.
                2. 'list' This mode downloads for the specified list.
                3. 'module' This mode downloads for a specified module.

            module (str, optional): The specific module to download. To install a specific version add [==] after the name and specify the version after the sign, keep no spaces. Defaults to 'PheonixAppAPI'.
            module_list (list, optional): The list of modules to download. To install a specific version add [==] after the name and specify the version after the sign, keep no spaces, do it for all the modules in the list that you want to have a specific version. Defaults to ['PheonixAppAPI'].
            log (bool, optional): If set to True this wil give info about the download, otherwise it will not. Defaults to False.
            upgraded_module (bool, optional): If set to True it will download the latest version of the module. Defaults to True.

        Returns:
            tuple[list, bool]: The tuple's first part is the uninstalled modules from the provided list [module_list]. The second part is True if the module/all modules from the provided list [module_list]  are successfully installed, else False.
    """

    if mode.lower() == "module":
        module_list_ = [module]
    elif mode.lower() == "list":
        module_list_ = module_list
    elif mode.lower() == "all":
        module_list_ = LIB.PSS.nonDEF_modules
    else:
        raise ValueError("Invalid [mode]. [PheonixAppAPI.apis.ModuleAPI.CheckModules]")

    not_installed = []

    try:
        for i, v in enumerate(module_list_):
            if upgraded_module:
                if log:
                    os.system(f"{sys.executable} -m pip install --upgrade {v} --verbose")
                else:
                    os.system(f"{sys.executable} -m pip install --upgrade {v} -q")
            else:
                if log:
                    os.system(f"{sys.executable} -m pip install {v} --verbose")
                else:
                    os.system(f"{sys.executable} -m pip install {v} -q")

            not_installed.pop(v)
    except Exception:
        return not_installed, False

    return not_installed, True