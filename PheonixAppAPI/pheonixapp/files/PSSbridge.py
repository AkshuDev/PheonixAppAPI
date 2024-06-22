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

    def BIN(self, path: str = "./aol_var-dict.aolvd", format: str = "vardict-v0.001JSON", encoding: str = "utf-16", encode: bool = False, content: str = "", content_dict: dict = {},
            use_base64: bool = False, use_pheonixApp_encoder: bool = True, compressed: bool = False, hyper_compressed: bool = False) -> bin_worker.BIN:
        return bin_worker.BIN(path, format, encoding, encode, content, content_dict, use_base64, use_pheonixApp_encoder, compressed, hyper_compressed)

    def run(self, mode) -> None:
        self.pss.run(mode)
        return None