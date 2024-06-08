import os
import sys

from PheonixAppAPI.pheonixapp.files import (PSSbridge)

PATF = None

def set_parent(parent:object) -> None:
    global PATF

    PATF = parent

class GUI():
    def __init__(self) -> None:
        pass

    def start(self) -> None:
        PATF.run("gui start")

class MiniGames():
    def __init__(self) -> None:
        pass

    def GuessTheNumber(self) -> None:
        PATF.run("fun !minigame guessthenumber")

class PATF_API():
    def __init__(self, useFileData:bool=False, email:str="", username:str="", password:str="") -> None:
        self.useFileData = useFileData
        self.email = email
        self.username = username
        self.password = password
        self.patf = PATF

    def run(self, cmd:str="terminal --createfile") -> None:
        self.patf.run(cmd)

    def CheckModules(self, mode:str="all", list:list=[], module:str="") -> None:
        self.patf.CheckModules(mode, list, module)

    def createfile(self, flag:str=""):
        self.patf.createfile(flag)

    def getCertificatePath(self, code:str="", flag:str="+BOOL"):
        return self.patf.getCertificatePath(code, flag)