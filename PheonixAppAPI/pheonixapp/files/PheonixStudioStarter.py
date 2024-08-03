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
import shutil
from PheonixAppAPI.pheonixapp.files import LIB
import time
import pathlib
from datetime import datetime
import pickle
import importlib.util as ILIBUtil
from PheonixAppAPI.pheonixapp.files import HashDecoderT
import binascii
import random
from PheonixAppAPI.pheonixapp.files import Utilities
from PheonixAppAPI.pheonixapp.files import Terminal

mainDir = ""
settingsFile = ""
PATFfile = ""
TempFILE = ""

try:
    mainDir = os.path.dirname(os.path.abspath(__file__))
    settingsFile = os.path.join(mainDir, "settings.ini")
    PATFfile = os.path.join(mainDir, "PATFsettings")
    TempFILE = os.path.join(mainDir, "TempFile.ini")
except NameError:
    # Fallback if __file__ is not defined (e.g., in Jupyter)
    mainDir = os.getcwd()
    settingsFile = os.path.join(mainDir, "settings.ini")
    PATFfile = os.path.join(mainDir, "PATF.patf")
    TempFILE = os.path.join(mainDir, "TempFile.ini")

if __name__ == "__main__":
    os.chdir(mainDir)
    sys.path.append(os.getcwd())

class Error():
    def __init__(self, type_:BaseException, name:str, details:str, log:bool=False, mode:str="") -> None:
        currentdetails = datetime.now()
        if mode == "":
            if log:
                raise type_(f"LOG:[{currentdetails}]\t{name}->\n{details}")
            else:
                raise type_(f"{name}->\n{details}")
        elif mode.upper() == "DECL":
            if log:
                print(f"LOG:[{currentdetails}]\t{name}->\n{details}")
                return None
            else:
                print(f"{name}->\n{details}")
                return None
        else:
            if log:
                raise type_(f"LOG:[{currentdetails}]\tWrong Mode->\n[{mode}] is not a part of Error Class Modes Available Modes are -> [None:DEFAULT, DECL]")
            else:
                raise type_(f"Wrong Mode->\n[{mode}] is not a part of Error Class Modes Available Modes are -> [None:DEFAULT, DECL]")

