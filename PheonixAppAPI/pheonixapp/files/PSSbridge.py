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

from PheonixAppAPI.pheonixapp.files import PheonixStudioStarter
from PheonixAppAPI.pheonixapp.files import (HashDecoderT, Utilities, Terminal)
from PheonixAppAPI import (bin_worker)

import os
import typing
import random

class PATFbridge():
    def __init__(self, usefileData:bool=False, email:str="", username:str="", password:str="") -> None:
        self.pss = PheonixStudioStarter.PATFHandler(usefileData, email, username, password)

    def createfile(self, flag:str=""):
        self.pss.createfile(flag)

    def getCertificatePath(self, code:str="", flag:str="+BOOL"):
        return self.pss.getCertificatePath(code, flag)

    def run(self, mode):
        self.pss.run(mode)

class API():
    def __init__(self, LoginOrSignup:bool=False, usefileData:bool=False, email:str="", username:str="", password:str="", get_patf:bool=False) -> None:
        self.LoginOrSignup:bool = LoginOrSignup
        self.usefiledata:bool = usefileData
        self.email:str = email
        self.username:str = username
        self.password:str = password
        self.get_patf = get_patf
        self.pss = None

        if LoginOrSignup:
            self.pss = PheonixStudioStarter.PATFHandler(self.usefiledata, self.email, self.username, self.password)
        else:
            self.email = "$AOS([APICALL->NOLogin])"
            self.username = "$AOS([APICALL->NOLogin])"
            self.password = "$AOS([APICALL->NOLogin])"

            self.pss = PheonixStudioStarter.PATFHandler(self.usefiledata, self.email, self.username, self.password)

        if self.get_patf:
            self.pss.run("terminal --createfile")

    def CheckModules(self, mode:str="all", list:list=[], module:str="") -> None:
        PheonixStudioStarter.CheckModules(mode, list, module)

    def CheckModulesAPI(self, prompt:bool=False, mode:str="list", module:str="PheonixAppAPI", module_list=["PheonixAppAPI"], log:bool=False) -> tuple[list, bool]:
        from PheonixAppAPI.apis.ModuleAPI import CheckModules
        return CheckModules(prompt, mode, module, module_list, log)

    def DownloadModulesAPI(self, prompt:bool=False, mode:str="list", module="PheonixAppAPI", module_list=["PheonixAppAPI"], log:bool=False, upgraded_module:bool=True) -> tuple[list, bool]:
        from PheonixAppAPI.apis.ModuleAPI import DownloadModules
        return DownloadModules(prompt, mode, module, module_list, log, upgraded_module)

    def getCertificatePath(self, code:str="", flag:str="+BOOL") -> str:
        return self.pss.getCertificatePath(code, flag)

    def Encode(self, msg:str="", type:str="Hype_Space", run_flags="") -> str:
        return HashDecoderT.Encode(msg, type, "Community").run(run_flags)

    def Decode(self, msg:str="", type:str="Hype_Space", run_flags="") -> str:
        return HashDecoderT.Decode(msg, type).run(run_flags)

    def Terminal_run(self, cmd:str) -> None:
        Terminal.TCmds(cmd).run()
        return None

    def Error_(self, type_:BaseException, name:str, details:str, log:bool=False, mode:str="") -> None:
        Terminal.Error(type_, name, details, log, mode)
        return None

    def HaCline(self, cmd:str) -> None:
        Terminal.HaCline(cmd)
        return None

    def Object_Detector(self) -> None:
        import PheonixAppAPI.pheonixapp.files.ObjectDetector.handler
        return None

    def Utilities_Calc_Terminal(self) -> None:
        Utilities.calculator()
        return None

    def Utilities_Wiki_Terminal(self) -> None:
        Utilities.wikipediasearch()
        return None

    def Utilities_Wiki_API(self, query:str) -> str:
        return Utilities.api_wiki_search(query)

    def str_to_bin(self, data:typing.Union[str, int, dict]) -> str:
        return bin_worker.BIN().str_to_bin(data)

    def bin_to_str(self, data:str) -> str:
        return bin_worker.BIN().bin_to_str(data)

    def str_to_bytes(self, data:typing.Union[str, int, dict], encoding:str="utf-16") -> bytes:
        return bin_worker.BIN().str_to_bytes(data, encoding)

    def bytes_to_str(self, data:bytes, encoding:str="utf-16") -> str:
        return bin_worker.BIN().bytes_to_str(data, encoding)

    def to_binINT(self, data_dict:dict={}, data_str:str="", useString:bool=True) -> int:
        return bin_worker.BIN().to_binINT(data_dict, data_str, useString)

    def PEMU(self, data:str) -> str:
        return bin_worker.BIN(content=data).PEMU()

    def PCEMU(self, data:str) -> str:
        return bin_worker.BIN(content=data).PCEMU()

    def PHCDMU(self, data:str) -> str:
        return bin_worker.BIN(content=data).PHCDMU()

    def PEDU(self, data:str) -> str:
        return bin_worker.BIN(content=data).PDMU()

    def PCDMU(self, data:str) -> str:
        return bin_worker.BIN(content=data).PCDMU()

    def PHCDMU(self, data:str) -> str:
        return bin_worker.BIN(content=data).PHCDMU()

    def BIN(self, path: str = "./aol_var-dict.aolvd", format: str = "vardict-v0.001JSON", encoding: str = "utf-16", encode: bool = False, content: str = "", content_dict: dict = {},
            use_base64: bool = False, use_pheonixApp_encoder: bool = True, compressed: bool = False, hyper_compressed: bool = False) -> bin_worker.BIN:
        return bin_worker.BIN(path, format, encoding, encode, content, content_dict, use_base64, use_pheonixApp_encoder, compressed, hyper_compressed)

    def GuessTheNumberScript(self, modeEasy:bool, modeNormal:bool, modeHard:bool, guess1:int, guess2:int, guess3:int, modeEasyRange:tuple[int, int]=(0, 100), modeNormalRange:tuple[int, int]=(0, 1000), modeHardRange:tuple[int, int]=(0, 10000)) -> bool:
        number = 0
        if modeEasy:
            number = random.randint(modeEasyRange[0], modeEasyRange[1])
        else:
            if modeNormal:
                number = random.randint(modeNormalRange[0], modeNormalRange[1])
            else:
                number = random.randint(modeHardRange[0], modeHardRange[1])

        if (guess1 == number or guess2 == number) or guess3 == number:
            return True
        else:
            return False

    def run(self, mode) -> None:
        self.pss.run(mode)
        return None