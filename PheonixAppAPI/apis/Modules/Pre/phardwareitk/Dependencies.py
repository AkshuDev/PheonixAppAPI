from typing import *

import os

class Requirements:
    @staticmethod
    def Modules(mode:Union[str, None, list]=None) -> Union[str, list, None]:
        """
        Args:
            mode (Union[str, None, list]): This argument allows the program to understand the specified mode. modes ->
                str: Returns the string representation of the required modules seperated via ' '.
                list: Returns the list representation of the required modules.
                None: Downloads the required modules.

        Returns:
            Union[str, list, None]: Returned Type will be the mode type.
        """
        download:bool = False
        list_:bool = False
        
        if mode == None:
            download = True
        else:
            download = False
        
        if isinstance(mode, str):
            list_ = False
        else:
            list_ = True

        required_modules = "cryptography psutil keyboard cython PyOpenGL pysdl2%pysdl2-dll"
        logPLUSstr = "Modules That are optional for downloading ->\n1. PheonixAppAPI: Great Module and Provides almost all functionality required for a devloper to move on. From playing games to working with Files.\nDetails ->\n\tSpace: MAX 50mb for the module + 6 GB for building PyQt5 [Microsoft C++ Build Tools 14 or higher] (you can skip the 6 GB by downloading a premade PyQt5 whl file online)."
        required_modules_list = []
        optional_required_compiling = "Please, to use GUI/HGame (Screen_X and Draw_X class) compile the renderGUI.pyx file using gcc (Microsoft Build tools/Mingw64)."

        if required_modules == "":
            print("No required modules.\n"+logPLUSstr+f"\n{optional_required_compiling}")
            return None

        if not " " in required_modules:
            required_modules_list.append(required_modules)
        else:
            required_modules_list = required_modules.split(" ")

        if download:
            for i, v in enumerate(required_modules_list):
                if "%" in v:
                    v = v.split("%")

                v_:str = v
                
                for k, j in enumerate(v):
                    v_ += j
                
                v = v_

                os.system(f"pip install {v}")

            print(logPLUSstr+"\n"+optional_required_compiling)

            return None
        
        if list_:
            return required_modules_list
        else:
            return required_modules
        
if __name__ == "__main__":
    opr:str = input("Usage (modules): ")
    opr = opr.lower()

    if opr == "modules":
        Requirements.Modules(None)
    else:
        print("Unknown Usage -> [" + opr + "]")