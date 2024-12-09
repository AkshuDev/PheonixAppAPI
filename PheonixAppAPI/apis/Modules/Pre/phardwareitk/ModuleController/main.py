import os
import sys

from typing import *

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

from phardwareitk import LIB

class CompilerOptions:
    """NOTE: Encryption is only supported in PHITKfile format."""
    def __init__(self, format_:str="COMPILER_pheonix$phardwareitk$v0001", output_format_:str="PHITKfile", encrypt:bool=True) -> None:
        """NOTE: Encryption is only supported in PHITKfile format."""
        self.format_:str = format_
        self.formatCompiler:str = format_.split("$")[0]
        self.formatModule:str = format_.split("$")[1]
        self.formatVersion:str = format_.split("$")[2]
        self.formatsCompilersAvail:list = ["COMPILER_pheonix"]
        self.formatsModulesAvail:list = ["phardwareitk"]
        self.formatsVersionsAvail:list = ["v0001", "v0002"]
        self.output_format_:str = output_format_
        self.encrypt:bool = encrypt

        if output_format_ == "PHITKfile":
            pass
        else:
            self.encrypt = False
            encrypt = False

class Compiler:
    """Main Module Handler Compiler for phardwareitk"""
    def __init__(self, path:str=LIB.Paths.defrunSettingsNOEXT, compilerOptions:CompilerOptions=CompilerOptions()) -> None:
        self.path:str = path + "." + compilerOptions.output_format_
        self.compilerOptions:CompilerOptions = compilerOptions
        self.content:str = ""
        self.sections:dict = {"_MAIN_": {}}
        self.clearedSections:dict = {"_MAIN_": {}}

        if not compilerOptions.formatCompiler in compilerOptions.formatsCompilersAvail:
            raise ValueError("In compilerOptions, Compiler Format is currently not supported or is not available. [Compiler.mainPY_ModuleController_phardwareitk.1]")
        
        if not compilerOptions.formatModule in compilerOptions.formatsModulesAvail:
            raise ValueError("In compilerOptions, Module Format is currently not supported or is not available. [Compiler.mainPY_ModuleController_phardwareitk.2]")
        
        if not compilerOptions.formatVersion in compilerOptions.formatsVersionsAvail:
            raise ValueError("In compilerOptions, Version Format is currently not supported or is not available. [Compiler.mainPY_ModuleController_phardwareitk.3]")

    def encrypt(self, data:str) -> bytes:
        import base64
        data = data.encode("utf-8")
        return base64.b64encode(data)
    
    def decrypt(self, data:bytes) -> str:
        import base64
        return base64.b64decode(data).decode("utf-8")

    def get(self, name:str, section:Union[None, str]=None) -> str:
        if section == None:
            return self.sections["_MAIN_"][name]
        else:
            return self.sections[section][name]

    def set(self, name:str, value:Union[int, str, dict], section:Union[None, str]=None) -> None:
        value = str(value)

        if section == None:
            self.sections["_MAIN_"][name] = value
        else:
            self.sections[section][name] = value

        return None 

    def makeSection(self, section:str) -> None:
        self.sections[section] = {}
        return None
    
    def decompile_v0001(self) -> dict:
        for i, v in enumerate(self.content.splitlines()):
            if v.startswith("$^S") and v.endswith("$^S"):
                self.sections[v.replace("$^S", "")] = {}

                for k, j in enumerate(self.content.splitlines()):
                    if k <= i:
                        continue

                    if " -> " in j:
                        name, value = j.split(" -> ")
                        self.sections[v.replace("$^S", "")][name] = value
            else:
                continue

        return self.sections

    def decompile_v0002(self) -> dict:
        for i, v in enumerate(self.content.splitlines()):
            if v.startswith("#%#") and v.endswith("#%#"):
                self.sections[v.replace("#%#", "")] = {}

                indexed_line = self.content.splitlines()[i + 1]
                Sindexed_line = indexed_line.split("@$@^^&^^@$@ ")

                for k, j in enumerate(Sindexed_line):
                    if " *=>>* " in j:
                        name, value = j.split(" *=>>* ")
                        self.sections[v.replace("#%#", "")][name] = value
            else:
                continue

        return self.sections

    def load(self) -> None:
        self.getFromFile()

        if self.compilerOptions.formatVersion == "v0001":
            self.decompile_v0001()
        elif self.compilerOptions.formatVersion == "v0002":
            self.decompile_v0002()
        
    def getFromFile(self) -> str:
        data:str = ""

        if self.compilerOptions.encrypt:
            with open(self.path, 'rb') as f:
                f.seek(0)
                data = self.decrypt(f.read())
                f.close()
        else:
            with open(self.path, 'r') as f:
                f.seek(0)
                data = f.read()
                f.close()

        self.content = data
        return self.content
    
    def Clear(self) -> None:
        self.sections = self.clearedSections
        self.content = ""
        return None
    
    def finalize_v0001(self) -> None:
        for i, v in enumerate(self.sections.keys()):
            if i != 0:
                self.content += "\n"
            self.content += "$^S" + v + "$^S\n"
            for k, j in enumerate(self.sections[v].keys()):
                self.content += j + " -> " + self.sections[v][j] + "\n"

    def finalize_v0002(self) -> None:
        for i, v in enumerate(self.sections.keys()):
            if i != 0:
                self.content += "\n"
            self.content += "#%#" + v + "#%#\n"
            for k, j in enumerate(self.sections[v].keys()):
                self.content += j + " *=>>* " + self.sections[v][j] + "@$@^^&^^@$@ "

    def finalize(self) -> None:
        if self.compilerOptions.formatVersion == "v0001":
            self.finalize_v0001()
        elif self.compilerOptions.formatVersion == "v0002":
            self.finalize_v0002()

    def saveToFile(self, clearAfterSave:bool=True) -> None:
        self.finalize()

        if self.compilerOptions.encrypt:
            self.content = self.encrypt(self.content)

            with open(self.path, "wb") as f:
                f.write(self.content)
                f.close()
        else:
            with open(self.path, "w") as f:
                f.write(self.content)
                f.close()

        if clearAfterSave:
            self.Clear()

        return None
    
class PHardwareITK:
    @staticmethod
    def check_file(filename:str=LIB.Paths.defrunSettingsNOEXT) -> bool:
        pass