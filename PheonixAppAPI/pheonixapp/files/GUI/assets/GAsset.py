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
from configparser import ConfigParser
config = ConfigParser()

Nfd = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")

if os.getcwd() == Nfd:
    pass
else:
    os.chdir(Nfd)

DFpath = os.path.join(os.path.join("GUI", "assets"), "defined.txt")
section_ = "Defined"

def checkFile():
    if os.path.exists(DFpath):
        pass
    else:
        with open(DFpath, "w") as df:
            config.clear()
            config.add_section(section_)
            config.write(df)
            config.clear()
            df.close()

def define(option:str="", value:str="", option_list:list=[], value_list:list=[]):
    checkFile()

    if option != "" and value != "":
        with open(DFpath, "w") as df:
            config.read_file(df)
            config.set(section_, option, value)
            config.write(df)
    elif option_list != [] and value_list != []:
        if len(option_list) == len(value_list):
            pList = []

            i = 0

            while not i == len(option_list):
                if i == len(option_list):
                    break

                pList.append(option_list[i])
                pList.append(value_list[i])
                i+=1

            config.clear()
            with open(DFpath, "r") as df:
                config.read_file(df)

            sv = -1
            skip = False

            for i,v in enumerate(pList):
                if skip and not sv == i:
                    skip = False

                if not skip:
                    config.set(section_, v, pList[i+1])
                    sv = i+1
                    skip = True

            with open(DFpath, "w") as df:
                config.write(df)
                df.close()

    else:
        return None

def get(value:str="", defined:bool=True):
    path = ""
    checkFile()

    with open(DFpath, "r") as df:
        config.read_file(df),
        df.close()

    path = config.get(section_, value)

    return path

Un = os.path.join(os.path.dirname(DFpath), "Username.png")
UnW = os.path.join(os.path.dirname(DFpath), "Username_W.png")
Mail = os.path.join(os.path.dirname(DFpath), "Mail.png")
MailW = os.path.join(os.path.dirname(DFpath), "Mail_W.png")
Pw = os.path.join(os.path.dirname(DFpath), "Password.png")
PwW = os.path.join(os.path.dirname(DFpath), "Password_W.png")