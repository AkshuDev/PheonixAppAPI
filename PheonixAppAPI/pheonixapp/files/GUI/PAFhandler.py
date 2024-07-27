#    _____              .___       __________            _____   __           .__          ___.   .__
#   /     \ _____     __| _/____   \______   \___.__.   /  _  \ |  | __  _____|  |__   ____\_ |__ |  |__ ___.__._____
#  /  \ /  \\__  \   / __ |/ __ \   |    |  _<   |  |  /  /_\  \|  |/ / /  ___/  |  \ /  _ \| __ \|  |  <   |  |\__  \
# /    Y    \/ __ \_/ /_/ \  ___/   |    |   \\___  | /    |    \    <  \___ \|   Y  (  <_> ) \_\ \   Y  \___  | / __ \_
# \____|__  (____  /\____ |\___  >  |______  // ____| \____|__  /__|_ \/____  >___|  /\____/|___  /___|  / ____|(____  /
#         \/     \/      \/    \/          \/ \/              \/     \/     \/     \/           \/     \/\/          \/
#     ___ ___________                      .___             ___
#    /  / \_   _____/___  __ __  ____    __| _/___________  \  \
#   /  /   |    __)/  _ \|  |  \/    \  / __ |/ __ \_  __ \  \  \
#  (  (    |     \(  <_> )  |  /   |  \/ /_/ \  ___/|  | \/   )  )
#   \  \   \___  / \____/|____/|___|  /\____ |\___  >__|     /  /
#    \__\      \/                   \/      \/    \/        /__/






# __________.__                        .__           _________ __            .___.__
# \______   \  |__   ____  ____   ____ |__|__  ___  /   _____//  |_ __ __  __| _/|__| ____  ______
#  |     ___/  |  \_/ __ \/  _ \ /    \|  \  \/  /  \_____  \\   __\  |  \/ __ | |  |/  _ \/  ___/
#  |    |   |   Y  \  ___(  <_> )   |  \  |>    <   /        \|  | |  |  / /_/ | |  (  <_> )___ \
#  |____|   |___|  /\___  >____/|___|  /__/__/\_ \ /_______  /|__| |____/\____ | |__|\____/____  >
#                \/     \/           \/         \/         \/                 \/               \/

import os
import sys
import time

mainDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
guiDir = os.path.join(mainDir, "GUI")

from PheonixAppAPI.pheonixapp.files import LIB
from PheonixAppAPI.pheonixapp.files import HashDecoderT

from configparser import ConfigParser

config = ConfigParser()

if __name__ == "__main__":
    os.chdir(mainDir)
    sys.path.append(os.getcwd())

class PAFhandler():
    def __init__(self, function:str="post", details:dict={}, useFile:bool=True, sectionAdd:str="", sectionGet:str="", option:str=""):
        self.function = function
        self.details = details
        self.useFile = useFile
        self.sectionAdd = sectionAdd
        self.sectionGet = sectionGet
        self.option = option

    def run(self):
        if self.function == "get":
            return self.get()
        elif self.function == "post":
            self.create()
        else:
            print("No Such Function. [PAEpafhR001]")
            exit(1)

    def create(self):
        config.clear()

        if os.path.exists("./gui.paf"):
            with open("./gui.paf", "r") as paf:
                config.read_file(paf)

        if self.sectionAdd != "":
            config.add_section(self.sectionAdd)

        for key, val in self.details.items():
            config.set(self.sectionAdd, key, val)

        with open("./gui.paf", "w") as paf:
            config.write(paf)

    def get(self) -> str:
        config.clear()

        if not os.path.exists("./gui.paf"):
            self.create()
            return ""

        config.clear()

        with open("./gui.paf", "r") as paf:
            config.read_file(paf)

        return config.get(self.sectionGet, self.option)

class PAFHandler_API():
    def __init__(self, file_path:str, function:str="post", details:dict={}, useFile:bool=True, sectionAdd:str="", sectionGet:str="", option:str=""):
        self.file_path = file_path
        self.function = function
        self.details = details
        self.useFile = useFile
        self.sectionAdd = sectionAdd
        self.sectionGet = sectionGet
        self.option = option

    def run(self):
        if self.function == "get":
            return self.get()
        elif self.function == "post":
            self.create()
        else:
            print("No Such Function. [PAEpafhR001]")
            exit(1)

    def create(self):
        config.clear()

        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as paf:
                config.read_file(paf)

        if self.sectionAdd != "":
            config.add_section(self.sectionAdd)

        for key, val in self.details.items():
            config.set(self.sectionAdd, key, val)

        with open(self.file_path, "w") as paf:
            config.write(paf)

    def get(self) -> str:
        config.clear()

        if not os.path.exists(self.file_path):
            self.create()
            return ""

        config.clear()

        with open(self.file_path, "r") as paf:
            config.read_file(paf)

        return config.get(self.sectionGet, self.option)