class CheckModules():
    def __init__(self, mode:str="all", list_:list = [], module:str="") -> None:
        self.settingsFile = os.path.join(mainDir, "settings.ini")
        notinstalled = []
        if os.path.exists(settingsFile):
            Gtl, Ni, ho = self.GTL()
            if Gtl:
                return None
            else:
                self.createMINI("all")
                self.installModules(Ni)
        else:
            self.createMINI("all")
        try:
            if mode.lower() == "all":
                for i, v in enumerate(LIB.PSS.modules):
                    spec = ILIBUtil.find_spec(v)
                    if spec == None:
                        notinstalled.append(v)
            elif mode.lower() == "list":
                for i, v in enumerate(list_):
                    spec = ILIBUtil.find_spec(v)
                    if spec == None:
                        notinstalled.append(v)
            elif mode.lower() == "module":
                spec = ILIBUtil.find_spec(module)
                if spec == None:
                    notinstalled.append(module)
            else:
                Error(AttributeError, "['mode'] unidentified", f"The ['mode'] attribute of class ['CheckModules'] in file ['PheonixStudioStarter.py'] is not a available ['mode']. The available ['mode'] are {LIB.PSS.modes_CM}", True)
        except:
            Error(Exception, "Trial Error", "Try Failed for Checking Modules.", True)

        try:
            if notinstalled != []:
                if input(f"Do you want to install these modules {notinstalled} (Y/N): ").lower() == "y":
                    self.installModules(notinstalled)
                    self.createMINI("all", notinstalled)
                else:
                    print("\n\nAll Modules are required to run PheonixApp\n\nExiting...")
                    exit(1)
            else:
                self.createMINI("all")
        except Exception as e:
            Error(Exception, "Trial Error", f"Try Failed for Checking Modules. -> {e}", True)

    def GTL(self):
        ni = []
        in_ = []
        nh = []

        from configparser import ConfigParser
        config = ConfigParser()

        with open(settingsFile, "r") as sfile:
            config.read_file(sfile)

        try:
            for i, v in enumerate(LIB.PSS.modules):
                spec = ILIBUtil.find_spec(v)
                if spec == None:
                    ni.append(v)
        except Exception:
            Error(Exception, "Something Went Wrong", "Something Went Wrong while checking modules [PSEC:CMsww0001]")

        try:
            for i, v in enumerate(LIB.PSS.modules):
                Ho = config.has_option("Modules", v)
                if Ho:
                    v = config.get("Modules", v)
                    if v == "installed":
                        in_.append(v)
                    else:
                        nh.append(v)
                else:
                    nh.append(v)
        except Exception:
            Error(Exception, "Something Went Wrong", "Something Went Wrong while checking modules [PSEC:CMsww0002]")

        if len(in_) == len(LIB.PSS.modules):
            if not config.has_section("PATF"):
                return False, ni, nh
            return True, ni, nh
        else:
            return False, ni, nh

    def installModules(self, notinstalled:list):
        if notinstalled == []:
            Error(Exception, "Modules Installed Successfully", "All Modules Required to run PheonixApp are now Installed Successfully. Please Restart the Script.")

        try:
            for i, v in enumerate(notinstalled):
                try:
                    os.system(f"pip install {v}")
                except:
                    Error(Exception, "PIP Error", "There is a issue running the pip command, Please make sure you have pip set as a Environment Variable", True)
        except:
            Error(Exception, "Trial Error", "Try Failed for Installing Modules.", True)

    def createMINI(self, mode:str="all", list_:list=[], module:str=""):
        from configparser import ConfigParser
        config = ConfigParser()

        with open(self.settingsFile, "w") as sfile:
            sfile.close()

        with open(self.settingsFile, "r") as sfile:
            config.read_file(sfile)

        try:
            if mode.lower() == "all":
                if not config.has_section("Modules"):
                    config.add_section("Modules")
                for i, v in enumerate(LIB.PSS.modules):
                    config.set("Modules", v, "installed")

                if config.has_section("PATF"):
                    config.remove_section("PATF")

                config.add_section("PATF")
                config.set("PATF", "extention", "patf")
                config.set("PATF", "devtools", "disabled")
                config.set("PATF", "release", "false")

            elif mode.lower() == "list":
                if not config.has_section("Modules"):
                    config.add_section("Modules")
                for i, v in enumerate(list_):
                    config.set("Modules", v, "installed")
            elif mode.lower() == "module":
                if not config.has_section("Modules"):
                    config.add_section("Modules")
                config.set("Modules", module, "installed")
            else:
                Error(AttributeError, "['mode'] unidentified", f"The ['mode'] attribute of class ['CheckModules'] in file ['PheonixStudioStarter.py'] is not a available ['mode']. The available ['mode'] are {LIB.PSS.modes_CM}", True)
        except:
            Error(Exception, "Trial Error", "Try Failed for Creating INI.", True)

        try:
            with open(settingsFile, "w") as configfile:
                config.write(configfile)
        except:
            Error(Exception, "Trial Error", "Try Failed for Creating INI.", True)

class SettingsHandler():
    def __init__(self) -> None:
        self.settingsFile = os.path.join(mainDir, "settings.ini")

        if not self.checkSFile():
            CheckModules()

    def checkSFile(self):
        return os.path.exists(self.settingsFile)

    def deletefile(self):
        if not self.checkSFile():
            Error(Exception, "File Already Deleted", "Settings File is already deleted, PheonixApp Requires this file to work. Quitting...")
        else:
            os.remove(self.settingsFile)
            print("Settings File is deleted, PheonixApp Requires this file to work. Quitting...")
            exit(0)

    def getfile(self, getcmd:str):
        try:
            if getcmd.lower() == "patfsettings_ext":
                if not self.checkSFile():
                    Error(FileNotFoundError, "File is not found", "Settings File is not found, PheonixApp Requires this file to work. Quitting...")

                from configparser import ConfigParser

                config = ConfigParser()

                with open(self.settingsFile, "r") as sfile:
                    config.read_file(sfile)

                return config.get("PATF", "extention")
            elif getcmd.lower() == "alldata":
                if not self.checkSFile():
                    Error(FileNotFoundError, "File is not found", "Settings File is not found, PheonixApp Requires this file to work. Quitting...")

                data = ""

                with open(self.settingsFile, "r") as sfile:
                    data = sfile.read()

                return data
        except Exception:
            return None

    def run(self, cmd:str="--createfile"):
        if cmd.lower() == "--createfile":
            CheckModules()
        elif cmd.lower() == "--deletefile":
            self.deletefile()
        elif "--getfile" in cmd.lower():
            maincmds = cmd.split(":")
            getcmd = maincmds[1]
            return self.getfile(getcmd)

