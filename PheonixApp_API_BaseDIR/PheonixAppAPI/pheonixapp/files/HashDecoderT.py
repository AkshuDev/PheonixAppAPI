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

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.getcwd())
from PheonixAppAPI.pheonixapp.files import LIB

libH = LIB.PSH

class CODE:
    def __init__(self, hash) -> None:
        self.hash = hash

    def PS_CODE(self, flag=""):
        msg = self.hash
        msg = msg.replace('$AOS', '#')
        self.hash = msg
        if self.hash:
            if "#CODEPSntxH1#" in self.hash and flag == "":
                return True, self.hash.replace("#CODEPSntxH1#", '')
            elif "#CODEPSntxH1#" in self.hash and flag == "CODE@HashDecoder":
                return "PSntx_H1"
            elif "#CODEpheonixUTX#" in self.hash and flag == "":
                return True, self.hash.replace("#CODEpheonixUTX#")
            elif "CODEpheonixUTX#" in self.hash and flag == "CODE@HashDecoder":
                return "pheonix_utx"
            elif "CODEhypeSPACE#" in self.hash and flag == "CODE@HashDecoder":
                return "hype_space"
            elif "#CODEhypeSPACE#" in self.hash and flag == "":
                return True, self.hash.replace("#CODEhypeSPACE#", '')

    def get_hash_type(self):
        hashTypeSTR = self.PS_CODE("CODE@HashDecoder")
        return hashTypeSTR

class Decode:
    def __init__(self, msg:str, type:str=None) -> None:
        self.msg = msg
        self.type = type

    def run(self, *args):
        type = self.type
        if type:
            if type == "PSntx_H1" or type.lower() == "psntx_h1":
                return self.decode_PSntx_H1()
            elif type.lower() == "pheonix_utx":
                return self.decode_pheonix_utx()
            elif type.lower() == "hype_space":
                return self.decode_Hype_Space()
        else:
            type = CODE(self.msg).get_hash_type()
            if type == "PSntx_H1" or type.lower() == "psntx_h1":
                return self.decode_PSntx_H1()
            elif type.lower() == "pheonix_utx":
                return self.decode_pheonix_utx()
            elif type.lower() == "hype_space":
                return self.decode_Hype_Space()

    def decode_PSntx_H1(self):
        hashTF, newHash = CODE(self.msg).PS_CODE()
        dict_ = libH.PSntx_H1
        decoded_str = ""
        if hashTF:
            self.msg = newHash
            for char in self.msg:
                for k, v in dict_.items():
                    if v == char:
                        decoded_str += k
            return decoded_str
        else:
            raise Exception("No Code, Failed. [Hash Type]-[Pheonix Studios Hash]"+f"\n[Pheonix Studios Hash] [Type-PSntx_H1] Description - {libH.PSntx_H1_DESC}")

    def decode_pheonix_utx(self, mes):
        c_t = LIB.PSH.pheonix_utx
        out = ''
        count = 0
        done = False

        if not 'n' in mes:
            while not done == True:
                for key, value in c_t.items():
                    if count == len(mes):
                        return out
                    if mes[count].lower() == value:
                        out = out + key
                        count += 1
                    if count > len(c_t):
                        return out
            return out
        else:
            out = 'Error - Ivalid Character "n" in Encoding'
            return out

    def decode_Hype_Space(self):
        hashTF, newHash = CODE(self.msg).PS_CODE()
        dict_ = libH.hype_space
        decoded_str = ""
        if hashTF:
            self.msg = newHash
            for char in self.msg:
                for k, v in dict_.items():
                    if v == char:
                        decoded_str += k
            return decoded_str
        else:
            raise Exception("No Code, Failed. [Hash Type]-[Pheonix Studios Hash]"+f"\n[Pheonix Studios Hash] [Type-PSntx_H1] Description - {libH.hype_space_DESC}")

class Encode:
    def __init__(self, msg:str, type:str, ComponentType:str) -> None:
        self.msg = msg
        self.type = type
        self.CType = ComponentType
        if not msg:
            raise Exception("No [Message] Given. [Encoder]")
        if not type:
            raise Exception("No [Type] Given. [Encoder]")
        if not ComponentType:
            raise Exception("No [Component Type] Given. [Encoder]")

    def run(self, *args):
        type = self.type
        if type:
            if type == "PSntx_H1" or type.lower() == "psntx_h1":
                msg = self.add_code(self.encode_PSntx_H1())
                return msg
            elif type.lower() == "pheonix_utx":
                msg = self.add_code(self.encode_pheonix_utx())
                return msg
            elif type.lower() == "hype_space":
                msg = self.add_code(self.encode_Hype_Space())
                return msg
        else:
            raise Exception("No Type found. [Encoder]")

    def add_code(self, msg:str):
        if self.type == "PSntx_H1" or self.type.lower() == "psntx_h1":
            msg = '$AOSCODEPSntxH1$AOS' + msg
            return msg
        elif self.type.lower() == "pheonix_utx":
            msg = '$AOSCODEpheonixUTX$AOS' + msg
            return msg
        elif self.type.lower() == "hype_space":
            msg = '$AOSCODEhypeSPACE$AOS' + msg
            return msg

    def encode_PSntx_H1(self):
        dict_ = libH.PSntx_H1
        encoded_str = ""
        if self.msg:
            for char in self.msg:
                for k, v in dict_.items():
                    if k == char:
                        encoded_str += v
            return encoded_str
        else:
            raise Exception("No Message, Failed. [Hash Type]-[Pheonix Studios Hash]"+f"\n[Pheonix Studios Hash] [Type-PSntx_H1] Description - {libH.PSntx_H1_DESC}")

    def encode_pheonix_utx(self, mes):
        c_t = LIB.PSH.pheonix_utx
        out = ''
        count = 0
        done = False

        while not done == True:
            if mes[count].lower() in c_t:
                out = out + c_t[mes[count].lower()]
                count += 1
            else:
                out = out + 'n'
                count += 1
            if count == len(mes):
                done = True
        return out

    def encode_Hype_Space(self):
        dict_ = libH.hype_space
        encoded_str = ""
        if self.msg:
            for char in self.msg:
                for k, v in dict_.items():
                    if k == char:
                        encoded_str += v
            return encoded_str
        else:
            raise Exception("No Message, Failed. [Hash Type]-[Pheonix Studios Hash]"+f"\n[Pheonix Studios Hash] [Type-PSntx_H1] Description - {libH.hype_space_DESC}")