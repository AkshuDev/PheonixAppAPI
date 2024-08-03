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
import time as TimeModule
from datetime import datetime
import requests

mainDir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    os.chdir(mainDir)
    sys.path.append(mainDir)

from PheonixAppAPI.pheonixapp.files import LIB
from PheonixAppAPI.pheonixapp.files import PSSbridge
from PheonixAppAPI.pheonixapp.files import HashDecoderT
import zlib

uselessF_url = "https://uselessfacts.jsph.pl/random.json?language=en"
quote_url = "https://api.quotable.io/random"

PSSUltraCode = HashDecoderT.Encode(HashDecoderT.Encode(HashDecoderT.Encode("SPUltraPs9878762b4jb23jvhgv34g", "Hype_Space", "PheonixStudios"), "Hype_Space", "PheonixStudios"), "Hype_Space", "PheonixStudios")

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

class TCmds():
    def __init__(self, cmd:str) -> None:
        self.cmd = cmd
        self.pss = LIB.PSS
        self.PATFcommands = self.pss.atribbs
        self.NPcommands = self.pss.Tcmds

    def run(self):
        command = False
        mainLOOP = self.cmd.splitlines()
        main = self.cmd.split(" ")
        main2 = ""

        try:
            main2 = main.split(":")
        except Exception:
            main2 = ""

        if main[0].lower() == "terminal":
            print(self.cmd)
            for b, j in enumerate(mainLOOP):
                for i, v in enumerate(main):
                    print(v)
                    if i != 0:
                        if v.lower() in self.PATFcommands and not command:
                            command = True
                        elif v.lower() in self.NPcommands and not command:
                            if v.lower() == "!time":
                                command = True
                                print(datetime.now())
                            elif v.lower() == "!hash":
                                os.system(f"py {os.path.join(os.path.dirname(os.path.abspath(__file__)), 'HashDecoder.py')}")
                            elif v.lower() == "!fact":
                                command = True
                                response = None

                                cp, isc = PSSbridge.PATFbridge().getCertificatePath(PSSUltraCode)

                                if isc:
                                    response = requests.get(uselessF_url, verify=cp)
                                else:
                                    response = requests.get(uselessF_url, verify=False)

                                if response.status_code == 200:
                                    fact_data = response.json()
                                    fact = fact_data['text']

                                    print(f"Random Fact: {fact}")
                            elif v.lower() == "!quote":
                                command = True
                                response = None

                                cp, isc = PSSbridge.PATFbridge().getCertificatePath(PSSUltraCode)

                                if isc:
                                    response = requests.get(quote_url, verify=cp)
                                else:
                                    response = requests.get(quote_url, verify=False)

                                if response.status_code == 200:
                                    quote_data = response.json()
                                    quote = quote_data['content']
                                    author = quote_data['author']

                                    print(f'Quote: "{quote}"  -  {author}')

                            elif v.lower() == "!remind":
                                command = True

                                self.remind(main[i+1], main[i+2])

                            elif v.lower() == "!encodefile":
                                command = True

                                filePath = main[2]
                                outfilePath = main[3]

                                if os.path.isdir(os.path.basename(outfilePath)):
                                    pass
                                else:
                                    outfilePath = outfilePath.replace(os.path.basename(outfilePath), "")

                                fileName = os.path.basename(filePath)

                                self.encode(fileName, filePath, outfilePath)

                                print(f"File Successfully Encoded at [{outfilePath}]")

                            elif v.lower() == "!decodefile":
                                command = True

                                filePath = main[2]
                                outfilePath = main[3]
                                fileName = os.path.basename(filePath)

                                self.decode(fileName, filePath, outfilePath)

                                print(f"File Successfully Decoded at [{outfilePath}]")
                            print(command)

                            if command:
                                break
                        else:
                            if b != 0:
                                Error(Exception, "Not a Command", f"This command [{self.cmd}] is not identified. [PSEtNAC001]", True)

    def remind(self, task, time):
        try:
            formatted_time = time.replace(":", "")

            command = f'schtasks /create /sc once /st {formatted_time} /tn "Reminder" /tr "msg * {task}"'

            os.system(command, shell=True, check=True)

            print(f"Reminder set for '{task}' at {time}.")

        except Exception as e:
            print("An error occurred while setting the reminder:", str(e))

    def encode(self, fileName:str, fileP:str, outFileP:str="", data:str="") -> None:
        #Todo: Setup
        fileName, extention = os.path.splitext(fileName)

        if outFileP == "":
            outFileP = os.path.dirname(fileP)

        outFileP = os.path.join(outFileP, fileName+".paef")

        from configparser import ConfigParser
        config = ConfigParser()

        #Todo: Set Data

        if data == "":
            data = ""

            #Todo: Read File
            with open(fileP, "r") as File:
                File.seek(0)
                data = File.read()
                File.close()

        data = HashDecoderT.Encode(data, "Hype_Space", "PheonixStudios").run()
        data = zlib.compress(data.encode("utf-8")).hex()

        #Todo: Process Data into a Config Format
        config.add_section("Define")
        config.set("Define", "filepath", fileP)
        config.set("Define", "outfilepath", outFileP)
        config.set("Define", "time", str(datetime.now()))
        config.set("Define", "ext", extention)
        config.set("Define", "compression", zlib.compress(HashDecoderT.Encode("zlib-utf8", "Hype_Space", "PheonixStudios").run().encode("utf-8")).hex())

        config.add_section("Data")
        config.set("Data", "data", data)

        #Todo: Write File
        with open(outFileP, "w", encoding="utf-8") as File:
            config.write(File)
            File.close()

        os.remove(fileP)

    def decode(self, fileP:str, ogFileP:str="", compression:str="", fileP_bool:bool=True, outFileP_bool:bool=True, time_bool:bool=True, extention_bool:bool=True, compression_bool:bool=True, write_file:bool=True) -> list:
        output=[]
        from configparser import ConfigParser
        config = ConfigParser()

        #Todo: Read File
        with open(fileP, "r", encoding="utf-8") as File:
            File.seek(0)
            config.read_file(File)
            File.close()

        #Todo: Get Data
        if ogFileP == "":
            ogFileP = config.get("Define", "filepath")

        if compression == "":
            compression = HashDecoderT.Decode(zlib.decompress(bytes.fromhex(config.get("Define", "compression"))).decode("utf-8"), "Hype_Space")

        outFilePath = config.get("Define", "outfilepath")
        time = config.get("Define", "time")
        ext = config.get("Define", "ext")

        data = HashDecoderT.Decode(zlib.decompress(bytes.fromhex(config.get("Data", "data"))).decode("utf-8"), "Hype_Space").run()

        output.append(data)
        if fileP_bool:
            output.append(ogFileP)
        if outFileP_bool:
            output.append(outFilePath)
        if time_bool:
            output.append(time)
        if extention_bool:
            output.append(ext)
        if compression_bool:
            output.append(compression)

        #Todo: Write File
        if write_file:
            with open(ogFileP, "w") as File:
                File.write(data)
                File.close()

        print(write_file)
        os.remove(outFilePath)

        return output

class HaCline():
    def __init__(self, cmd:str="") -> None:
        self.cmd = cmd
        self.pss = LIB.PSS

    def run(self):
        pass