class CLcmds():
    def __init__(self, type_:str="T", devMCmd:str="", *args) -> None:
        self.type_ = type_
        self.devMCmd = devMCmd

        self.pss = LIB.PSS

        if type_.lower() == "t":
            self.terminalRun()

    def get(self, file:str, section:str="", option:str="", value_con:str=""):
        from configparser import ConfigParser
        config = ConfigParser()

        if file.lower() == "settings":
            if os.path.exists(settingsFile):
                with open(settingsFile, "r") as sfile:
                    config.read_file(sfile)
            else:
                Error(FileNotFoundError, "File was not found", "Settings file was not found. Quitting...")

        output = config.get(section, option)

        if value_con != "":
            SVC = value_con.split("@")

            try:
                condition = SVC[1]
                giw = False
                gw = ""
                gws = []

                for char in value_con:
                    if giw and char == "@" or char == ":":
                        gws.append(gw)
                        gw = ""

                    if giw and char == ";":
                        gws.append(gw)
                        gw = ""

                    if giw:
                        gw += char

                    if char == "@":
                        value = SVC[0]

                        gws.append("@")
                        giw = True

                    if char == ":":
                        gws.append(":")
                        giw = True

                value = SVC[0]
                ifVal = False
                elseVal = False

                for i, v in enumerate(gws):
                    if v == "@":
                        NVal = gws[i+1]
                        if NVal == "true":
                            ifVal = "true"
                        else:
                            ifVal = "false"
                    if v == ":":
                        NVal = gws[i+1]
                        if NVal == "true":
                            elseVal = "true"
                        else:
                            elseVal = "false"

                        if NVal == "pass":
                            elseVal = output

                if output == ifVal:
                    pass
                else:
                    value = elseVal

                if file.lower() == "settings":
                    if os.path.exists(settingsFile):
                        with open(settingsFile, "w") as sfile:
                            config.set(section, option, value)
                            config.write(sfile)
                    else:
                        Error(FileNotFoundError, "File was not found", "Settings file was not found. Quitting...")

            except Exception:
                value = SVC[0].lower()

                if file.lower() == "settings":
                    if os.path.exists(settingsFile):
                        with open(settingsFile, "w") as sfile:
                            config.set(section, option, value)
                            config.write(sfile)
                    else:
                        Error(FileNotFoundError, "File was not found", "Settings file was not found. Quitting...")

    def terminalRun(self):
        if self.devMCmd in self.pss.clcmdsT:
            if self.devMCmd.lower() == "release":
                self.get("settings", "PATF", "release", "true@false:false;")
        else:
            Error(Exception, "Wrong Command", "Sorry Either you have written a command not present inside the PACD(Pheonix App Command Dictionary) or either you have used a wrong Command Interpreter -> Available are ['terminal', 'gui'].", True, "DECL")

class PATFHandler():
    def __init__(self, usefileData:bool=False, email:str="", username:str="", password:str="") -> None:
        self.configdata = ""
        self.format_file = "patf"
        self.pss = LIB.PSS

        from configparser import ConfigParser
        config = ConfigParser()

        self.isCertificate = False
        self.certificateP = " "

        if usefileData == True:
            if self.find_file("extention") == "patf":
                with open(PATFfile+"PATFsettings.patf", "rb") as PSettings:
                    self.configdata = pickle.load(PSettings)
                    self.format_file = "patf"

                config.read_string(self.configdata)
            elif self.find_file("extention") == "ini":
                with open(PATFfile+".ini", "r") as PSettings:
                    config.read_file(PSettings)
                    self.format_file = "ini"
            elif self.find_file("extention") == "txt":
                with open(PATFfile+".txt", "r") as PSettings:
                    config.read_file(PSettings)
                    self.format_file = "txt"

            self.certificateP = HashDecoderT.Decode(config.get("User", "certificatep"), "Hype_Space").run()

            email = HashDecoderT.Decode(config.get("User", "Email"), "Hype_Space").run()
            self.runmodes = config.get("User", "RunModes")

            username = HashDecoderT.Decode(config.get("User", "Username"), "Hype_Space").run()
            password = HashDecoderT.Decode(config.get("User", "Password"), "Hype_Space").run()

        if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.ini")):
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.ini"), "r") as sfile:
                config.read_file(sfile)

            self.devtools = config.get("PATF", "devtools")
            if self.devtools == "enabled":
                self.devtools = True
            else:
                self.devtools = False

            self.release = config.get("PATF", "release")

            self.email = email

            self.username = username
            self.password = password

            if self.certificateP == " ":
                self.isCertificate = False
            else:
                self.isCertificate = True
        else:
            SettingsHandler().run("--createfile")
            print("Dependencies are installed.")
            exit(0)

    def find_file(self, mode:str="fullname"):
        if mode == "fullname":
            for i,v in enumerate(self.pss.attribs_cft):
                if os.path.exists(PATFfile+"."+v):
                    return PATFfile+"."+v
        if mode == "extention":
            for i,v in enumerate(self.pss.attribs_cft):
                if os.path.exists(PATFfile+"."+v):
                    return v

    def createfile(self, flag:str=""):
        from configparser import ConfigParser

        # data = {
        #     "[User]":{
        #         "RunModes": ["terminal", "gui"],
        #         "Name": self.email,
        #         "Username": f"{HashDecoderT.Encode(self.username, "Hype_Space", "Pheonix Studios")}",
        #         "Password": f"{HashDecoderT.Encode(self.password, "Hype_Space", "Pheonix Studios")}"
        #     }
        # }

        if flag != "devtools":
            config = ConfigParser()
            config.add_section("User")
            config.set("User", "RunModes", "[terminal, gui]")
            config.set("User", "certificatep", HashDecoderT.Encode(self.certificateP, "Hype_Space", "PheonixStudios").run())
            config.set("User", "Email", HashDecoderT.Encode(self.email, "Hype_Space", "PheonixStudios").run())
            config.set("User", "Username", HashDecoderT.Encode(self.username, "Hype_Space", "Pheonix Studios").run())
            config.set("User", "Password", HashDecoderT.Encode(self.password, "Hype_Space", "Pheonix Studios").run())

            data = ""

            if self.format_file.lower() == "patf":
                with open(TempFILE, "w") as Tempfile:
                    config.write(Tempfile)

                time.sleep(2)

                with open(TempFILE, "r") as TempfileR:
                    TempfileR.seek(0)
                    data = TempfileR.read()

                time.sleep(2)

                with open(PATFfile+".patf", "wb") as Psettings:
                    pickle.dump(data, Psettings)

                os.remove(TempFILE)

            elif self.format_file.lower() == "ini":
                with open(PATFfile+".ini", "w") as Psettings:
                    config.write(Psettings)

            elif self.format_file.lower() == "txt":
                with open(PATFfile+".txt", "w") as Psettings:
                    config.write(Psettings)
            else:
                Error(AttributeError, "PA-No Attribute Found", f"No Attribute Found For ['--createfile']. File Formats Accepted are {LIB.PSS.attribs_cft}")

        if not os.path.exists(settingsFile):
            Error(FileNotFoundError, "File is not found", "Settings File is not found, PheonixApp Requires this file to work. Quitting...")

        config2 = ConfigParser()
        with open(settingsFile, "r") as sfile:
            config2.read_file(sfile)
        if config2.has_section("PATF"):
            config2.remove_section("PATF")
            with open(settingsFile, "w") as sfile2:
                config2.write(sfile2)

        config3 = ConfigParser()
        config3.add_section("PATF")
        config3.set("PATF", "extention", self.format_file.lower())

        if self.devtools:
            config3.set("PATF", "devtools", "enabled")
        else:
            config3.set("PATF", "devtools", "disabled")

        config3.set("PATF", "release", "false")

        with open(settingsFile, "a+") as sfile3:
            config3.write(sfile3)

    def modifyfile(self):
        pass
    def deletefile(self, extention:str="", mode:str="find"):
        if mode == "find":
            for i, v in enumerate(self.pss.attribs_cft):
                if os.path.exists(PATFfile+"."+v):
                    os.remove(PATFfile+"."+v)
                    print("./PheonixApp needs the PATFsettings file, so BYE!!!")
                    exit(0)
            Error(FileExistsError, "File not Found", "PATFsettings File was not Found!")
        elif mode == "extention":
            avail_files = []
            for i, v in enumerate(self.pss.attribs_cft):
                if os.path.exists(PATFfile+"."+v) and not v == extention:
                    avail_files.append(v)

            if not avail_files == len(self.pss.attribs_cft) - 1:
                if os.path.exists(PATFfile+"."+extention):
                    os.remove(PATFfile+"."+extention)
                    print("./PheonixApp needs the PATFsettings file, so BYE!!!")
                    exit(0)
            else:
                if os.path.exists(PATFfile+"."+extention):
                    os.remove(PATFfile+"."+extention)
                    return None
        elif mode == "revert":
            if os.path.exists(PATFfile+"."+extention):
                pass

            for i,v in enumerate(self.pss.attribs_cft):
                if os.path.exists(PATFfile+"."+v) and v != extention:
                    os.remove(PATFfile+"."+v)

            return None
        Error(FileExistsError, "File not Found", "PATFsettings File was not Found!")
    def upgradefile(self):
        email = input("Please Enter your Pheonix Studios Email ->\n")
        username = input("Please Enter your Pheonix Studios Username ->\n").lower()
        password = input("Please Enter your Pheonix Studios Password ->\n").lower()

        from configparser import ConfigParser

        # data = {
        #     "[User]":{
        #         "RunModes": ["terminal", "gui"],
        #         "Name": self.email,
        #         "Username": f"{HashDecoderT.Encode(self.username, "Hype_Space", "Pheonix Studios")}",
        #         "Password": f"{HashDecoderT.Encode(self.password, "Hype_Space", "Pheonix Studios")}"
        #     }
        # }

        config = ConfigParser()
        config.add_section("User")
        config.set("User", "RunModes", "[terminal, gui]")
        config.set("User", "certificatep", HashDecoderT.Encode(self.certificateP, "Hype_Space", "PheonixStudios").run())
        config.set("User", "Email", HashDecoderT.Encode(email, "Hype_Space", "PheonixStudios").run())
        config.set("User", "Username", HashDecoderT.Encode(username, "Hype_Space", "Pheonix Studios").run())
        config.set("User", "Password", HashDecoderT.Encode(password, "Hype_Space", "Pheonix Studios").run())

        data = ""

        if self.format_file.lower() == "patf":
            with open(TempFILE, "w") as Tempfile:
                config.write(Tempfile)

            time.sleep(2)

            with open(TempFILE, "r") as TempfileR:
                TempfileR.seek(0)
                data = TempfileR.read()

            time.sleep(2)

            with open(PATFfile+".patf", "wb") as Psettings:
                pickle.dump(data, Psettings)

            os.remove(TempFILE)

        elif self.format_file.lower() == "ini":
            with open(PATFfile+".ini", "w") as Psettings:
                config.write(Psettings)

        elif self.format_file.lower() == "txt":
            with open(PATFfile+".txt", "w") as Psettings:
                config.write(Psettings)
        else:
            Error(AttributeError, "PA-No Attribute Found", f"No Attribute Found For ['--createfile']. File Formats Accepted are {LIB.PSS.attribs_cft}")
    def changeFileType(self, type_:str):
        if not type_:
            Error(AttributeError, "PA-No Attribute Found", "No Attribute Found For ['--changefiletype'].")
        elif not type_ in LIB.PSS.attribs_cft:
            Error(AttributeError, "PA-No Attribute Found", f"No Attribute Found For ['--changefiletype']. File Formats Accepted are {LIB.PSS.attribs_cft}")
        else:
            self.format_file = type_
            self.createfile()

    def getCertificatePath(self, code:str="", flag:str="+BOOL") -> str:
        if code == HashDecoderT.Encode(HashDecoderT.Encode(HashDecoderT.Encode("SPUltraPs9878762b4jb23jvhgv34g", "Hype_Space", "PheonixStudios"), "Hype_Space", "PheonixStudios"), "Hype_Space", "PheonixStudios"):
            if flag.lower() != "+bool":
                return self.certificateP, ""
            else:
                return self.certificateP, self.isCertificate
        else:
            return "", ""

    def run(self, mode:str="terminal --createfile"):
        try:
            command = False
            main = mode.split(" ")
            main2 = ''

            release = False

            if self.release == "true":
                release = True
                main2 = main[0].split(":")
            else:
                release = False
                main2 = main[1].split(":")

            if main[0] == "terminal":
                i = 0
                for j, v in enumerate(main):
                    if i != 0:
                        if main[j].lower() in self.pss.atribbs:
                            if main[j] == "--createfile":
                                command = True
                                self.createfile()
                            elif main[j] == "--modifyfile":
                                command = True
                                self.modifyfile()
                            elif main[j] == "--deletefile":
                                command = True
                                self.deletefile()
                            elif main[j] == "--upgradefile":
                                command = True
                                self.upgradefile()
                            elif main[j] == "!clear":
                                command = True
                                os.system("cls")
                            elif main[j] == "!color:DEFAULT":
                                command = True
                                os.system("color 07")
                            elif main[j] == "!minigame":
                                command = True
                                if main[2].lower() == "guessthenumber":
                                    minigames()
                            elif "!utilities" in main[j].lower():
                                command = True
                                if main2[1].lower() == "calc":
                                    Utilities.calculator()
                                elif main2[1].lower() == "wiki":
                                    Utilities.wikipediasearch()
                            elif main[j].lower() == "!certificate:s:path":
                                command = True
                                self.certificateP = main[j + 1]
                                self.createfile()
                        else:
                            command = True
                            Terminal.TCmds(mode).run()
                    i += 1

                if main2[0] == "--changefiletype":
                    command = True
                    if main2[1] in self.pss.attribs_cft:
                        pass
                    else:
                        Error(AttributeError, "PA-No Attribute Found", "No Attribute Found For ['--changefiletype'].")
                    self.changeFileType(main2[1])
                    self.deletefile(extention=main2[1], mode="revert")

                elif main2[0] == "!color" and not command:
                    command = True
                    os.system("color "+main2[1])

                elif main2[0] == '!devtools' and not command:
                    command = True

                    devT = main2[0]
                    devCmd = main2[1]
                    devMCmd = ""

                    if not devCmd.lower() == "enable" and not devCmd.lower() == "disable":
                        devMCmd = main2[2]

                    from configparser import ConfigParser
                    config = ConfigParser()

                    if os.path.exists(settingsFile):
                        with open(settingsFile, "r") as sfile:
                            config.read_file(sfile)

                    devT = config.get("PATF", "devtools")

                    if devCmd.lower() == "enable" or devCmd.lower() == "disable":
                        if devT == "enabled":
                            if devCmd.upper() == "DISABLE":
                                self.devtools = False
                                self.createfile("devtools")
                                print("DEVTOOLS: DISABLED\n\n")
                            elif devCmd.upper() == "ENABLE":
                                print("DEVTOOLS: ALREADY ENABLED\n\n")
                            else:
                                Error(Exception, "Wrong Command", "Sorry Either you have written a command not present inside the PACD(Pheonix App Command Dictionary) or either you have used a wrong Command Interpreter -> Available are ['terminal', 'gui'].[PSEdevtoolsE/D001]", True, "DECL")
                        else:
                            if devCmd.upper() == "ENABLE":
                                self.devtools = True
                                self.createfile("devtools")
                                print("DEVTOOLS: ENABLED\n\n")
                            elif devCmd.upper() == "DISABLE":
                                print("DEVTOOLS: ALREADY DISABLED\n\n")
                            else:
                                Error(Exception, "Wrong Command", "Sorry Either you have written a command not present inside the PACD(Pheonix App Command Dictionary) or either you have used a wrong Command Interpreter -> Available are ['terminal', 'gui'].[PSEdevtoolsE/D002]", True, "DECL")

                    if devCmd in self.pss.devtools_3S:
                        if devCmd.lower() == "cmds":
                            if devMCmd in self.pss.cmds_devtool:
                                if devMCmd.lower() == "all":
                                    print(f'\n{self.pss.desc_devtools.get("ENABLE")}\n{self.pss.desc_devtools.get("DISABLE")}\n{self.pss.desc_devtools.get("CMDS")}\n{self.pss.desc_devtools.get("CLcmds")}\n')
                                elif devMCmd.lower() == "enable":
                                    print(f'\n{self.pss.desc_devtools.get("ENABLE")}\n')
                                elif devMCmd.lower() == "disable":
                                    print(f'\n{self.pss.desc_devtools.get("DISABLE")}\n')
                                elif devMCmd.lower() == "cmds":
                                    print(f'\n{self.pss.desc_devtools.get("CMDS")}\n')
                                elif devMCmd.lower() == "clcmds":
                                    print(f'\n{self.pss.desc_devtools.get("CLcmds")}\n')

                        elif devCmd.lower() == "clcmds":
                            if devMCmd.lower() == "t":
                                devMCmd = main2[3]
                                CLcmds(devMCmd=devMCmd)
                                command = True

                if not command:
                    Error(Exception, "Wrong Command", "Sorry Either you have written a command not present inside the PACD(Pheonix App Command Dictionary) or either you have used a wrong Command Interpreter -> Available are ['terminal', 'gui'].[PSEdevtoolsE/D003]", True, "DECL")

            elif release and main[0] != "terminal" and not main[0] == "gui" and main[0] == "fun":
                    # if main[j] in self.pss.atribbs:
                        #     if main[j] == "!clear":
                            #         command = True
                            #         os.system("cls")
                            #     elif main[j] == "!color:DEFAULT":
                            #         command = True
                            #         os.system("color 07")
                if main2[0] == "!clear":
                    command = True
                    os.system("cls")
                elif main2[0] == "!color" and main2[1] == "DEFAULT":
                    command = True
                    os.system("color 07")

                if main2[0] == "!color" and not command:
                    command = True
                    os.system("color "+main2[1])

                if main[1] == "!minigame" and not command:
                    command = True
                    if main[2].lower() == "guessthenumber":
                        minigames()

                elif main2[0] == '!devtools' and not command:
                    command = True

                    devT = main2[0]
                    devCmd = main2[1]
                    devMCmd = ""

                    if not devCmd.lower() == "enable" and not devCmd.lower() == "disable":
                        devMCmd = main2[2]

                    from configparser import ConfigParser
                    config = ConfigParser()

                    if os.path.exists(settingsFile):
                        with open(settingsFile, "r") as sfile:
                            config.read_file(sfile)

                    devT = config.get("PATF", "devtools")

                    if devCmd.lower() == "enable" or devCmd.lower() == "disable":
                        if devT == "enabled":
                            if devCmd.upper() == "DISABLE":
                                self.devtools = False
                                self.createfile("devtools")
                                print("DEVTOOLS: DISABLED\n\n")
                            elif devCmd.upper() == "ENABLE":
                                print("DEVTOOLS: ALREADY ENABLED\n\n")
                            else:
                                Error(Exception, "Wrong Command", "Sorry Either you have written a command not present inside the PACD(Pheonix App Command Dictionary) or either you have used a wrong Command Interpreter -> Available are ['terminal', 'gui'].[PSEdevtoolsRE/D001]", True, "DECL")
                        else:
                            if devCmd.upper() == "ENABLE":
                                self.devtools = True
                                self.createfile("devtools")
                                print("DEVTOOLS: ENABLED\n\n")
                            elif devCmd.upper() == "DISABLE":
                                print("DEVTOOLS: ALREADY DISABLED\n\n")
                            else:
                                Error(Exception, "Wrong Command", "Sorry Either you have written a command not present inside the PACD(Pheonix App Command Dictionary) or either you have used a wrong Command Interpreter -> Available are ['terminal', 'gui'].[PSEdevtoolsRE/D002]", True, "DECL")

                    if devCmd in self.pss.devtools_3S:
                        if devCmd.lower() == "cmds":
                            if devMCmd in self.pss.cmds_devtool:
                                if devMCmd.lower() == "all":
                                    print(f'\n{self.pss.desc_devtools.get("ENABLE")}\n{self.pss.desc_devtools.get("DISABLE")}\n{self.pss.desc_devtools.get("CMDS")}\n{self.pss.desc_devtools.get("CLcmds")}\n')
                                elif devMCmd.lower() == "enable":
                                    print(f'\n{self.pss.desc_devtools.get("ENABLE")}\n')
                                elif devMCmd.lower() == "disable":
                                    print(f'\n{self.pss.desc_devtools.get("DISABLE")}\n')
                                elif devMCmd.lower() == "cmds":
                                    print(f'\n{self.pss.desc_devtools.get("CMDS")}\n')
                                elif devMCmd.lower() == "clcmds":
                                    print(f'\n{self.pss.desc_devtools.get("CLcmds")}\n')

                        elif devCmd.lower() == "clcmds":
                            if devMCmd.lower() == "t":
                                devMCmd = main2[3]
                                CLcmds(devMCmd=devMCmd)
                                command = True

                    else:
                        Error(Exception, "Wrong Command", "Sorry Either you have written a command not present inside the PACD(Pheonix App Command Dictionary) or either you have used a wrong Command Interpreter -> Available are ['terminal', 'gui'].[PSEdevtoolsRDNIPSS001]", True, "DECL")

            elif main[0] == "gui" and not command:
                if main[1] == "start":
                    os.system("python .\\GUI\\gui.py")

            elif main[0] == "fun" and not command:
                if main[1] == "!minigame" and not command:
                    command = True
                    if main[2].lower() == "guessthenumber":
                        minigames()

            elif not command:
                Error(Exception, "Wrong Command", "Sorry Either you have written a command not present inside the PACD(Pheonix App Command Dictionary) or either you have used a wrong Command Interpreter -> Available are ['terminal', 'gui'].[PSEnocmd001]", True, "DECL")

        except Exception:
            Error(Exception, "Wrong Command", "Sorry Either you have written a command not present inside the PACD(Pheonix App Command Dictionary) or either you have used a wrong Command Interpreter -> Available are ['terminal', 'gui'].", True, "DECL")

class minigames():
    def __init__(self, minigamenumber:int=1) -> None:
        self.minigamenumber = minigamenumber
        if self.minigamenumber == 1:
            self.guessnumber()
        else:
            Error(Exception, "Invalid Minigame", "Not a valid minigame number. Error code [PSEM00]")

        return None

    def guessnumber(self):
        choice = input("\n"+"Do you want to start the GuessNumber Minigame? (Y/N): ")

        if choice.lower() == 'y':
            difficulty = input("\n"+ "Please pick a difficulty! (Easy, Hard, Nightmare, Asian, Ultra Asian): ")
            if difficulty.lower() == "easy":
                np = random.randint(0 , 10)
                guess = input("\n"+ "Guess the number! (0-10): ")
                if guess == np:
                    print("You won!!!")
                    return None
                else:
                    guess = input("\n"+ "Wrong!\nGuess the number again! (0-10): ")
                    if guess == np:
                        print("You won!!!")
                        return None
                    else:
                        guess = input("\n"+ "Wrong!\nGuess the number again! (0-10): ")
                        if guess == np:
                            print("You won!!!")
                            return None
                        else:
                            print("\nYOU FAILED MISERABLE CHILD!")
                            print("\nThe correct answer was:", np)
                            return None
            elif difficulty.lower() == "hard":
                np = random.randint(0 , 50)
                guess = input("\n"+ "Guess the number! (0-50): ")
                if guess == np:
                    print("You won!!!")
                    return None
                else:
                    guess = input("\n"+ "Wrong!\nGuess the number again! (0-50): ")
                    if guess == np:
                        print("You won!!!")
                        return None
                    else:
                        guess = input("\n"+ "Wrong!\nGuess the number again! (0-50): ")
                        if guess == np:
                            print("You won!!!")
                            return None
                        else:
                            print("\nYOU FAILED MISERABLE CHILD!")
                            print("\nThe correct answer was:", np)
                            return None
            elif difficulty.lower() == "nightmare":
                np = random.randint(0 , 100)
                guess = input("\n"+ "Guess the number! (0-100): ")
                if guess == np:
                    print("You won!!!")
                    return None
                else:
                    guess = input("\n"+ "Wrong!\nGuess the number again! (0-100): ")
                    if guess == np:
                        print("You won!!!")
                        return None
                    else:
                        guess = input("\n"+ "Wrong!\nGuess the number again! (0-100): ")
                        if guess == np:
                            print("You won!!!")
                            return None
                        else:
                            print("\nYOU FAILED MISERABLE CHILD!")
                            print("\nThe correct answer was:", np)
                            return None
            elif difficulty.lower() == "asian":
                np = random.randint(0 , 1000)
                guess = input("\n"+ "Guess the number! (0-1000): ")
                if guess == np:
                    print("You won!!!")
                    return None
                else:
                    guess = input("\n"+ "Wrong!\nGuess the number again! (0-1000): ")
                    if guess == np:
                        print("You won!!!")
                        return None
                    else:
                        guess = input("\n"+ "Wrong!\nGuess the number again! (0-1000): ")
                        if guess == np:
                            print("You won!!!")
                            return None
                        else:
                            print("\nYOU FAILED MISERABLE CHILD!")
                            print("\nThe correct answer was:", np)
                            return None
            elif difficulty.lower() == "ultra asian":
                np = random.randint(0 , 10000)
                guess = input("\n"+ "Guess the number! (0-10000): ")
                if guess == np:
                    print("You won!!!")
                    return None
                else:
                    guess = input("\n"+ "Wrong!\nGuess the number again! (0-10000): ")
                    if guess == np:
                        print("You won!!!")
                        return None
                    else:
                        guess = input("\n"+ "Wrong!\nGuess the number again! (0-10000): ")
                        if guess == np:
                            print("You won!!!")
                            return None
                        else:
                            print("\nYOU FAILED MISERABLE CHILD!")
                            print("\nThe correct answer was:", np)
                            return None
            else:
                Error(Exception,
                      "Not a Difficulty",
                      "Get LOST!!!!!",)

CheckModules()
# for i, v in enumerate(LIB.PSS.attribs_cft):
#     if not os.path.exists(PATFfile."+v):
if not os.path.exists(settingsFile):
    CheckModules()

if __name__ == "__main__":
    patfsettings_ext = SettingsHandler().run("--getfile:patfsettings_ext")

    if patfsettings_ext == None or not os.path.exists("PATFsettings."+patfsettings_ext):
        if input("Before Starting Please Enter these Questions (Y/N): ").lower() == "n":
            print("Sorry but PheonixApp requires these details to run.\nExiting...")
            exit(1)
        email = input("Please Enter your Pheonix Studios Email ->\n")
        username = input("Please Enter your Pheonix Studios Username ->\n").lower()
        password = input("Please Enter your Pheonix Studios Password ->\n").lower()
        PATFHandler(False, email, username, password).run()
        #break
        #print('PATFsettings.'+v)

    while True:
        usrinput = input(f"{os.getcwd()} && ->\n")
        if usrinput.lower() == "!stop":
            print("\nBye!")
            exit(0)
        PATFHandler(True).run(usrinput)